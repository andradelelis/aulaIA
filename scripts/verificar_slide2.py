"""Confere o conteúdo e os limites do slide 2 após a correção da introdução."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
out = root / "verificacao"
checks = []
with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        headless=True,
        args=["--allow-file-access-from-files", "--disable-background-networking"],
    )
    context = browser.new_context(offline=True)
    page = context.new_page()
    for width, height in [(1366, 768), (1920, 1080)]:
        page.set_viewport_size({"width": width, "height": height})
        page.goto((root / "ia_financas.html").as_uri(), wait_until="load")
        page.wait_for_function("window.Reveal && Reveal.isReady()")
        page.evaluate("Reveal.configure({transition: 'none'})")
        page.evaluate("Reveal.slide(1)")
        page.wait_for_timeout(500)
        result = page.evaluate("""() => {
            const s = Reveal.getCurrentSlide();
            const b = s.getBoundingClientRect();
            const scale = Reveal.getScale();
            const overflow = [];
            for (const e of s.querySelectorAll('h2,h3,p,img,.card,.question,.source')) {
                if(e.closest('.notes')) continue;
                const r = e.getBoundingClientRect();
                if(r.width && r.height && (r.left < b.left-2 || r.right > b.right+2 ||
                    r.top < b.top-2 || r.bottom > b.top+680*scale+2))
                    overflow.push(e.textContent.trim().slice(0,80));
            }
            return {
                title: s.querySelector('h2').textContent,
                cards: s.querySelectorAll('.card').length,
                nestedSections: s.querySelectorAll('section').length,
                hasContent: s.innerText.includes('trabalhadores de alta'),
                hasPageReference: !!s.querySelector('.source a[href$="#page=2"]'),
                totalSlides: Reveal.getTotalSlides(),
                overflow
            };
        }""")
        result["viewport"] = [width, height]
        checks.append(result)
        page.screenshot(path=str(out / f"slide_02_corrigido_{width}.png"))
    browser.close()
passed = all(x["title"] == "Introdução" and x["cards"] == 3 and not x["nestedSections"]
             and x["hasContent"] and x["hasPageReference"] and not x["overflow"] for x in checks)
report = {"passed": passed, "checks": checks}
(out / "validacao_slide2.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
