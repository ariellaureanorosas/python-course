"""
Gabarito EXERCÍCIO 11 - Contagem Regressiva com for

Raciocínio sênior
-----------------
O range(numero_limite, VALOR_FINAL - 1, PASSO_REGRESSIVO) expressa
"de N até 0 incluindo o 0": o stop é exclusivo, então é VALOR_FINAL - 1
(= -1). Passo negativo é a alma do exercício — e a constante
PASSO_REGRESSIVO deixa a intenção documentada no nome.
A validação da entrada isolada no try/except evita propagar erro
de digitação para o laço.

Alternativas descartadas: range(numero_limite, -1, -1) — funciona,
mas o "número mágico" -1 não explica a si mesmo como
VALOR_FINAL - 1 = -1.
"""

VALOR_FINAL: int = 0
PASSO_REGRESSIVO: int = -1

try:
    numero_limite: int = int(input('Digite um número para contagem regressiva: '))
except ValueError:
    print('Erro: digite um número inteiro válido.')
else:
    for contador in range(numero_limite, VALOR_FINAL - 1, PASSO_REGRESSIVO):
        print(contador)

    print('Fogo!')

# Onde você provavelmente divergiu:
# - escreveu range(n, -1, -1) direto — funciona, mas VALOR_FINAL - 1
#   explica a si mesmo ("até o 0 inclusive") enquanto -1 é cifra
# - usou range(n, 0, -1) e perdeu o 0 na saída
# - não tratou ValueError na entrada (o enunciado pede validação)
# - imprimiu o "Fogo!" dentro do laço (sairia N vezes)