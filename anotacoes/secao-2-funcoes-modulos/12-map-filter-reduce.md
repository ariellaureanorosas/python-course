# Map, Filter, Reduce

## Quando você vai usar isso?
Você tem uma lista de preços e precisa aplicar 10% de aumento em todos. Depois, filtrar só os acima de R$ 50. Por fim, somar o valor total do estoque. Em vez de `for` com `append` três vezes, você encadeia transformação, filtro e acumulação em uma linha funcional.

## Modelo mental
Uma esteira de fábrica: `map` aplica uma máquina em cada peça, `filter` desvia as que passam no controle de qualidade, `reduce` empilha tudo em uma caça só. Nenhuma peça toca no chão — tudo flui.

## Em uma linha
Transforme, filtre e acumule iteráveis sem loops explícitos, com funções puras e sem efeito colateral.

## Na prática

### Caso simples

```python
precos = [100, 200, 300]

def aumentar(preco, percentual):                  # ← função pura: entra preço, sai preço
    return preco * (1 + percentual / 100)

list(map(lambda p: p * 1.1, precos))              # ← [110.0, 220.0, 330.0]
```

### Com variação

```python
from functools import partial, reduce

def aumentar(preco, percentual):
    return preco * (1 + percentual / 100)

aumento_10 = partial(aumentar, percentual=10)     # ← fixa o 2º argumento
precos = [100, 200, 300]
list(map(aumento_10, precos))                     # ← [110.0, 220.0, 330.0]

precos = [10, 60, 30, 80]
list(filter(lambda p: p > 50, precos))            # ← [60, 80]

reduce(lambda a, b: a + b, [1, 2, 3, 4])          # ← (((1+2)+3)+4) = 10
reduce(lambda a, b: a + b, [1, 2, 3, 4], 0)       # ← com valor inicial = 0+1+2+3+4 = 10
```

### Em uso real

```python
produtos = [
    {"nome": "Camisa", "preco": 50, "qtd": 10},
    {"nome": "Calça", "preco": 100, "qtd": 5},
]

list(map(lambda p: {**p, "preco": p["preco"] * 1.1}, produtos))  # ← aplica 10% em cada

list(filter(lambda p: p["qtd"] > 0, produtos))                   # ← só itens em estoque

reduce(lambda acc, p: acc + p["preco"] * p["qtd"], produtos, 0)  # ← valor total do estoque
# 50*10 + 100*5 = 1000
```

## O que NÃO fazer

```python
precos = [100, 200, 300]
resultado = map(lambda p: p * 1.1, precos)
print(resultado)                                  # ← <map object at 0x...> — não é a lista!
# ← map retorna iterador, não lista. Esquecer list() é o erro mais comum.

# Outro erro:
reduced = reduce(lambda a, b: a + b, [])          # ← ERRO: empty sequence, sem valor inicial
# ← reduce sem initializer quebra em sequência vazia.
```

## Por que Python funciona assim?
`map` e `filter` são **lazy**: retornam iteradores que só calculam quando consumidos (`list()`, `for`). Isso economiza memória em coleções grandes. `reduce` vem do `functools` (não é built-in) porque Guido achava que `reduce` era menos legível que loops, mas útil para acumulações. Diferente de `map`/`filter`, `reduce` **consome** o iterável inteiro e devolve um valor único.

## Conexões
- Você já usou esse padrão quando: fez `[x*2 for x in lista]` — compreensão de lista é syntactic sugar para `map` + `filter`
- Aparece também em: processamento de dados com pandas (`df.apply()` é `map`), pipelines de streaming
- Diferente de: `map` transforma 1 pra 1; `filter` seleciona subconjunto; `reduce` colapsa em 1

---

## Teste de recuperação — responda sem olhar para cima

1. O que `map` retorna? E por que isso importa para memória?
2. Dada `lista = [1, 2, 3, 4, 5]`, escreva uma linha que retorne a soma dos números pares dobrados.
3. Qual a diferença entre `map` e `reduce`?

---

**Frase-âncora:** "Pipeline de dados: transforma, filtra, acumula sem loops."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
