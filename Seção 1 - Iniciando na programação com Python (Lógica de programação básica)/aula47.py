"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os
import random

lista_de_nomes = [
    "Lucas",
    "Mariana",
    "João",
    "Beatriz",
    "Rafael",
    "Camila",
    "Pedro",
    "Ana",
    "Gabriel",
    "Larissa",
    "Felipe",
    "Juliana",
    "Matheus",
    "Bianca",
    "Gustavo",
    "Renata",
    "Thiago",
    "Vanessa",
    "Bruno",
]

palavra_secreta = random.choice(lista_de_nomes).lower()
tentativas = 0
letras_acertadas = ""
quantidade_de_acertos = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_digitada) > 1:
        print("digite apenas uma letra")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    quantidade_de_acertos = 0
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
            quantidade_de_acertos += 1
        else:
            palavra_formada += "*"

    print(
        f"Palavra Formada: {palavra_formada} | quantidade de acertos: {quantidade_de_acertos}"
    )
    print("------------------------------------")

    if palavra_formada == palavra_secreta:
        while True:
            print(f"Você Acertou!, a palavra certa era: {palavra_secreta}".upper())
            print(f"numeros de tentativas: {tentativas}".upper())
            print("------------------------------------")
            opcao_saida = input("você deseja sair? [S] ou [N]: ").lower()
            if len(opcao_saida) > 1:
                print("Digite apenas um valor")
                continue
            elif opcao_saida not in ("s", "n"):
                print("Digite apenas [S] ou [N]")
                continue

            break

        if opcao_saida == "s":
            print("Saindo...")
            break
        os.system("cls" if os.name == "nt" else "clear")
        tentativas = 0
        letras_acertadas = ""
        palavra_secreta = random.choice(lista_de_nomes).lower
        quantidade_de_acertos = 0
