# GEO OS

Sistema operacional modular para Generative Engine Optimization (GEO), criado para transformar diagnóstico, modelagem de entidades e testes de AI Search em processos versionáveis, auditáveis e portáteis.

## Princípio central

O GEO OS não promete ranking, citação ou recomendação em respostas geradas por IA. Ele organiza evidências e intervenções para melhorar:

- **Recuperabilidade:** possibilidade de o conteúdo ser encontrado e processado.
- **Selecionabilidade:** adequação como fonte candidata.
- **Citabilidade:** clareza com que claims podem ser sustentados.
- **Absorção:** contribuição observável do conteúdo para a resposta final.
- **Autoridade de entidade:** consistência e corroboração das entidades.
- **Mensuração:** capacidade de comparar resultados ao longo do tempo.

## Arquitetura

```text
geo-os/
├── AGENTS.md
├── skills/                 # Fonte canônica das skills
├── .agents/skills/         # Descoberta nativa pelo Codex
├── modules/                # Método operacional reutilizável
├── rubrics/                # Critérios de pontuação 0–4
├── templates/              # Contratos de entregáveis
├── datasets/golden/        # Prompts de benchmark reutilizáveis
├── scripts/                # Validação determinística
├── tests/                  # Fundação de qualidade do validador
└── docs/                   # Metodologia, fontes e atualização
```

Cada skill executa um trabalho específico. As rubricas definem critérios; os templates padronizam entregáveis; o dataset oferece cenários de teste; o script verifica a integridade estrutural. A avaliação estratégica continua sendo humana.

## Skills iniciais

| Skill | Uso |
|---|---|
| `geo-diagnosis` | Produzir diagnóstico de maturidade, evidências e prioridades GEO. |
| `entity-map` | Normalizar entidades, aliases, relações e fontes de corroboração. |
| `ai-search-testing` | Planejar e registrar benchmarks reproduzíveis entre engines. |
| `answer-blocks` | Criar unidades de resposta autocontidas e verificáveis. |
| `citation-engineering` | Mapear claims, lacunas e evidências necessárias. |

## Camada de execução de conteúdo

```text
Intent Map
    ↓
Evidence Ledger
    ↓
Citation Opportunity Map
    ↓
Answer Block
    ↓
Revisão e benchmark
```

- `modules/intent-map.md`: traduz demanda em perguntas, contexto e formato.
- `modules/evidence-ledger.md`: controla claims, fontes, datas, confiança, uso e risco.
- `modules/citation-engineering.md`: define o que precisa ser provado.
- `modules/answer-blocks.md`: transforma evidência liberada em conteúdo reutilizável.

## Uso rápido

Requisitos: Python 3.11+ e PyYAML.

```powershell
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

Para usar uma skill no Codex, invoque-a explicitamente ou descreva uma tarefa compatível com seu `description`:

```text
$geo-diagnosis audite as páginas prioritárias e gere um backlog baseado em evidências.
```

## Convenções de evidência

- `[FATO]`: sustentado por fonte verificável.
- `[INFERÊNCIA]`: conclusão derivada de fatos explicitados.
- `[HIPÓTESE]`: tese ainda não validada por teste suficiente.
- `[FRAMEWORK PRÓPRIO]`: síntese metodológica criada no GEO OS.

Toda afirmação técnica não óbvia deve indicar fonte e data de acesso. Estatísticas voláteis devem incluir período, população e limitações.

## Limites do MVP

Esta versão não inclui scraping, execução automática em engines, APIs proprietárias, plugins, empacotamento multiplataforma ou julgamento automático de qualidade estratégica. Resultados de AI Search variam por engine, modelo, localização, personalização, data e repetição.

## Próxima evolução recomendada

Adicionar content brief, topical authority e competitor analysis. Scripts de análise, automação externa e empacotamento continuam fora do escopo até os contratos editoriais serem testados em casos reais.

## Linguagem comercial

`GEO OS` permanece como nome interno. Em materiais para decisores, priorizar linguagem direta como **AI Search Visibility System** ou **Sistema de Presença em Buscas por IA**: como a marca aparece, é entendida e é citada em respostas de IA.
