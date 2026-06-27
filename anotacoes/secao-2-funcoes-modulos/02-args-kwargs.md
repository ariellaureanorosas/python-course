# `*args`, `**kwargs` e Higher Order Functions

Usado para criar funções flexíveis que aceitam quantidade variável de argumentos.

## `*args` — argumentos posicionais extras

```python
def soma(*args):
    return sum(args)

soma(1, 2, 3, 4)  # 10
```

## `**kwargs` — argumentos nomeados extras

```python
def mostrar(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar(nome="João", idade=30)
```

## Desempacotamento em Chamadas

```python
def soma(a, b, c):
    return a + b + c

lista = [1, 2, 3]
soma(*lista)  # desempacota lista como args

dados = {"a": 1, "b": 2, "c": 3}
soma(**dados)  # desempacota dict como kwargs
```

## Higher Order Functions

```python
def executar(funcao, *args):
    return funcao(*args)

executar(print, "Olá")    # imprime "Olá"
executar(sum, [1, 2, 3])  # 6
```
