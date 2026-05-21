"""
GABARITO 18 - Combinar map/filter/reduce em Pipeline
"""

from functools import reduce


def processar_numeros(numeros: list[int]) -> int:
    """Processa números em pipeline: filtra pares -> eleva ao quadrado -> soma.

    Args:
        numeros: Lista de inteiros.

    Returns:
        Soma dos quadrados dos números pares.
    """
    pares = filter(lambda n: n % 2 == 0, numeros)
    quadrados = map(lambda n: n ** 2, pares)
    return reduce(lambda acc, n: acc + n, quadrados, 0)


def processar_numeros_flexivel(
    numeros: list[int],
    *,
    pares: bool = True,
    expoente: int = 2,
) -> int:
    """Processa números com filtro configurável e expoente.

    Args:
        numeros: Lista de inteiros.
        pares: Se True filtra pares, se False filtra ímpares.
        expoente: Expoente para elevar cada número.

    Returns:
        Soma dos números filtrados elevados ao expoente.
    """
    filtro = (lambda n: n % 2 == 0) if pares else (lambda n: n % 2 != 0)
    return reduce(
        lambda acc, n: acc + n,
        map(lambda n: n ** expoente, filter(filtro, numeros)),
        0,
    )


def processar_texto(palavras: list[str]) -> list[str]:
    """Filtra palavras curtas e converte para maiúsculas.

    Args:
        palavras: Lista de strings.

    Returns:
        Lista com palavras de 3+ caracteres em maiúsculas.
    """
    return list(map(
        str.upper,
        filter(lambda p: len(p) >= 3, palavras),
    ))
