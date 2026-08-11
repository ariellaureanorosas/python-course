# Mensagens de Commit — Guia Sênior

A mensagem de commit é a documentação viva do projeto. Quando alguém (inclusive você, daqui a 6 meses) abre o `git log`, é a mensagem que conta a história. Código diz o QUE acontece; a mensagem diz POR QUE aconteceu — e o porquê não dá para deduzir do código.

## A estrutura que todo mundo senior usa

O padrão de facto da indústria é o **Conventional Commits** — uma convenção que máquinas e humanos entendem (geradores de changelog, busca por tipo, análise automatizada):

```
<tipo>(<opcional escopo>): <resumo>

<corpo: por que e como, se precisar>

<rodapé: breaking changes, issues relacionadas>
```

Exemplo completo e real:

```
fix(contrato): retorna lista vazia quando arquivo nao existe

ler_arquivo levantava FileNotFoundError para um caminho inexistente,
o que obrigava o chamador a envolver tudo em try/except so para
"checar se ha algo".

O enunciado do contrato exige retorno vazio ([]) nesse caso; quem
chama pergunta "existe algo?" e recebe um sinal simples, sem excecao.

Refs: #142
```

Subject curto, corpo com o porquê, rodapé com a referência. É isso que sustenta um `git log --oneline` legível e um `git blame` útil anos depois.

## Os tipos (e quando usar cada um)

- `feat` — funcionalidade nova para o usuário. Ex.: `feat(gabarito): adiciona exercicio 17 de JSON`
- `fix` — correção de bug/contrato. Ex.: `fix(ler-arquivo): retorna [] em vez de levantar FileNotFoundError`
- `refactor` — muda estrutura sem mudar comportamento. Ex.: `refactor(validacao): extrai funcao _credenciais_validas`
- `docs` — só documentação. Ex.: `docs(anotacoes): corrige exemplo de ternario na secao 1`
- `test` — testes (adicionar/corrigir). Ex.: `test(gabaritos): adiciona doctest para calcular com desconto`
- `style` — formatação sem mudança de lógica. Ex.: `style: ajusta quebras de linha para PEP 8`
- `perf` — melhora de performance. Ex.: `perf(fatorial): memoiza resultado com lru_cache`
- `chore` — manutenção (deps, build). Ex.: `chore(deps): atualiza Python para 3.14`
- `ci` — configuração de CI/CD. Ex.: `ci: roda doctest de todos os gabaritos no push`
- `revert` — desfaz um commit. Ex.: `revert: volta "feat(gabarito): adiciona exercicio 18"`

Um truque de senior: se você não consegue decidir o tipo, o commit provavelmente mistura mais de uma coisa — divida.

## As 5 regras do assunto (subject line)

1. **Imperativo, tempo presente**: "corrige", "adiciona", "remove". O assunto é uma ordem: "aplique este commit" — o próprio Git usa esse padrão nas mensagens de merge/revert (`Revert "..."`).
2. **≤ 50 caracteres**. Se estourou, a ideia é grande demais — quebre o commit ou jogue o detalhe no corpo.
3. **Sem ponto final** no fim do assunto.
4. **Capitalize a primeira letra** (escolha de estilo do projeto; o Conventional Commits não obriga, mas consistência vence).
5. **Sem detached details**: deixa o quê e o porquê; o como vai no corpo (ou nem precisa).

Antes e depois das regras:

```
ruim:    mudanças feitas
ruim:    final
ruim:    v2
ruim:    corrigindo bugs
ruim:    atualiza arquivo
bom:     fix(ler-arquivo): retorna [] se arquivo nao existe
bom:     feat(gabaritos): adiciona gabarito 16 de arquivo txt
bom:     refactor(quiz): extrai gerador de perguntas para modulo proprio
```

## O corpo — onde mora o porquê

Um commit sem corpo diz O QUE; um commit sênior diz POR QUE. O corpo responde:

- Por que essa mudança era necessária?
- O que o código anterior fazia de errado (e como isso aparecia)?
- Por que essa solução em vez de outra?

```
fix(fatorial): trata n <= 0

A recursao base so cobria n == 1; fatorial(0) estourava a pilha
(RecursionError) quando o usuario digitava 0. Adicionar o caso
n <= 0 na base iguala o contrato matematico (0! == 1) sem custo.
```

## O rodapé — informações estruturais

- `Breaking change:` — aviso obrigatório quando a mudança quebra API/contrato existente (chamadas, formatos de arquivo):

```
Breaking change: remover_tarefa agora retorna None em vez de
levantar IndexError para indice invalido.
```

- `Refs:`/`Closes:`/`Fixes:` — referências a issues/tickets:

```
Closes: #42
```

- `Co-authored-by:` — quando a mudança foi em par/dupla:

```
Co-authored-by: Maria Silva <maria@email.com>
```

## Antes e depois — o mesmo commit, dois níveis

Mensagem que o junior escreve:

```
update

changes in file
```

A mensagem que o senior escreve para o MESMO trabalho:

```
refactor(groupby): ordena produtos antes de agrupar

groupby so agrupa elementos consecutivos iguais; sem o sorted()
por categoria, produtos intercalados caem em grupos separados e
o dict final vem com duplicatas de categoria.

Refs: #88
```

Repare: quem ler o log entende o problema, a causa e a decisão sem abrir UMA linha de código.

## Práticas de senior no dia a dia

- **Um commit, uma ideia.** O commit perfeito não é o maior possível — é o menor que faça uma mudança coerente. Dividir `feat` + `fix` + `refactor` em três commits transforma `git bisect` (achar qual commit quebrou algo) de pesadelo em procedimento trivial.
- **Commit pequeno e frequente localmente; squash antes do main.** No seu branch você pode commitar "wip", "ajeita", "duh"; antes de integrar (merge/PR), reescreva em poucos commits com `git rebase -i` (squash). O histórico do main fica limpo — a crônica do "como cheguei lá" não precisa ser pública.
- **Escreva para o reviewer.** A mensagem é o resumo que o revisor lê antes do diff. Se a mudança é grande, o corpo precisa ser ainda mais generoso.
- **`--amend` só no que não foi publicado.** Reescrever mensagem de commit já enviado ao remoto é reescrever história compartilhada — em time, vira desculpa para conflito e confusão.
- **Mensagens em português ou inglês?** Uma língua só. Se o time escreve em português, tudo em português; se o repo é público/internacional, inglês. Misturar as duas é o único padrão errado.
- **Template do projeto** (time/projeto maior): `.git/COMMIT_EDITMSG` ou `commit.template` no git config força o formato — senior em time configura para o time não ter que lembrar.
- **Nunca omita contexto que só você sabe.** "corrige" sem dizer o quê é informação útil apenas para quem fez. Se você precisou de 10 minutos para entender o bug, o revisor vai precisar do mesmo — deixe a mensagem.

## Checklist antes de cada commit

A mensagem responde as três perguntas?

1. **O quê** — o assunto descreve a mudança de forma específica (não dá para confundir com outro commit)?
2. **Por quê** — existe corpo quando o porquê não é óbvio?
3. **Escopo** — o conteúdo do commit é uma única ideia coerente (e não três misturadas)?

Se a resposta a qualquer uma for "não", ainda não é hora de commitar.

---

**Frase-âncora:** *Código conta o quê; a mensagem conta o porquê — escreva-a para quem vai ler o log daqui a meses.*
**Nível:** Intermediário
**Revisão sugerida:** 30 dias