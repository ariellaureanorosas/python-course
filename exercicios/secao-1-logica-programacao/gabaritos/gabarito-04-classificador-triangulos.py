"""
Classifica três medidas de lados em triângulo equilátero, isósceles
ou escaleno, após validar se formam um triângulo válido.
"""

try:
    lado_1: float = float(input('Primeiro lado: '))
    lado_2: float = float(input('Segundo lado: '))
    lado_3: float = float(input('Terceiro lado: '))
except ValueError:
    print('Erro: todos os lados devem ser números válidos.')
else:
    if lado_1 <= 0 or lado_2 <= 0 or lado_3 <= 0:
        print('Erro: os lados devem ser maiores que zero.')
    elif (
        lado_1 >= lado_2 + lado_3
        or lado_2 >= lado_1 + lado_3
        or lado_3 >= lado_1 + lado_2
    ):
        print('Erro: estas medidas não formam um triângulo.')
    elif lado_1 == lado_2 == lado_3:
        print('Triângulo equilátero.')
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print('Triângulo isósceles.')
    else:
        print('Triângulo escaleno.')
