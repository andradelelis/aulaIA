-- Inclui a marca em todos os slides de nível 2, inclusive novos slides.
-- O CSS distingue a abertura dos demais slides, sem alterar a proporção da imagem.
function Header(header)
  if header.level == 2 and quarto.doc.is_format("revealjs") then
    return {
      header,
      pandoc.RawBlock("html", '<img class="ifmg-mark" src="assets/ifmg-formiga.png" alt="Instituto Federal de Minas Gerais — Campus Formiga">')
    }
  end
end
