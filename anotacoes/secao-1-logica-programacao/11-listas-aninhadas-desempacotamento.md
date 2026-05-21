# Listas Aninhadas e Desempacotamento

## Listas de Listas (Matriz)
```python
salas = [
    ["Ana", "João"],
    ["Maria", "Pedro", "Paulo"],
    ["Lucas"],
]

salas[0][1]     # "João"
salas[1][2]     # "Paulo"

for sala in salas:
    for aluno in sala:
        print(aluno)
```

## Desempacotamento *
```python
# Em atribuição
primeiro, segundo, *resto = [1, 2, 3, 4, 5]
# primeiro=1, segundo=2, resto=[3,4,5]

_, nome, *_ = ["Sr.", "João", "Silva", "Jr."]
# nome = "João"

# Em chamadas de funções
print(*[1, 2, 3])  # 1 2 3
print(*"ABC")       # A B C
```
