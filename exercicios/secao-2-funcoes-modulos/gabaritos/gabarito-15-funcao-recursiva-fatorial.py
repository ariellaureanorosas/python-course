"""
GABARITO 15 - Função Recursiva para Fatorial
"""

import sys


def fatorial(n: int) -> int:
    """Calcula o fatorial de forma recursiva.

    Args:
        n: Número inteiro não negativo.

    Returns:
        Fatorial de n.

    Raises:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError('Fatorial não definido para números negativos')
    if n <= 1:
        return 1
    return n * fatorial(n - 1)


def fatorial_iterativo(n: int) -> int:
    """Calcula o fatorial de forma iterativa.

    Args:
        n: Número inteiro não negativo.

    Returns:
        Fatorial de n.

    Raises:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError('Fatorial não definido para números negativos')
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def calcular_fatorial_com_limite(n: int, limite: int) -> int:
    """Calcula fatorial recursivo ajustando o recursion limit.

    Altera sys.setrecursionlimit para o valor informado, calcula o
    fatorial recursivamente e restaura o limite original ao final.

    Args:
        n: Número inteiro não negativo.
        limite: Novo limite de recursão.

    Returns:
        Fatorial de n.

    Raises:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError('Fatorial não definido para números negativos')

    limite_original = sys.getrecursionlimit()

    try:
        sys.setrecursionlimit(limite)
        return fatorial(n)
    finally:
        sys.setrecursionlimit(limite_original)
