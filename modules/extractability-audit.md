# Extractability Audit

## Objetivo

Auditar se um conteúdo pode ser compreendido e reutilizado em blocos discretos sem depender de contexto implícito, layout visual ou leitura integral.

`[FRAMEWORK PRÓPRIO]` Extraibilidade é propriedade editorial observável. Não prova que uma engine recuperará, resumirá ou citará o conteúdo.

## Quando usar

- Em conteúdo existente antes de um refresh.
- Quando respostas generativas distorcem ou omitem o ponto central.
- Quando há paredes de texto, headings vagos ou claims dispersos.
- Para alimentar `geo-scorecard` e `answer-blocks`.

## Inputs

Mínimos:

- conteúdo completo ou trecho identificado;
- target intent;
- tipo de ativo;
- estrutura preservada quando disponível.

Opcionais: HTML fornecido, content brief, answer blocks, entity map, evidence ledger e schema atual.

Não inferir elementos visuais, markup ou conteúdo fora do material recebido.

## Processo

1. Confirmar escopo e target intent.
2. Localizar respostas diretas e definições.
3. Verificar se headings descrevem perguntas ou tarefas.
4. Inventariar blocos autossuficientes:
   - definições;
   - listas;
   - tabelas;
   - comparações;
   - passos;
   - FAQs reais;
   - claims e dados citáveis.
5. Verificar se cada bloco preserva contexto, entidade, período e ressalva.
6. Identificar:
   - texto contínuo excessivo;
   - dependência visual;
   - pronomes ou referências ambíguas;
   - claims compostos;
   - tabelas sem critério;
   - FAQs artificiais;
   - evidência distante.
7. Sugerir answer blocks e reestruturação.
8. Sugerir schema apenas quando o conteúdo visível já sustenta o tipo.
9. Priorizar correções por impacto e esforço.
10. Alimentar o scorecard com evidências, não apenas nota.

## Outputs

- diagnóstico;
- blocos encontrados e ausentes;
- trechos frágeis;
- answer block opportunities;
- schema opportunities;
- recomendações de reestruturação;
- correções prioritárias;
- limitações.

## Critérios de qualidade

- Cada problema aponta para trecho ou localização.
- Extraibilidade não é confundida com brevidade.
- Recomendações preservam evidência e nuance.
- Blocos sugeridos respondem intents reais.
- Schema opportunities dependem de conteúdo visível.
- Output alimenta `answer-blocks`, `content-brief` ou refresh.

## Erros comuns

- Exigir sempre 40–60 palavras.
- Transformar todo conteúdo em FAQ.
- Dar nota alta só porque há listas.
- Ignorar ambiguidade entre entidades.
- Sugerir tabelas sem critérios equivalentes.
- Declarar conteúdo não fornecido como ausente.
