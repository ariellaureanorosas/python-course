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
    ordenados = sorted(produtos, key=lambda p: p["categoria"])
    return {
        categoria: list(grupo)
        for categoria, grupo in groupby(ordenados, key=lambda p: p["categoria"])
    }


if __name__ == "__main__":
    resultado = agrupar_por_categoria(PRODUTOS)
    for categoria, itens in resultado.items():
        print(f"{categoria}: {[i['nome'] for i in itens]}")
