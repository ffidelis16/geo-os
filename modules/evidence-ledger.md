# Evidence Ledger

## Objetivo

Manter um registro auditável entre claim, fonte, tipo de evidência, data, confiabilidade, uso permitido e risco.

`[FRAMEWORK PRÓPRIO]` O ledger é a camada de controle factual do GEO OS. Ele preserva contradições e limitações; não escolhe automaticamente a fonte “vencedora”.

## Quando usar

- Antes de criar answer blocks ou claims comparativos.
- Durante auditorias de citabilidade.
- Quando várias fontes sustentam versões diferentes do mesmo claim.
- Para controlar estatísticas, datas, credenciais e fontes de terceiros.

## Inputs

Mínimos:

- claim textual;
- página e seção onde será usado;
- fonte identificável;
- tipo de fonte;
- data de acesso.

Opcionais: data de publicação, trecho de suporte, metodologia, população, owner, validade, restrições legais e fontes contraditórias.

## Processo

1. Dividir claims compostos em unidades verificáveis.
2. Classificar como `[FATO]`, `[INFERÊNCIA]`, `[HIPÓTESE]` ou `[FRAMEWORK PRÓPRIO]`.
3. Registrar URL, título, autor ou organização e tipo de fonte.
4. Identificar o tipo de evidência: definição, dado, experimento, política, testemunho, observação ou síntese.
5. Registrar publicação, acesso e validade temporal.
6. Avaliar confiabilidade e confiança sem confundir as duas:
   - confiabilidade avalia a fonte;
   - confiança avalia a força da relação claim-evidência.
7. Definir uso permitido: público, interno, inspiração, hipótese ou proibido.
8. Classificar risco: baixo, médio, alto ou crítico.
9. Registrar contradições sem apagá-las.
10. Definir owner, status e próxima revisão.

Claims de alto risco exigem fonte compatível com o risco e revisão humana.

## Outputs

- `templates/evidence-ledger.csv` preenchido;
- lista de claims liberados;
- claims bloqueados ou incompletos;
- contradições;
- agenda de atualização;
- insumos para citation engineering.

## Critérios de qualidade

- Cada linha contém um claim atômico.
- A fonte pode ser recuperada por outra pessoa.
- Datas e limitações estão explícitas.
- Confiabilidade, confiança e risco usam vocabulário controlado.
- Uso permitido evita transformar material fraco em claim público.
- Contradições permanecem rastreáveis.

## Erros comuns

- Salvar apenas uma lista de links.
- Usar fonte que repete outra sem chegar à origem.
- Confundir fonte conhecida com evidência forte.
- Não registrar data para preço, política ou estatística.
- Rebaixar contradições a notas invisíveis.
- Autorizar uso público de hipótese ou material promocional sem ressalva.
