# Loop `for` e `range()`

## `for` com string

```python
texto = "Python"
for letra in texto:
    print(letra)
```

## `range()`

```python
range(5)            # 0, 1, 2, 3, 4
range(2, 8)         # 2, 3, 4, 5, 6, 7
range(0, 10, 2)     # 0, 2, 4, 6, 8
range(10, 0, -1)    # 10, 9, 8, ... 1
```

## `continue` / `break` / `else`

```python
for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
else:
    print("Completo sem break")
```

## Iterável vs Iterador

```python
texto = "abc"
iterador = iter(texto)

next(iterador)  # 'a'
next(iterador)  # 'b'
next(iterador)  # 'c'
next(iterador)  # StopIteration
```

- **Iterável**: tem `__iter__()` → retorna iterator
- **Iterator**: tem `__iter__()` + `__next__()` → levanta `StopIteration`
