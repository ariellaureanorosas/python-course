"""
Gabarito EXERCÍCIO 17 - Sorteio da Mega-Sena com random

Raciocínio sênior
-----------------
A unicidade dos números é garantida com um while que só avança
quando o número sorteado não está na lista — um "guarda" na
entrada em vez de filtrar (remove) depois. Duas fases: sortear
(única responsabilidade) e exibir (formatar com :02d e join).
Alternativas descartadas: sorteio com random.sample(range(1, 61), 6)
— resolve em uma linha mas não exercita o while + operador in
pedido no enunciado; set para unicidade — idem, mascara o conceito.
"""

import random

QUANTIDADE_SORTEIO: int = 6
VALOR_MINIMO: int = 1
VALOR_MAXIMO: int = 60

numeros_sorteados: list[int] = []

while len(numeros_sorteados) < QUANTIDADE_SORTEIO:
    numero_sorteado: int = random.randint(VALOR_MINIMO, VALOR_MAXIMO)
    if numero_sorteado not in numeros_sorteados:
        numeros_sorteados.append(numero_sorteado)

numeros_ordenados: list[int] = sorted(numeros_sorteados)

numeros_formatados: list[str] = []
for numero in numeros_ordenados:
    numeros_formatados.append(f"{numero:02d}")

print(f"Números sorteados: [{', '.join(numeros_formatados)}]")

# Onde você provavelmente divergiu:
# - usou random.sample() ou set() — resolve a unicidade em uma linha,
#   mas o enunciado pede o while + operador in exercitados
# - digitou `list` sem tipo em alguma das listas (aqui todas têm)
# - esqueceu o :02d no f-string (05 em vez de 5 quando o número é
#   menor que 10)
# - imprimiu a lista crua ([5, 12, ...]) sem o formato do exemplo
