# GEO Scorecard

## Objetivo

Avaliar se um conteúdo existente está pronto para ser entendido, confiado, extraído, resumido e citado, produzindo pontuação transparente e diagnóstico acionável.

`[FRAMEWORK PRÓPRIO]` O scorecard consolida sinais observáveis. Ele não estima probabilidade de ranking ou citação e não substitui `geo-readiness.yaml`, `citation-readiness.yaml` ou `entity-authority.yaml`.

`geo-readiness.yaml` avalia um domínio, site ou ecossistema como porta de entrada para o trabalho. O GEO Scorecard avalia um ativo específico. Ambos produzem um número de `0–100`, mas medem objetos diferentes e não são comparáveis entre si.

## Quando usar

- Para auditar conteúdo fornecido pelo usuário.
- Antes e depois de uma revisão editorial.
- Para comparar páginas, versões ou concorrentes sob o mesmo protocolo.
- Para consolidar outputs de extractability e trust signal audits.

## Inputs

Mínimos:

- conteúdo completo ou trecho identificado;
- tipo de ativo;
- target intent;
- público;
- entidade principal;
- data e origem do material.

Opcionais: content brief, intent map, entity map, evidence ledger, sources, extractability audit, trust signal audit, benchmark e páginas comparáveis.

Se apenas uma URL for fornecida sem conteúdo, registrar `não avaliado`; não afirmar que a URL foi rastreada.

## Processo

1. Definir escopo, versão, intenção, público e limitações.
2. Separar evidência observada de inferência e recomendação.
3. Executar ou consumir `extractability-audit`.
4. Executar ou consumir `trust-signal-audit`.
5. Pontuar cada dimensão de `0` a `4`:

| Dimensão | Peso |
|---|---:|
| intent alignment | 8 |
| entity clarity | 7 |
| entity relationship coverage | 6 |
| evidence quality | 9 |
| citation readiness | 8 |
| answer block readiness | 7 |
| extractability | 8 |
| topical completeness | 6 |
| trust signals | 8 |
| freshness signals | 5 |
| source transparency | 6 |
| structural clarity | 6 |
| schema opportunities | 3 |
| internal linking opportunities | 4 |
| limitations disclosure | 5 |
| actionability | 4 |

6. Justificar cada nota com evidência textual ou status `não avaliado`.
7. Calcular:

```text
total = soma(score / 4 × peso)
```

8. Identificar main gap, risco e dependências.
9. Priorizar correções por impacto, risco, confiança e esforço.
10. Preencher os templates Markdown e CSV.

Escala:

- `0`: ausente ou evidência contrária;
- `1`: fraco e inconsistente;
- `2`: parcial;
- `3`: sólido;
- `4`: forte e reproduzível;
- `N/A`: não avaliado; excluir do denominador e informar cobertura.

## Outputs

- score total e cobertura da avaliação;
- pontuação e justificativa por dimensão;
- evidências observadas;
- lacunas;
- prioridades;
- recomendações;
- limitações e próximos passos;
- linha comparável em `templates/geo-scorecard.csv`.

## Critérios de qualidade

- Toda nota tem justificativa textual.
- `N/A` não é convertido em zero.
- Score total exibe cobertura e denominador.
- Recomendações apontam para problema, evidência e resultado esperado.
- Diagnóstico diferencia fato, inferência e recomendação.
- O output pode orientar content refresh, answer blocks ou citation engineering.

## Erros comuns

- Dar nota com base em impressão geral.
- Comparar scores obtidos com escopos diferentes.
- Pontuar URL não fornecida como se tivesse sido rastreada.
- Confundir schema opportunity com schema existente.
- Entregar score sem prioridades.
- Somar critérios sem registrar limitações.
