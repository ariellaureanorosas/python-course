from copy import deepcopy

PRODUTOS = [
    {"nome": "Camiseta", "preco": 49.90},
    {"nome": "Calça", "preco": 129.90},
    {"nome": "Tênis", "preco": 249.90},
    {"nome": "Boné", "preco": 29.90},
    {"nome": "Meia", "preco": 9.90},
]


def aumentar_preco_10(produtos: list[dict]) -> list[dict]:
    return [
        {**produto, "preco": round(produto["preco"] * 1.1, 2)}
        for produto in produtos
    ]


def filtrar_caros(produtos: list[dict], limite: float = 50.0) -> list[dict]:
    return [produto for produto in produtos if produto["preco"] > limite]


def ordenar_por_preco(
    produtos: list[dict], reverso: bool = False
) -> list[dict]:
    return sorted(produtos, key=lambda p: p["preco"], reverse=reverso)


if __name__ == "__main__":
    print(filtrar_caros(PRODUTOS))
    print(ordenar_por_preco(PRODUTOS, reverso=True))
