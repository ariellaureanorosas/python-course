"""
GABARITO — EXERCÍCIO 16 — Desempacotamento com Ternário

Recebe 3 números e usa sorted(), desempacotamento e operação ternária
para determinar menor, meio e maior.
"""

n1: int = int(input("Digite o 1º número: "))
n2: int = int(input("Digite o 2º número: "))
n3: int = int(input("Digite o 3º número: "))

numeros_ordenados: list = sorted([n1, n2, n3])

menor, meio, maior = numeros_ordenados

print(f"Menor: {menor}, Meio: {meio}, Maior: {maior}")
