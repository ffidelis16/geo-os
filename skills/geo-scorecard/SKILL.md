---
name: geo-scorecard
description: Use quando um único ativo com conteúdo fornecido precisa ser pontuado e diagnosticado quanto a intenção, entidades, evidência, citabilidade, answer blocks, extraibilidade, confiança, frescor, estrutura e acionabilidade. Consolida auditorias; não é o primeiro diagnóstico de conteúdo bruto.
---

# GEO Scorecard

## Objetivo

Consolidar auditorias em um score transparente de `0–100`, com justificativa, cobertura, lacunas e prioridades de melhoria.

Ler `modules/geo-scorecard.md`. Usar os templates `geo-scorecard-template.md` e `geo-scorecard.csv`.

## Quando usar

- Para auditar conteúdo fornecido.
- Antes e depois de um refresh.
- Para comparar ativos sob o mesmo protocolo.
- Para consolidar extractability e trust signal audits.

## Quando não usar

- Se apenas uma URL foi informada e o conteúdo não foi fornecido.
- Para prever ranking ou citação.
- Para comparar scores com escopos incompatíveis.
- Como substituto de revisão factual.

## Inputs

- Conteúdo, trecho ou artefato.
- Target intent, público e entidade principal.
- Origem, data e escopo.
- Fontes fornecidas.
- Outputs de `extractability-audit` e `trust-signal-audit`, quando disponíveis.
- Artefatos de intent, evidence, content brief, topical authority e competitor analysis.

## Outputs

- Score e cobertura.
- Notas justificadas por dimensão.
- Evidências, lacunas e riscos.
- Correções priorizadas.
- Próximos passos.

## Processo

1. Confirmar o conteúdo realmente disponível.
2. Consultar `intent-map`, `entity-map` e `evidence-ledger`.
3. Executar `extractability-audit`.
4. Executar `trust-signal-audit`.
5. Pontuar as 16 dimensões do módulo.
6. Usar `N/A` quando não houver evidência.
7. Calcular total com denominador ajustado e informar cobertura.
8. Relacionar cada nota a evidência observada.
9. Transformar main gaps em ações para `content-brief`, `citation-engineering` ou `answer-blocks`.

## Restrições

- Não afirmar que URL foi rastreada.
- Não atribuir score sem justificativa.
- Não converter `N/A` em zero.
- Não usar score como probabilidade de citação.
- Não esconder limitações para elevar nota.

## Critérios de qualidade

- Diagnóstico diferencia evidência, inferência e recomendação.
- Toda nota é auditável.
- Cobertura acompanha o score.
- Recomendações têm prioridade e resultado esperado.
- Output é executável por editor ou estrategista.

## Modos de falha

- Score decorativo sem evidência.
- Muitas notas médias para evitar decisão.
- Comparação entre versões com protocolos diferentes.
- Recomendações genéricas.
- Conteúdo ausente tratado como conteúdo fraco.

## Exemplo

Se o usuário fornece apenas `https://example.com`, registrar que a página não foi rastreada, pontuar dimensões como `N/A` e pedir texto ou arquivo. Se fornece o HTML, auditar o material observado e citar trechos.

## Erros comuns

- Somar scores manualmente sem pesos.
- Ignorar a cobertura.
- Confundir schema opportunity com implementação válida.
- Entregar nota sem plano de correção.
