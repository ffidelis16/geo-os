# Exemplo fictício de rewrite plan

## Contexto

| Campo | Valor |
|---|---|
| Plan ID | EXAMPLE-REWRITE-001 |
| Ativo | Guia fictício sobre desperdício doméstico |
| Target intent | Como reduzir desperdício doméstico |
| Entidade principal | Farol Urbano |

## Conteúdo avaliado

Texto integral, scorecard, extractability audit e trust signal audit. Schema, analytics e resultados em engines não foram fornecidos.

## Principais gaps

| Gap ID | Origem | Classificação | Seção | Problema |
|---|---|---|---|---|
| GAP-001 | extractability-audit | `[FATO]` | Introdução | Resposta principal dispersa. |
| GAP-002 | trust-signal-audit | `[FATO]` | Estatística | Fonte sem período ou população. |

## Plano por seção

| Action ID | Seção | Gap | Tipo de intervenção | Bloco sugerido | Impacto | Esforço | Prioridade | Critério de reavaliação |
|---|---|---|---|---|---|---|---:|---|
| ACT-001 | Introdução | GAP-001 | adicionar answer block | Definição curta seguida de três etapas | high | low | 1 | Bloco compreensível isoladamente e alinhado à intenção. |
| ACT-002 | Estatística | GAP-002 | adicionar evidência | Claim atômico com período, população e fonte | high | medium | 2 | Correspondência claim-fonte validada por humano. |

## Ações priorizadas

1. `[RECOMENDAÇÃO]` Bloquear o claim sem suporte.
2. `[RECOMENDAÇÃO]` Planejar a resposta direta.
3. `[RECOMENDAÇÃO]` Revisar autoria e limitações.

## Evidências necessárias

- Fonte primária para a estatística.
- Data de revisão editorial.
- Credencial verificável relacionada ao tema.

## Riscos

- Simplificar a introdução e remover ressalvas necessárias.
- Substituir uma fonte fraca por outra igualmente inadequada.
- Tratar o plano como texto final aprovado.

## Critérios de reavaliação

- Repetir extractability audit após a edição.
- Repetir trust signal audit após liberar a fonte.
- Recalcular scorecard com o mesmo protocolo.
