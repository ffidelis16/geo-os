# Exemplo fictício de optimization cycle

## Auditoria de origem

| Campo | Valor |
|---|---|
| Cycle ID | EXAMPLE-CYCLE-001 |
| Ativo | Guia fictício sobre desperdício doméstico |
| Versão inicial | 0.1 |
| Auditorias | scorecard, extraibilidade e confiança |

## Gaps priorizados

| Gap ID | Origem | Impacto | Risco | Prioridade |
|---|---|---|---|---:|
| GAP-001 | extractability-audit | high | medium | 1 |
| GAP-002 | trust-signal-audit | high | high | 2 |

## Ações planejadas

| Action ID | Gap ID | `[RECOMENDAÇÃO]` | Owner | Esforço | Status |
|---|---|---|---|---|---|
| ACT-001 | GAP-001 | Criar bloco direto preservando ressalvas. | editor | low | approved |
| ACT-002 | GAP-002 | Localizar fonte primária ou remover claim. | pesquisador | medium | blocked |

## Critérios de sucesso

| Action ID | Baseline | Critério observável |
|---|---|---|
| ACT-001 | resposta dispersa | bloco autossuficiente validado na auditoria |
| ACT-002 | fonte insuficiente | claim sustentado ou removido |

## Reavaliação

- **Gatilho:** após edição e revisão factual.
- **Auditorias:** extractability, trust e scorecard.
- **Limitação:** nenhuma engine foi testada.

## Decisão

- **Decisão:** revisar
- **Justificativa:** ACT-001 pode avançar; ACT-002 permanece bloqueada.
- **Evidência:** auditorias e evidence ledger.
- **Próxima ação:** obter fonte primária.
