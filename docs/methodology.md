# Metodologia GEO OS

## Tese operacional

`[FRAMEWORK PRÓPRIO]` GEO é tratado neste repositório como uma disciplina aplicada sobre fundamentos de busca, conteúdo, entidades, evidência e avaliação. O objetivo não é controlar uma engine, mas aumentar a qualidade e a mensurabilidade dos ativos que podem ser recuperados, selecionados, citados e absorvidos em respostas.

`[FATO]` O paper original de GEO formaliza visibilidade em motores generativos como um problema diferente do ranking linear e relata que os efeitos das intervenções variam por domínio. Fonte: Aggarwal et al., KDD 2024, registrada em `docs/source-ledger.md`.

`[FATO]` O Google declara que suas experiências de AI Search não exigem otimizações técnicas especiais além das práticas fundamentais de SEO e elegibilidade existentes. Fonte: Google Search Central, registrada no ledger.

## Camadas de avaliação

### Recuperabilidade

Pergunta: o conteúdo pode ser descoberto, acessado e identificado?

Observar:

- indexabilidade e canonicalização;
- presença do conteúdo principal no HTML ou renderização disponível;
- consistência de URLs, títulos, autores e datas;
- restrições de crawler conhecidas.

### Selecionabilidade

Pergunta: o ativo é uma fonte candidata adequada para a intenção?

Observar:

- correspondência entre intent e página;
- especificidade e informação incremental;
- clareza do propósito da página;
- atualidade compatível com o tema.

Não inferir seleção apenas porque uma página ranqueia organicamente.

### Citabilidade

Pergunta: claims podem ser associados a suporte claro?

Observar:

- granularidade;
- fonte, data e contexto;
- autoria e responsabilidade;
- comparações simétricas;
- ressalvas e condições.

`[FATO]` Pesquisas de verificabilidade mostram que uma citação apresentada por uma engine não garante suporte integral ao texto associado. Por isso, o benchmark verifica a correspondência claim-fonte.

### Absorção

Pergunta: evidências, linguagem, estrutura ou fatos do ativo contribuíram para a resposta?

Absorção deve ser tratada como avaliação graduada e revisada por humano. Ausência de citação não permite concluir automaticamente ausência de influência; presença de citação também não prova absorção forte.

### Autoridade de entidade

Pergunta: a entidade é clara e corroborada?

Observar:

- nome canônico e aliases;
- tipo e definição;
- relações;
- consistência própria;
- corroboração independente;
- expertise verificável;
- alinhamento entre locales.

Dados estruturados devem representar conteúdo visível. Eles ajudam a explicitar significado, mas não são promessa de citação.

### Mensuração

Pergunta: o resultado pode ser comparado de modo honesto?

Exigir:

- prompt set e versão;
- engine, modo, locale e timestamp;
- repetição;
- resultado bruto;
- estados de erro ou indisponibilidade;
- critérios estáveis;
- denominadores visíveis.

## Workflow operacional

1. **Escopo:** definir marca, categoria, páginas, locale, concorrentes e perguntas.
2. **Intent map:** transformar demanda em perguntas, follow-ups, entidades, evidências e formatos.
3. **Entity map:** normalizar entidades e relações.
4. **Evidence ledger:** registrar claims, fontes, datas, confiabilidade, confiança, uso e risco.
5. **Diagnóstico:** aplicar a rubrica de prontidão com evidências.
6. **Citabilidade:** aplicar a rubrica somente às páginas com material suficiente.
7. **Citation engineering:** mapear claims bloqueados, lacunas e evidências necessárias.
8. **Answer blocks:** criar unidades autocontidas apenas com claims liberados.
9. **Avaliação:** auditar extraibilidade e sinais de confiança; consolidar no scorecard.
10. **Benchmark:** executar prompts sob protocolo controlado.
11. **Síntese:** separar `[FATO]`, `[INFERÊNCIA]`, `[HIPÓTESE]` e `[FRAMEWORK PRÓPRIO]`.
12. **Prioridade:** combinar impacto esperado, confiança, esforço e dependências.
13. **Re-teste:** repetir o protocolo e registrar mudanças ambientais.

## Ponte entre diagnóstico e execução

`[FRAMEWORK PRÓPRIO]` A camada editorial usa quatro contratos:

| Contrato | Pergunta respondida |
|---|---|
| Intent Map | O que a pessoa precisa decidir ou realizar? |
| Evidence Ledger | O que pode ser afirmado, com qual fonte e risco? |
| Citation Opportunity Map | O que ainda precisa ser provado ou limitado? |
| Answer Block | Como responder com clareza sem exceder a evidência? |

O fluxo não deve começar pelo answer block. Quando a evidência é insuficiente, a saída correta é bloquear, limitar ou remover o claim.

## Camada de planejamento estratégico

`[FRAMEWORK PRÓPRIO]` O content brief funciona como contrato central, mas é iterativo:

1. intent, entidades e evidências produzem um draft;
2. topical authority verifica cobertura, relações e profundidade;
3. competitor analysis identifica gaps observáveis em páginas comparáveis;
4. os dois mapas refinam o brief;
5. citation engineering e answer blocks executam o plano;
6. benchmark e revisão humana avaliam o resultado.

### Content brief

Deve tornar explícitos:

- target intent, audiência e estágio;
- entidade principal, entidades de suporte e relações;
- core claims e evidências;
- oportunidades de citação e answer blocks;
- frescor e qualidade mínima das fontes;
- links internos;
- riscos, suposições e limitações;
- estrutura e critérios de aceite.

