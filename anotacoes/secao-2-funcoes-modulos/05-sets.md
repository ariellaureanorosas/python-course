# Sets (Conjuntos)

## Criação

```python
s = {1, 2, 3}
vazio = set()  # {} é dict vazio
```

## Características

- Remove duplicatas automaticamente
- Não tem índices
- Não garante ordem
- Aceita apenas tipos imutáveis (`int`, `str`, `tuple`, etc.)

## Métodos

```python
s.add(4)            # adiciona
s.update([5, 6])    # adiciona múltiplos
s.discard(1)        # remove (sem erro se não existir)
s.clear()           # limpa
```

## Operadores de Conjunto

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b   # união: {1, 2, 3, 4}
a & b   # interseção: {2, 3}
a - b   # diferença: {1}
a ^ b   # diferença simétrica: {1, 4}
```

## Exemplo: primeiro duplicado

```python
def primeiro_duplicado(lista):
    vistos = set()
    for item in lista:
        if item in vistos:
            return item
        vistos.add(item)
    return None
```
