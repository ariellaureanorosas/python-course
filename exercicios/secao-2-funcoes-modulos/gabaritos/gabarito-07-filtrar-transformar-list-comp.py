"""
Gabarito EXERCÍCIO 07 - Filtrar e Transformar com List Comprehension

Raciocínio sênior
-----------------
Três funções, três preocupações: transformar (aumentar_preco_10),
filtrar (filtrar_caros) e ordenar (ordenar_por_preco). Nenhuma
delas MODIFICA a lista original — a primeira usa dict unpacking
({**produto}) para retornar novos dicts, e as outras devolvem
novas listas. Esse "imutabilidade funcional" é o que torna as
funções combináveis: produto -> filtrar -> ordenar sem efeitos
colaterais.
Alternativas descartadas: deepcopy em cada produto (desnecessário
para valores escalares; {**produto} já copia); função única que
faz tudo (quebra a testabilidade de cada etapa).
"""

PRODUTOS = [
    {"nome": "Camiseta", "preco": 49.90},
    {"nome": "Calça", "preco": 129.90},
    {"nome": "Tênis", "preco": 249.90},
    {"nome": "Boné", "preco": 29.90},
    {"nome": "Meia", "preco": 9.90},
]


def aumentar_preco_10(produtos: list[dict]) -> list[dict]:
    """Retorna nova lista com os preços aumentados em 10%.

    A lista ORIGINAL não é modificada: cada produto é copiado com
    dict unpacking e recebe o novo preço.

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicts com ao menos a chave 'preco'.

    Returns
    -------
    list[dict]
        Nova lista com os preços arredondados a 2 casas.

    Exemplos
    --------
    >>> aumentar_preco_10([{'nome': 'A', 'preco': 50.0}])
    [{'nome': 'A', 'preco': 55.0}]
    >>> aumentar_preco_10([])
    []
    """
    return [
        {**produto, "preco": round(produto["preco"] * 1.1, 2)}
        for produto in produtos
    ]


def filtrar_caros(produtos: list[dict], limite: float = 50.0) -> list[dict]:
    """Retorna nova lista apenas com produtos mais caros que o limite.

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicts com a chave 'preco'.
    limite : float, opcional
        Preço mínimo para considerar "caro" (padrão 50.0).

    Returns
    -------
    list[dict]
        Nova lista filtrada.

    Exemplos
    --------
    >>> filtrar_caros([{'preco': 30.0}, {'preco': 80.0}])
    [{'preco': 80.0}]
    >>> filtrar_caros([{'preco': 30.0}], limite=10.0)
    [{'preco': 30.0}]
    """
    return [produto for produto in produtos if produto["preco"] > limite]


def ordenar_por_preco(
    produtos: list[dict], reverso: bool = False
) -> list[dict]:
    """Retorna nova lista ordenada pelo preço.

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicts com a chave 'preco'.
    reverso : bool, opcional
        True para ordem decrescente (padrão False).

    Returns
    -------
    list[dict]
        Nova lista ordenada.

    Exemplos
    --------
    >>> ordenar_por_preco([{'preco': 80.0}, {'preco': 30.0}])
    [{'preco': 30.0}, {'preco': 80.0}]
    >>> ordenar_por_preco([{'preco': 80.0}, {'preco': 30.0}], reverso=True)
    [{'preco': 80.0}, {'preco': 30.0}]
    """
    return sorted(produtos, key=lambda p: p["preco"], reverse=reverso)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(aumentar_preco_10(PRODUTOS))
    print(filtrar_caros(PRODUTOS))
    print(ordenar_por_preco(PRODUTOS, reverso=True))

# Onde você provavelmente divergiu:
# - usou deepcopy para "não modificar a original" (desnecessário:
#   {**produto} já cria novo dict; valores são escalares aqui)
# - fez produtos[novo] = ... dentro do loop (mutação direta —
#   quebra a promessa de retornar uma nova lista)
# - acertou o round depois do cálculo (round(49.9 * 1.1, 2) = 54.89 —
#   sem o round apareceria 54.89000000000001)