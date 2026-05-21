"""
GABARITO 11 - Zip para Combinar Dados
"""

from itertools import zip_longest


def combinar_listas(nomes: list[str], idades: list[int]) -> list[str]:
    """Combina duas listas de mesmo tamanho com zip.

    Args:
        nomes: Lista de nomes.
        idades: Lista de idades.

    Returns:
        Lista de strings "Nome tem X anos".
    """
    return [f'{nome} tem {idade} anos' for nome, idade in zip(nomes, idades)]


def combinar_listas_desiguais(
    nomes: list[str],
    idades: list[int],
    preenchimento: int = 0,
) -> list[str]:
    """Combina duas listas de tamanhos diferentes com zip_longest.

    Args:
        nomes: Lista de nomes.
        idades: Lista de idades.
        preenchimento: Valor para preencher itens faltantes.

    Returns:
        Lista de strings "Nome tem X anos".
    """
    return [
        f'{nome} tem {idade} anos'
        for nome, idade in zip_longest(nomes, idades, fillvalue=preenchimento)
    ]


def combinar_tres_listas(
    nomes: list[str],
    idades: list[int],
    cidades: list[str],
) -> list[str]:
    """Combina três listas de mesmo tamanho com zip.

    Args:
        nomes: Lista de nomes.
        idades: Lista de idades.
        cidades: Lista de cidades.

    Returns:
        Lista de strings "Nome tem X anos e mora em Cidade".
    """
    return [
        f'{nome} tem {idade} anos e mora em {cidade}'
        for nome, idade, cidade in zip(nomes, idades, cidades)
    ]
