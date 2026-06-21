# Exemplos de uso

Os exemplos usam o projeto fictício **Farol Urbano**, com domínio reservado `farol-urbano.example.invalid`.

## Escolher um fluxo com o orquestrador

Quando o pedido ainda não indica a skill correta:

```text
$geo-os-orchestrator Tenho uma landing page antiga, conheço os principais gaps e quero preparar uma atualização sem escrever o texto final.
```

Resultado esperado:

- fluxo `prepare-content-refresh`;
- `content-refresh` como skill mínima;
- gaps, versão do ativo e critério de sucesso conferidos como inputs;
- `templates/content-refresh-plan.csv` e `templates/optimization-cycle-template.md`;
- output sugerido em `outputs/farol-urbano/workflow-selection.md`;
- próximo comando pronto para executar a skill selecionada.

O orquestrador registra rotas descartadas e não adiciona auditorias quando os gaps já estão disponíveis.

## Auditar um conteúdo

Input mínimo:

- texto completo;
- target intent: “como reduzir desperdício doméstico”;
- público: pessoas iniciantes;
- entidade principal: Farol Urbano;
- fontes fornecidas.

Fluxo:

```text
extractability-audit
        ↓
trust-signal-audit
        ↓
geo-scorecard
```

Saídas esperadas: trechos frágeis, sinais de confiança, scores justificados, cobertura, gaps e limitações. Veja [sample-geo-audit.md](../examples/sample-geo-audit.md).

## Criar um mapa de entidades

1. Copie `templates/entity-map.csv` para `outputs/entity-map.csv`.
2. Remova a linha de exemplo.
3. Registre nome canônico, tipo, definição, aliases e URL.
4. Crie relações direcionais apenas quando houver evidência.
5. Separe entidade principal, organização, projeto, autor e tópicos.

```text
$entity-map normalize as entidades do conteúdo fornecido e registre fontes.
```

Veja [sample-entity-map.csv](../examples/sample-entity-map.csv).

## Transformar gaps em plano de otimização

Inputs:

- scorecard;
- extractability audit;
- trust signal audit;
- conteúdo avaliado.

Fluxo:

```text
Gaps → rewrite-plan → aprovação editorial
     ↘ content-refresh
     ↘ schema-opportunity
                ↓
      optimization-cycle
```

Toda ação deve indicar origem do gap, impacto, esforço, risco, owner e critério de reavaliação. O plano não deve escrever o conteúdo final.

Veja [sample-rewrite-plan.md](../examples/sample-rewrite-plan.md) e [sample-optimization-cycle.md](../examples/sample-optimization-cycle.md).
