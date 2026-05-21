"""
Jogo de adivinhação onde o usuário tenta descobrir um número secreto
entre 1 e 100. A cada palpite são fornecidas dicas de maior ou menor.
"""

NUMERO_SECRETO: int = 42
LIMITE_INFERIOR: int = 1
LIMITE_SUPERIOR: int = 100

tentativas: int = 0

print(f'Tente adivinhar o número secreto ({LIMITE_INFERIOR}-{LIMITE_SUPERIOR}).')

while True:
    try:
        palpite: int = int(input('Palpite: '))
    except ValueError:
        print('Erro: digite um número inteiro válido.')
        continue

    tentativas += 1

    if palpite < NUMERO_SECRETO:
        print('Maior!')
    elif palpite > NUMERO_SECRETO:
        print('Menor!')
    else:
        print(f'Parabéns! Você acertou em {tentativas} tentativa(s).')
        break
