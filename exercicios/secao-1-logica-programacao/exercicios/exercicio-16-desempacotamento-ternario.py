"""
EXERCÍCIO 16 — Desempacotamento com Ternário

Tópicos: input(), int, listas, sorted(), desempacotamento, ternário

Receba 3 números inteiros do usuário.
Use desempacotamento para extrair o maior, o menor e o valor do meio.

Exemplo:
    Números: 8, 3, 5
    Menor: 3, Meio: 5, Maior: 8

Restrição: resolva SEM usar as funções max() e min().

Dica: você pode colocar os números em uma lista, ordenar com sorted()
      e desempacotar o resultado em três variáveis — ou fazer as
      comparações com operação ternária. Escolha o caminho que
      fizer mais sentido para você.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
lista: list[int] = []
try:
    n1 = int(input("Digite o 1º número: "))
    n2 = int(input("Digite o 2º número: "))
    n3 = int(input("Digite o 3º número: "))
except ValueError:
    print("ERRO: Digite os valores corretamente")
else:
    lista.extend([n1, n2, n3])
    ordenados: list[int] = sorted(lista)
    print(f"Menor: {ordenados[0]}, Meio: {ordenados[1]}, Maior: {ordenados[2]}")