### Topical authority

Avalia cobertura e profundidade separadamente. Uma coleção extensa de páginas não constitui autoridade se as relações forem vagas, os conteúdos se contradisserem ou as evidências forem insuficientes.

### Competitor analysis

Compara páginas equivalentes por critérios observáveis. Não usa ranking, tamanho, backlinks, schema ou presença em IA como prova isolada de qualidade.

### Avaliação qualitativa

O dataset `strategic-planning-prompts-pt-br.json` define cenários e critérios esperados para:

- completude dos outputs;
- disciplina de evidência;
- relações entre entidades;
- limitações;
- acionabilidade.

As rubricas existentes permanecem transversais. Esta iteração não cria uma rubrica por skill porque o repositório não adota equivalência automática entre módulo e score.

## Camada de avaliação

`[FRAMEWORK PRÓPRIO]` A Evaluation Layer verifica o conteúdo produzido antes de recomendar otimização:

```text
Planejamento → Produção → Extractability Audit
                         → Trust Signal Audit
                         → GEO Scorecard
                         → Backlog de otimização
```

### Extractability audit

Avalia se respostas, definições, listas, tabelas, comparações, passos, FAQs, claims e dados funcionam como unidades autossuficientes. Paredes de texto, headings vagos, referências ambíguas, claims compostos, evidência distante e dependência visual são sinais de risco.

`[INFERÊNCIA]` Um bloco mais curto não é necessariamente mais extraível. A unidade precisa preservar entidade, contexto, período, evidência e ressalvas materiais.

### Trust signal audit

Avalia sinais observáveis de:

- autoria e credenciais verificáveis;
- organização responsável;
- correspondência entre fonte e claim;
- evidência primária e independência;
- datas, frescor e validade temporal;
- metodologia;
- transparência, conflitos e limitações;
- consistência factual.

Informação fora do input deve ser marcada como `não observado`. Ausência no material fornecido não prova inexistência.

### GEO scorecard

O scorecard consolida 16 dimensões ponderadas: intenção, clareza e relações de entidades, qualidade de evidência, citabilidade, answer blocks, extraibilidade, completude temática, confiança, frescor, transparência de fontes, estrutura, schema opportunities, links internos, limitações e acionabilidade.

Cada dimensão usa `0–4` ou `N/A`. O total exclui dimensões não avaliadas do denominador e sempre informa cobertura. Toda nota exige justificativa e evidência; o score não representa probabilidade de ranking ou citação.

### Avaliação qualitativa da camada

O dataset `evaluation-prompts-pt-br.json` possui dois cenários por módulo e verifica:

- diagnóstico;
- identificação de gaps;
- recomendações de melhoria;
- evidência necessária;
- riscos de interpretação;
- limitações;
- acionabilidade.

`[INFERÊNCIA]` O material didático `apostila_geo_v2.html` reforça como sinais operacionais a combinação claim + contexto + evidência + takeaway, o uso de formatos discretos e a auditoria de autoria, datas, fontes, metodologia e limitações. Estatísticas e claims de mercado presentes no material não foram promovidos a fatos metodológicos sem fonte primária.

## Pontuação

Cada critério usa escala ordinal `0–4`:

| Score | Interpretação |
|---:|---|
| 0 | ausente ou sem evidência |
| 1 | fraco e inconsistente |
| 2 | parcial |
| 3 | sólido |
| 4 | forte e reproduzível |

Score ponderado:

```text
score_total = soma(score_do_criterio / 4 × peso)
```

Os pesos somam 100. O score deve ser acompanhado de cobertura de evidência. Um score aparentemente alto com baixa cobertura não é comparável a uma avaliação completa.

## Classes de evidência

| Classe | Uso |
|---|---|
| Documentação oficial | Comportamento e políticas declaradas por uma plataforma. |
| Paper revisado por pares | Evidência científica com escopo e limitações descritos. |
| Preprint | Evidência emergente; usar como direção, não consenso. |
| Dados próprios | Evidência do projeto, desde que método e período estejam registrados. |
| Curso ou material didático | Apoio operacional; claims devem ser triangulados. |
| Vendor ou practitioner study | Hipótese ou evidência observacional com risco comercial. |

## Métricas mínimas do benchmark

- presença da marca;
- recomendação explícita;
- domínio ou URL citada;
- suporte da citação;
- absorção;
- precisão da entidade;
- concorrentes presentes;
- estabilidade entre repetições;
- taxa de erros ou estados não avaliáveis.

Não usar apenas contagem de screenshots, volume bruto de menções ou uma única engine.

## Limites

- Engines e modelos mudam sem preservar comparabilidade perfeita.
- Interfaces podem ocultar modelo, índice, personalização ou ativação de busca.
- Scores são instrumentos de decisão, não indicadores universais.
- Correlação entre intervenção e resultado não prova causalidade sem desenho adequado.
- GEO não substitui SEO técnico, conteúdo útil, pesquisa de usuário, analytics ou estratégia de marca.
- Answer blocks e citation engineering melhoram a disciplina editorial, mas não garantem seleção, absorção ou citação.
- Content briefs, mapas de autoridade e competitor gaps são artefatos de planejamento; precisam de validação em casos reais antes de automação.
- Scorecards e auditorias organizam julgamento humano; não determinam verdade, qualidade estratégica universal ou comportamento futuro de engines.
