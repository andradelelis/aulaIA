# Petrobras 2024 — gabarito de conferência

Este arquivo contém cálculos próprios, independentes de qualquer resposta de IA. Não é uma transcrição de saída de um modelo.

Fonte: [Petrobras, Relatório Anual e Form 20-F 2024, tradução livre em português](https://petrobras.com.br/documents/d/f3a44542-113e-11ee-be56-0242ac120002/form-20f-2024?download=true), demonstrações consolidadas em **milhões de dólares norte-americanos**. BP: F-3 / PDF 344; DRE: F-4 / PDF 345; DFC: F-6 / PDF 347. Consulta e download: 14/10/2026.

## Cálculos

| Indicador | Fórmula 2024 | Resultado 2024 | Fórmula 2023 | Resultado 2023 |
|---|---|---:|---|---:|
| Liquidez corrente | 21.836 / 31.460 | 0,694 | 32.445 / 33.860 | 0,958 |
| Margem líquida | 7.605 / 91.416 × 100 | 8,32% | 24.995 / 102.409 × 100 | 24,41% |
| Variação anual da receita em US$ | (91.416 / 102.409 − 1) × 100 | −10,73% | Não calculada | — |

A margem usa **lucro líquido do exercício**, incluindo a parcela dos acionistas não controladores. Não usa apenas o lucro atribuível aos acionistas da Petrobras. Pontos nas expressões acima são separadores de milhares; o CSV usa inteiros sem separadores. Liquidez corrente é uma razão, não um percentual.

Identidade do caixa de 2024:

```text
Caixa inicial                         12.727
Fluxo operacional                    +37.984
Fluxo de investimento                −13.369
Fluxo de financiamento               −33.088
Efeito cambial                          −983
Caixa final                            3.271
Variação do caixa                     −9.456
```

Conferência 2023: 7.996 + 43.212 − 7.955 − 30.700 + 174 = 12.727.

## Interpretação com limites

- **Fato:** a liquidez corrente calculada caiu entre as datas comparadas e ficou abaixo de 1. **Limite:** isso não prova insolvência; estudar vencimentos, geração de caixa, linhas disponíveis e condições do setor.
- **Fato:** receita e margem líquida em US$ ficaram menores. **Limite:** não é possível atribuir a mudança exclusivamente a vendas físicas, preços ou eficiência com esse recorte. É necessário examinar moeda funcional, conversão e notas.
- **Fato:** houve geração operacional de caixa positiva e redução do saldo final. A identidade mostra que saídas líquidas de investimento e financiamento, além do efeito cambial, superaram o fluxo operacional. **Limite:** a identidade não explica sozinha o mérito econômico das decisões.
- **Fato:** lucro e FCO são diferentes. **Limite:** um FCO elevado em relação ao lucro não é, por si, prova definitiva de qualidade dos lucros; há ajustes e mudanças no capital de giro.

## Perguntas para as notas

1. O que explica a composição do resultado financeiro e dos efeitos cambiais? Consultar nota 12 e base de elaboração (nota 2).
2. Como se distribuem os vencimentos e compromissos de financiamentos e arrendamentos? Notas 30 e 31.
3. Qual a natureza e disponibilidade de caixa e títulos e valores mobiliários? Nota 8.

As notas estão em `petrobras_2024.pdf`. O extrato de três páginas é feito para leitura em sala e não substitui o documento integral.

## Roteiro da atividade (25 minutos)

1. **7 min:** confirmar escopo e unidades, abrir os demonstrativos e anexar os documentos públicos a um assistente que aceite arquivos.
2. **8 min:** executar `prompt_petrobras.txt`, ler a resposta e identificar afirmações que carecem de evidência.
3. **10 min:** recalcular indicadores e a conciliação em duplas; comparar com este gabarito e pedir correções documentadas.

Registrar modelo, data e anexos caso se queira comparar respostas. A preparação desta aula não inclui uma resposta real de um provedor de IA. Não há resultados de modelo inventados.

**Plano sem internet ou sem assistente:** usar PDF, CSV, calculadora ou planilha. Auditar a afirmação hipotética “FCO positivo garante que o caixa aumentou”. Ela é falsa: há também fluxos de investimento e financiamento e efeito cambial. Os materiais de apoio estão disponíveis localmente.
