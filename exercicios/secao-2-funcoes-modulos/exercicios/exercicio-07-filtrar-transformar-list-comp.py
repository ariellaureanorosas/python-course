"""
Exercício 07 - Filtrar e Transformar com List Comprehension

Baseado no exemplo da aula 102 (list comprehension com produtos), você tem a
seguinte lista de produtos:

produtos = [
    {'nome': 'Camiseta', 'preco': 49.90},
    {'nome': 'Calça', 'preco': 129.90},
    {'nome': 'Tênis', 'preco': 249.90},
    {'nome': 'Boné', 'preco': 29.90},
    {'nome': 'Meia', 'preco': 9.90},
]

Crie as funções:

1. `aumentar_preco_10(produtos: list[dict]) -> list[dict]`
   - Usa list comprehension com dict unpacking ({**produto}) para
     retornar uma nova lista, sem modificar a original
   - Aumenta cada preço em 10% (preco * 1.1)
   - Arredonda o preço para 2 casas decimais

2. `filtrar_caros(produtos: list[dict], limite: float) -> list[dict]`
   - Usa list comprehension para filtrar produtos com preço > limite
   - Valor padrão de limite = 50.0

3. `ordenar_por_preco(produtos: list[dict], reverso: bool) -> list[dict]`
   - Usa sorted() com key=lambda para ordenar por preço

Tópicos da aula: list comprehension, dict unpacking, lambda, sorted(), valores padrão
"""

from typing import cast

produtos = [
    {"nome": "Camiseta", "preco": 49.90},
    {"nome": "Calça", "preco": 129.90},
    {"nome": "Tênis", "preco": 249.90},
    {"nome": "Boné", "preco": 29.90},
    {"nome": "Meia", "preco": 9.90},
]


def aumentar_preco_10(
    produtos: list[dict[str, str | float]],
) -> list[dict[str, str | float]]:
    return [
        {**produto, "preco": round(cast("float", produto["preco"]) * 1.1, 2)}
        for produto in produtos
    ]


def filtrar_caros(
    produtos: list[dict[str, str | float]], limite: float = 50.0
) -> list[dict[str, str | float]]:
    return [produto for produto in produtos if cast("float", produto["preco"]) > limite]


def ordenar_por_preco(
    produtos: list[dict[str, str | float]], *, reverso: bool = False
) -> list[dict[str, str | float]]:
    return sorted(produtos, key=lambda p: cast("float", p["preco"]), reverse=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(aumentar_preco_10(produtos))
    print(filtrar_caros(produtos))
    print(ordenar_por_preco(produtos, reverso=True))
