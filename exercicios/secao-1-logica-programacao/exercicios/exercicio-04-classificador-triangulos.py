"""
Exercício 04 — Classificador de Triângulos

Receba 3 valores (lados de um triângulo) e determine se eles formam
um triângulo válido. Caso positivo, classifique-o em equilátero,
isósceles ou escaleno.

Regras para existência de um triângulo:
  - Cada lado deve ser menor que a soma dos outros dois (válido para
    todas as 3 combinações).
  - Nenhum lado pode ser zero ou negativo.

Classificação:
  - Equilátero: 3 lados iguais.
  - Isósceles: 2 lados iguais e 1 diferente.
  - Escaleno: 3 lados diferentes.

Dica: use if/elif/else encadeados.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
try:
    lado1: float = float(input("Digite um Número:"))
    lado2: float = float(input("Digite um Número:"))
    lado3: float = float(input("Digite um Número:"))
except ValueError:
    print("Digite números válidos")
else:
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print("Triângulo Inválido")
    elif lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
        print("Erro: as medidas não formam um triângulo")
    elif lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles")
    else:
        print("Triângulo Escaleno")
finally:
    print("-" * 10)
    print("Deus seja Louvado")
