"""
GABARITO — EXERCÍCIO 17 — Sorteio da Mega-Sena com random

Sorteia 6 números únicos entre 1 e 60 usando random.randint(),
verifica duplicatas com o operador in e exibe ordenado com sorted().
"""

import random

sorteio: list = []
QUANTIDADE: int = 6
MINIMO: int = 1
MAXIMO: int = 60

while len(sorteio) < QUANTIDADE:
    numero: int = random.randint(MINIMO, MAXIMO)
    if numero not in sorteio:
        sorteio.append(numero)

sorteio_ordenado: list = sorted(sorteio)

print("Números sorteados:", end=" [")
for i, numero in enumerate(sorteio_ordenado):
    if i == len(sorteio_ordenado) - 1:
        print(f"{numero:02d}", end="")
    else:
        print(f"{numero:02d}", end=", ")
print("]")
