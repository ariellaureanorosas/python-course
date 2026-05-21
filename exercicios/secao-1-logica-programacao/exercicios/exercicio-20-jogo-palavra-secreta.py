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
import os

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
