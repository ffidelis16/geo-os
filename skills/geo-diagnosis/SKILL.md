---
name: geo-diagnosis
description: Diagnostica prontidão GEO no escopo de domínio, site ou ecossistema de conteúdo, não um único ativo colado. Use para baseline de AI Search, avaliação de citabilidade e backlog priorizado baseado em evidências.
---

# Diagnóstico GEO

## Objetivo

Avaliar maturidade GEO sem prometer resultados de ranking ou citação. Separar problemas de recuperabilidade, estrutura de resposta, evidência, entidades e mensuração.

## Quando usar

- Antes de uma estratégia ou sprint GEO.
- Ao revisar páginas prioritárias, templates ou um domínio.
- Quando o cliente precisa de baseline, scorecards e prioridades.
- Após mudanças relevantes para comparar evolução metodológica.

## Quando não usar

- Para garantir inclusão em uma engine.
- Como substituto de auditoria técnica de SEO completa.
- Quando não há páginas, fontes ou escopo minimamente definidos.
- Para atribuir causalidade a uma única observação.

## Inputs

Mínimos:

- objetivo de negócio;
- URLs ou artefatos prioritários;
- marca, categoria e locale;
- período do diagnóstico.

Opcionais: concorrentes, analytics, Search Console, logs, schema, benchmark anterior, entrevistas e políticas editoriais.

## Processo

1. Definir escopo, unidade de análise e limitações.
2. Inventariar páginas, entidades, intents e fontes disponíveis.
3. Registrar evidências com `[FATO]`; marcar deduções e lacunas.
4. Avaliar os critérios de `rubrics/geo-readiness.yaml`.
5. Aplicar rubricas complementares quando houver evidência suficiente.
6. Separar achados técnicos, editoriais, semânticos e de mensuração.
7. Priorizar ações por impacto esperado, confiança, esforço e dependências.
8. Preencher `templates/audit-report.md` e registrar limitações.

Não pontuar critérios sem evidência. Não transformar ausência de acesso em falha do site.

## Outputs

- relatório de auditoria;
- scorecards com evidências;
- inventário de lacunas;
- backlog priorizado;
- plano de re-teste.

## Critérios de qualidade

- Escopo e data explícitos.
- Cada score aponta para evidência.
- Fatos, inferências e hipóteses estão separados.
- Prioridades derivam de problemas observados.
- Promessas e limitações estão visíveis.
- Outro analista consegue reproduzir o raciocínio.

## Erros comuns

- Avaliar somente homepage ou um artigo e generalizar para o domínio.
- Somar scores sem verificar evidência.
- Confundir SEO técnico, menção de marca e citação de URL.
- Copiar estatísticas de mercado sem data e fonte.
- Criar lista de boas práticas sem diagnóstico causal.
