"""
Exibe a tabuada de 1 a 10 para um número inteiro informado pelo usuário.
"""

INICIO_TABUADA: int = 1
FIM_TABUADA: int = 10

try:
    numero: int = int(input('Digite um número: '))
except ValueError:
    print('Erro: digite um número inteiro válido.')
else:
    contador: int = INICIO_TABUADA
    while contador <= FIM_TABUADA:
        print(f'{contador:>2} x {numero:>2} = {contador * numero:>3}')
        contador += 1
