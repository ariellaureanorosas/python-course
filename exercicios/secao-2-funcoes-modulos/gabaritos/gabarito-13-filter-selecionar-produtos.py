from copy import deepcopy


def _produto_valido(produto: dict, /) -> bool:
    """Retorna True se produto tem preco e quantidade positivos."""
    return produto.get('preco', 0) > 0 and produto.get('quantidade', 0) > 0


def produtos_disponiveis(
    produtos: list[dict],
    /,
) -> list[dict]:
    """Retorna nova lista apenas com produtos com preco e quantidade > 0.

    Parametros:
        produtos: Lista de dicionarios de produtos.

    Returns:
        Lista filtrada de produtos disponiveis.

    Exemplos:
    >>> p1 = {'nome': 'Caneta', 'preco': 1.5, 'quantidade': 10}
    >>> p2 = {'nome': 'Lapis', 'preco': 0.0, 'quantidade': 5}
    >>> produtos_disponiveis([p1, p2])
    [{'nome': 'Caneta', 'preco': 1.5, 'quantidade': 10}]
    >>> produtos_disponiveis([])
    []
    """
    return list(filter(_produto_valido, produtos))


def produtos_por_faixa_de_preco(
    produtos: list[dict],
    minimo: float,
    maximo: float,
    /,
) -> list[dict]:
    """Retorna nova lista com produtos dentro da faixa de preco (inclusive).

    Parametros:
        produtos: Lista de dicionarios de produtos.
        minimo: Preco minimo.
        maximo: Preco maximo.

    Returns:
        Lista filtrada de produtos na faixa.

    Exemplos:
    >>> p1 = {'preco': 10.0}
    >>> p2 = {'preco': 50.0}
    >>> p3 = {'preco': 100.0}
    >>> produtos_por_faixa_de_preco([p1, p2, p3], 10.0, 50.0)
    [{'preco': 10.0}, {'preco': 50.0}]
    """
    return list(filter(
        lambda p: minimo <= p['preco'] <= maximo,
        produtos,
    ))


def filtrar_por_nome(
    produtos: list[dict],
    termo: str,
    /,
) -> list[dict]:
    """Retorna nova lista com produtos cujo nome contenha o termo.

    A busca e case insensitive.

    Parametros:
        produtos: Lista de dicionarios de produtos.
        termo: Texto a buscar no nome.

    Returns:
        Lista filtrada de produtos.

    Exemplos:
    >>> p1 = {'nome': 'Caneta Azul'}
    >>> p2 = {'nome': 'Lapis Preto'}
    >>> filtrar_por_nome([p1, p2], 'caneta')
    [{'nome': 'Caneta Azul'}]
    >>> filtrar_por_nome([p1, p2], 'preto')
    [{'nome': 'Lapis Preto'}]
    >>> filtrar_por_nome([p1, p2], 'borracha')
    []
    """
    return list(filter(
        lambda p: termo.lower() in p.get('nome', '').lower(),
        produtos,
    ))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
