---
name: entity-map
description: Cria e normaliza mapas de entidades, aliases, relações, URLs canônicas e fontes de corroboração. Use quando houver ambiguidade de marca, inconsistência semântica, planejamento de schema ou arquitetura de conteúdo orientada a entidades.
---

# Mapa de entidades

## Objetivo

Representar pessoas, organizações, produtos, conceitos, lugares e relações de forma consistente e verificável para reduzir ambiguidade entre site, conteúdo, dados estruturados e fontes externas.

## Quando usar

- Ao iniciar diagnóstico ou estratégia GEO.
- Antes de implementar schema ou reorganizar arquitetura de conteúdo.
- Quando nomes, produtos, autores ou categorias aparecem de formas conflitantes.
- Para mapear relações necessárias a briefs e answer units.

## Quando não usar

- Para inventar entidades, aliases ou relações sem fonte.
- Para criar Wikipedia ou Wikidata sem notoriedade e referências adequadas.
- Como prova de que uma engine reconhece ou recomendará a entidade.

## Inputs

Mínimos:

- nome oficial da organização ou projeto;
- URLs canônicas disponíveis;
- lista inicial de produtos, pessoas, categorias e locais;
- locale.

Opcionais: schema existente, perfis oficiais, bases públicas, documentos legais, guidelines de marca, sitemaps e fontes externas.

## Processo

1. Definir a entidade raiz e o escopo do grafo.
2. Extrair entidades observadas sem normalizar prematuramente.
3. Classificar tipo e atribuir identificador interno estável.
4. Definir nome canônico, aliases válidos e termos que não devem ser usados.
5. Registrar URL canônica, definição e fonte de corroboração.
6. Modelar relações direcionais, propriedade e dependências.
7. Marcar conflitos, ambiguidades e evidências ausentes.
8. Preencher `templates/entity-map.csv`.
9. Revisar consistência com conteúdo visível e schema; não recomendar markup oculto.

## Outputs

- mapa de entidades em CSV;
- regras de nomenclatura;
- relações prioritárias;
- lista de conflitos e lacunas;
- recomendações de alinhamento entre conteúdo e dados estruturados.

## Critérios de qualidade

- Cada entidade tem ID, nome canônico e tipo.
- Aliases são observados ou oficialmente autorizados.
- Relações têm direção e evidência.
- Claims de identidade não dependem de uma única fonte promocional quando há alternativa primária.
- Ambiguidades e contradições permanecem visíveis.
- O mapa pode ser atualizado sem trocar IDs existentes.

## Erros comuns

- Tratar palavra-chave como entidade sem identidade própria.
- Criar aliases por conveniência editorial.
- Misturar organização, produto e categoria no mesmo registro.
- Usar `sameAs` para páginas que não identificam a mesma entidade.
- Declarar relações no schema que não aparecem no conteúdo.
