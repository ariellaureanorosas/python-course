# Projetos da Seção 1

## Calculadora com Menu

```python
while True:
    n1 = input("Número 1: ")
    n2 = input("Número 2: ")
    operador = input("Operador (+-*/): ")

    if operador not in "+-*/":
        print("Operador inválido")
        continue

    # try/except para conversão
    # if/elif para operação
    # Perguntar se quer sair (S/N)
```

## Jogo da Palavra Secreta

```python
palavra_secreta = "python"
letras_acertadas = ""
tentativas = 0

while True:
    letra = input("Digite uma letra: ")
    tentativas += 1

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
```

## Lista de Compras

```python
lista = []
while True:
    opcao = input("[I]nserir [A]pagar [L]istar [S]air: ")

    if opcao == "i":
        lista.append(input("Item: "))
    elif opcao == "a":
        try:
            lista.pop(int(input("Índice: ")))
        except IndexError:
            print("Índice inválido")
    elif opcao == "l":
        for i, item in enumerate(lista):
            print(i, item)
    elif opcao == "s":
        break
```
