"""
EXERCÍCIO 11 — Contagem Regressiva com for

Tópicos: for, range(), passo negativo

Receba um número inteiro N do usuário.
Use um laço for com range() para fazer uma contagem regressiva de N até 0.
Exiba cada número na tela (um por linha).
Ao final da contagem, exiba a palavra "Fogo!".

Exemplo com N = 5:
    5
    4
    3
    2
    1
    0
    Fogo!

Dica: range(início, fim, passo) aceita passo negativo.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

try:
    N = int(input("Digite um número: "))
except ValueError:
    print("ERRO: Digite um Número")
else:
    for numero in range(N, -1, -1):
        print(numero)
    print("Fogo!")
