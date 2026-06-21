# AGENTS.md

## Objetivo do repositório

Manter um sistema operacional modular, auditável e seguro para publicação pública. O repositório deve separar metodologia, execução, evidência, avaliação, otimização e documentação.

## Regras de arquitetura

- Manter cada skill focada em um único trabalho.
- Usar `skills/` como fonte canônica e `.agents/skills/` apenas como camada de descoberta.
- Usar `modules/` para metodologia operacional compartilhada; skills devem apontar para módulos em vez de duplicá-los.
- Evitar prompts monolíticos, duplicação de regras e dependências pesadas.
- Preferir instruções em Markdown; usar scripts apenas para comportamento determinístico.
- Preservar compatibilidade com o padrão Agent Skills: diretório em kebab-case e `SKILL.md` com `name` e `description`.
- Não criar novos módulos, adapters ou automações sem necessidade demonstrada.

## Política de evidência

- Marcar claims não triviais como `[FATO]`, `[INFERÊNCIA]`, `[HIPÓTESE]`, `[RECOMENDAÇÃO]` ou `[FRAMEWORK PRÓPRIO]`.
- Exigir URL ou referência identificável, data de acesso e tipo de fonte para claims técnicos.
- Priorizar documentação oficial, papers revisados por pares e fontes primárias.
- Tratar preprints, cursos, relatórios de vendors e estudos observacionais como evidência limitada.
- Não converter correlação, teste isolado ou opinião de mercado em causalidade.
- Registrar conflitos entre fontes; não escolher silenciosamente a versão mais conveniente.
- Em evidence ledgers, registrar confiabilidade da fonte, confiança na relação claim-evidência, uso permitido e risco como campos distintos.

## Limites de promessa e ética

- Nunca prometer ranking, citação, inclusão, recomendação ou tráfego em sistemas de IA.
- Não apresentar schema, `llms.txt`, keyword stuffing ou qualquer técnica isolada como garantia.
- Não recomendar conteúdo oculto, claims sem suporte, avaliações falsas, spam de comunidade ou manipulação adversarial.
- Comunicar GEO como melhoria de recuperabilidade, selecionabilidade, citabilidade, autoridade e capacidade de mensuração.
- Informar que outputs de engines são variáveis e que benchmarks são fotografias controladas, não verdades permanentes.

## Publicação e privacidade

- Tratar o repositório como artefato público por padrão.
- Nunca incluir caminhos pessoais, secrets, tokens, dados identificáveis ou outputs de projetos reais.
- Não publicar apostilas, slides, prints, transcrições, PDFs, DOCX, PPTX ou imagens de materiais fechados.
- Fontes privadas podem ser registradas genericamente no source ledger como influência não publicável.
- Exemplos devem ser fictícios, usar domínios `.invalid` e declarar seu caráter demonstrativo.
- Antes de publicar, revisar `git ls-files`, executar testes, validador e busca por caminhos pessoais.
- Não criar linguagem de venda, proposta comercial ou promessa de resultado como parte da arquitetura principal.
- Seguir `docs/publishing-notes.md` e `docs/limitations-and-ethics.md`.

## Overlay privado local

O repositório funciona em dois modos:

- **Modo público:** usar somente arquivos versionados no `geo-os`. Nenhuma tarefa deve falhar, perder contrato ou produzir resultado incompleto porque o overlay não existe.
- **Modo privado/local:** procurar primeiro `../geo-os-private/README.md`, usando o repositório privado versionado. Consultar `private/README.md` somente como fallback de compatibilidade. Se um deles existir, ler suas instruções antes de trabalhos metodológicos extensos.

Regras:

- Tratar o overlay privado como fonte complementar e opcional, nunca como dependência obrigatória.
- Não referenciar o overlay em contratos de `SKILL.md`, módulos, templates, scripts ou testes públicos.
- Tratar qualquer uso do overlay como síntese interna, não como citação pública.
- Não copiar automaticamente conteúdo, caminhos, números voláteis ou fontes fechadas para outputs públicos ou arquivos rastreados pelo Git.
- Ao promover conhecimento privado para o núcleo público, criar síntese autoral, registrar a decisão em `docs/source-ledger.md` e exigir fonte primária para claims técnicos.
- Seguir `docs/private-overlay.md` para armazenamento, migração e conferência de publicação.

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

## Sequência da camada de avaliação

Executar avaliação sobre conteúdo fornecido, preservando esta ordem:

1. Confirmar ativo, versão, intenção, público, entidade e escopo.
2. Executar `extractability-audit` para estrutura e autonomia dos blocos.
3. Executar `trust-signal-audit` para autoria, fontes, frescor, método e transparência.
4. Consolidar no `geo-scorecard`.
5. Transformar gaps em ações para content brief, citation engineering, answer blocks ou refresh.
6. Reavaliar somente sob protocolo compatível.

Regras:

- Auditar antes de produzir recomendações de otimização.
- Não afirmar crawl, acesso ou inspeção de uma URL quando somente a URL foi fornecida.
- Toda nota deve ter justificativa e evidência observável.
- Usar `N/A` para dimensão não avaliada no scorecard; não converter ausência de input em nota zero.
- Informar cobertura e denominador ao apresentar score total.
- Não usar score como probabilidade de ranking, seleção, citação ou tráfego.
- Recomendações devem indicar problema, evidência necessária, prioridade e resultado esperado.
- Skills de avaliação devem incluir restrições, critérios de qualidade, modos de falha e exemplo.

## Sequência da camada de otimização

Executar otimização como ciclo fechado:

1. Confirmar ativo, versão, intenção, entidades e auditorias.
2. Normalizar gaps e registrar origem.
3. Criar `rewrite-plan` quando houver intervenção por seção.
4. Criar `content-refresh` quando houver manutenção de ativo existente.
5. Executar `schema-opportunity` apenas sobre conteúdo visível.
6. Registrar ações no `optimization-cycle-template.md`.
7. Aprovar direção editorial antes de qualquer reescrita final.
8. Reavaliar sob protocolo compatível.
9. Decidir entre manter, revisar, expandir ou abandonar.

Regras:

- Não criar skill ou output de reescrita final nesta camada.
- Toda ação deve registrar origem do gap.
- Separar `[FATO]`, `[INFERÊNCIA]`, `[HIPÓTESE]` e `[RECOMENDAÇÃO]`.
- Toda ação deve incluir impacto, esforço, prioridade, risco e critério de reavaliação.
- Não recomendar expansão, consolidação, remoção ou republicação sem justificativa observável.
- Schema deve corresponder ao conteúdo visível e à documentação oficial aplicável.
- Não prometer ranking, citação, rich result ou presença em mecanismos generativos.
- Não criar referência a skill inexistente; usar apenas contratos presentes no repositório.

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
- Revisar planos de otimização quando gaps, fontes, conteúdo, owners ou critérios de sucesso mudarem.
- Atualizar `CHANGELOG.md` e revisar higiene pública antes de cada release.
- Manter nomes de arquivos em inglês e conteúdo em português brasileiro.
