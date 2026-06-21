# Arquitetura

## Princípios

- Arquivos são a interface principal.
- Cada skill executa um trabalho delimitado.
- Módulos guardam metodologia compartilhada.
- Templates funcionam como contratos de saída.
- Rubricas e datasets tornam critérios explícitos.
- Scripts validam estrutura; humanos avaliam estratégia e verdade.
- O repositório público não contém fontes privadas.

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
Intent + Entity + Evidence
            ↓
Planejamento → Produção → Avaliação
                           ↓
                     Otimização
                           ↓
                    Reavaliação
                           ↓
                    Documentação
```

Cada transição preserva origem, evidência, limitações e responsável.

## Skills canônicas e proxies

`skills/<name>/SKILL.md` é a fonte de verdade. `.agents/skills/<name>/SKILL.md` deve conter o mesmo frontmatter e uma referência relativa para a fonte canônica.

Não edite apenas o proxy. O validador rejeita divergência de metadados e referência quebrada.

## Contratos

- Skills exigem frontmatter `name` e `description` e seções operacionais.
- Módulos exigem objetivo, uso, inputs, processo, outputs, qualidade e erros.
- Templates Markdown exigem headings definidos por tipo.
- CSVs exigem headers e largura consistente em todas as linhas.
- JSONs exigem locale, IDs únicos, módulos válidos e critérios qualitativos.
- YAMLs exigem escala, pesos, evidências, interpretação e limitações.

Mudança de heading, header ou critério pode ser mudança de contrato.

## Limites de arquitetura

- Não há runtime de agente próprio.
- Não há integração com engines, analytics ou plataformas.
- Não há sincronização automática entre outputs.
- Não há julgamento automático de qualidade estratégica.
- Não há material privado, transcrição, apostila ou slide no repositório.
- Adapters de plataforma só devem existir quando houver necessidade demonstrada.
