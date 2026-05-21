"""
GABARITO — EXERCÍCIO 20 — Jogo da Palavra Secreta

Jogo de adivinhar palavra secreta baseado na aula 47. Usa lista,
random.choice(), os.system() para limpar tela e laço while.
"""

import random
import os

palavras: list = [
    "python",
    "programacao",
    "computador",
    "algoritmo",
    "variavel",
    "estrutura",
]

palavra_secreta: str = random.choice(palavras)
letras_acertadas: list = ["*"] * len(palavra_secreta)
tentativas: int = 0
acertou: bool = False

os.system("clear")

print("=== JOGO DA PALAVRA SECRETA ===")
print("Digite 'sair' a qualquer momento para encerrar.\n")

while not acertou:
    print("Palavra: " + " ".join(letras_acertadas))

    chute: str = input("Digite uma letra: ").strip().lower()

    if chute == "sair":
        print(f"\nVocê desistiu! A palavra era: {palavra_secreta}")
        break

    if len(chute) != 1:
        print("Digite apenas uma letra.\n")
        continue

    tentativas += 1

    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_acertadas[i] = chute
    else:
        print(f"A letra '{chute}' não está na palavra.")

    if "*" not in letras_acertadas:
        acertou = True
        os.system("clear")
        print("Palavra: " + " ".join(letras_acertadas))
        print(f"\nParabéns! Você acertou a palavra '{palavra_secreta}'!")
        print(f"Tentativas: {tentativas}")

    print()
