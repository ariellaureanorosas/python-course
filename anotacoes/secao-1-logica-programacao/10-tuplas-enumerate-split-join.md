# Tuplas, enumerate, split/join

## Tuplas (imutáveis)
```python
tupla = (1, 2, 3)
tupla = 1, 2, 3         # sem parênteses
a, b, c = tupla          # desempacotamento
# tupla[0] = 0           # ERRO! tupla é imutável
```

## enumerate()
```python
lista = ["Ana", "João", "Maria"]
for indice, nome in enumerate(lista, start=1):
    print(indice, nome)
```

## split() — string → lista
```python
frase = "banana,maçã,uva"
lista = frase.split(",")  # ["banana", "maçã", "uva"]
```

## join() — lista → string
```python
palavras = ["Python", "é", "legal"]
frase = " ".join(palavras)  # "Python é legal"
frase = "-".join(palavras)  # "Python-é-legal"
```

## strip() — remove espaços extras
```python
"  texto  ".strip()   # "texto"
"  texto".lstrip()    # "texto"
"texto  ".rstrip()    # "texto"
```
