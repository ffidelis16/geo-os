---
name: ai-search-testing
description: Planeja, executa e documenta benchmarks reproduzíveis de AI Search. Use para medir presença, citação, suporte, absorção, precisão de entidade, concorrentes e estabilidade entre engines, locales, datas e repetições.
---

# Testes de AI Search

## Objetivo

Transformar observações de respostas generativas em um benchmark auditável, comparável e honesto sobre suas limitações.

## Quando usar

- Para estabelecer baseline de marca, categoria ou página.
- Antes e depois de mudanças relevantes.
- Para comparar engines, concorrentes, locales ou tipos de intenção.
- Em monitoramento periódico com método estável.

## Quando não usar

- Para concluir causalidade com uma execução.
- Para comparar resultados coletados com prompts ou condições diferentes sem normalização.
- Quando a engine, data, locale ou modo de busca não podem ser registrados.
- Como substituto de métricas de negócio ou analytics.

## Inputs

Mínimos:

- prompt set versionado;
- marca, domínio e concorrentes;
- engines e modos;
- locale, data e número de repetições.

Opcionais: páginas-alvo, respostas anteriores, screenshots, parâmetros de conta, persona e estágio da jornada.

## Processo

1. Selecionar prompts sem alterar a redação durante a rodada.
2. Registrar engine, modelo quando exposto, modo web, conta, locale e timestamp.
3. Executar no mínimo três repetições quando a engine for não determinística.
4. Salvar resposta e URLs citadas sem corrigir manualmente o conteúdo.
5. Avaliar separadamente:
   - presença da entidade;
   - citação do domínio ou URL;
   - suporte real da citação ao claim;
   - absorção de evidência ou estrutura;
   - precisão de nomes e atributos;
   - posição relativa de concorrentes;
   - continuação em follow-ups, quando testada;
   - hand-off para uma próxima ação observável, quando houver dados.
6. Registrar indisponibilidade, bloqueio ou ausência de busca como estado próprio.
7. Separar métricas da resposta de métricas posteriores: presença e atribuição não substituem analytics; hand-off e conversão exigem instrumentação própria.
8. Agregar resultados por prompt, intenção, engine e rodada.
9. Comparar versões apenas quando o protocolo permanecer compatível.
10. Tratar qualquer delta como observação do protocolo. Correlação temporal não implica causalidade da intervenção.

## Outputs

- planilha de benchmark;
- resumo por engine e intenção;
- lista de fontes recorrentes;
- incidentes de atribuição ou entidade;
- sinais de continuação e hand-off, quando medidos;
- hipóteses para intervenção e plano de re-teste.

## Critérios de qualidade

- Protocolo e prompt set são versionados.
- Resultados brutos permanecem disponíveis.
- Ausência de citação não é confundida com ausência de influência.
- Citação é verificada contra o conteúdo da fonte.
- Comparações usam o mesmo denominador e condições equivalentes.
- Limitações de personalização, volatilidade e acesso estão explícitas.
- Métricas de resposta, analytics e resultados de negócio permanecem separadas.

## Erros comuns

- Usar screenshots como única evidência.
- Rodar prompts diferentes para cada concorrente.
- Misturar menção, recomendação, citação e absorção.
- Forçar busca web e comparar com uma rodada sem busca.
- Reportar percentuais sem informar amostra e repetições.
