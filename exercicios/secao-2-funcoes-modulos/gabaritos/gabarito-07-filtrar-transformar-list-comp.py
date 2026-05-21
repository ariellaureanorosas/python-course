"""
Gabarito 07 - Filtrar e Transformar com List Comprehension
"""
from copy import deepcopy


produtos = [
    {"nome": "Camiseta", "preco": 49.90},
    {"nome": "Calça", "preco": 129.90},
    {"nome": "Tênis", "preco": 249.90},
    {"nome": "Boné", "preco": 29.90},
    {"nome": "Meia", "preco": 9.90},
]


def aumentar_preco_10(produtos: list[dict]) -> list[dict]:
    """Retorna nova lista com preços aumentados em 10% (sem modificar original).

    Exemplo:
        >>> len(aumentar_preco_10(produtos))
        5
        >>> aumentar_preco_10(produtos)[0]['preco']
        54.89
    """
    return [
        deepcopy({**produto, "preco": round(produto["preco"] * 1.1, 2)})
        for produto in produtos
    ]


def filtrar_caros(produtos: list[dict], limite: float = 50.0) -> list[dict]:
    """Retorna produtos com preço acima do limite.

    Exemplo:
        >>> len(filtrar_caros(produtos))
        2
        >>> filtrar_caros(produtos, limite=30.0)
        [{'nome': 'Camiseta', 'preco': 49.9}, {'nome': 'Calça', 'preco': 129.9}, {'nome': 'Tênis', 'preco': 249.9}]
    """
    return [produto for produto in produtos if produto["preco"] > limite]


def ordenar_por_preco(
    produtos: list[dict], reverso: bool = False
) -> list[dict]:
    """Retorna produtos ordenados por preço (crescente ou decrescente).

    Exemplo:
        >>> ordenar_por_preco(produtos)[0]['nome']
        'Meia'
        >>> ordenar_por_preco(produtos, reverso=True)[0]['nome']
        'Tênis'
    """
    return sorted(produtos, key=lambda p: p["preco"], reverse=reverso)
