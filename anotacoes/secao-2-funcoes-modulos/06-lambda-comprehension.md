# Lambda, List/Dict/Set Comprehension

Usado para criar funções anônimas e construir coleções de forma concisa.

## Lambda

```python
# função anônima de uma linha
soma = lambda a, b: a + b
soma(2, 3)  # 5

# Uso com sort/sorted
pessoas = [("Ana", 30), ("João", 25)]
pessoas.sort(key=lambda p: p[1])          # ordena por idade
sorted(pessoas, key=lambda p: p[0])      # ordena por nome
```

## List Comprehension

```python
# [expressão for item in iterável if condição]
[n * 2 for n in range(10)]                    # [0,2,4,...18]
[n for n in range(20) if n % 2 == 0]          # pares
[n * 2 for n in range(10) if n > 5]           # condicional

# Aninhada
[(x, y) for x in range(3) for y in range(3)]
```

## Dict Comprehension

```python
{chave: valor for chave, valor in iteravel}
{n: n**2 for n in range(5)}                  # {0:0, 1:1, 2:4, ...}
{k: v for k, v in d.items() if isinstance(v, str)}
```

## Set Comprehension

```python
{n for n in [1, 1, 2, 2, 3]}  # {1, 2, 3}
```

## `isinstance()`

```python
isinstance(10, int)                  # True
isinstance("texto", str)             # True
isinstance(valor, (int, float))      # int ou float
```
