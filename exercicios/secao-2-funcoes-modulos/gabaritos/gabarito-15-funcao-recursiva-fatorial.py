import sys


def fatorial(
    n: int,
    /,
) -> int:
    """Retorna o fatorial de n usando recursao.

    Parametros:
        n: Numero inteiro nao negativo.

    Returns:
        Fatorial de n.

    Raises:
        ValueError: Se n for negativo.
        RecursionError: Se profundidade maxima de recursao for excedida.

    Exemplos:
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
    /,
) -> int:
    """Retorna o fatorial de n usando laco iterativo (sem recursao).

    Parametros:
        n: Numero inteiro nao negativo.

    Returns:
        Fatorial de n.

    Raises:
        ValueError: Se n for negativo.

    Exemplos:
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
    /,
) -> int:
    """Retorna fatorial recursivo ajustando temporariamente recursionlimit.

    O limite original de recursao e restaurado ao final, mesmo em caso de erro.

    Parametros:
        n: Numero inteiro nao negativo.
        limite: Novo limite de profundidade de recursao.

    Returns:
        Fatorial de n.

    Raises:
        ValueError: Se n for negativo.
        RecursionError: Se o limite for insuficiente para calcular.

    Exemplos:
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
