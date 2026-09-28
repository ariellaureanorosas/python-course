"""
EXERCÍCIO 13 - Filter para Selecionar Produtos

Tópicos: filter()
Aula: 114

Crie as funções abaixo usando filter().

Considere a seguinte estrutura de produto:
    produto = {"nome": "Camiseta", "preco": 59.90, "quantidade": 10}

1. Função `produtos_disponiveis(produtos: list[dict]) -> list[dict]`
   - Usa filter() para selecionar produtos com preco > 0 e quantidade > 0
   - Retorna lista

2. Função `produtos_por_faixa_de_preco(produtos: list[dict], minimo: float,
   maximo: float) -> list[dict]`
   - Usa filter() com lambda para selecionar produtos dentro da faixa
     de preço [minimo, maximo]
   - Retorna lista

3. Função `filtrar_por_nome(produtos: list[dict], termo: str) -> list[dict]`
   - Usa filter() para selecionar produtos cujo nome contém `termo` (case insensitive)
   - Retorna lista
"""

from typing import cast


def _produto_valido(produto: dict[str, str | float | int]) -> bool:
    return (
        cast("float", produto.get("preco", 0)) > 0
        and cast("float", produto.get("quantidade", 0)) > 0
    )


def produtos_disponiveis(
    produtos: list[dict[str, str | float | int]],
) -> list[dict[str, str | float | int]]:
    return list(filter(_produto_valido, produtos))


def produtos_por_faixa_de_preco(
    produtos: list[dict[str, str | float | int]],
    minimo: float,
    maximo: float,
) -> list[dict[str, str | float | int]]:
    return list(
        filter(lambda p: minimo <= cast("float", p["preco"]) <= maximo, produtos)
    )


def filtrar_por_nome(
    produtos: list[dict[str, str | float | int]], termo: str
) -> list[dict[str, str | float | int]]:
    return list(
        filter(
            lambda p: termo.lower() in cast("str", p.get("nome", "")).lower(), produtos
        )
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
