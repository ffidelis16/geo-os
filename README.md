# GEO OS

GEO OS é um sistema operacional modular, baseado em arquivos, para transformar pedidos de Generative Engine Optimization e AI Search em fluxos documentados, auditáveis e executáveis.

Projeto independente mantido por Fernando Fidelis / [@ffidelis16](https://github.com/ffidelis16).

O projeto não promete ranqueamento, citação, recomendação, tráfego, adoção ou presença garantida em mecanismos generativos.

> GEO OS is a modular, file-based operating system for Generative Engine Optimization and AI Search workflows.

## O que é o GEO OS

O repositório organiza skills, módulos, templates, rubricas, datasets e validação estrutural. A entrada padrão é o `geo-os-orchestrator`: você descreve o problema em linguagem natural, e ele seleciona o menor fluxo suficiente, lista inputs faltantes e entrega o próximo comando operacional.

O fluxo central é:

```text
Pedido → Orquestrador → Skill especializada → Output auditável
                                                ↓
                              Revisão humana → Reavaliação
```

O orquestrador funciona como roteador. Ele não executa todas as skills, não substitui julgamento humano e não produz reescrita final por padrão.

## Uso rápido

O primeiro passo recomendado é testar o orquestrador no Codex com um pedido simples.

### No terminal

Requisitos:

- Git;
- Python 3.11+;
- PyYAML.

```powershell
git clone https://github.com/ffidelis16/GEO-OS.git
cd GEO-OS
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

### No chat do Codex

Abra o projeto no Codex e cole:

```text
$geo-os-orchestrator

Quero auditar um conteúdo existente para identificar problemas de clareza, extraibilidade e confiança.

Não execute todas as skills.
Escolha o menor fluxo suficiente.
```

O Codex deve retornar o fluxo selecionado, skills em ordem, inputs disponíveis e faltantes, templates, limitações, pasta de output e próximo comando.

Não execute no CMD: prefixos como `$geo-os-orchestrator` são instruções para o chat do Codex, não comandos do Windows. Também não cole esses prompts no PowerShell.

Guia completo: [docs/getting-started.md](docs/getting-started.md).

## Exemplo de fluxo

Um pedido pode percorrer esta sequência:

```text
Pedido:
"Quero avaliar se este README comunica bem o projeto."

Fluxo selecionado:
audit-existing-content

Skills:
extractability-audit → trust-signal-audit → geo-scorecard

Output inicial:
outputs/projeto/workflow-selection.md
```

O exemplo demonstra o contrato operacional; não representa garantia de resultado em qualquer engine.

Como próximo passo, consulte os [exemplos preenchidos](examples/) e depois a [arquitetura detalhada](docs/architecture.md).

## Para quem serve

- Profissionais de marketing, SEO, conteúdo, Growth, CRO, Design e IA.
- Pessoas estudando GEO e AI Search com método reproduzível.
- Times que precisam separar evidência, inferência, hipótese e recomendação.
- Pessoas desenvolvendo skills e workflows baseados em arquivos.
- Contribuidores interessados em testar e melhorar o framework.

Não é necessário ser desenvolvedor de carreira, mas o uso local exige operação técnica básica com Codex, Git, Markdown/CSV/JSON/YAML e Python para testes e validação.

## O que o projeto faz

- Seleciona o menor fluxo operacional para um pedido em linguagem natural.
- Estrutura diagnósticos e mapas de entidades.
- Organiza claims, fontes, riscos e contradições.
- Planeja conteúdo, answer blocks e citation engineering.
- Audita extraibilidade, confiança e prontidão GEO.
- Converte gaps em planos de reescrita, refresh e oportunidades de schema.
- Define benchmarks qualitativos e ciclos de reavaliação.
- Valida contratos de arquivos sem tentar substituir avaliação humana.

## O que o projeto não faz

- Não garante ranking, citação, recomendação, tráfego, adoção ou visibilidade.
- Não executa crawler, scraping ou consultas automáticas a engines.
- Não usa APIs externas ou dependências pesadas.
- Não gera reescrita final automática.
- Não implementa schema automaticamente.
- Não determina se um claim é verdadeiro ou se uma estratégia é adequada.
- Não inclui apostilas, slides, transcrições ou materiais privados usados no estudo.

## Como usar os templates

1. Comece pelo orquestrador quando o fluxo ainda não estiver definido.
2. Copie o template indicado para uma pasta local ignorada, como `outputs/`.
3. Substitua a linha de exemplo nos CSVs.
4. Preserve IDs, headers e headings obrigatórios.
5. Registre fontes, datas, limitações e estados não avaliáveis.
6. Reexecute testes e validador se alterar contratos do repositório.

Uso manual de uma skill específica continua disponível para pessoas que já conhecem o fluxo necessário. Veja [docs/usage-examples.md](docs/usage-examples.md).

## Skills

O `geo-os-orchestrator` é a entrada padrão. As demais skills executam trabalhos especializados.

### Orquestração

| Skill | Uso |
|---|---|
| `geo-os-orchestrator` | Classificar pedidos e selecionar o menor fluxo operacional suficiente. |

### Fundação

| Skill | Uso |
|---|---|
| `geo-diagnosis` | Produzir diagnóstico de maturidade, evidências e prioridades GEO. |
| `entity-map` | Normalizar entidades, aliases, relações e fontes de corroboração. |
| `ai-search-testing` | Planejar e registrar benchmarks reproduzíveis entre engines. |

### Conteúdo e evidência

| Skill | Uso |
|---|---|
| `answer-blocks` | Criar unidades de resposta autocontidas e verificáveis. |
| `citation-engineering` | Mapear claims, lacunas e evidências necessárias. |

### Planejamento

| Skill | Uso |
|---|---|
| `content-brief` | Transformar planejamento e evidência em contrato editorial. |
| `topical-authority` | Mapear cobertura, relações, profundidade e clusters. |
| `competitor-analysis` | Comparar páginas equivalentes por critérios observáveis. |

### Avaliação

| Skill | Uso |
|---|---|
| `geo-scorecard` | Consolidar sinais em score justificado, cobertura e prioridades. |
| `extractability-audit` | Auditar blocos, ambiguidades e dependência de contexto. |
| `trust-signal-audit` | Auditar autoria, fontes, frescor, método e transparência. |

### Otimização

| Skill | Uso |
|---|---|
| `rewrite-plan` | Converter gaps em plano de reescrita por seção. |
| `content-refresh` | Planejar atualização, remoção, expansão ou consolidação. |
| `schema-opportunity` | Mapear dados estruturados sustentados pelo conteúdo visível. |

`skills/` é a fonte canônica. `.agents/skills/` contém proxies de descoberta.

## Método e limites

O GEO OS trata GEO como disciplina emergente apoiada em fundamentos de busca, conteúdo, entidades, evidência e avaliação.

- [Metodologia](docs/methodology.md): tese operacional, camadas e workflow.
- [Source ledger](docs/source-ledger.md): fontes públicas, confiabilidade e decisões derivadas.
- [Limitações e ética](docs/limitations-and-ethics.md): variabilidade, ausência de garantias e usos proibidos.
- [Política de atualização](docs/update-policy.md): manutenção de claims, contratos e versões.

Os testes e o validador confirmam estrutura e contratos. Eles não comprovam eficácia estratégica, verdade factual ou resultados em mecanismos generativos.

O projeto suporta um [overlay privado opcional](docs/private-overlay.md) para sínteses e playbooks pessoais. Esse material não integra o contrato público nem é necessário para usar as skills.

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

Use [GitHub Issues](https://github.com/ffidelis16/GEO-OS/issues) para relatar bugs, inconsistências factuais ou propostas de melhoria.

Não envie materiais privados, outputs com dados pessoais ou exemplos baseados em marcas reais sem necessidade. Consulte [docs/contribution-guide.md](docs/contribution-guide.md).

## Status do projeto

**Status:** release candidate operacional.

Utilizável nesta versão:

- núcleo modular baseado em arquivos;
- 15 skills e seus módulos;
- templates, rubricas e datasets golden;
- testes e validador estrutural;
- documentação e exemplos públicos.

Fora do escopo desta versão:

- app ou Workbench;
- API própria;
- automação de engines;
- crawler e scraping;
- reescrita final automática;
- implementação automática de schema.

Consulte o [changelog](CHANGELOG.md) para acompanhar a evolução. O status não representa garantia de estabilidade futura ou resultado estratégico.

## Licença

Distribuído sob a [MIT License](LICENSE).
