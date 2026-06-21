# AGENTS.md

## Objetivo do repositório

Manter um sistema operacional modular e auditável para GEO. O repositório deve separar metodologia, execução, evidência, avaliação e apresentação comercial.

## Regras de arquitetura

- Manter cada skill focada em um único trabalho.
- Usar `skills/` como fonte canônica e `.agents/skills/` apenas como camada de descoberta.
- Usar `modules/` para metodologia operacional compartilhada; skills devem apontar para módulos em vez de duplicá-los.
- Evitar prompts monolíticos, duplicação de regras e dependências pesadas.
- Preferir instruções em Markdown; usar scripts apenas para comportamento determinístico.
- Preservar compatibilidade com o padrão Agent Skills: diretório em kebab-case e `SKILL.md` com `name` e `description`.
- Não criar novos módulos, adapters ou automações sem necessidade demonstrada.

## Política de evidência

- Marcar claims não triviais como `[FATO]`, `[INFERÊNCIA]`, `[HIPÓTESE]` ou `[FRAMEWORK PRÓPRIO]`.
- Exigir URL ou referência identificável, data de acesso e tipo de fonte para claims técnicos.
- Priorizar documentação oficial, papers revisados por pares e fontes primárias.
- Tratar preprints, cursos, relatórios de vendors e estudos observacionais como evidência limitada.
- Não converter correlação, teste isolado ou opinião de mercado em causalidade.
- Registrar conflitos entre fontes; não escolher silenciosamente a versão mais conveniente.
- Em evidence ledgers, registrar confiabilidade da fonte, confiança na relação claim-evidência, uso permitido e risco como campos distintos.

## Limites comerciais e éticos

- Nunca prometer ranking, citação, inclusão, recomendação ou tráfego em sistemas de IA.
- Não apresentar schema, `llms.txt`, keyword stuffing ou qualquer técnica isolada como garantia.
- Não recomendar conteúdo oculto, claims sem suporte, avaliações falsas, spam de comunidade ou manipulação adversarial.
- Comunicar GEO como melhoria de recuperabilidade, selecionabilidade, citabilidade, autoridade e capacidade de mensuração.
- Informar que outputs de engines são variáveis e que benchmarks são fotografias controladas, não verdades permanentes.

## Contratos das skills

Cada `SKILL.md` deve conter:

- `name` e `description` no frontmatter;
- objetivo;
- quando usar e quando não usar;
- inputs mínimos e opcionais;
- processo;
- outputs;
- critérios de qualidade;
- erros comuns.

A descrição deve ser curta, ter escopo claro e permitir acionamento correto. Não duplicar metodologia extensa dentro de todas as skills.

## Contratos da camada de conteúdo

- Criar intent map antes de redigir quando houver múltiplas intenções ou contextos.
- Não criar answer block com claim bloqueado, sem evidência ou sem uso público permitido.
- Tratar cada linha do evidence ledger como claim atômico.
- Em citation engineering, descrever a evidência necessária antes de sugerir uma fonte específica.
- Manter atribuição próxima ao claim e preservar ressalvas materiais.
- Usar `templates/evidence-ledger.csv`, `templates/citation-opportunity-map.csv` e `templates/answer-block-template.md`.

## Sequência de planejamento estratégico

Usar o seguinte ciclo, adaptando apenas quando o escopo justificar:

1. Confirmar intent map, entity map e evidence ledger.
2. Criar um draft do content brief com lacunas explícitas.
3. Executar `topical-authority` para cobertura, profundidade e clusters.
4. Executar `competitor-analysis` somente com páginas comparáveis.
5. Consolidar o content brief final.
6. Executar `citation-engineering` para claims e provas.
7. Executar `answer-blocks` somente com claims liberados.
8. Validar por revisão humana e benchmark.

Regras:

- `content-brief` é o artefato central; topical authority e competitor gaps devem alimentá-lo.
- Não criar cluster, gap ou ação sem entidade, intenção e evidência observável.
- Não usar word count, backlinks, ranking ou schema isolados como conclusão competitiva.
- Toda análise deve registrar data, URLs, suposições, limitações e estados não avaliáveis.
- Skills estratégicas devem incluir restrições, critérios de qualidade, modos de falha e exemplo.

## Rubricas

- Usar escala ordinal de `0` a `4`.
- Declarar pesos, evidências exigidas, interpretação e limitações.
- Pontuar somente o que tiver evidência observável.
- Usar `0` para ausência de evidência, não como sinônimo automático de baixa qualidade.
- Não comparar scores entre projetos com escopos ou métodos incompatíveis.

## Benchmarks

- Usar prompts versionados, locale, engine, data, condições de execução e repetição.
- Avaliar critérios de comportamento, não respostas textuais rígidas.
- Separar presença, citação, suporte da citação, absorção, precisão da entidade e comparação competitiva.
- Registrar falhas, ausência de busca web e indisponibilidade da engine como dados, sem imputar zero artificial.
- Nunca inferir evolução a partir de uma única execução.

## Validação

Antes de concluir mudanças:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

O validador verifica estrutura e contratos de arquivo. Ele não substitui revisão estratégica, checagem factual nem análise humana.

## Atualizações

- Atualizar `docs/source-ledger.md` ao adicionar ou alterar claims metodológicos.
- Seguir `docs/update-policy.md` para mudanças de versão.
- Documentar mudanças incompatíveis nos contratos de CSV, JSON ou YAML.
- Atualizar módulos canônicos antes de ajustar skills que dependem deles.
- Revisar content briefs quando intent, evidência, mapa tópico ou cenário competitivo mudar materialmente.
- Manter nomes de arquivos em inglês e conteúdo em português brasileiro.
