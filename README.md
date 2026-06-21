# GEO OS

GEO OS é um sistema operacional modular, baseado em arquivos, para estudar, auditar e estruturar conteúdo orientado a Generative Engine Optimization, visibilidade em buscas por IA, clareza de entidades, prontidão para citação e avaliação de conteúdo.

> GEO OS is a modular, file-based operating system for studying and structuring content for Generative Engine Optimization and AI Search.

O projeto não promete ranqueamento, citação, tráfego ou presença garantida em mecanismos generativos.

## O que é o GEO OS

O repositório organiza metodologia, skills, rubricas, templates, datasets de teste e validação estrutural. Ele trata GEO como disciplina emergente apoiada em fundamentos de busca, conteúdo, entidades, evidência e avaliação.

O fluxo central é:

```text
Pedido → Orquestrar → Diagnosticar/Mapear/Planejar/Auditar/Otimizar
                              ↓
                 Documentar → Reavaliar
```

O `geo-os-orchestrator` interpreta o pedido e seleciona o menor fluxo suficiente. Ele não executa todas as skills nem substitui a decisão estratégica humana.

## Para quem serve

- Pessoas estudando GEO e AI Search com método reproduzível.
- Profissionais de conteúdo, SEO, Growth, CRO e Design.
- Times que precisam separar evidência, inferência, hipótese e recomendação.
- Pessoas desenvolvendo skills e workflows baseados em arquivos.
- Contribuidores interessados em testar e melhorar o framework.

Não é necessário ser desenvolvedor de carreira. O uso básico exige leitura de Markdown/CSV/JSON/YAML e Python para executar os testes.

## O que o projeto faz

- Estrutura diagnósticos e mapas de entidades.
- Organiza claims, fontes, riscos e contradições.
- Planeja conteúdo, answer blocks e citation engineering.
- Audita extraibilidade, confiança e prontidão GEO.
- Converte gaps em planos de reescrita, refresh e oportunidades de schema.
- Define benchmarks qualitativos e ciclos de reavaliação.
- Valida contratos de arquivos sem tentar substituir avaliação humana.

## O que o projeto não faz

- Não garante ranking, citação, recomendação, tráfego ou visibilidade.
- Não executa crawler, scraping ou consultas automáticas a engines.
- Não usa APIs externas ou dependências pesadas.
- Não gera reescrita final automática.
- Não implementa schema automaticamente.
- Não determina se um claim é verdadeiro ou se uma estratégia é adequada.
- Não inclui apostilas, slides, transcrições ou materiais privados usados no estudo.

## Arquitetura

```text
geo-os/
├── .agents/skills/         # Proxies para descoberta pelo Codex
├── .github/                # Templates de issues e pull requests
├── datasets/golden/        # Cenários qualitativos e benchmarks
├── docs/                   # Metodologia e documentação pública
├── examples/               # Exemplos fictícios e seguros
├── modules/                # Método operacional canônico
├── rubrics/                # Rubricas ponderadas em escala 0–4
├── scripts/                # Validação estrutural
├── skills/                 # Fonte canônica das skills
├── templates/              # Contratos de entregáveis
├── tests/                  # Testes do validador e dos contratos
├── AGENTS.md               # Regras para agentes
├── CHANGELOG.md
├── LICENSE
└── README.md
```

Detalhes: [docs/architecture.md](docs/architecture.md).

O projeto também suporta um overlay privado opcional para sínteses e playbooks pessoais. Ele não faz parte do contrato público nem é necessário para usar as skills. Consulte [docs/private-overlay.md](docs/private-overlay.md).

## Skills

