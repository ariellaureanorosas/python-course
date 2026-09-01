"""
EXERCÍCIO 20 — Jogo da Palavra Secreta

Baseado no jogo da aula 47. Implemente um jogo de adivinhar a palavra secreta.

Regras:
    - Crie uma lista com pelo menos 5 palavras secretas.
    - Use random.choice() para selecionar uma palavra da lista.
    - Exiba as letras acertadas e esconda as erradas com "*".
    - A cada tentativa, o jogador digita uma letra.
    - Se a letra estiver na palavra, revele sua posição(ões).
    - Conte quantas tentativas o jogador fez.
    - Se o jogador digitar "sair" (ou "Sair"), o jogo encerra.
    - Use os.system("clear") ou os.system("cls") para limpar a tela
      a cada iteração (deixe o jogo mais limpo visualmente).
    - Quando acertar a palavra inteira, exiba uma mensagem de parabéns
      e mostre quantas tentativas foram necessárias.

Dica: crie uma variável com "*" * len(palavra_secreta) para começar
      e vá substituindo as posições conforme o jogador acerta.
      Para substituir em uma string, converta para lista primeiro.
"""

import random

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
PALAVRAS: list[str] = ["python", "lista", "palavras", "exemplo", "Ariel"]
palavra_escolhida: str = random.choice(PALAVRAS)
tentativas = 0
letras_acertadas = ""

while True:
    entrada_letra: str = input("Digite apenas uma letra: ")
    tentativas += 1

    if len(entrada_letra) > 1:
        print("Digite apenas uma letra")
        continue

    if entrada_letra in palavra_escolhida:
        letras_acertadas += entrada_letra

    palavra_formada = ""
    quantidade_acertos = 0
    for letra in palavra_escolhida:
        if letra in letras_acertadas:
            palavra_formada += letra
            quantidade_acertos += 1
        else:
            palavra_formada += "*"
    print(
        f"Palavra Formada: {palavra_formada} | quantidade de acertos: {quantidade_acertos}"
    )
    print("------------------------------------")

    if palavra_formada == palavra_escolhida:
        print(f"Você Acertou!, a palavra certa era: {palavra_escolhida}".upper())
        print(f"numeros de tentativas: {tentativas}".upper())
        print("------------------------------------")
        break
