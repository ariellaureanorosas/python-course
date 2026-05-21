"""
Jogo da Palavra Secreta

Jogo interativo de adivinhação de palavras. O programa escolhe
aleatoriamente uma palavra de uma lista pré-definida, e o usuário
tenta acertar letra por letra. Utiliza random.choice() e laço while.
"""

import random
import os

PALAVRAS_DISPONIVEIS: list = [
    "python",
    "programacao",
    "computador",
    "algoritmo",
    "variavel",
    "estrutura",
]
SIMBOLO_OCULTO: str = "*"
COMANDO_SAIDA: str = "sair"

palavra_secreta: str = random.choice(PALAVRAS_DISPONIVEIS)
letras_reveladas: list = [SIMBOLO_OCULTO] * len(palavra_secreta)
quantidade_tentativas: int = 0
palavra_revelada: bool = False

os.system("clear")

print("=== JOGO DA PALAVRA SECRETA ===")
print(f"Digite '{COMANDO_SAIDA}' a qualquer momento para encerrar.\n")

while not palavra_revelada:
    print("Palavra:", " ".join(letras_reveladas))

    chute: str = input("Digite uma letra: ").strip().lower()

    if chute == COMANDO_SAIDA:
        print(f"\nVocê desistiu! A palavra era: {palavra_secreta}")
        break

    if len(chute) != 1:
        print("Digite apenas uma letra.\n")
        continue

    quantidade_tentativas += 1

    if chute in palavra_secreta:
        for indice, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_reveladas[indice] = chute
    else:
        print(f"A letra '{chute}' não está na palavra.")

    if SIMBOLO_OCULTO not in letras_reveladas:
        palavra_revelada = True
        os.system("clear")
        print("Palavra:", " ".join(letras_reveladas))
        print(f"\nParabéns! Você acertou a palavra '{palavra_secreta}'!")
        print(f"Total de tentativas: {quantidade_tentativas}")

    print()
