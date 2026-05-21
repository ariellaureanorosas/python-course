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

2. Função `produtos_por_faixa_de_preco(produtos: list[dict], minimo: float, maximo: float) -> list[dict]`
   - Usa filter() com lambda para selecionar produtos dentro da faixa de preço [minimo, maximo]
   - Retorna lista

3. Função `filtrar_por_nome(produtos: list[dict], termo: str) -> list[dict]`
   - Usa filter() para selecionar produtos cujo nome contém `termo` (case insensitive)
   - Retorna lista
"""


def produtos_disponiveis(produtos: list[dict]) -> list[dict]:
    ...


def produtos_por_faixa_de_preco(
    produtos: list[dict],
    minimo: float,
    maximo: float,
) -> list[dict]:
    ...


def filtrar_por_nome(produtos: list[dict], termo: str) -> list[dict]:
    ...
