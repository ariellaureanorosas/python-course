"""
EXERCÍCIO 15 - Função Recursiva para Fatorial

Tópicos: Funções recursivas, recursion limit, sys.setrecursionlimit
Aula: 117

Crie as funções abaixo.

1. Função `fatorial(n: int) -> int`
   - Retorna o fatorial de n recursivamente
   - n! = n * (n-1)! para n > 1
   - n! = 1 para n <= 1
   - Se n for negativo, levanta ValueError com mensagem "Fatorial não definido para números negativos"

2. Função `fatorial_iterativo(n: int) -> int`
   - Retorna o fatorial de n de forma iterativa (sem recursão)
   - Trata n negativo com ValueError

3. Função `calcular_fatorial_com_limite(n: int, limite: int) -> int`
   - Ajusta o recursion limit com sys.setrecursionlimit(limite)
   - Calcula o fatorial recursivamente
   - Restaura o recursion limit original ao final (use try/finally)
   - Se n for negativo, levanta ValueError

Dica: import sys e guarde o limite original antes de alterar.
"""

import sys


def fatorial(n: int) -> int:
    ...


def fatorial_iterativo(n: int) -> int:
    ...


def calcular_fatorial_com_limite(n: int, limite: int) -> int:
    ...
