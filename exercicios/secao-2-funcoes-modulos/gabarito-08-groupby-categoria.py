"""
Gabarito 08 - Group By com itertools.groupby
"""
from itertools import groupby


produtos = [
    {"nome": "Arroz", "preco": 25.90, "categoria": "Alimento"},
    {"nome": "Feijão", "preco": 12.90, "categoria": "Alimento"},
    {"nome": "Detergente", "preco": 4.50, "categoria": "Limpeza"},
    {"nome": "Sabão", "preco": 8.90, "categoria": "Limpeza"},
    {"nome": "Mouse", "preco": 89.90, "categoria": "Eletrônico"},
    {"nome": "Teclado", "preco": 149.90, "categoria": "Eletrônico"},
]


def agrupar_por_categoria(produtos: list[dict]) -> dict:
    """Agrupa os produtos por categoria usando itertools.groupby.

    A lista é ordenada por categoria antes do agrupamento.

    Exemplo:
        >>> resultado = agrupar_por_categoria(produtos)
        >>> list(resultado.keys())
        ['Alimento', 'Eletrônico', 'Limpeza']
        >>> len(resultado['Alimento'])
        2
    """
    produtos_ordenados = sorted(produtos, key=lambda p: p["categoria"])

    resultado: dict = {}
    for categoria, grupo in groupby(produtos_ordenados, key=lambda p: p["categoria"]):
        resultado[categoria] = list(grupo)

    return resultado
