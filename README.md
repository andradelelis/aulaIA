# Intelig?ncia Artificial e aplica??es em Finan?as

Material de **T?picos Especiais em Finan?as**, Bacharelado em Administra??o ? IFMG Campus Formiga. Professor: **Lelis Pedro de Andrade**.

## Acesso para estudantes

- [Apresenta??o em HTML](ia_financas.html): baixe o projeto para apresentar no navegador; o GitHub exibe o c?digo do HTML ao abrir esse arquivo.
- [Demonstra??es financeiras da Petrobras ? extrato para a atividade](dados/petrobras_2024_demonstracoes.pdf).
- [Dados da atividade em CSV](dados/petrobras_2024_recorte.csv).
- [Prompt da atividade](dados/prompt_petrobras.txt).
- [Gabarito comentado e c?lculos](dados/gabarito_petrobras.md).
- [Refer?ncias bibliogr?ficas](referencias.md).
- [Fontes da contextualiza??o](contextualizacao_fontes.md).

Para baixar tudo no GitHub, use **Code ? Download ZIP** e extraia o arquivo. Abra `ia_financas.html` no Edge, Chrome ou Firefox e mantenha as pastas do projeto junto dele. Os slides funcionam offline; links externos exigem internet.

## Publica??o no GitHub Pages

Depois de enviar os arquivos ao reposit?rio p?blico `andradelelis/aulaIA`, abra **Settings ? Pages ? Build and deployment ? Deploy from a branch**, selecione **main** e **/(root)** e salve. Ap?s a implanta??o, o endere?o esperado ser? `https://andradelelis.github.io/aulaIA/`. O arquivo `index.html` encaminha para a apresenta??o. Esse endere?o s? funciona depois de habilitar e concluir a implanta??o do Pages.

## Apresenta??o

A apresenta??o tem **28 slides**, incluindo panorama de t?cnicas de machine learning e leitura guiada de uma ?rvore de decis?o. A data do t?tulo ? atualizada a cada renderiza??o, no formato DD/MM/AAAA.

- Setas: avan?ar e voltar.
- `F`: tela cheia.
- `O`: vis?o geral.
- `S`: notas do apresentador. Se o navegador bloquear as notas ao abrir um arquivo local, use `quarto preview ia_financas.qmd`.

Os exemplos hipot?ticos est?o identificados nos slides. A apresenta??o e o c?digo-fonte incluem notas do professor e o material inclui gabarito, ambos acess?veis a quem baixar o projeto.

## Editar e gerar o HTML

Instale o [Quarto](https://quarto.org/) e execute na pasta do projeto:

```powershell
quarto render ia_financas.qmd --to revealjs
```

A renderiza??o n?o depende de Python. A vers?o usada neste projeto ? Quarto 1.9.36. O HTML incorpora estilos e bibliotecas de apresenta??o; os materiais complementares permanecem em arquivos separados.

## Arquivos do projeto

| Arquivo ou pasta | Conte?do |
|---|---|
| `ia_financas.qmd` | Slides, fontes e notas do professor |
| `ia_financas.css` | Estilos da apresenta??o |
| `ia_financas.html` | Apresenta??o pronta para abrir |
| `partials/` | Filtro da marca institucional e configura??o da abertura |
| `assets/` | Marca institucional e diagrama vetorial |
| `dados/` | Demonstrativos, dados, prompt e gabarito da atividade |
| `fontes/` | Documentos de refer?ncia e extratos utilizados |
| `referencias.md` | Bibliografia e mapa das fontes |
| `contextualizacao_fontes.md` | Fundamenta??o dos slides de contextualiza??o |
| `fundamentacao_slides.md` | Registro de fundamenta??o e revis?o conceitual |
| `scripts/` | Rotinas auxiliares de prepara??o e verifica??o |

Os documentos de terceiros preservam sua autoria e seus direitos; sua inclus?o no material n?o altera a licen?a original. O relat?rio da Petrobras foi obtido da fonte oficial. O extrato preserva as p?ginas F-3, F-4 e F-6; o CSV ? uma transcri??o parcial, e os demonstrativos e notas originais s?o a refer?ncia.

## Verifica??o

Os 28 slides foram identificados no arquivo-fonte e todos os links locais do HTML foram conferidos antes da prepara??o para publica??o. Relat?rios e imagens antigos em `verificacao/` podem corresponder a vers?es anteriores. Os tempos e n?meros escritos em notas antigas devem ser revistos para planejar a dura??o da aula atual.
