"""
EXERCÍCIO 12 — Tabuada com Lista

Tópicos: for, range(), listas, append()

Receba um número inteiro do usuário.
Use um laço for de 1 a 10 para calcular a tabuada desse número.
Armazene cada resultado em uma lista.
Ao final, exiba a lista formatada no estilo:

    Tabuada do 7:
    7 x 1 = 7
    7 x 2 = 14
    ...
    7 x 10 = 70

Requisitos:
    - Use uma lista para guardar os resultados.
    - Use for com range().
    - Exiba a tabuada percorrendo a lista com outro for.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
TABUADA = 10
while True:
    try:
        numero = int(input("Digite um número para ver sua tabuada: "))
    except ValueError:
        print("ERRO: Digite um número corretamente")
    else:
        resultados_tabuada: list[int] = []
        for multiplicador in range(0, TABUADA + 1):
            resultados_tabuada.append(numero * multiplicador)
        for indice, valor in enumerate(resultados_tabuada):
            print(f"{numero} x {indice} = {valor}")
        break
