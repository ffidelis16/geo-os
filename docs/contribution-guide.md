# Guia de contribuição

## Antes de contribuir

- Leia `AGENTS.md`.
- Abra uma issue quando a mudança alterar contrato ou metodologia.
- Não inclua material privado, proprietário ou dados pessoais.
- Use exemplos fictícios e domínios `.invalid`.

## Ambiente local

```powershell
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

Não adicione dependência externa sem justificar necessidade, risco e manutenção.

## Tipos de mudança

- Correção editorial ou link: `PATCH`.
- Novo módulo, skill, prompt ou campo compatível: `MINOR`.
- Mudança de escala, header obrigatório ou significado: `MAJOR`.

Para mudança de comportamento, escreva o teste primeiro e confirme a falha esperada.

## Política de fontes

- Priorize documentação oficial e fontes primárias.
- Registre acesso, tipo, confiabilidade e limitação.
- Fontes privadas podem ser citadas genericamente como influência, sem caminho local ou reprodução.
- Não copie slides, apostilas, transcrições, imagens ou exemplos exclusivos de curso.

## Pull request

Inclua:

- problema resolvido;
- arquivos e contratos afetados;
- classificação dos claims;
- testes executados;
- limitações;
- confirmação de que não há material privado.

Use `.github/pull_request_template.md`.

## Checklist

- [ ] Nomes de arquivos em inglês e conteúdo em PT-BR.
- [ ] Exemplos fictícios.
- [ ] Sem promessa de ranking ou citação.
- [ ] Sem caminhos pessoais, secrets ou fontes privadas.
- [ ] Testes aprovados.
- [ ] Validador aprovado.
- [ ] Source ledger atualizado quando necessário.
