"""
Gabarito EXERCÍCIO 12 - Tabuada com Lista

Raciocínio sênior
-----------------
O problema é separado em duas fases claras: 1) construir a lista
de resultados (for de 1 a 10 + append) e 2) exibir percorrendo a
lista com enumerate(..., start=1) — o índice da lista é o
multiplicador, sem variável de contagem extra.
A lista é tipada como list[int] desde o nascimento: documentação
viva do que ela contém.
Alternativas descartadas: exibir com uma única variável acumulada
sem lista — o enunciado exige a lista para treinar armazenamento;
imprimir dentro do loop de construção (mistura fases e impede
reuso dos resultados).
"""

INICIO_TABUADA: int = 1
FIM_TABUADA: int = 10

try:
    numero_tabuada: int = int(input('Digite um número para ver sua tabuada: '))
except ValueError:
    print('Erro: digite um número inteiro válido.')
else:
    resultados_tabuada: list[int] = []

    for multiplicador in range(INICIO_TABUADA, FIM_TABUADA + 1):
        resultados_tabuada.append(numero_tabuada * multiplicador)

    print(f'\nTabuada do {numero_tabuada}:')

    for indice, resultado in enumerate(resultados_tabuada, start=INICIO_TABUADA):
        print(f'{numero_tabuada} x {indice} = {resultado}')

# Onde você provavelmente divergiu:
# - digitou `list` sem o parâmetro de tipo (list[int] documenta o
#   conteúdo; com type checker, `list` é um convite a bugs)
# - imprimiu dentro do for de construção (a exibição virou parte da
#   fase de cálculo — aqui as fases são separadas)
# - usou uma variável extra para o multiplicador em vez de
#   enumerate(..., start=1)
# - ficou tentado a usar while (o enunciado pede for)