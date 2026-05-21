"""
Tabuada com Lista

Solicita um número inteiro, calcula sua tabuada de 1 a 10,
armazena os resultados em uma lista e exibe no formato tradicional.
"""

INICIO_TABUADA: int = 1
FIM_TABUADA: int = 10

try:
    numero_tabuada: int = int(input("Digite um número para ver sua tabuada: "))
except ValueError:
    print("Erro: digite um número inteiro válido.")
else:
    resultados_tabuada: list = []

    for multiplicador in range(INICIO_TABUADA, FIM_TABUADA + 1):
        resultados_tabuada.append(numero_tabuada * multiplicador)

    print(f"\nTabuada do {numero_tabuada}:")

    for indice, resultado in enumerate(
        resultados_tabuada, start=INICIO_TABUADA
    ):
        print(f"{numero_tabuada} x {indice} = {resultado}")
