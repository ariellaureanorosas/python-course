"""
Contagem Regressiva com for

Solicita um número inteiro N ao usuário e exibe uma contagem
regressiva de N até 0, finalizando com a palavra "Fogo!".
"""

VALOR_FINAL: int = 0
PASSO_REGRESSIVO: int = -1

try:
    numero_limite: int = int(input("Digite um número para contagem regressiva: "))
except ValueError:
    print("Erro: digite um número inteiro válido.")
else:
    for contador in range(numero_limite, VALOR_FINAL - 1, PASSO_REGRESSIVO):
        print(contador)

    print("Fogo!")
