"""
Gabarito 10 — Jogo de Adivinhação com Número Secreto
"""

NUMERO_SECRETO: int = 42
tentativas: int = 0

print('Tente adivinhar o número secreto (1-100).')

while True:
    try:
        palpite: int = int(input('Palpite: '))
    except ValueError:
        print('Digite um número inteiro válido.')
        continue

    tentativas += 1

    if palpite < NUMERO_SECRETO:
        print('Maior!')
    elif palpite > NUMERO_SECRETO:
        print('Menor!')
    else:
        print(f'Parabéns! Você acertou em {tentativas} tentativa(s).')
        break
