from functools import partial


def aumentar(
    preco: float,
    percentual: float,
) -> float:
    """Aplica percentual de aumento sobre o preco e retorna novo valor.

    Parametros:
        preco: Valor original.
        percentual: Percentual de aumento (ex: 10 para 10%%).

    Returns:
        Preco com aumento.

    Exemplos:
    >>> aumentar(100.0, 10.0)
    110.0
    >>> aumentar(50.0, 50.0)
    75.0
    """
    return round(preco * (1 + percentual / 100), 2)


def aplicar_aumento(
    precos: list[float],
    percentual: float,
    /,
) -> list[float]:
    """Retorna nova lista com mesmo percentual de aumento em todos os precos.

    Parametros:
        precos: Lista de precos originais.
        percentual: Percentual de aumento.

    Returns:
        Lista de precos com aumento.

    Exemplos:
    >>> aplicar_aumento([100.0, 200.0, 50.0], 10.0)
    [110.0, 220.0, 55.0]
    >>> aplicar_aumento([], 10.0)
    []
    """
    return list(map(partial(aumentar, percentual=percentual), precos))


def aplicar_descontos(
    precos: list[float],
    /,
) -> list[float]:
    """Retorna nova lista com descontos progressivos conforme faixa de preco.

    Regras:
    - Preco <= 50: 5%% de desconto
    - Preco <= 100: 10%% de desconto
    - Preco > 100: 15%% de desconto

    Parametros:
        precos: Lista de precos originais.

    Returns:
        Lista de precos com desconto.

    Exemplos:
    >>> aplicar_descontos([50.0, 100.0, 200.0])
    [47.5, 90.0, 170.0]
    >>> aplicar_descontos([33.33])
    [31.66]
    >>> aplicar_descontos([])
    []
    """
    return [round(p * 0.95, 2) if p <= 50 else (
        round(p * 0.90, 2) if p <= 100 else round(p * 0.85, 2)
    ) for p in precos]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
