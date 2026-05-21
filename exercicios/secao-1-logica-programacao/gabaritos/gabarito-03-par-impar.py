"""
Determina se um número inteiro digitado pelo usuário é par ou ímpar.
"""

try:
    numero: int = int(input('Digite um número: '))
except ValueError:
    print('Erro: digite um número inteiro válido.')
else:
    paridade: str = 'par' if numero % 2 == 0 else 'ímpar'
    print(f'{numero} é {paridade}.')
