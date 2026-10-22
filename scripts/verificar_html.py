"""Verificação local e offline de slides RevealJS usando Edge e Playwright."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "verificacao"
OUT.mkdir(exist_ok=True)
errors = []
remote = []
with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        headless=True,
        args=["--allow-file-access-from-files", "--disable-background-networking"],
    )
    context = browser.new_context(viewport={"width": 1366, "height": 768}, offline=True)
    page = context.new_page()
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.on("request", lambda req: remote.append(req.url) if req.url.startswith("http") else None)
    page.goto((ROOT / "ia_financas.html").as_uri(), wait_until="load")
    page.wait_for_function("window.Reveal && Reveal.isReady()")
    count = page.evaluate("Reveal.getTotalSlides()")
    report = {"slides": count, "offline": True, "viewport": [1366, 768], "results": []}
    for index in range(count):
        page.evaluate("i => Reveal.slide(i)", index)
        page.wait_for_timeout(100)
        item = page.evaluate("""() => {
            const s=Reveal.getCurrentSlide();
            const b=s.getBoundingClientRect();
            const scale=Reveal.getScale();
            const outside=[];
            for (const e of s.querySelectorAll('h2,h3,p,table,svg,img,.card,.step,.milestone,.nest,.prompt,li')) {
                if(e.closest('.notes') || getComputedStyle(e).display==='none') continue;
                const r=e.getBoundingClientRect();
                if(!r.width || !r.height) continue;
                if(r.right > b.right+2 || r.bottom > b.bottom+2 || r.left < b.left-2 || r.top < b.top-2)
                    outside.push({tag:e.tagName, text:e.textContent.trim().slice(0,90),
                        rect:[r.left,r.top,r.right,r.bottom],slide:[b.left,b.top,b.right,b.bottom]});
            }
            // Reservar 40 pixels do canvas para rodapé e navegação.
            const maxBottom=b.top+(Reveal.getConfig().height-40)*scale;
            const maxRight=b.left+Reveal.getConfig().width*scale;
            const canvasOutside=[];
            for(const e of s.querySelectorAll('h2,h3,p,table,svg,img,.card,.step,.milestone,.nest,.prompt,li')) {
                if(e.closest('.notes')) continue;
                const r=e.getBoundingClientRect();
                if(r.height && (r.bottom>maxBottom+2 || r.right>maxRight+2))
                    canvasOutside.push(e.textContent.trim().slice(0,90));
            }
            const logos=s.querySelectorAll('img.ifmg-mark');
            const logo=logos[0];
            const lr=logo?.getBoundingClientRect();
            const title=s.querySelector('h2');
            const range=document.createRange();
            range.selectNodeContents(title);
            const tr=range.getBoundingClientRect();
            const logoOverlap=lr && lr.left<tr.right && lr.right>tr.left && lr.top<tr.bottom && lr.bottom>tr.top;
            const opening=s.classList.contains('opening-slide');
            const logoPositionOK=lr && Math.abs(lr.top-b.top)<2 && (opening
                ? Math.abs((lr.left+lr.right)/2-(b.left+b.right)/2)<2
                : Math.abs(lr.right-b.right)<2);
            return {title:title?.textContent, id:s.id, outside, canvasOutside,
                logoCount:logos.length, logoLoaded:!!logo?.naturalWidth,
                logoWidth:lr?.width/scale, logoPositionOK:!!logoPositionOK, logoOverlap:!!logoOverlap,
                slideHeight:s.scrollHeight, hasNotes:!!s.querySelector('.notes'),
                literalFence:s.innerText.includes(':::')};
        }""")
        item["index"] = index + 1
        report["results"].append(item)
        page.screenshot(path=str(OUT / f"slide_{index+1:02}.png"))
    # Navegação real com teclado e links para materiais locais.
    page.evaluate("Reveal.slide(0)")
    page.keyboard.press("ArrowRight")
    report["keyboardNavigation"] = page.evaluate("Reveal.getIndices().h === 1")
    report["localLinks"] = page.evaluate("""() => Array.from(document.querySelectorAll('.slides a[href]'))
        .map(a=>a.getAttribute('href')).filter(u=>!u.startsWith('http')&&!u.startsWith('#')&&!u.startsWith('data:'))""")
    report["missingLocalLinks"] = [link for link in report["localLinks"] if not (ROOT / link).exists()]
    report["remoteRequests"] = remote
    report["javascriptErrors"] = errors
    # Segundo formato de tela: a geometria deve manter o formato 16:9 sem cortes.
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.evaluate("Reveal.layout()")
    page.evaluate("i => Reveal.slide(i)", count - 1)
    page.wait_for_timeout(200)
    page.screenshot(path=str(OUT / "referencias_1920.png"))
    browser.close()
report["passed"] = (count == 24 and report["keyboardNavigation"]
    and not report["missingLocalLinks"] and not errors and not remote
    and all(not x["outside"] and not x["canvasOutside"] and not x["literalFence"] and x["hasNotes"]
        and x["logoCount"] == 1 and x["logoLoaded"] and x["logoPositionOK"] and not x["logoOverlap"]
        for x in report["results"]))
(OUT / "validacao_html.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k: v for k,v in report.items() if k not in ["results", "localLinks"]}, ensure_ascii=False, indent=2))
for item in report["results"]:
    print(item["index"], item["title"], "height", item["slideHeight"],
          "outside", len(item["outside"]), "canvas", len(item["canvasOutside"]), "fence", item["literalFence"])
if not report["passed"]:
    raise SystemExit(1)
