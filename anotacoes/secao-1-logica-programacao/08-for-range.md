# Loop `for` e `range()`

## Quando você vai usar isso?
Você tem uma lista de clientes, as letras de um nome, ou precisa rodar algo exatamente N vezes. O `for` percorre cada elemento sem você gerenciar manualmente índices ou condições de parada.

## Modelo mental
É uma esteira: cada objeto passa na sua vez, você pega ele, faz algo, e o próximo vem automaticamente. `range()` é um atalho pra gerar números na esteira sem criar uma lista.

## Em uma linha
Percorra cada item de uma sequência automaticamente, do primeiro ao último.

## Na prática

### Caso simples — iterando string
```python
texto = "Python"

# ← `letra` recebe cada caractere, um por um, na ordem
for letra in texto:
    print(letra)       # ← P, y, t, h, o, n
# ← acabou a string, loop termina — sem contador, sem índice
```

### Com variação — range() e controle de fluxo
```python
# ← range(fim): 0 até fim-1 (5 = 0,1,2,3,4)
for i in range(5):
    print(i)

# ← range(início, fim): 2 até 7
for i in range(2, 8):
    print(i)

# ← range(início, fim, passo): 0,2,4,6,8
for i in range(0, 10, 2):
    print(i)

# ← passo negativo: 10,9,8...1
for i in range(10, 0, -1):
    print(i)

# ← continue: pula o 5, break: para no 8, else: só roda se NÃO deu break
for i in range(10):
    if i == 5:
        continue               # ← volta ao for sem printar 5
    if i == 8:
        break                  # ← sai do loop, else NÃO executa
    print(i)                   # ← 0,1,2,3,4,6,7
else:
    print("Completo sem break") # ← NÃO vai printar (break aconteceu)
```

### Em uso real — iterável vs iterador
```python
# ← Iterável: objeto que pode gerar um iterador (tem __iter__)
# ← Iterator: objeto que produz itens um por vez (tem __next__)

texto = "abc"           # ← string é ITERÁVEL (pode ser usada no for)

iterador = iter(texto)  # ← iter() PEGA o iterador da string

print(next(iterador))   # ← 'a' — next() puxa o próximo item
print(next(iterador))   # ← 'b'
print(next(iterador))   # ← 'c'
print(next(iterador))   # ← StopIteration! — acabou, iterador esgotado

# ← O for faz isso internamente:
# ← 1. chama iter(sequência) pra criar iterador
# ← 2. chama next() em loop até receber StopIteration
```

## O que NÃO fazer
```python
# ← NÃO modifique a lista enquanto itera sobre ela
lista = [1, 2, 3, 4]
for item in lista:
    if item == 2:
        lista.remove(item)   # ← bagunça os índices! Pula o 3

# ← range() não aceita float
for i in range(0, 1, 0.1):   # ← TypeError: 'float' object cannot be...
    print(i)

# ← esquecer que range(fim) termina em fim-1
for i in range(3):           # ← 0,1,2 — NÃO 3
    print(i)
```

## Por que Python funciona assim?
O `for` em Python é um **for-each**, não um for com índice. Ele funciona com o **protocolo de iteração**: qualquer objeto que implemente `__iter__()` (retorna um iterador) pode ser usado no `for`. O iterador implementa `__next__()` que retorna o próximo item ou levanta `StopIteration`. O `range()` é um objeto lazy — ele NÃO cria uma lista de todos os números, ele gera um por vez sob demanda. Isso economiza memória: `range(1000000)` ocupa o mesmo espaço que `range(10)`.

## Conexões
- Você já usou esse padrão quando: percorreu uma string com `for letra in "abc"`
- Aparece também em: `enumerate()`, `zip()`, `dict.items()`, leitura de arquivos (`for linha in arquivo`)
- Diferente de: `while` (precisa de condição manual, pode virar infinito); `for` em C (usa índice explícito)

---

## Teste de recuperação — responda sem olhar para cima

1. O que é um iterador e qual a diferença de um iterável?
2. Escreva um loop que imprime os números pares de 0 a 10 usando `range()`.
3. Qual a vantagem de `range()` sobre criar uma lista com `[0, 1, 2, ...]`?

---

**Frase-âncora:** "For each item in sequence: faça algo. Range gera números sob demanda."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
