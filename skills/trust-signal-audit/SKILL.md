---
name: trust-signal-audit
description: Use quando um conteúdo precisa ser auditado quanto a autoria, credenciais, organização responsável, fontes, evidência, datas, metodologia, transparência, consistência factual, conflitos de interesse e riscos de credibilidade.
---

# Trust Signal Audit

## Objetivo

Diagnosticar se os sinais observáveis permitem confiar nos claims e quais lacunas precisam ser corrigidas antes da publicação ou reutilização.

Ler `modules/trust-signal-audit.md`. Usar `templates/trust-signal-audit-template.md`.

## Quando usar

- Antes de liberar claims.
- Em conteúdo técnico, comparativo ou sensível.
- Quando autoria, fontes ou frescor são incertos.
- Para alimentar `geo-scorecard` e `citation-engineering`.

## Quando não usar

- Sem conteúdo ou sinais fornecidos.
- Para confirmar credenciais que não foram verificadas.
- Para tratar schema ou design como confiança.
- Como due diligence jurídica completa.

## Inputs

- Conteúdo, byline e dados de autoria disponíveis.
- Organização responsável.
- Fontes, datas e metodologia.
- Evidence ledger e entity map.
- Content brief, topical authority e competitor analysis, quando relevantes.

## Outputs

- Sinais fortes e fracos.
- Lacunas de evidência.
- Riscos de credibilidade.
- Recomendações de fonte e processo.
- Melhorias prioritárias.
- Limitações.
- Inputs para o scorecard.

## Processo

1. Confirmar origem e escopo.
2. Auditar autor, credenciais e experiência.
3. Auditar organização e responsabilidade editorial.
4. Relacionar fontes aos claims no `evidence-ledger`.
5. Avaliar frescor e metodologia.
6. Identificar evidência primária, transparência e conflitos.
7. Verificar consistência factual e linguagem especulativa.
8. Encaminhar lacunas para `citation-engineering`.
9. Registrar sinais no `geo-scorecard`.

## Restrições

- Usar `não observado` para informação fora do input.
- Não validar credencial apenas porque foi declarada.
- Não tratar citação como endorsement.
- Não inferir revisão real apenas por `dateModified`.
- Não ocultar conflito ou limitação.

## Critérios de qualidade

- Cada sinal possui evidência.
- Fonte e claim são avaliados juntos.
- Frescor é proporcional ao tema.
- Riscos são priorizados.
- Recomendações indicam prova, owner ou processo.
- Diagnóstico diferencia fato, inferência e recomendação.

## Modos de falha

- Checklist de E-E-A-T sem evidência.
- Confiança baseada em tom.
- Fontes secundárias tratadas como primárias.
- Ausência de input tratada como falha.
- Recomendações vagas como "melhorar autoridade".

## Exemplo

Uma página tem byline e `dateModified`, mas nenhuma credencial verificável, método ou fonte primária. Registrar autoria como parcial, frescor como não confirmado e priorizar verificação do autor, metodologia e fontes.

## Erros comuns

- Pontuar design ou branding.
- Ignorar conflitos de interesse.
- Aceitar lista de referências distante dos claims.
- Não registrar riscos de credibilidade.
