# Inteligência Artificial e aplicações em Finanças

Material de **Tópicos Especiais em Finanças**, Bacharelado em Administração — IFMG Campus Formiga. Professor: **Lelis Pedro de Andrade**.

## Acesso para estudantes

- [Apresentação em HTML](ia_financas.html).
- [Demonstrações financeiras da Petrobras — extrato da atividade](dados/petrobras_2024_demonstracoes.pdf).
- [Dados em CSV](dados/petrobras_2024_recorte.csv).
- [Prompt da atividade](dados/prompt_petrobras.txt).
- [Gabarito comentado](dados/gabarito_petrobras.md).
- [Referências bibliográficas](referencias.md).
- [Fontes da contextualização](contextualizacao_fontes.md).

Para baixar tudo, use **Code → Download ZIP** e extraia o arquivo. Abra `ia_financas.html` no navegador, mantendo as pastas do projeto junto dele. Os slides funcionam offline; links externos exigem internet. No GitHub, o HTML é exibido como código até que seja baixado ou publicado no Pages.

## Publicação no GitHub Pages

Abra **Settings → Pages → Build and deployment → Deploy from a branch**, selecione **main** e **/(root)** e salve. Após a implantação, o endereço será [andradelelis.github.io/aulaIA](https://andradelelis.github.io/aulaIA/). Esse endereço só funciona após habilitar e concluir a implantação do Pages. O arquivo `index.html` encaminha para os slides.

## Apresentação

São **28 slides**, incluindo técnicas de machine learning e leitura de uma árvore de decisão. A data do título é atualizada a cada renderização (DD/MM/AAAA).

- Setas: avançar e voltar.
- `F`: tela cheia.
- `O`: visão geral.
- `S`: notas do professor. Se o navegador bloquear notas em arquivo local, use `quarto preview ia_financas.qmd`.

Os exemplos hipotéticos estão identificados. O projeto inclui notas do professor e gabarito, acessíveis aos estudantes.

## Editar e renderizar

Instale o [Quarto](https://quarto.org/) e execute:

```powershell
quarto render ia_financas.qmd --to revealjs
```

Versão usada: Quarto 1.9.36. A renderização não depende de Python.

## Organização

- `ia_financas.qmd`, `ia_financas.css`, `ia_financas.html`: fonte, estilos e apresentação pronta.
- `partials/` e `assets/`: configuração da abertura, marca institucional e diagramas.
- `dados/`: demonstrativos, CSV, prompt e gabarito.
- `fontes/`: documentos e extratos utilizados.
- `referencias.md`, `contextualizacao_fontes.md`, `fundamentacao_slides.md`: referências e fundamentação.
- `scripts/`: preparação e verificação.

Documentos de terceiros preservam autoria e direitos. O relatório da Petrobras foi obtido da fonte oficial. O extrato preserva as páginas F-3, F-4 e F-6; o CSV é parcial, e os demonstrativos e notas originais são a referência.

## Verificação

Foram conferidos os 28 slides no arquivo-fonte e todos os links locais do HTML. Relatórios antigos em `verificacao/` não integram esta publicação. Tempos e números escritos em notas antigas devem ser revistos para planejar a duração da aula atual.
