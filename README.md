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
| `content-brief` | Transformar planejamento e evidência em contrato editorial executável. |
| `topical-authority` | Mapear entidades, relações, cobertura, profundidade e clusters. |
| `competitor-analysis` | Comparar concorrentes por critérios GEO observáveis e gaps. |
| `geo-scorecard` | Consolidar sinais observáveis em score justificado, cobertura e prioridades. |
| `extractability-audit` | Auditar blocos autossuficientes, ambiguidades e oportunidades de reestruturação. |
| `trust-signal-audit` | Auditar autoria, fontes, frescor, metodologia, transparência e riscos. |

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

## Camada de planejamento estratégico

O content brief é o artefato central e passa por enriquecimento iterativo:

```text
Intent + Entity + Evidence
          ↓
Draft Content Brief
     ↙           ↘
Topical Map   Competitor Gaps
     ↘           ↙
Final Content Brief
          ↓
Citation Engineering → Answer Blocks → Benchmark
```

- `modules/content-brief.md`: contrato editorial completo.
- `modules/topical-authority.md`: cobertura por entidades, relações e profundidade.
- `modules/competitor-analysis.md`: comparação baseada em evidência e páginas equivalentes.

Exemplos:

```text
$content-brief crie um brief para [tema] usando o intent map e o evidence ledger.
$topical-authority mapeie lacunas de cobertura para [entidade principal].
$competitor-analysis compare as URLs fornecidas para a intenção [intenção].
```

## Camada de avaliação

A Evaluation Layer fecha o ciclo entre planejamento, produção, auditoria e otimização:

```text
Planejar → Produzir → Auditar → Priorizar → Otimizar → Reavaliar
                         ↓
     Extractability + Trust Signals + GEO Scorecard
```

- `modules/extractability-audit.md`: identifica respostas diretas, definições, listas, tabelas, passos, FAQs reais, claims, ambiguidades e dependência visual.
- `modules/trust-signal-audit.md`: verifica autoria, organização, fontes, frescor, metodologia, transparência e consistência factual.
- `modules/geo-scorecard.md`: consolida 16 dimensões ponderadas, cobertura, evidências, gaps e ações.
- `datasets/golden/evaluation-prompts-pt-br.json`: testa diagnóstico, lacunas, evidência, riscos, limitações e acionabilidade em seis cenários.

Exemplos:

```text
$extractability-audit audite este conteúdo para a intenção [intenção].
$trust-signal-audit verifique autoria, fontes, método e frescor deste artigo.
$geo-scorecard consolide as auditorias e priorize as correções.
```

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

Criar a Optimization Layer para converter gaps avaliados em planos de refresh, experimentos e ciclos de reavaliação. Scripts de análise, automação externa e empacotamento continuam fora do escopo até os contratos serem testados em casos reais.

## Linguagem comercial

`GEO OS` permanece como nome interno. Em materiais para decisores, priorizar linguagem direta como **AI Search Visibility System** ou **Sistema de Presença em Buscas por IA**: como a marca aparece, é entendida e é citada em respostas de IA.
