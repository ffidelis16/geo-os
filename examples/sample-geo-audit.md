# Exemplo fictício de auditoria GEO

Todos os nomes, URLs e dados abaixo foram criados exclusivamente para demonstrar o contrato.

## Metadados

| Campo | Valor |
|---|---|
| Audit ID | EXAMPLE-AUDIT-001 |
| Data | 2026-06-21 |
| Ativo | `https://farol-urbano.example.invalid/guia-desperdicio` |
| Target intent | Como reduzir desperdício doméstico |
| Entidade principal | Farol Urbano |

## Escopo

Foram fornecidos o texto integral, headings, byline e duas fontes públicas. Elementos visuais, HTML, schema e desempenho em engines não foram avaliados.

## Achados

- `[FATO]` A introdução demora quatro parágrafos para responder à pergunta principal.
- `[FATO]` A estatística central não informa período nem população.
- `[FATO]` A autoria é identificada, mas não há perfil ou credencial verificável.
- `[INFERÊNCIA]` A resposta pode perder contexto quando extraída porque usa “essa prática” sem antecedente no mesmo bloco.
- `[HIPÓTESE]` Uma definição direta e uma lista de etapas podem melhorar a reutilização do conteúdo.

## Prioridades

1. `[RECOMENDAÇÃO]` Bloquear a estatística até localizar fonte adequada.
2. `[RECOMENDAÇÃO]` Criar resposta direta após o heading principal.
3. `[RECOMENDAÇÃO]` Substituir referências ambíguas por nomes explícitos.
4. `[RECOMENDAÇÃO]` Adicionar perfil de autor somente após verificar credenciais.

## Limitações

- Não houve crawl ou inspeção da URL.
- Não houve teste em engine generativa.
- A auditoria não prevê ranking, citação ou tráfego.
- Scores dependem do conteúdo fornecido e da data da análise.
