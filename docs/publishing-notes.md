# Notas de publicação

## Escopo público

O repositório público contém síntese autoral, metodologia transformada, templates próprios, rubricas, datasets, exemplos fictícios e código de validação.

Ele não contém materiais fechados usados durante o estudo.

## Material privado

Manter fora do Git:

- apostilas e sínteses com imagens incorporadas;
- PDFs, DOCX e PPTX de cursos;
- slides, prints e transcrições;
- anotações pessoais;
- outputs de projetos reais;
- relatórios com marcas, pessoas ou dados identificáveis.

A versão v3 da síntese privada revisada em 2026-06-21 incorpora imagens originais do curso em base64 e não deve ser publicada.

## Checklist pré-publicação

```powershell
python -m unittest discover -s tests -v
python scripts/validate_output.py --root .
git status --short
git ls-files
```

Também verificar:

- ausência de caminhos como diretórios pessoais do Windows;
- ausência de arquivos privados rastreados;
- exemplos exclusivamente fictícios;
- licença e changelog presentes;
- links relativos válidos;
- working tree limpa.

## Processo de release

1. Atualizar `CHANGELOG.md`.
2. Revisar `docs/source-ledger.md`.
3. Executar testes e validador.
4. Revisar `git diff --cached`.
5. Criar commit semântico.
6. Publicar somente após inspeção final dos arquivos rastreados.

## Comunicação pública

Posicionamento recomendado:

> Estou organizando meu estudo de GEO e AI Search em um repositório modular aberto. A proposta é tratar GEO como método de clareza de entidades, evidência, estrutura, extraibilidade e avaliação — não como truque de ranking.

Evitar superlativos, resultados não medidos e linguagem de garantia.
