# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

lista1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
lista2 = ["BA", "SP", "MG", "RJ"]

print(list(zip(lista1, lista2)))
print()
print(list(zip_longest(lista1, lista2, fillvalue="Sem Cidade")))

# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [(lista1[indice], lista2[indice]) for indice in range(intervalo_maximo)]


# print(zipper(lista1, lista2))
