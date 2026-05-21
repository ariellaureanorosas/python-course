"""
GABARITO 14 - Reduce para Calcular Total
"""

from functools import reduce


def calcular_total_estoque(produtos: list[dict]) -> float:
    """Calcula o valor total do estoque com reduce.

    Soma preco * quantidade de cada produto usando reduce.

    Args:
        produtos: Lista de dicionários de produtos.

    Returns:
        Valor total do estoque.
    """
    return reduce(
        lambda acc, p: acc + p['preco'] * p['quantidade'],
        produtos,
        0.0,
    )


def calcular_total_sum(produtos: list[dict]) -> float:
    """Calcula o valor total do estoque com sum e generator.

    Args:
        produtos: Lista de dicionários de produtos.

    Returns:
        Valor total do estoque.
    """
    return sum(p['preco'] * p['quantidade'] for p in produtos)


def calcular_total_com_desconto(
    produtos: list[dict],
    desconto: float,
) -> float:
    """Calcula o valor total do estoque aplicando desconto no preço.

    Usa reduce para aplicar desconto percentual no preço de cada produto
    antes de somar ao total.

    Args:
        produtos: Lista de dicionários de produtos.
        desconto: Percentual de desconto (ex: 10 para 10%).

    Returns:
        Valor total com desconto aplicado.
    """
    return reduce(
        lambda acc, p: acc + (p['preco'] * (1 - desconto / 100)) * p['quantidade'],
        produtos,
        0.0,
    )
