"""
Gabarito EXERCÍCIO 20 - Jogo da Palavra Secreta

Raciocínio sênior
-----------------
O estado do jogo é uma lista de letras (letras_reveladas) iniciada
como ["*"] * tamanho — o símbolo oculto é uma constante
(SIMBOLO_OCULTO) para o loop de vitória testar `in`. O chute é
normalizado (.strip().lower()) antes do if do "sair": um espaço ou
maiúscula extra não sai do jogo por acidente.
a limpeza de tela usa 'cls' (Windows) quando disponível — roda no
seu ambiente por padrão, mas o código aceita os dois.

Alternativas descartadas: substituir na string com replace() —
espalharia todas as letras no primeiro chute; acumular o chute
em um set() para revelar — conceito de set ainda não visto nessa
altura do curso.
"""

import os
import random

PALAVRAS_DISPONIVEIS: list[str] = [
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
letras_reveladas: list[str] = [SIMBOLO_OCULTO] * len(palavra_secreta)
quantidade_tentativas: int = 0
palavra_revelada: bool = False

os.system("cls")

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
        os.system("cls")
        print("Palavra:", " ".join(letras_reveladas))
        print(f"\nParabéns! Você acertou a palavra '{palavra_secreta}'!")
        print(f"Total de tentativas: {quantidade_tentativas}")

    print()

# Onde você provavelmente divergiu:
# - usou os.system("clear") (é do Linux/macOS; 'cls' é o do Windows —
#   o enunciado aceita os dois, mas este roda no seu ambiente)
# - tentou substituir '*' na string com replace ou f-string — revelaria
#   todas as ocorrências de uma vez; aqui a lista é o estado e *cada
#   letra do loop de revelação é testada uma vez
# - contou tentativa mesmo quando o jogador digita "sair" (aqui o
#   break vem antes do +1)
# - não normalizou o chute ('  A' não bate com a letra 'a' no check)