| Skill | Uso |
|---|---|
| `geo-os-orchestrator` | Classificar pedidos e selecionar o menor fluxo operacional suficiente. |
| `geo-diagnosis` | Produzir diagnóstico de maturidade, evidências e prioridades GEO. |
| `entity-map` | Normalizar entidades, aliases, relações e fontes de corroboração. |
| `ai-search-testing` | Planejar e registrar benchmarks reproduzíveis entre engines. |
| `answer-blocks` | Criar unidades de resposta autocontidas e verificáveis. |
| `citation-engineering` | Mapear claims, lacunas e evidências necessárias. |
| `content-brief` | Transformar planejamento e evidência em contrato editorial. |
| `topical-authority` | Mapear cobertura, relações, profundidade e clusters. |
| `competitor-analysis` | Comparar páginas equivalentes por critérios observáveis. |
| `geo-scorecard` | Consolidar sinais em score justificado, cobertura e prioridades. |
| `extractability-audit` | Auditar blocos, ambiguidades e dependência de contexto. |
| `trust-signal-audit` | Auditar autoria, fontes, frescor, método e transparência. |
| `rewrite-plan` | Converter gaps em plano de reescrita por seção. |
| `content-refresh` | Planejar atualização, remoção, expansão ou consolidação. |
| `schema-opportunity` | Mapear dados estruturados sustentados pelo conteúdo visível. |

`skills/` é a fonte canônica. `.agents/skills/` contém apenas proxies de descoberta.

## Uso rápido

Requisitos:

- Python 3.11+
- PyYAML

```powershell
git clone <URL-DO-REPOSITORIO>
cd geo-os
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

Para começar por um pedido em linguagem natural, abra o projeto no Codex e cole a instrução no **chat do Codex**:

```text
$geo-os-orchestrator Quero melhorar uma landing page existente sem reescrever o texto final.
```

Não execute no CMD: `$geo-os-orchestrator` não é um comando do Windows. O terminal continua sendo usado apenas para comandos como testes, validação e Git.

O resultado indica fluxo, skills em ordem, inputs faltantes, templates, pasta em `outputs/`, limitações e o próximo comando operacional.

Guia completo: [docs/getting-started.md](docs/getting-started.md).

## Como usar os templates

1. Escolha um fluxo em [docs/usage-examples.md](docs/usage-examples.md).
2. Copie o template relevante para uma pasta local ignorada, como `outputs/`.
3. Substitua a linha de exemplo nos CSVs.
4. Preserve IDs, headers e headings obrigatórios.
5. Registre fontes, datas, limitações e estados não avaliáveis.
6. Reexecute testes e validador se alterar contratos do repositório.

Exemplos preenchidos estão em [examples/](examples/).

## Convenções de evidência

- `[FATO]`: sustentado por fonte verificável.
- `[INFERÊNCIA]`: conclusão derivada de fatos explicitados.
- `[HIPÓTESE]`: tese ainda não validada por teste suficiente.
- `[RECOMENDAÇÃO]`: ação proposta a partir do diagnóstico.
- `[FRAMEWORK PRÓPRIO]`: síntese metodológica criada no GEO OS.

Toda afirmação técnica não óbvia deve indicar fonte e data de acesso. Estatísticas voláteis devem incluir período, população, método conhecido e limitações.

## Limitações e ética

GEO é um campo emergente. Resultados variam por engine, modelo, idioma, localização, personalização, data e repetição. Citações podem existir sem sustentar integralmente um claim.

O projeto não deve ser usado para conteúdo oculto, spam, avaliações falsas, fontes inventadas, manipulação adversarial ou criação artificial de autoridade.

Leia [docs/limitations-and-ethics.md](docs/limitations-and-ethics.md).

## Como contribuir

Antes de contribuir:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

Não envie materiais privados, outputs com dados pessoais ou exemplos baseados em marcas reais sem necessidade. Consulte [docs/contribution-guide.md](docs/contribution-guide.md).

## Status do projeto

**Status:** release candidate para publicação pública.

Camadas disponíveis:

- fundação modular;
- evidência e answer blocks;
- planejamento estratégico;
- avaliação;
- otimização;
- orquestração;
- publicação e documentação.

Ainda fora do escopo: automação de engines, crawler, scraping, APIs externas, reescrita final e implementação automática de schema.

## Licença

Distribuído sob a [MIT License](LICENSE).
