"""
Gabarito EXERCÍCIO 08 - Group By com itertools.groupby

Raciocínio sênior
-----------------
groupby() NÃO agrupa elementos iguais espalhados: ele agrupa
somente CONSECUTIVOS iguais. Por isso o gabarito ORDENA por
categoria antes de agrupar — sem o sorted(), as categorias
intercaladas cairiam em grupos separados. Esse é o erro clássico:
"esqueci de ordenar" é a primeira coisa que o groupby ensina.
O dict comprehension monta o resultado com {categoria: list(grupo)};
list(grupo) é necessário porque o grupo é um iterator descartável.
Alternativas descartadas: defaultdict(list) + loop manual para o
agrupamento — mais verboso e não exercita o groupby pedido.
"""

from itertools import groupby

PRODUTOS = [
    {"nome": "Arroz", "preco": 25.90, "categoria": "Alimento"},
    {"nome": "Feijão", "preco": 12.90, "categoria": "Alimento"},
    {"nome": "Detergente", "preco": 4.50, "categoria": "Limpeza"},
    {"nome": "Sabão", "preco": 8.90, "categoria": "Limpeza"},
    {"nome": "Mouse", "preco": 89.90, "categoria": "Eletrônico"},
    {"nome": "Teclado", "preco": 149.90, "categoria": "Eletrônico"},
]


def agrupar_por_categoria(produtos: list[dict]) -> dict:
    """Retorna dict agrupando os produtos por categoria.

    A lista é ordenada por categoria ANTES do groupby (obrigatório:
    groupby agrupa apenas consecutivos iguais).

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicts com a chave 'categoria'.

    Returns
    -------
    dict
        {categoria: [produtos da categoria]}.

    Exemplos
    --------
    >>> p1 = {'nome': 'Arroz', 'categoria': 'Alimento'}
    >>> p2 = {'nome': 'Detergente', 'categoria': 'Limpeza'}
    >>> agrupar_por_categoria([p1, p2])
    {'Alimento': [{'nome': 'Arroz', 'categoria': 'Alimento'}], 'Limpeza': [{'nome': 'Detergente', 'categoria': 'Limpeza'}]}
    >>> agrupar_por_categoria([])
    {}
    """
    ordenados = sorted(produtos, key=lambda p: p["categoria"])
    return {
        categoria: list(grupo)
        for categoria, grupo in groupby(
            ordenados, key=lambda p: p["categoria"]
        )
    }


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    resultado = agrupar_por_categoria(PRODUTOS)
    for categoria, itens in resultado.items():
        print(f"{categoria}: {[i['nome'] for i in itens]}")

# Onde você provavelmente divergiu:
# - esqueceu o sorted() antes do groupby (o agrupamento falhava com
#   categorias intercaladas — o erro clássico deste exercício)
# - guardou o grupo direto no dict sem list(grupo) (o grupo é um
#   iterator exaurível; sem list() o dict guardaria itens vazios)
# - usou defaultdict(list) em vez do groupby pedido