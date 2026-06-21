# Source ledger

Registro inicial das fontes que sustentam a arquitetura e a metodologia do GEO OS.

## Escala de confiabilidade

- **Alta:** documentação oficial, especificação ou paper revisado por pares.
- **Média:** preprint, curso institucional ou fonte primária ainda não consolidada.
- **Baixa:** material promocional, opinião ou dado sem método recuperável.
- **Síntese:** relatório derivado de múltiplas fontes; útil para descoberta, não para sustentar claim sozinho.

## Fontes externas

| ID | Fonte | Tipo | Uso no GEO OS | Acesso | Confiabilidade | Limitações |
|---|---|---|---|---|---|---|
| SRC-001 | [Agent Skills Specification](https://agentskills.io/specification) | especificação aberta | Contrato de `SKILL.md`, `name`, `description` e nome de diretório | 2026-06-21 | Alta | A implementação pode variar por produto. |
| SRC-002 | [OpenAI — Agent Skills](https://developers.openai.com/codex/skills) | documentação oficial | Skills focadas, progressive disclosure, scripts opcionais e descoberta em `.agents/skills` | 2026-06-21 | Alta | Comportamento do produto pode mudar. |
| SRC-003 | [OpenAI — Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md) | documentação oficial | Uso de `AGENTS.md`, escopo e precedência | 2026-06-21 | Alta | Aplicável ao Codex, não a toda plataforma de agentes. |
| SRC-004 | [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) | documentação oficial | Limite de promessa e relação entre fundamentos de SEO e AI features | 2026-06-21 | Alta | Descreve Google Search; não generalizar para outras engines. |
| SRC-005 | [Google Search Central — Introduction to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | documentação oficial | Dados estruturados como explicitação de significado e correspondência com a página | 2026-06-21 | Alta | Não afirma garantia de citação em AI Search. |
| SRC-006 | [Google Search Central — General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | documentação oficial | Política contra markup enganoso e limites de elegibilidade | 2026-06-21 | Alta | Foco em recursos do Google Search. |
| SRC-007 | [Schema.org Documentation](https://schema.org/docs/documents.html) | vocabulário oficial | Tipos e propriedades para representação de entidades | 2026-06-21 | Alta | Uso do vocabulário não implica suporte por uma engine específica. |
| SRC-008 | [Aggarwal et al. — GEO: Generative Engine Optimization](https://doi.org/10.1145/3637528.3671900) | paper revisado por pares, KDD 2024 | Formulação de GEO, métricas de visibilidade, benchmark e variabilidade por domínio | 2026-06-21 | Alta | Ambiente experimental e engines evoluem; não converter efeito médio em garantia. |
| SRC-009 | [Liu et al. — Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) | paper, EMNLP Findings 2023 | Separação entre presença de citação e suporte real ao claim | 2026-06-21 | Alta | Engines avaliadas representam um período específico. |
| SRC-010 | [Yu et al. — Structural Feature Engineering for GEO](https://arxiv.org/abs/2603.29979) | preprint | Hipótese de estrutura macro, meso e micro como variável de citação | 2026-06-21 | Média | Preprint recente; resultados precisam de replicação independente. |
| SRC-011 | [A Measurement Framework for GEO](https://arxiv.org/abs/2604.25707) | preprint | Distinção operacional entre seleção e absorção | 2026-06-21 | Média | Preprint recente; framework tratado como evidência emergente. |

## Fontes privadas consultadas

As entradas abaixo registram influência metodológica sem expor caminho local, conteúdo fechado ou material proprietário.

| ID | Fonte | Tipo | Publicável? | Uso no GEO OS | Acesso | Confiabilidade | Limitações |
|---|---|---|---|---|---|---|---|
| LOC-001 | Materiais privados de curso GEO | curso institucional | Não | AI question map, entity inventory e padrão de answer units | 2026-06-21 | Média | Claims amplos exigem triangulação; arquivos originais não integram o repositório. |
| LOC-002 | Exercício privado de content mapping | exemplo didático | Não | Inspiração para campos de templates | 2026-06-21 | Média | Exemplo fechado não foi reproduzido; exemplos públicos foram criados do zero. |
| LOC-003 | Síntese privada de pesquisa GEO | síntese de pesquisa | Não | Arquitetura modular, riscos e fontes candidatas | 2026-06-21 | Síntese | Marcadores internos não são referências finais; claims usados foram rechecados. |
| LOC-004 | Relatório estratégico privado | relatório de síntese | Não | Hipóteses para backlog | 2026-06-21 | Síntese | Números voláteis e fontes de vendors não foram incorporados como regras. |
| LOC-005 | Histórico privado de briefing | contexto de projeto | Não | Requisitos e decisões de arquitetura | 2026-06-21 | Contextual | Não é fonte técnica independente. |
| LOC-006 | Síntese privada do curso, versão v3 | material didático com recursos visuais | Não | Extraibilidade, relações, autoria, fontes, frescor, metodologia, transparência e limites | 2026-06-21 | Síntese | Contém imagens originais incorporadas e não deve ser publicada; estatísticas exigem fonte primária. |

## Decisões derivadas

| ID | Classificação | Decisão | Base |
|---|---|---|---|
| DEC-001 | `[FRAMEWORK PRÓPRIO]` | Organizar GEO em recuperabilidade, selecionabilidade, citabilidade, absorção, autoridade e mensuração. | SRC-004, SRC-008, SRC-009, SRC-011 |
| DEC-002 | `[INFERÊNCIA]` | Usar `skills/` como fonte canônica e `.agents/skills/` como camada de descoberta. | SRC-001, SRC-002 |
| DEC-003 | `[FRAMEWORK PRÓPRIO]` | Aplicar rubricas 0–4 com pesos e cobertura de evidência. | Necessidade operacional do projeto; inspirada em LOC-001 e LOC-003 |
| DEC-004 | `[INFERÊNCIA]` | Avaliar critérios esperados em benchmarks, não respostas exatas. | SRC-008, SRC-009 e variabilidade observada das engines |
| DEC-005 | `[FATO]` | Dados estruturados devem corresponder ao conteúdo da página e não garantem exibição. | SRC-005, SRC-006 |
| DEC-006 | `[FRAMEWORK PRÓPRIO]` | Usar intent map como contrato entre demanda, página, entidades, evidências e formato de resposta. | LOC-001, LOC-002 e síntese operacional do projeto |
| DEC-007 | `[FRAMEWORK PRÓPRIO]` | Separar confiabilidade da fonte, confiança na relação claim-evidência, uso permitido e risco no evidence ledger. | SRC-009 e necessidade de governança factual |
| DEC-008 | `[INFERÊNCIA]` | Descrever a evidência necessária antes de sugerir uma fonte específica em citation engineering. | SRC-009 e política de prevenção de citation theatre |
| DEC-009 | `[FRAMEWORK PRÓPRIO]` | Criar answer blocks somente após mapear intenção e liberar claims no evidence ledger. | LOC-001, LOC-002, DEC-006 e DEC-007 |
| DEC-010 | `[FRAMEWORK PRÓPRIO]` | Usar o content brief como contrato central enriquecido por topical authority e competitor analysis. | DEC-006, DEC-007, DEC-008 e necessidade operacional do projeto |
| DEC-011 | `[FRAMEWORK PRÓPRIO]` | Avaliar topical authority por entidades, relações, cobertura, profundidade, evidência e links, não por volume de páginas. | SRC-005, SRC-007 e síntese metodológica |
| DEC-012 | `[INFERÊNCIA]` | Comparar concorrentes apenas por páginas equivalentes e critérios observáveis reduz conclusões inválidas. | Política de evidência do GEO OS |
| DEC-013 | `[FRAMEWORK PRÓPRIO]` | Consolidar avaliação em scorecard de 16 dimensões com nota justificada, cobertura e denominador ajustado. | Rubricas existentes, LOC-006 e necessidade operacional do projeto |
| DEC-014 | `[INFERÊNCIA]` | Avaliar autonomia, contexto, granularidade e dependência visual é mais útil do que usar tamanho ou presença de bullets como proxy de extraibilidade. | LOC-001, LOC-006 e módulos de answer blocks |
| DEC-015 | `[FRAMEWORK PRÓPRIO]` | Tratar confiança como verificabilidade observável de autoria, fonte, frescor, método, transparência e consistência. | SRC-009, LOC-006 e política de evidência |
| DEC-016 | `[FRAMEWORK PRÓPRIO]` | Exigir origem do gap, ação, impacto, esforço, risco e critério de reavaliação em toda otimização. | Evaluation Layer e necessidade de ciclo fechado |
| DEC-017 | `[INFERÊNCIA]` | Planejar a reescrita antes de produzir o texto reduz o risco de apagar ressalvas, inventar evidência ou expandir conteúdo sem gap real. | DEC-007, DEC-008, DEC-009 e Evaluation Layer |
| DEC-018 | `[FATO]` | Oportunidades de schema devem representar conteúdo visível e não garantem exibição. | SRC-005, SRC-006 e SRC-007 |
| DEC-019 | `[FRAMEWORK PRÓPRIO]` | Publicar apenas síntese autoral, templates próprios e exemplos fictícios; fontes privadas permanecem fora do Git. | Política de publicação e limites de direitos autorais |
| DEC-020 | `[INFERÊNCIA]` | Medição GEO deve complementar analytics e SEO, e não substituir instrumentos existentes. | LOC-006 e limites metodológicos do projeto |

## Fila de fontes para pesquisas estratégicas

Entradas `PENDING` são placeholders de pesquisa, não sustentam claims até serem preenchidas e revisadas.

| ID | Escopo | Fonte necessária | Tipo preferido | Status | Uso previsto | Risco |
|---|---|---|---|---|---|---|
| PENDING-TA-001 | Autoridade tópica | Documentação ou paper sobre cobertura semântica e relações de entidades | fonte primária ou paper | pending | Revisar critérios de topical authority | Não usar como claim público antes da revisão |
| PENDING-TA-002 | Links internos | Documentação oficial sobre descoberta e arquitetura de informação | documentação oficial | pending | Revisar critérios de links internos | Evitar transformar recomendação em fator de ranking garantido |
| PENDING-COMP-001 | Concorrente analisado | URL e versão da página concorrente | fonte primária | pending | Competitor gap analysis | Registrar acesso e preservar evidência |
| PENDING-COMP-002 | Autoria e confiança | Página de autor, organização ou política editorial | fonte primária | pending | Avaliar authorship/trust | Ausência não prova baixa qualidade |
| PENDING-COMP-003 | Frescor | Data publicada, modificada ou evidência de atualização | fonte primária | pending | Avaliar freshness | Não usar aparência visual como data |
| PENDING-SCHEMA-001 | Schema opportunity | Documentação oficial do tipo de structured data aplicável | documentação oficial | pending | Recomendar apenas markup compatível | Schema não garante citação ou exibição |
| PENDING-TRUST-001 | Autoria e credenciais | Perfil oficial, currículo, registro profissional ou produção verificável | fonte primária | pending | Confirmar expertise relevante | Credencial declarada não equivale a credencial verificada |
| PENDING-TRUST-002 | Metodologia | Método, amostra, período, critérios e limitações do dado citado | fonte primária | pending | Avaliar reprodutibilidade e risco | Ausência de método pode bloquear claims materiais |
| PENDING-TRUST-003 | Conflitos de interesse | Disclosure editorial, vínculo comercial ou financiamento | fonte primária | pending | Avaliar transparência | Ausência no input deve ser registrada como não observada |

## Manutenção

Ao adicionar claim metodológico:

1. criar ou atualizar uma entrada;
2. registrar data de acesso;
3. classificar confiabilidade;
4. declarar limitações;
5. ligar a fonte à decisão correspondente.

Antes de publicação:

1. remover caminhos pessoais;
2. confirmar se cada fonte privada está marcada como não publicável;
3. não copiar trechos extensos, imagens, slides ou exemplos exclusivos;
4. manter apenas síntese transformada e autoral.
