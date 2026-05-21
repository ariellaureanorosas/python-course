# Projetos da Seção 1

## 1. Calculadora com Menu (aula 40)
```python
while True:
    n1 = input("Número 1: ")
    n2 = input("Número 2: ")
    operador = input("Operador (+-*/): ")
    
    if operador not in "+-*/":
        print("Operador inválido")
        continue
    
    # Converter com try/except
    # Executar operação com if/elif
    # Perguntar se quer sair (S/N)
```

## 2. Jogo da Palavra Secreta (aula 47)
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

## 3. Lista de Compras (aula 56)
```python
lista = []
while True:
    opcao = input("[I]nserir [A]pagar [L]istar [S]air: ")
    
    if opcao == "i":
        valor = input("Item: ")
        lista.append(valor)
    elif opcao == "a":
        indice = int(input("Índice: "))
        try:
            lista.pop(indice)
        except IndexError:
            print("Índice inválido")
    elif opcao == "l":
        for i, item in enumerate(lista):
            print(i, item)
    elif opcao == "s":
        break
```
