"""
Gabarito 04 — Classificador de Triângulos
"""

lado_1: float = float(input('Primeiro lado: '))
lado_2: float = float(input('Segundo lado: '))
lado_3: float = float(input('Terceiro lado: '))

if lado_1 <= 0 or lado_2 <= 0 or lado_3 <= 0:
    print('Os lados devem ser maiores que zero.')
elif (
    lado_1 >= lado_2 + lado_3
    or lado_2 >= lado_1 + lado_3
    or lado_3 >= lado_1 + lado_2
):
    print('Estes valores não formam um triângulo.')
elif lado_1 == lado_2 == lado_3:
    print('Triângulo equilátero.')
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print('Triângulo isósceles.')
else:
    print('Triângulo escaleno.')
