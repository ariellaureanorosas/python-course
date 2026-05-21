"""
GABARITO 13 - Filter para Selecionar Produtos
"""


def produtos_disponiveis(produtos: list[dict]) -> list[dict]:
    """Seleciona produtos com preço e quantidade positivos.

    Args:
        produtos: Lista de dicionários de produtos.

    Returns:
        Lista filtrada de produtos disponíveis.
    """
    return list(filter(
        lambda p: p['preco'] > 0 and p['quantidade'] > 0,
        produtos,
    ))


def produtos_por_faixa_de_preco(
    produtos: list[dict],
    minimo: float,
    maximo: float,
) -> list[dict]:
    """Seleciona produtos dentro de uma faixa de preço.

    Args:
        produtos: Lista de dicionários de produtos.
        minimo: Preço mínimo (inclusive).
        maximo: Preço máximo (inclusive).

    Returns:
        Lista filtrada de produtos na faixa.
    """
    return list(filter(
        lambda p: minimo <= p['preco'] <= maximo,
        produtos,
    ))


def filtrar_por_nome(produtos: list[dict], termo: str) -> list[dict]:
    """Seleciona produtos cujo nome contenha o termo (case insensitive).

    Args:
        produtos: Lista de dicionários de produtos.
        termo: Texto a buscar no nome.

    Returns:
        Lista filtrada de produtos com nome correspondente.
    """
    return list(filter(
        lambda p: termo.lower() in p['nome'].lower(),
        produtos,
    ))
