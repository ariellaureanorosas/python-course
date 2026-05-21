"""
Gabarito 08 — Calculadora de Tabuada com while
"""

try:
    numero: int = int(input('Digite um número: '))
except ValueError:
    print('Erro: digite um número inteiro válido.')
else:
    contador: int = 1
    while contador <= 10:
        print(f'{contador:>2} x {numero:>2} = {contador * numero:>3}')
        contador += 1
