# Schema Opportunity

## Objetivo

Mapear oportunidades de dados estruturados sustentadas pelo conteúdo visível, com requisitos, riscos e critérios de validação.

`[FATO]` Dados estruturados devem representar o conteúdo visível e seguir a documentação aplicável da plataforma. Schema não garante ranking, citação, presença em IA ou exibição de recurso.

## Quando usar

- Depois de auditar conteúdo e entidades.
- Quando o ativo possui tipo, autoria, produto, serviço, processo, perguntas, avaliações ou dados próprios claramente observáveis.
- Antes de implementar ou revisar markup.
- Para alimentar um plano de otimização, não para substituir conteúdo.

Não usar para inventar FAQs, avaliações, preços, autores, etapas ou propriedades ausentes.

## Inputs

Mínimos:

- conteúdo visível fornecido;
- tipo de ativo;
- entidades identificadas;
- schema atual, quando houver;
- documentação oficial aplicável ou status `pending`.

Opcionais: entity map, trust signal audit, content brief, campos técnicos disponíveis e URLs canônicas.

## Processo

1. Confirmar conteúdo, tipo de ativo, entidade e escopo.
2. Identificar oportunidades candidatas:
   - `Article`;
   - `BlogPosting`;
   - `FAQPage`, quando as perguntas e respostas forem reais e elegíveis;
   - `HowTo`, quando houver processo claro;
   - `Product`, quando houver produto;
   - `Service`, quando houver serviço;
   - `Organization`;
   - `Person`;
   - `LocalBusiness`;
   - `BreadcrumbList`;
   - `Review` ou `AggregateRating`, somente com evidência legítima;
   - `Dataset`, quando houver dados próprios;
   - `QAPage`, quando o formato for aplicável.
3. Relacionar cada tipo ao conteúdo que o sustenta.
4. Listar propriedades essenciais e campos ausentes.
5. Consultar documentação oficial antes de recomendar implementação.
6. Classificar risco de marcação inadequada.
7. Priorizar por adequação, completude, risco e esforço.
8. Definir validação sintática, correspondência com conteúdo e revisão humana.
9. Registrar como `candidate`, `blocked`, `not_applicable` ou `ready_for_implementation`.

## Outputs

- oportunidade de schema;
- justificativa;
- conteúdo necessário;
- propriedades essenciais;
- campos ausentes;
- risco de marcação inadequada;
- prioridade;
- critério de validação.

## Critérios de qualidade

- Toda oportunidade corresponde ao conteúdo visível.
- A documentação oficial aplicável é identificada ou marcada como pendente.
- Propriedades não são inventadas.
- Reviews e ratings possuem evidência legítima.
- O output diferencia vocabulário Schema.org de elegibilidade em plataformas.
- Validação inclui sintaxe, correspondência factual e revisão humana.

## Erros comuns

- Recomendar `FAQPage` apenas porque o tema permite perguntas.
- Usar `HowTo` sem etapas executáveis.
- Marcar produto, serviço ou pessoa que não aparece no conteúdo.
- Criar avaliações ou agregados artificiais.
- Tratar validação sintática como prova de elegibilidade.
- Prometer impacto em AI Search.
