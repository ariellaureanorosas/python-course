"""
Gabarito EXERCÍCIO 15 - Função Recursiva para Fatorial

Raciocínio sênior
-----------------
O caso-base (n <= 1 → 1) é a porta de saída da recursão; sem ele, a
função não termina nunca. O caso recursivo (n * fatorial(n - 1))
reduz o problema em 1 a cada volta — dois pontos que todo sênior
verifica em qualquer recursão escrita.
calcular_fatorial_com_limite usa try/finally para RESTAURAR o
recursion limit original aconteça o que acontecer: se um erro
ocorre no meio, o finally garante que o programa volta ao estado
inicial — padrão de segurança de recurso global.
Alternativas descartadas: memoização (desnecessária aqui), lambda
recursivo (precisa truques Y-combinator; ilegível sem ganho).
"""

import sys


def fatorial(
    n: int,
) -> int:
    """Retorna o fatorial de n usando recursao.

    Parametros
    ----------
    n : int
        Numero inteiro nao negativo.

    Returns
    -------
    int
        Fatorial de n.

    Raises
    ------
    ValueError
        Se n for negativo.
    RecursionError
        Se profundidade maxima de recursao for excedida.

    Exemplos
    --------
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(5)
    120
    >>> fatorial(10)
    3628800
    """
    if n < 0:
        raise ValueError('Fatorial nao definido para numeros negativos')
    if n <= 1:
        return 1
    return n * fatorial(n - 1)


def fatorial_iterativo(
    n: int,
) -> int:
    """Retorna o fatorial de n usando laco iterativo (sem recursao).

    Parametros
    ----------
    n : int
        Numero inteiro nao negativo.

    Returns
    -------
    int
        Fatorial de n.

    Raises
    ------
    ValueError
        Se n for negativo.

    Exemplos
    --------
    >>> fatorial_iterativo(0)
    1
    >>> fatorial_iterativo(5)
    120
    >>> fatorial_iterativo(10)
    3628800
    """
    if n < 0:
        raise ValueError('Fatorial nao definido para numeros negativos')
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def calcular_fatorial_com_limite(
    n: int,
    limite: int,
) -> int:
    """Retorna fatorial recursivo ajustando temporariamente recursao.

    O limite original de recursao e restaurado ao final, mesmo em
    caso de erro (try/finally).

    Parametros
    ----------
    n : int
        Numero inteiro nao negativo.
    limite : int
        Novo limite de profundidade de recursao.

    Returns
    -------
    int
        Fatorial de n.

    Raises
    ------
    ValueError
        Se n for negativo.
    RecursionError
        Se o limite for insuficiente para calcular.

    Exemplos
    --------
    >>> calcular_fatorial_com_limite(5, 100)
    120
    >>> calcular_fatorial_com_limite(0, 100)
    1
    """
    if n < 0:
        raise ValueError('Fatorial nao definido para numeros negativos')

    limite_original = sys.getrecursionlimit()
    try:
        sys.setrecursionlimit(limite)
        return fatorial(n)
    finally:
        sys.setrecursionlimit(limite_original)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - esqueceu o caso-base (fatorial(0) = 1) — a recursão entrava em
#   loop infinito para 0
# - não restaurou o recursion limit no finally (alterava o limite
#   global do processo permanentemente e, em um programa maior,
#   quebrava outras partes)
# - errou o caso-base: fatorial(0) == 1, não 0
# - validou negativo somente no iterativo (aqui os dois validam
#   antes de calcular)