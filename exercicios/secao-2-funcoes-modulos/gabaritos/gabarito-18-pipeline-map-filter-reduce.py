from functools import reduce


def processar_numeros(
    numeros: list[int],
    /,
) -> int:
    """Retorna soma dos quadrados dos numeros pares (pipeline map/filter/reduce).

    Parametros:
        numeros: Lista de inteiros.

    Returns:
        Soma dos quadrados dos numeros pares.

    Exemplos:
    >>> processar_numeros([1, 2, 3, 4, 5])
    20
    >>> processar_numeros([])
    0
    >>> processar_numeros([1, 3, 5])
    0
    """
    return reduce(
        lambda acc, n: acc + n,
        map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numeros)),
        0,
    )


def processar_numeros_flexivel(
    numeros: list[int],
    /,
    *,
    pares: bool = True,
    expoente: int = 2,
) -> int:
    """Retorna soma dos numeros filtrados elevados ao expoente configurado.

    Parametros:
        numeros: Lista de inteiros.
        pares: True filtra pares, False filtra impares.
        expoente: Expoente para elevar cada numero.

    Returns:
        Soma calculada.

    Exemplos:
    >>> processar_numeros_flexivel([1, 2, 3, 4], pares=True, expoente=2)
    20
    >>> processar_numeros_flexivel([1, 2, 3, 4], pares=False, expoente=2)
    10
    >>> processar_numeros_flexivel([1, 2, 3], pares=True, expoente=3)
    8
    >>> processar_numeros_flexivel([], pares=True)
    0
    """
    if expoente < 0:
        raise ValueError('Expoente nao pode ser negativo')

    filtro: object = (lambda n: n % 2 == 0) if pares else (lambda n: n % 2 != 0)

    return reduce(
        lambda acc, n: acc + n,
        map(lambda n: n ** expoente, filter(filtro, numeros)),
        0,
    )


def processar_texto(
    palavras: list[str],
    /,
) -> list[str]:
    """Retorna lista com palavras de 3+ caracteres em maiusculas.

    Parametros:
        palavras: Lista de strings.

    Returns:
        Lista filtrada com strings em maiusculas.

    Exemplos:
    >>> processar_texto(['oi', 'mundo', 'a', 'Python'])
    ['MUNDO', 'PYTHON']
    >>> processar_texto(['a', 'bc', ''])
    []
    >>> processar_texto([])
    []
    """
    return list(map(
        str.upper,
        filter(lambda p: len(p) >= 3, palavras),
    ))


if __name__ == '__main__':
    print(processar_numeros([1, 2, 3, 4, 5]))
    print(processar_numeros_flexivel([1, 2, 3, 4], pares=False, expoente=3))
    print(processar_texto(['oi', 'mundo', 'a', 'Python']))
