# Tuplas, Enumerate, Split/Join

Usado para dados imutáveis, iteração com índice e manipulação de strings.

## Tuplas (imutáveis)

```python
tupla = (1, 2, 3)
tupla = 1, 2, 3          # sem parênteses
a, b, c = tupla           # desempacotamento
# tupla[0] = 0            # ERRO! tupla é imutável
```

## `enumerate()`

```python
lista = ["Ana", "João", "Maria"]
for indice, nome in enumerate(lista, start=1):
    print(indice, nome)
```

## `split()` — string → lista

```python
frase = "banana,maçã,uva"
lista = frase.split(",")  # ["banana", "maçã", "uva"]
```

## `join()` — lista → string

```python
palavras = ["Python", "é", "legal"]
" ".join(palavras)   # "Python é legal"
"-".join(palavras)   # "Python-é-legal"
```

## `strip()` — remove espaços

```python
"  texto  ".strip()    # "texto"
"  texto".lstrip()     # "texto"
"texto  ".rstrip()     # "texto"
```
