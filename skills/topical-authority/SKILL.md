---
name: topical-authority
description: Use quando for necessário mapear cobertura temática por entidade principal, subentidades, relações, perguntas, profundidade, sinais de confiança, evidências, clusters, links internos e prioridade editorial.
---

# Topical Authority

## Objetivo

Produzir um mapa de cobertura coerente que alimente content briefs e impeça que "autoridade" seja reduzida a volume de artigos.

Ler `modules/topical-authority.md`. Usar `templates/topical-authority-map.csv`.

## Quando usar

- Antes de planejar clusters.
- Quando faltam páginas de suporte para uma entidade.
- Ao encontrar cobertura superficial, duplicada ou conflitante.
- Para priorizar briefs dentro de um território.

## Quando não usar

- Para justificar publicação em massa.
- Sem uma entidade principal e fronteira temática.
- Como score de autoridade externa.
- Para criar páginas por variação de keyword.

## Inputs

- Entity map e entidade principal.
- Intent map e perguntas recorrentes.
- Inventário de páginas.
- Evidence ledger.
- Competitor analysis, quando disponível.

## Outputs

- Subentidades e relações.
- Perguntas e intents.
- Status de cobertura e profundidade.
- Trust signals e evidências.
- Oportunidades de cluster.
- Links internos e prioridades.
- Inputs para `content-brief`.

## Processo

1. Confirmar entidade principal, audiência, locale e fronteira.
2. Consultar `modules/intent-map.md` e o entity map.
3. Mapear subentidades e relações direcionais dentro da página, entre páginas e com fontes externas.
4. Relacionar perguntas e estágios de decisão.
5. Auditar cobertura e profundidade.
6. Definir trust signals e evidências necessárias.
7. Identificar clusters sem duplicação.
8. Sugerir links internos semânticos.
9. Priorizar lacunas.
10. Entregar prioridades para `content-brief`.

## Restrições

- Não usar número de URLs como proxy de autoridade.
- Não propor página sem intenção, relação e papel claros.
- Não declarar cobertura suficiente sem evidência.
- Não criar clusters que contradizem páginas canônicas.
- Não inferir confiança somente por backlinks ou menções.

## Critérios de qualidade

- Fronteira e entidade principal são explícitas.
- Relações justificam cada tópico.
- Relações locais, internas e externas permanecem coerentes.
- Cobertura e profundidade usam estados controlados.
- Evidências e trust signals são verificáveis.
- Clusters reduzem lacunas sem criar redundância.
- Prioridades podem virar briefs.

## Modos de falha

- O mapa vira uma taxonomia genérica.
- Keywords substituem entidades e relações.
- Todo gap recebe prioridade alta.
- Profundidade é confundida com extensão.
- Links sugeridos não representam relações.

## Exemplo

Para "gestão financeira de clínicas", mapear clínica, fluxo de caixa, faturamento, convênios, inadimplência e conciliação; relacionar perguntas por decisão; classificar cobertura; exigir fontes regulatórias quando necessário; priorizar lacunas que alimentam briefs.

## Erros comuns

- Copiar clusters de concorrentes.
- Ignorar locale e regulação.
- Criar páginas sem owner ou atualização.
- Não registrar conteúdo duplicado ou conflitante.
