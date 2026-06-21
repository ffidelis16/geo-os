# GEO OS Orchestrator

## Objetivo

Classificar pedidos em linguagem natural e selecionar o menor fluxo suficiente entre as skills, módulos e templates existentes do GEO OS.

`[FRAMEWORK PRÓPRIO]` O orquestrador é um roteador operacional. Ele não executa todas as skills, não reescreve conteúdo final e não substitui julgamento humano.

## Quando usar

- Quando o usuário sabe o resultado desejado, mas não a skill adequada.
- Quando um pedido pode exigir uma sequência curta de skills.
- Para registrar lacunas antes de iniciar uma análise.
- Para padronizar output path, templates e próximo comando.

## Inputs

Mínimos:

- pedido original;
- tipo de ativo ou ausência de ativo;
- resultado desejado.

Opcionais:

- conteúdo ou artefato;
- target intent;
- público;
- entidade principal;
- fontes e evidence ledger;
- auditorias e scorecards;
- locale;
- concorrentes;
- restrições editoriais ou regulatórias.

## Processo

1. Preservar o texto do pedido.
2. Identificar verbo principal: auditar, planejar, melhorar, mapear, testar, atualizar ou consultar.
3. Verificar se existe conteúdo, evidência ou auditoria anterior.
4. Classificar em um único fluxo principal.
5. Selecionar o menor fluxo suficiente.
6. Adicionar skill anterior somente quando ela desbloquear um input essencial.
7. Registrar inputs faltantes sem inventá-los.
8. Indicar templates e `outputs/<slug>/workflow-selection.md`.
9. Explicar fluxos descartados.
10. Entregar próximo comando operacional pronto para Codex.

Se o pedido for ambíguo, escolher a rota mais conservadora e declarar a suposição. Não executar todas as skills por padrão.

## Matriz de roteamento

| Fluxo | Gatilho principal | Skills mínimas | Expansão condicional | Templates principais |
|---|---|---|---|---|
| `audit-existing-content` | avaliar conteúdo existente | `extractability-audit` → `trust-signal-audit` → `geo-scorecard` | remover auditoria já fornecida | `extractability-audit-template.md`, `trust-signal-audit-template.md`, `geo-scorecard-template.md` |
| `plan-new-content` | criar conteúdo ainda inexistente | `content-brief` | `entity-map` se entidades não estiverem normalizadas; `topical-authority` para cluster; `citation-engineering` somente com claims | `content-brief-template.md`, `entity-map.csv`, `evidence-ledger.csv` |
| `improve-existing-content` | corrigir ativo com gaps conhecidos | `rewrite-plan` | executar auditorias apenas se os gaps não foram fornecidos | `rewrite-plan-template.md`, `optimization-cycle-template.md` |
| `create-entity-map` | normalizar entidades e relações | `entity-map` | nenhuma por padrão | `entity-map.csv` |
| `create-answer-blocks` | produzir unidades de resposta | `answer-blocks` | bloquear até existir intent e evidência liberada | `answer-block-template.md`, `evidence-ledger.csv` |
| `map-evidence-citations` | mapear claims, provas e fontes | `citation-engineering` | nenhuma por padrão | `evidence-ledger.csv`, `citation-opportunity-map.csv` |
| `plan-ai-search-benchmark` | desenhar ou registrar benchmark | `ai-search-testing` | nenhuma por padrão | `ai-search-benchmark.csv` |
| `prepare-content-refresh` | atualizar, consolidar ou revisar ativo antigo | `content-refresh` | auditoria somente quando gaps não estão definidos | `content-refresh-plan.csv`, `optimization-cycle-template.md` |
| `map-schema-opportunity` | avaliar markup sustentado pelo visível | `schema-opportunity` | trust audit se autoria ou organização forem materiais e não avaliadas | `schema-opportunity-map.csv` |
| `consult-methodology` | explicar método sem produzir artefato | nenhuma skill executora | apontar documentação ou módulo relevante | `workflow-selection-template.md` |

## Regras de dependência

- `geo-scorecard` consolida auditorias; não deve ser o primeiro diagnóstico de um conteúdo bruto.
- `rewrite-plan` exige gaps observáveis; não deve inventar auditoria.
- `answer-blocks` exige intenção, entidade e claims liberados.
- `citation-engineering` descreve evidência necessária antes de sugerir fonte específica.
- `schema-opportunity` representa conteúdo visível e não implementa markup.
- `content-refresh` decide ações sobre ativo existente; não serve para artigo novo.
- `consult-methodology` não aciona skills operacionais.

## Outputs

Preencher `templates/workflow-selection-template.md` com:

- tipo de demanda;
- fluxo selecionado;
- fluxos descartados;
- justificativa;
- skills em ordem;
- inputs mínimos e inputs faltantes;
- templates;
- output path;
- limitações;
- próximo comando.

## Critérios de qualidade

- Um fluxo principal por pedido.
- Sequência menor que resolve o objetivo declarado.
- Skills e templates existem no repositório.
- Inputs faltantes são acionáveis e específicos.
- Etapas condicionais não são apresentadas como obrigatórias.
- O comando final pode ser colado no Codex.
- O overlay privado, quando disponível, não aparece como fonte pública.

## Erros comuns

- Selecionar auditoria completa para uma pergunta documental.
- Recomendar todas as skills “por segurança”.
- Confundir criação nova com refresh.
- Recomendar answer blocks sem evidência.
- Pular auditorias e produzir rewrite plan baseado em impressão.
- Usar URL como prova de que o conteúdo foi acessado.
- Não reescrever conteúdo final virar apenas uma nota, mas entregar texto final mesmo assim.
