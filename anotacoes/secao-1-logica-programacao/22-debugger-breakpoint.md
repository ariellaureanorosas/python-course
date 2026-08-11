# Debugger e breakpoint (depuração)

## Quando você vai usar isso?
Quando o código "funciona" mas o resultado não é o esperado — e você não sabe em qual linha os valores começam a divergir do seu raciocínio. O debugger (aula 18) pausa a execução em linhas escolhidas para você inspecionar as variáveis ali na hora; `breakpoint()` (aula 25) faz o mesmo sem depender do editor, abrindo o depurador `pdb` no terminal.

## Modelo mental
É assistir à execução em câmera lenta com medidor de pressão: você marca onde quer congelar o filme (breakpoint), congela (pausa), olha o painel de variáveis (painel/watch), avança para a próxima cena (step) ou deixa rodar até o próximo congelamento (continue). O `print()` é o bilhete pregado na parede do set; o debugger é a tela do diretor.

## Em uma linha
Breakpoint pausa a execução num ponto escolhido; dali você inspeciona variáveis, percorre a execução passo a passo e reinicia sem re-editar nada.

## Na prática

### Caso simples — pausar com o debugger do VS Code (aula 18)

```python
a = 1
b = 2
c = a + b          # ← breakpoint aqui (F9): veja a, b e c no painel
print(c)
```

Ao pausar, use os controles na barra de depuração:
- <kbd>F10</kbd> step over — executa a linha e para na próxima (entra SEM detalhar funções)
- <kbd>F11</kbd> step into — entra DENTRO da função chamada
- <kbd>Shift</kbd>+<kbd>F11</kbd> step out — termina a função atual e volta ao chamador
- <kbd>F5</kbd> continue — roda até o próximo breakpoint
- Painel WATCH: digite qualquer expressão (ex.: `b * 2`) e veja o valor mudar a cada passo

### Com variação — breakpoint() e pdb no terminal (aula 25)

```python
a = 1
b = 2
breakpoint()       # ← pausa aqui e abre o (Pdb) no terminal
print(a + b)
```

No prompt `(Pdb)`:
```text
(Pdb) p a          # print a      → 1
(Pdb) p b          # print b      → 2
(Pdb) n            # next: executa a linha atual e para na próxima
(Pdb) s            # step: entra na função da linha atual
(Pdb) c            # continue: roda até o próximo breakpoint
(Pdb) q            # quit: encerra a execução
```

### Em uso real — suspeitando de uma função

```python
def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto

preco = 100
percentual = 10
breakpoint()                      # ← inspecione preco e percentual aqui
total = calcular_desconto(preco, percentual)
print(total)                      # ← se o total vier errado, F11 dentro de calcular_desconto
```

## O que NÃO fazer

```python
# ← ERRADO: "print-debug" abandonado solto no código
print(desconto)      # ← ficou no código depois do bug resolvido
print(percentual)
# ← o certo: debugger/breakpoint para depurar, depois REMOVA os prints

# ← ERRADO: breakpoint() commitado na entrega
breakpoint()         # ← em produção isso pausa o servidor esperando input!
# ← o certo: só em desenvolvimento; apague antes de entregar

# ← ERRADO: depurar chutando — adicionar print aleatório e rodar de novo
# ← o certo: parar NO ponto onde o valor diverge e olhar as variáveis reais
```

## Por que Python funciona assim?
A execução não é um "script que roda de uma vez": o interpretador avalia expressão por expressão, e o depurador usa isso a seu favor — pausar é "espiar entre uma expressão e a próxima". O `breakpoint()` chama `sys.breakpointhook()`, que por padrão abre o `pdb` com os frame (o "andar" atual da pilha de chamadas) já carregado: `p` consulta variáveis, `n/s` escolhem o próximo passo, tudo sem recompilar. Quando a função não para no lugar certo, é sinal de que o breakpoint está ANTES (execução nunca chegou lá) ou o loop/pula a linha — o debugger mostra isso imediatamente.

## Conexões
- Você já usou esse padrão quando: reusou um print para "ver" um valor — o breakpoint faz isso sem sujar o código
- Aparece também em: tratamento de erros (try/except, nota 08 da seção 2) — o except captura DEPOIS, o debugger olha o momento exato do problema
- Diferente de: `assert` (valida premissas no código e quebra se falsas), testes automatizados (verificam o resultado final), `print()` (registro bruto, sem pausa e sem introspecção)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre step over e step into?
2. O que `breakpoint()` faz no terminal e quais os comandos `p`, `n`, `c` e `q` significam?
3. Por que `breakpoint()` não deve ficar no código entregue em produção?

---

**Frase-âncora:** "O interpretador executa; o depurador mostra o que ele executa de verdade — e print-debug só enche o código de entulho."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14