"""
GABARITO — EXERCÍCIO 11 — Contagem Regressiva com for

Recebe um número inteiro N e exibe contagem regressiva de N até 0,
seguida da palavra "Fogo!".
"""

N: int = int(input("Digite um número: "))

for i in range(N, -1, -1):
    print(i)

print("Fogo!")
