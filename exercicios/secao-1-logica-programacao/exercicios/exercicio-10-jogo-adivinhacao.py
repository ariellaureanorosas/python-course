"""
EXERCÍCIO 10 — Jogo de Adivinhação com Número Secreto

Tópicos: constantes, while, break, try/except, contadores

Crie um jogo onde o computador "pensa" em um número secreto (fixo,
definido como constante no código) e o usuário tenta adivinhar.

Regras:
  - Defina NUMERO_SECRETO como constante (ex.: 42).
  - O usuário tem quantas tentativas quiser (while infinito com
    break quando acertar).
  - A cada palpite, dê uma dica: "Maior!" ou "Menor!".
  - Conte quantas tentativas foram necessárias.
  - Valide com try/except se o palpite é um número inteiro.
  - Quando acertar, exiba:
      "Parabéns! Você acertou em X tentativa(s)."

Exemplo:
  Tente adivinhar o número secreto (1-100).
  Palpite: 50
  Menor!
  Palpite: 25
  Maior!
  Palpite: 37
  Maior!
  Palpite: 42
  Parabéns! Você acertou em 4 tentativa(s).

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

NUMERO_SECRETO = 10
LIMITE_MENOR = 0
LIMITE_MAIOR = 50
contador_tentativas = 0

print(f"Tente adivinha um número entre {LIMITE_MENOR} e {LIMITE_MAIOR}")
while True:
    try:
        palpite = int(input("Digite o Número: "))
    except ValueError:
        print("Digite o valor correto")
        continue

    if palpite == NUMERO_SECRETO:
        print(f"ACERTOU!!! Números de tentativas - {contador_tentativas}")
        break
    else:
        contador_tentativas += 1
        print(f"ERROU, Número da tentativa {contador_tentativas}")
        print("Maior!" if palpite < NUMERO_SECRETO else "Menor!")
