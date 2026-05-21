"""
Exercício 08 - Group By com itertools.groupby

Crie uma função `agrupar_por_categoria(produtos: list[dict]) -> dict` onde
cada produto é um dict com nome, preco e categoria.

A lista de produtos é:

produtos = [
    {'nome': 'Arroz', 'preco': 25.90, 'categoria': 'Alimento'},
    {'nome': 'Feijão', 'preco': 12.90, 'categoria': 'Alimento'},
    {'nome': 'Detergente', 'preco': 4.50, 'categoria': 'Limpeza'},
    {'nome': 'Sabão', 'preco': 8.90, 'categoria': 'Limpeza'},
    {'nome': 'Mouse', 'preco': 89.90, 'categoria': 'Eletrônico'},
    {'nome': 'Teclado', 'preco': 149.90, 'categoria': 'Eletrônico'},
]

A função deve:
    - Ordenar a lista por categoria (obrigatório para groupby funcionar)
    - Usar itertools.groupby para agrupar por categoria
    - Retornar um dict onde cada chave é a categoria
      e o valor é a lista de produtos daquela categoria

Tópicos da aula: itertools.groupby, sorted(), lambda, dict comprehension
"""


produtos = [
    {"nome": "Arroz", "preco": 25.90, "categoria": "Alimento"},
    {"nome": "Feijão", "preco": 12.90, "categoria": "Alimento"},
    {"nome": "Detergente", "preco": 4.50, "categoria": "Limpeza"},
    {"nome": "Sabão", "preco": 8.90, "categoria": "Limpeza"},
    {"nome": "Mouse", "preco": 89.90, "categoria": "Eletrônico"},
    {"nome": "Teclado", "preco": 149.90, "categoria": "Eletrônico"},
]


def agrupar_por_categoria(produtos: list[dict]) -> dict:
    ...
