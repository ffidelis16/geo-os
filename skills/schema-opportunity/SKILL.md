---
name: schema-opportunity
description: Use quando conteúdo e entidades já auditados precisam ser avaliados para oportunidades legítimas de dados estruturados, propriedades ausentes, riscos e critérios de validação.
---

# Schema Opportunity

## Objetivo

Mapear dados estruturados possíveis sem implementar markup nem prometer impacto em AI Search.

Ler `modules/schema-opportunity.md`. Usar `templates/schema-opportunity-map.csv` e `templates/optimization-cycle-template.md`.

## Quando usar

- Depois da auditoria de conteúdo e entidades.
- Antes de implementar ou revisar schema.
- Quando há conteúdo visível compatível com tipos conhecidos.
- Para registrar campos ausentes e riscos.

## Quando não usar

- Sem conteúdo visível.
- Para inventar FAQ, review, rating, autor ou processo.
- Para garantir ranking, citação ou rich result.
- Como substituto da documentação oficial.

## Inputs

- Conteúdo visível e tipo de ativo.
- Entidades identificadas.
- Schema atual, quando houver.
- Documentação oficial aplicável ou status pendente.
- Outputs de entity map, trust audit e content brief.

## Outputs

- Tipo candidato e justificativa.
- Conteúdo e propriedades necessários.
- Campos ausentes.
- Risco, prioridade e status.
- Critérios de validação.

## Processo

1. Confirmar ativo, conteúdo e entidade.
2. Selecionar tipos candidatos do módulo.
3. Relacionar cada tipo ao conteúdo visível.
4. Listar propriedades essenciais e ausentes.
5. Verificar documentação oficial aplicável.
6. Classificar risco e prioridade.
7. Definir validação sintática, factual e humana.
8. Registrar status da oportunidade.

## Restrições

- Não implementar markup nesta skill.
- Não inventar propriedades ou evidências.
- Não recomendar reviews artificiais.
- Não confundir Schema.org com elegibilidade de plataforma.
- Não prometer presença em IA.

## Critérios de qualidade

- Toda oportunidade é sustentada pelo conteúdo.
- Campos obrigatórios e ausentes estão claros.
- Fonte oficial está registrada ou pendente.
- Riscos de marcação inadequada são visíveis.
- Critérios de validação excedem a sintaxe.

## Modos de falha

- FAQ para conteúdo sem perguntas reais.
- HowTo sem processo executável.
- Review sem evidência legítima.
- Tipo escolhido apenas por popularidade.
- Validação reduzida a ferramenta sintática.

## Exemplo

Uma página de serviço pode ser candidata a `Service` e `Organization` se o conteúdo identifica oferta e responsável. Propriedades não observadas ficam como campos ausentes; não são inventadas.

## Erros comuns

- Marcar entidades que não aparecem.
- Ignorar conteúdo visível divergente.
- Recomendar AggregateRating sem base.
- Tratar schema como atalho GEO.
