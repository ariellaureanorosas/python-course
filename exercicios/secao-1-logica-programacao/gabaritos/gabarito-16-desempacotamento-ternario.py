"""
Gabarito EXERCÍCIO 16 - Desempacotamento com Ternário

Raciocínio sênior
-----------------
estrategia escolhida: ordenar com sorted() e desempacotar —
menor, meio, maior = numeros_ordenados. A própria ordem da lista
resolve a classificação: nenhuma comparação manual necessária.
A pergunta original ("maior, menor, meio") vira simplesmente
índices 0, 1, 2 da lista ordenada.
Alternativas descartadas: ternário encadeado (a>b and a>c etc.) —
funciona, mas 3 comparações manuais são mais fáceis de errar;
max()/min() — o enunciado proíbe.
"""

QUANTIDADE_NUMEROS: int = 3

numeros_digitados: list[int] = []

for posicao in range(1, QUANTIDADE_NUMEROS + 1):
    while True:
        try:
            valor_atual: int = int(input(f'Digite o {posicao}º número: '))
            break
        except ValueError:
            print('Erro: digite um número inteiro válido.')
    numeros_digitados.append(valor_atual)

numeros_ordenados: list[int] = sorted(numeros_digitados)
menor, meio, maior = numeros_ordenados

print(f'Menor: {menor}  |  Meio: {meio}  |  Maior: {maior}')

# Onde você provavelmente divergiu:
# - comparou "na mão" com ternários encadeados (a > b and a > c ...)
#   e errou um caso de borda; sorted + desempacotamento elimina
#   essas 3 comparações
# - usou max()/min() (o enunciado proíbe explicitamente)
# - digitou `list` sem tipo (aqui list[int])
# - não validou a entrada com while/break (um "abc" derrubava tudo)