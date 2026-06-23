# Getting started

## Requisitos

- Git.
- Python 3.11 ou superior.
- PyYAML.
- Editor capaz de abrir Markdown, CSV, JSON e YAML.

O projeto não precisa de banco, serviço externo, crawler ou chave de API.

## Início rápido

```powershell
git clone https://github.com/ffidelis16/GEO-OS.git
cd GEO-OS
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

O primeiro comando testa os contratos. O segundo valida estrutura, frontmatter, headings, JSON, YAML, CSV e higiene pública.

## Tour do repositório

- Comece pelo [README](../README.md).
- Leia [architecture.md](architecture.md) para entender as fronteiras.
- Escolha um fluxo em [usage-examples.md](usage-examples.md).
- Consulte `modules/` para o método canônico.
- Use `skills/` quando quiser acionar um trabalho específico.
- Copie arquivos de `templates/` para `outputs/`, que é ignorado pelo Git.
- Compare o preenchimento com `examples/`.

## Primeiro fluxo

Para auditar um conteúdo:

1. Forneça o texto ou arquivo; não apenas uma URL.
2. Registre intenção, público e entidade principal.
3. Execute `extractability-audit` e `trust-signal-audit`.
4. Consolide em `geo-scorecard`.
5. Use `rewrite-plan` ou `content-refresh` para os gaps priorizados.
6. Registre reavaliação em `optimization-cycle-template.md`.

Exemplo preenchido: [sample-geo-audit.md](../examples/sample-geo-audit.md).

## Validação

Execute antes de qualquer commit:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
```

O validador é estrutural. Ele não comprova verdade factual, adequação estratégica, elegibilidade em plataformas ou qualidade de uma fonte.

Se alterar um contrato, ajuste os testes primeiro e confirme que o novo teste falha pela razão esperada.
