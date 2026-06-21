---
name: answer-blocks
description: Use quando for necessário criar ou revisar blocos de resposta curtos, autocontidos, verificáveis e reutilizáveis para definições, comparações, procedimentos, critérios de escolha, FAQs ou páginas orientadas a AI Search.
---

# Answer Blocks

## Objetivo

Criar uma unidade editorial que responda uma intenção específica com contexto mínimo, claims verificáveis, evidência próxima e ressalvas proporcionais ao risco.

Antes de executar, ler `modules/answer-blocks.md`. Usar `templates/answer-block-template.md` como contrato de saída.

## Quando usar

- Depois de mapear a intenção e liberar as evidências.
- Ao dividir páginas longas em unidades mais claras.
- Para definições, comparações, procedimentos e critérios.
- Ao corrigir conteúdo vago, dependente de contexto ou difícil de verificar.

## Quando não usar

- Quando não há evidência suficiente para os claims.
- Para forçar resposta curta em tema que exige nuance.
- Como promessa de extração, absorção ou citação.
- Para substituir a página inteira por fragmentos desconectados.

## Inputs

Mínimos:

- intenção principal;
- audiência e restrições;
- entidades canônicas;
- claims e evidências liberados.

Opcionais: página-alvo, formato, limite editorial, links, CTA e requisitos regulatórios.

## Processo

1. Confirmar uma intenção principal por bloco.
2. Consultar o intent map e o evidence ledger.
3. Escolher entre definição, passos, lista, tabela, critérios ou mini-FAQ.
4. Aplicar o contrato `claim + contexto + evidência + takeaway`.
5. Fazer front-loading da resposta, sem introdução promocional.
6. Delimitar condição, período, local ou audiência.
7. Associar cada claim à sua evidência.
8. Separar `[FATO]`, `[INFERÊNCIA]`, `[HIPÓTESE]` e `[FRAMEWORK PRÓPRIO]`.
9. Incluir ressalvas que alterem a decisão.
10. Usar answer sandwich somente quando a síntese final acrescentar orientação.
11. Posicionar CTA contextual depois da resposta, quando houver próxima ação válida.
12. Preencher a checklist do template.

Exemplo mínimo:

> **Resposta direta:** O prazo varia conforme X e Y. Em cenários Z, a faixa observada é A–B.
> **Evidência:** fonte, período e escopo.
> **Ressalva:** casos fora de Z exigem avaliação específica.

## Outputs

- answer block preenchido;
- claims e fontes relacionados;
- ressalvas;
- links e dependências;
- status de revisão.

## Critérios de qualidade

- Responde somente uma intenção.
- Funciona fora do restante da página.
- Não afirma mais do que a evidência permite.
- Mantém fonte próxima ao claim.
- Preserva contexto e exceções materiais.
- Usa nomes de entidades canônicos.
- Entrega valor antes de qualquer CTA.

## Erros comuns

- Misturar resposta, propaganda e CTA.
- Citar uma fonte genérica para vários claims.
- Remover ressalvas para reduzir palavras.
- Usar superlativos ou falsa certeza.
- Criar blocos que contradizem páginas canônicas.
