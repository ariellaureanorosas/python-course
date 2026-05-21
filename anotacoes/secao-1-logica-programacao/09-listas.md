# Listas

## Criação
```python
lista = [1, 2, 3]
vazia = []
mista = ["texto", 42, True]
```

## Métodos Principais (CRUD)
```python
lista.append(4)          # adiciona ao final (Create)
lista.insert(0, 0)       # adiciona em posição
item = lista[0]          # acessa (Read)
lista[0] = "novo"        # atualiza (Update)
lista.pop()              # remove do final (Delete)
lista.pop(0)             # remove do índice
del lista[0]             # deleta índice
lista.clear()            # limpa tudo
lista.extend([5, 6])     # adiciona múltiplos
lista + [7, 8]           # concatena (nova lista)
```

## Iterar Lista
```python
for item in lista:
    print(item)

for i in range(len(lista)):
    print(i, lista[i])
```

## Cuidado com Mutabilidade
```python
a = [1, 2, 3]
b = a           # b aponta para o MESMO objeto
b.append(4)     # altera a e b!
print(a)        # [1, 2, 3, 4]

# Para copiar de verdade:
c = a.copy()    # shallow copy
```
