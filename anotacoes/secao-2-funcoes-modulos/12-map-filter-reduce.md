# Map, Filter, Reduce

Usado para transformar, filtrar e acumular dados em sequências de forma funcional.

## `map` — transformar cada elemento

```python
map(funcao, iteravel)  # retorna iterator

from functools import partial

def aumentar(preco, percentual):
    return preco * (1 + percentual / 100)

precos = [100, 200, 300]
aumento_10 = partial(aumentar, percentual=10)
list(map(aumento_10, precos))  # [110.0, 220.0, 330.0]
```

## `filter` — filtrar elementos

```python
filter(funcao_booleana, iteravel)  # retorna iterator

precos = [10, 60, 30, 80]
list(filter(lambda p: p > 50, precos))  # [60, 80]
```

## `reduce` — acumular em um valor

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])  # 10
reduce(lambda a, b: a + b, [1, 2, 3, 4], 0)  # 10 (com valor inicial)
```

## Exemplo Prático

```python
produtos = [
    {"nome": "Camisa", "preco": 50, "qtd": 10},
    {"nome": "Calça", "preco": 100, "qtd": 5},
]

list(map(lambda p: {**p, "preco": p["preco"] * 1.1}, produtos))
list(filter(lambda p: p["qtd"] > 0, produtos))
reduce(lambda acc, p: acc + p["preco"] * p["qtd"], produtos, 0)
```
