from functools import reduce


def calcular_total_estoque(
    produtos: list[dict],
    /,
) -> float:
    """Retorna soma de preco * quantidade de todos os produtos com reduce.

    Parametros:
        produtos: Lista de dicionarios de produtos.

    Returns:
        Valor total do estoque.

    Exemplos:
    >>> p1 = {'preco': 10.0, 'quantidade': 3}
    >>> p2 = {'preco': 5.0, 'quantidade': 2}
    >>> calcular_total_estoque([p1, p2])
    40.0
    >>> calcular_total_estoque([])
    0.0
    """
    return reduce(
        lambda acc, p: acc + p['preco'] * p['quantidade'],
        produtos,
        0.0,
    )


def calcular_total_sum(
    produtos: list[dict],
    /,
) -> float:
    """Retorna soma de preco * quantidade com sum e generator expression.

    Parametros:
        produtos: Lista de dicionarios de produtos.

    Returns:
        Valor total do estoque.

    Exemplos:
    >>> p1 = {'preco': 10.0, 'quantidade': 3}
    >>> p2 = {'preco': 5.0, 'quantidade': 2}
    >>> calcular_total_sum([p1, p2])
    40.0
    >>> calcular_total_sum([])
    0.0
    """
    return float(sum(p['preco'] * p['quantidade'] for p in produtos))


def calcular_total_com_desconto(
    produtos: list[dict],
    desconto: float,
    /,
) -> float:
    """Retorna valor total do estoque aplicando desconto percentual no preco.

    Parametros:
        produtos: Lista de dicionarios de produtos.
        desconto: Percentual de desconto (ex: 10 para 10%%).

    Returns:
        Valor total com desconto.

    Exemplos:
    >>> p1 = {'preco': 100.0, 'quantidade': 1}
    >>> p2 = {'preco': 200.0, 'quantidade': 1}
    >>> calcular_total_com_desconto([p1, p2], 10.0)
    270.0
    >>> calcular_total_com_desconto([], 10.0)
    0.0
    """
    if desconto < 0:
        raise ValueError('Desconto nao pode ser negativo')

    return reduce(
        lambda acc, p: acc + (p['preco'] * (1 - desconto / 100)) * p['quantidade'],
        produtos,
        0.0,
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
