# Arquitetura

## Princípios

- Arquivos são a interface principal.
- Cada skill executa um trabalho delimitado.
- Módulos guardam metodologia compartilhada.
- Templates funcionam como contratos de saída.
- Rubricas e datasets tornam critérios explícitos.
- Scripts validam estrutura; humanos avaliam estratégia e verdade.
- O repositório público não contém fontes privadas.
- A camada de orquestração seleciona trabalho; as skills executoras mantêm seus próprios contratos.

## Diretórios

| Diretório | Responsabilidade |
|---|---|
| `skills/` | Fonte canônica das instruções acionáveis. |
| `.agents/skills/` | Proxies de descoberta que apontam para as skills canônicas. |
| `modules/` | Método operacional reutilizável. |
| `templates/` | Contratos vazios ou linhas de exemplo removíveis. |
| `rubrics/` | Critérios ponderados em escala ordinal 0–4. |
| `datasets/golden/` | Cenários qualitativos e prompts de benchmark. |
| `scripts/` | Validação determinística. |
| `tests/` | Regressão dos contratos. |
| `docs/` | Metodologia, fontes, uso e governança. |
| `examples/` | Demonstrações fictícias criadas para o projeto. |
| `.github/` | Templates para colaboração pública. |

## Fluxo operacional

```text
Pedido em linguagem natural
            ↓
geo-os-orchestrator
            ↓
menor fluxo suficiente
            ↓
skill executora → template → output → revisão humana
```

Cada transição preserva origem, evidência, limitações e responsável.

O `geo-os-orchestrator` é o roteador da camada de orquestração. Ele escolhe um fluxo principal, adiciona somente dependências que desbloqueiam inputs essenciais e encerra sua função ao entregar o próximo comando. Não duplica metodologia, não executa todas as skills e não produz conteúdo final.

## Skills canônicas e proxies

`skills/<name>/SKILL.md` é a fonte de verdade. `.agents/skills/<name>/SKILL.md` deve conter o mesmo frontmatter e uma referência relativa para a fonte canônica.

Não edite apenas o proxy. O validador rejeita divergência de metadados e referência quebrada.

## Contratos

- Skills exigem frontmatter `name` e `description` e seções operacionais.
- Módulos exigem objetivo, uso, inputs, processo, outputs, qualidade e erros.
- Templates Markdown exigem headings definidos por tipo.
- CSVs exigem headers e largura consistente em todas as linhas.
- JSONs exigem locale, IDs únicos, módulos válidos e critérios qualitativos.
- O dataset do orquestrador exige os dez fluxos, skills e templates existentes, suficiência mínima, lacunas, limitações e próximo comando.
- YAMLs exigem escala, pesos, evidências, interpretação e limitações.

Mudança de heading, header ou critério pode ser mudança de contrato.

## Limites de arquitetura

- Não há runtime de agente próprio.
- Não há integração com engines, analytics ou plataformas.
- Não há sincronização automática entre outputs.
- Não há julgamento automático de qualidade estratégica.
- O orquestrador não é runtime, agente autônomo ou super-skill.
- Não há material privado, transcrição, apostila ou slide no repositório.
- Adapters de plataforma só devem existir quando houver necessidade demonstrada.
