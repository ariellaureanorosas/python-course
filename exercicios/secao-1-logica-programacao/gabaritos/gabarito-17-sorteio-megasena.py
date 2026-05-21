"""
Sorteio da Mega-Sena com random

Gera 6 números aleatórios únicos entre 1 e 60 simulando
um sorteio da Mega-Sena. Utiliza random.randint() e verifica
duplicatas com o operador in. Exibe os números ordenados.
"""

import random

QUANTIDADE_SORTEIO: int = 6
VALOR_MINIMO: int = 1
VALOR_MAXIMO: int = 60

numeros_sorteados: list = []

while len(numeros_sorteados) < QUANTIDADE_SORTEIO:
    numero_sorteado: int = random.randint(VALOR_MINIMO, VALOR_MAXIMO)
    if numero_sorteado not in numeros_sorteados:
        numeros_sorteados.append(numero_sorteado)

numeros_ordenados: list = sorted(numeros_sorteados)

numeros_formatados: list = []
for numero in numeros_ordenados:
    numeros_formatados.append(f"{numero:02d}")

print(f"Números sorteados: [{', '.join(numeros_formatados)}]")
