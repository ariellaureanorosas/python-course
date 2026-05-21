# Map, Filter, Reduce

## map — transformar cada elemento
```python
map(funcao, iteravel)  # retorna iterator

# Exemplo: aumentar preços
from functools import partial

def aumentar(preco, percentual):
    return preco * (1 + percentual / 100)

precos = [100, 200, 300]
aumento_10 = partial(aumentar, percentual=10)
list(map(aumento_10, precos))  # [110.0, 220.0, 330.0]
```

## filter — filtrar elementos
```python
filter(funcao_booleana, iteravel)  # retorna iterator

def maior_que_50(preco):
    return preco > 50

precos = [10, 60, 30, 80]
list(filter(maior_que_50, precos))  # [60, 80]
```

## reduce — acumular em um valor
```python
from functools import reduce

def somar(a, b):
    return a + b

reduce(somar, [1, 2, 3, 4])  # 10

# Com valor inicial
reduce(somar, [1, 2, 3, 4], 0)  # 10
```

## Exemplo Prático
```python
produtos = [
    {"nome": "Camisa", "preco": 50, "qtd": 10},
    {"nome": "Calça", "preco": 100, "qtd": 5},
]

# Aumentar preço em 10%
list(map(lambda p: {**p, "preco": p["preco"] * 1.1}, produtos))

# Filtrar com estoque
list(filter(lambda p: p["qtd"] > 0, produtos))

# Total do estoque
reduce(lambda acc, p: acc + p["preco"] * p["qtd"], produtos, 0)
```
