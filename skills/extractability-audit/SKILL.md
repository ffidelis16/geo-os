---
name: extractability-audit
description: Use quando um ativo fornecido precisa ser auditado apenas quanto a estrutura e extraibilidade, incluindo respostas diretas, definições, blocos autossuficientes, headings, listas, tabelas, passos, FAQs, dados citáveis, ambiguidades e dependência visual. É uma subdimensão que alimenta o geo-scorecard.
---

# Extractability Audit

## Objetivo

Identificar o que pode ser extraído com segurança, o que depende de contexto e como reestruturar o conteúdo em unidades reutilizáveis.

Ler `modules/extractability-audit.md`. Usar `templates/extractability-audit-template.md`.

## Quando usar

- Antes de um content refresh.
- Quando o conteúdo é longo ou ambíguo.
- Quando resumos gerados perdem contexto.
- Para alimentar `geo-scorecard` e `answer-blocks`.

## Quando não usar

- Sem conteúdo fornecido.
- Para afirmar como uma engine específica processou a página.
- Para reduzir todo texto a fragmentos curtos.
- Como avaliação de confiança ou verdade factual completa.

## Inputs

- Conteúdo ou trecho.
- Target intent, público e entidade principal.
- Estrutura fornecida.
- Evidence ledger e content brief, quando disponíveis.
- Outputs de `citation-engineering` e `competitor-analysis`, quando relevantes.

## Outputs

- Blocos encontrados e ausentes.
- Seções e trechos frágeis.
- Answer block e schema opportunities.
- Recomendações de reestruturação.
- Prioridades e limitações.

## Processo

1. Confirmar conteúdo e escopo.
2. Consultar `intent-map` e `entity-map`.
3. Inventariar definições, listas, tabelas, comparações, passos, FAQs, claims e dados.
4. Testar autonomia, contexto, evidência e ambiguidade.
5. Marcar dependência visual e texto contínuo.
6. Propor blocos para `answer-blocks`.
7. Encaminhar claims frágeis para `citation-engineering`.
8. Registrar sinais no `geo-scorecard`.

## Restrições

- Não inventar elementos fora do conteúdo.
- Não confundir extraibilidade com tamanho.
- Não sugerir schema sem conteúdo visível.
- Não remover ressalvas para obter bloco mais curto.
- Não afirmar que URL foi rastreada.

## Critérios de qualidade

- Todo problema aponta para localização observada.
- Blocos sugeridos atendem intents reais.
- Recomendações preservam contexto e evidência.
- Limitações de input estão explícitas.
- Output pode ser executado por editor.

## Modos de falha

- Checklist de formatos sem diagnóstico.
- Nota alta por haver bullets.
- FAQs artificiais.
- Tabelas sem base comparável.
- Blocos que não fazem sentido isoladamente.

## Exemplo

Um parágrafo com três claims, duas entidades e uma fonte no final deve ser dividido em unidades; cada claim recebe contexto e evidência adjacente, sem apagar a ressalva.

## Erros comuns

- Impor answer capsule a todas as seções.
- Tratar heading genérico como pergunta.
- Ignorar referências como "isso" e "essa solução".
- Sugerir reescrita sem prioridade.
