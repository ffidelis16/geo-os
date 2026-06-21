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

## Materiais locais fornecidos

| ID | Arquivo | Tipo | Uso no GEO OS | Acesso | Confiabilidade | Limitações |
|---|---|---|---|---|---|---|
| LOC-001 | `C:\Users\ffide\Downloads\GEO Course.pdf` e `.docx` | curso institucional | AI question map, entity inventory e padrão de answer units | 2026-06-21 | Média | Material didático; alguns claims amplos exigem triangulação. |
| LOC-002 | `C:\Users\ffide\Downloads\Sample Content Mapping Solution.pdf` e `.docx` | exemplo didático | Estrutura de templates e campos de mapeamento | 2026-06-21 | Média | Exemplo setorial fictício; não usar números como benchmark geral. |
| LOC-003 | `C:\Users\ffide\Downloads\deep-research-report (19).md` | síntese de pesquisa | Arquitetura modular, riscos, roadmap e fontes candidatas | 2026-06-21 | Síntese | Tokens de citação originais não são referências finais; claims foram rechecados quando usados. |
| LOC-004 | `C:\Users\ffide\Downloads\compass_artifact_wf-4b2a172a-02e5-4ba2-a2ce-de4451a5701e_text_markdown.md` | relatório estratégico | Táticas e hipóteses para backlog futuro | 2026-06-21 | Síntese | Contém números voláteis e fontes de vendors; não incorporados como regras nas rubricas. |
| LOC-005 | `C:\Users\ffide\.codex\attachments\017e5b76-d3b4-447b-94b0-d06f315db013\pasted-text.txt` | histórico de conversa e briefing | Requisitos, decisões de arquitetura e limites do MVP | 2026-06-21 | Contextual | Não é fonte técnica independente. |

## Decisões derivadas

| ID | Classificação | Decisão | Base |
|---|---|---|---|
| DEC-001 | `[FRAMEWORK PRÓPRIO]` | Organizar GEO em recuperabilidade, selecionabilidade, citabilidade, absorção, autoridade e mensuração. | SRC-004, SRC-008, SRC-009, SRC-011 |
| DEC-002 | `[INFERÊNCIA]` | Usar `skills/` como fonte canônica e `.agents/skills/` como camada de descoberta. | SRC-001, SRC-002 |
| DEC-003 | `[FRAMEWORK PRÓPRIO]` | Aplicar rubricas 0–4 com pesos e cobertura de evidência. | Necessidade operacional do projeto; inspirada em LOC-001 e LOC-003 |
| DEC-004 | `[INFERÊNCIA]` | Avaliar critérios esperados em benchmarks, não respostas exatas. | SRC-008, SRC-009 e variabilidade observada das engines |
| DEC-005 | `[FATO]` | Dados estruturados devem corresponder ao conteúdo da página e não garantem exibição. | SRC-005, SRC-006 |

## Manutenção

Ao adicionar claim metodológico:

1. criar ou atualizar uma entrada;
2. registrar data de acesso;
3. classificar confiabilidade;
4. declarar limitações;
5. ligar a fonte à decisão correspondente.
