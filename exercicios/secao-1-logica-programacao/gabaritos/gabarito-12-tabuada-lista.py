"""
GABARITO — EXERCÍCIO 12 — Tabuada com Lista

Recebe um número, calcula a tabuada de 1 a 10, armazena em uma lista
e exibe o resultado formatado.
"""

numero: int = int(input("Digite um número para ver sua tabuada: "))

resultados: list = []

for i in range(1, 11):
    resultado: int = numero * i
    resultados.append(resultado)

print(f"\nTabuada do {numero}:")

for i, valor in enumerate(resultados, start=1):
    print(f"{numero} x {i} = {valor}")
