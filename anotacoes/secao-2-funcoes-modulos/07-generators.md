# Generators

## Generator Expression
```python
# (expressão for item in iterável)
gen = (n**2 for n in range(1000000))
soma = sum(gen)  # sem alocar lista na memória

# Comparação de tamanho
import sys
lista = [n for n in range(1000000)]
gen = (n for n in range(1000000))

sys.getsizeof(lista)  # ~8MB
sys.getsizeof(gen)    # ~200 bytes
```

## Generator Functions (yield)
```python
def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

for valor in contador(5):
    print(valor)  # 0, 1, 2, 3, 4
```

## yield from — delegação
```python
def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()  # executa gen1 primeiro
    yield 3

list(gen2())  # [1, 2, 3]
```

## Iterável vs Iterador
```python
# Iterável: tem __iter__() → retorna iterator
# Iterator: tem __iter__() + __next__() → levanta StopIteration
```
