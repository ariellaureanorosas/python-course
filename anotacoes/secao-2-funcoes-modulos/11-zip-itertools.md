# zip e itertools

## zip() — unir iteráveis
```python
nomes = ["Ana", "João", "Maria"]
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

list(zip(nomes, idades))
# [("Ana", 25), ("João", 30), ("Maria", 22)]
```

## zip_longest — unir com tamanhos diferentes
```python
from itertools import zip_longest

a = [1, 2, 3]
b = [1, 2]
list(zip_longest(a, b, fillvalue=0))
# [(1, 1), (2, 2), (3, 0)]
```

## itertools.count()
```python
from itertools import count
for i in count(start=0, step=2):
    if i > 10:
        break
    print(i)  # 0, 2, 4, 6, 8, 10
```

## combinations, permutations, product
```python
from itertools import combinations, permutations, product

list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

list(product([1, 2], [3, 4]))
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

## groupby — agrupar dados
```python
from itertools import groupby
alunos = [("A", 8), ("B", 7), ("A", 9), ("B", 6)]
alunos.sort(key=lambda a: a[0])  # precisa ordenar antes

for turma, grupo in groupby(alunos, key=lambda a: a[0]):
    print(turma, list(grupo))
```
