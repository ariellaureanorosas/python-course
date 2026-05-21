"""
Desempacotamento com Ternário e sorted()

Solicita três números inteiros, utiliza sorted() para ordená-los,
desempacota os valores ordenados e exibe menor, valor do meio e maior.
"""

QUANTIDADE_NUMEROS: int = 3

numeros_digitados: list = []

for posicao in range(1, QUANTIDADE_NUMEROS + 1):
    while True:
        try:
            valor_atual: int = int(input(f"Digite o {posicao}º número: "))
            break
        except ValueError:
            print("Erro: digite um número inteiro válido.")
    numeros_digitados.append(valor_atual)

numeros_ordenados: list = sorted(numeros_digitados)
menor, meio, maior = numeros_ordenados

print(f"Menor: {menor}  |  Meio: {meio}  |  Maior: {maior}")
