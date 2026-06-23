---
name: geo-os-orchestrator
description: Use quando um pedido em linguagem natural precisa ser classificado e roteado para o menor fluxo suficiente entre as skills, módulos e templates existentes do GEO OS.
---

# GEO OS Orchestrator

## Objetivo

Transformar um pedido em um plano operacional curto: fluxo selecionado, skills em ordem, inputs faltantes, templates, output path e próximo comando.

Ler `modules/geo-os-orchestrator.md` e preencher `templates/workflow-selection-template.md`.

## Quando usar

- Quando o usuário descreve um objetivo sem saber qual skill acionar.
- Quando há duas ou mais rotas plausíveis.
- Antes de um trabalho GEO com múltiplas etapas.
- Para reduzir um pedido amplo ao menor fluxo suficiente.

## Quando não usar

- Quando o usuário já escolheu uma skill única e forneceu seus inputs.
- Para executar todas as skills por padrão.
- Para substituir auditoria, planejamento, redação ou julgamento humano.
- Para criar app, API, crawler, scraping ou automação externa.

## Inputs

Mínimos:

- pedido original;
- ativo ou tipo de ativo, quando houver;
- resultado desejado.

Opcionais: conteúdo, URL, intenção, público, entidade, fontes, auditorias, concorrentes, locale, prazo e restrições.

## Processo

1. Preservar o pedido original.
2. Classificar a demanda em um dos dez fluxos canônicos do módulo, considerando suas expansões condicionais.
3. Escolher o menor fluxo suficiente e descartar etapas sem necessidade demonstrada.
4. Mapear somente skills existentes e ordenar dependências reais.
5. Separar inputs disponíveis de inputs faltantes.
6. Se faltar input essencial, não iniciar a skill dependente; indicar o próximo input mínimo.
7. Indicar templates e uma pasta `outputs/<slug>/`.
8. Registrar suposições, limitações e risco de excesso.
9. Entregar um próximo comando operacional pronto para Codex.

Não executar todas as skills por padrão. Não reescrever conteúdo final.

## Outputs

- workflow selection preenchido;
- fluxo e justificativa;
- skills em ordem;
- inputs necessários e inputs faltantes;
- templates e output path;
- limitações;
- próximo comando operacional.

## Critérios de qualidade

- Seleciona exatamente um fluxo principal.
- Usa somente skills existentes.
- Não antecipa trabalho bloqueado por falta de input.
- Explica por que fluxos maiores foram descartados.
- Mantém overlay privado como contexto complementar.
- Não promete ranking, citação, tráfego ou presença.
- Separa `[FATO]`, `[INFERÊNCIA]`, `[HIPÓTESE]` e `[RECOMENDAÇÃO]` quando aplicável.

## Erros comuns

- Virar uma super-skill que executa o programa inteiro.
- Confundir roteamento com auditoria.
- Recomendar scorecard sem auditorias ou evidências.
- Incluir answer blocks antes de intenção e claims liberados.
- Indicar skill inexistente ou template incompatível.
- Inventar inputs em vez de registrar lacunas.
- Entregar explicação sem próximo comando.
