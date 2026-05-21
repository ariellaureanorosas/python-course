# Input e Estruturas Condicionais

## `input()` — Entrada do Usuário

```python
nome = input("Digite seu nome: ")          # sempre retorna str
idade = int(input("Digite sua idade: "))   # converter para int
```

## `if` / `elif` / `else`

```python
if condicao:
    bloco
elif outra_condicao:
    bloco
else:
    bloco
```

## Operadores de Comparação

```python
>   # maior
>=  # maior ou igual
<   # menor
<=  # menor ou igual
==  # igual
!=  # diferente
```

## Exemplo

```python
a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
if a > b:
    print(f"{a} é maior")
elif a < b:
    print(f"{b} é maior")
else:
    print("Iguais")
```
