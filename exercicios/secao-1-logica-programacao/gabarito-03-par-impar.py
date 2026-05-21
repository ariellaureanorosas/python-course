"""
Gabarito 03 — Par ou Ímpar com Validação
"""

try:
    numero: int = int(input('Digite um número: '))
except ValueError:
    print('Erro: digite um número inteiro válido.')
else:
    if numero % 2 == 0:
        print(f'{numero} é par.')
    else:
        print(f'{numero} é ímpar.')
