# Overlay privado

## Finalidade

O GEO OS público contém método autoral, skills, módulos, templates, rubricas, datasets e exemplos fictícios. Um overlay privado pode preservar sínteses densas de cursos, playbooks internos, notas de ferramentas, pesquisas em andamento e heurísticas voláteis sem publicar esse material.

O overlay é complementar. O repositório público deve funcionar integralmente sem ele.

## Modos de operação

### Modo público

O Codex usa somente os arquivos versionados no `geo-os`. A ausência de um overlay não pode interromper uma tarefa, reduzir contratos obrigatórios ou exigir arquivos privados.

### Modo privado/local

O Codex procura, nesta ordem:

1. `private/README.md`, para compatibilidade com uma pasta local ainda não migrada;
2. `../geo-os-private/README.md`, para um repositório privado irmão.

Quando encontrado, o overlay pode complementar a análise. Seu conteúdo deve ser tratado como síntese interna, não como citação pública. Claims técnicos continuam exigindo fontes publicáveis e verificáveis.

## Estrutura recomendada

```text
geo-os-private/
├── README.md
├── knowledge/
│   ├── geo-course-synthesis-v3.md
│   ├── advanced-tactics.md
│   ├── execution-playbooks.md
│   ├── measurement-and-tools.md
│   ├── platform-playbooks.md
│   ├── glossary.md
│   └── incorporation-matrix.md
├── sources/
│   └── .gitkeep
└── update-log.md
```

O diretório `sources/` deve ter política própria. PDFs, apostilas, vídeos e transcrições não precisam ser versionados apenas porque o repositório é privado. Arquivos grandes ou licenciados podem permanecer em backup local protegido.

## Migração segura

Não mover automaticamente o conteúdo atual. O procedimento deve copiar antes de remover e preservar a origem até a verificação final.

### 1. Confirmar a separação pública

No `geo-os`:

```powershell
git ls-files private sources course-materials outputs exports reports
git status --ignored --short
```

O primeiro comando não deve listar arquivos. O segundo deve mostrar o material local com `!!`, indicando que está ignorado.

### 2. Criar o repositório irmão local

A partir do diretório que contém `geo-os`:

```powershell
New-Item -ItemType Directory -Path .\geo-os-private
New-Item -ItemType Directory -Path .\geo-os-private\knowledge
New-Item -ItemType Directory -Path .\geo-os-private\sources
```

### 3. Copiar, sem apagar a origem

```powershell
Copy-Item .\geo-os\private\README.md .\geo-os-private\README.md
Copy-Item .\geo-os\private\knowledge\* .\geo-os-private\knowledge\ -Recurse
```

Não usar `Move-Item` nesta etapa.

### 4. Verificar a cópia

```powershell
$sourceFiles = Get-ChildItem .\geo-os\private -File -Recurse
$targetFiles = Get-ChildItem .\geo-os-private -File -Recurse
$sourceFiles.Count
$targetFiles.Count
```

Para comparar conteúdo:

```powershell
Get-FileHash .\geo-os\private\knowledge\*.md
Get-FileHash .\geo-os-private\knowledge\*.md
```

Os arquivos correspondentes devem ter hashes iguais.

### 5. Versionar somente o repositório privado

Dentro de `geo-os-private`:

```powershell
git init
git add README.md knowledge
git commit -m "docs: initialize private GEO knowledge overlay"
```

Criar o remoto como privado antes do primeiro push. Não adicionar o repositório privado como submodule do projeto público.

### 6. Validar recuperação

Antes de remover a origem:

1. confirmar o commit local;
2. confirmar que o remoto é privado;
3. fazer o primeiro push;
4. testar um clone em outro diretório;
5. abrir os arquivos clonados;
6. somente então remover a cópia em `geo-os/private/`.

Esta rodada de preparação pública apenas documenta o procedimento; não executa a migração.

## Uso pelo Codex

- Ler o `README.md` do overlay antes dos arquivos de conhecimento.
- Usar o overlay para contexto, hipóteses, checklists e aprofundamento.
- Separar `[FATO]`, `[INFERÊNCIA]`, `[HIPÓTESE]` e `[FRAMEWORK PRÓPRIO]`.
- Reconfirmar informações voláteis sobre engines, crawlers, preços, ferramentas e políticas.
- Não apresentar uma síntese privada como fonte pública.
- Não revelar caminho local, nome de arquivo fechado ou trecho proprietário em outputs públicos.
- Promover para o repositório público apenas conhecimento transformado, durável e sustentado.

## Prevenção de publicação acidental

Antes de commit ou push público:

```powershell
git status --ignored --short
git ls-files private sources course-materials outputs exports reports
git diff --cached --name-only
```

Também:

- confirmar que `.gitignore` protege materiais privados e outputs;
- não usar `git add -f` em diretórios protegidos;
- procurar caminhos pessoais e nomes de arquivos fechados;
- revisar anexos, imagens e exemplos;
- executar testes e o validador;
- verificar o repositório remoto antes do push.

O fato de um arquivo estar em um repositório privado não autoriza sua publicação posterior.
