# Política de atualização

## Objetivo

Manter o GEO OS útil sem transformar sinais voláteis em regras permanentes.

## Versionamento

Usar versionamento semântico:

- `PATCH`: correções editoriais, links, exemplos e validações sem mudança de contrato.
- `MINOR`: novos módulos, skills, critérios, prompts ou campos opcionais compatíveis.
- `MAJOR`: mudanças de escala, pesos, campos obrigatórios ou significado de métricas.

Rubricas e datasets devem declarar `version` ou `schema_version`.

## Gatilhos de revisão

Revisar a metodologia quando ocorrer:

- mudança oficial de documentação de uma plataforma;
- publicação relevante revisada por pares;
- alteração material no comportamento observado das engines;
- falha recorrente em uso real;
- novo requisito comercial, legal ou ético;
- mudança incompatível em templates ou validações.
- alteração material de intent, entidade, oferta, regulação ou cenário competitivo.

Na ausência de gatilho, revisar o ledger e os links ao menos trimestralmente.

## Hierarquia de fontes

1. documentação oficial e especificações;
2. papers revisados por pares;
3. datasets ou documentação primária;
4. preprints;
5. estudos independentes reproduzíveis;
6. materiais didáticos;
7. relatórios de vendors, posts e opinião.

Fonte inferior pode gerar hipótese, mas não deve sobrescrever silenciosamente fonte superior.

## Processo de mudança

1. Registrar a nova fonte em `docs/source-ledger.md`.
2. Identificar claims, módulos, skills, rubricas, templates e prompts afetados.
3. Classificar a mudança como fato, inferência, hipótese ou framework próprio.
4. Atualizar primeiro o módulo canônico e depois as skills dependentes; nunca alterar apenas `.agents/skills/`.
5. Ajustar testes quando houver mudança de contrato.
6. Executar:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

7. Registrar versão e motivo da alteração no commit.

## Atualização dos artefatos estratégicos

### Content briefs

Revisar quando mudar:

- target intent ou audiência;
- estágio de decisão;
- core claims ou evidências;
- entidade principal ou relações;
- requisito de frescor;
- estrutura canônica;
- risco regulatório.

### Topical authority maps

Revisar quando houver novas páginas, mudança de taxonomia, duplicação, conflito, lacuna priorizada ou alteração relevante no entity map.

### Competitor analyses

Registrar sempre `accessed_at`. Reavaliar quando URLs mudarem, conteúdo for atualizado, concorrentes deixarem de ser comparáveis ou critérios de mercado mudarem.

### Scorecards e auditorias

Revisar o scorecard, extractability audit e trust signal audit quando mudar:

- o conteúdo, sua versão ou o target intent;
- a entidade principal, o público ou o estágio de decisão;
- autoria, fontes, método, datas ou limitações;
- a estrutura, os answer blocks ou os dados visíveis;
- a versão das rubricas ou do protocolo de avaliação.

Scores só podem ser comparados quando escopo, critérios, pesos e tratamento de `N/A` forem compatíveis. Toda reavaliação deve registrar data, versão do método, cobertura e evidências utilizadas.

### Planos de otimização

Revisar rewrite plans, content refresh plans, schema opportunities e optimization cycles quando mudar:

- o gap de origem ou sua prioridade;
- o conteúdo, intent, entidade ou evidência;
- a documentação oficial de schema;
- o owner, dependência, risco ou esforço;
- o critério de sucesso ou o protocolo de reavaliação.

Encerrar cada ciclo com decisão explícita: `manter`, `revisar`, `expandir` ou `abandonar`. Não promover resultado esperado de `[HIPÓTESE]` para `[FATO]` sem evidência da reavaliação.

## Regras para estatísticas

Toda estatística deve registrar:

- fonte;
- data de publicação ou período;
- data de acesso;
- população/amostra;
- método conhecido;
- limitação material.

Remover ou rebaixar para `[HIPÓTESE]` quando a origem não puder ser recuperada.

## Compatibilidade

- Não renomear IDs de critérios ou prompts sem necessidade.
- Preferir campos novos opcionais em versões `MINOR`.
- Para mudança `MAJOR`, documentar migração de CSV, JSON e YAML.
- Tratar mudanças de headings obrigatórios em módulos e templates Markdown como mudança de contrato.
- Tratar mudança de headers nos mapas CSV e de critérios no dataset golden como mudança de contrato.
- Manter conteúdo em PT-BR e nomes de arquivos em inglês.

## Depreciação

Marcar item como `deprecated` antes de remover quando ele tiver consumidores conhecidos. Informar substituto, motivo e versão prevista para remoção.

## Revisão humana

O validador estrutural não determina se um claim é verdadeiro, se uma fonte é adequada ou se uma recomendação é estratégica. Toda release metodológica exige revisão humana desses pontos.
