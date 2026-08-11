"""
Gabarito EXERCÍCIO 13 - Filter para Selecionar Produtos

Raciocínio sênior
-----------------
O critério "preco > 0 e quantidade > 0" é nomeado como função
privada (_produto_valido) porque será usado por produtos_disponiveis
e porque um nome próprio documenta melhor que um lambda aninhado.
Para os critérios pontuais (faixa, nome), o lambda dentro de
filter() é o equilíbrio: a regra vive junto do filter e não polui
o módulo.
Os acessos usam .get() com default (0, '') — produto ausente não
quebra o filter (dados de borda defensivos).
Alternativas descartadas: list comprehension com if (equivalente
em resultado, mas o exercício pede filter()).
"""


def _produto_valido(produto: dict) -> bool:
    """Retorna True se produto tem preco e quantidade positivos."""
    return produto.get('preco', 0) > 0 and produto.get('quantidade', 0) > 0


def produtos_disponiveis(
    produtos: list[dict],
) -> list[dict]:
    """Retorna nova lista apenas com produtos com preco e quantidade > 0.

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicionarios de produtos.

    Returns
    -------
    list[dict]
        Lista filtrada de produtos disponiveis.

    Exemplos
    --------
    >>> p1 = {'nome': 'Caneta', 'preco': 1.5, 'quantidade': 10}
    >>> p2 = {'nome': 'Lapis', 'preco': 0.0, 'quantidade': 5}
    >>> produtos_disponiveis([p1, p2])
    [{'nome': 'Caneta', 'preco': 1.5, 'quantidade': 10}]
    >>> produtos_disponiveis([])
    []
    """
    return list(filter(_produto_valido, produtos))


def produtos_por_faixa_de_preco(
    produtos: list[dict],
    minimo: float,
    maximo: float,
) -> list[dict]:
    """Retorna nova lista com produtos dentro da faixa de preco.

    Faixa inclusiva em ambas as pontas: [minimo, maximo].

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicionarios de produtos.
    minimo : float
        Preco minimo.
    maximo : float
        Preco maximo.

    Returns
    -------
    list[dict]
        Lista filtrada de produtos na faixa.

    Exemplos
    --------
    >>> p1 = {'preco': 10.0}
    >>> p2 = {'preco': 50.0}
    >>> p3 = {'preco': 100.0}
    >>> produtos_por_faixa_de_preco([p1, p2, p3], 10.0, 50.0)
    [{'preco': 10.0}, {'preco': 50.0}]
    """
    return list(filter(
        lambda p: minimo <= p['preco'] <= maximo,
        produtos,
    ))


def filtrar_por_nome(
    produtos: list[dict],
    termo: str,
) -> list[dict]:
    """Retorna nova lista com produtos cujo nome contenha o termo.

    A busca e case insensitive.

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicionarios de produtos.
    termo : str
        Texto a buscar no nome.

    Returns
    -------
    list[dict]
        Lista filtrada de produtos.

    Exemplos
    --------
    >>> p1 = {'nome': 'Caneta Azul'}
    >>> p2 = {'nome': 'Lapis Preto'}
    >>> filtrar_por_nome([p1, p2], 'caneta')
    [{'nome': 'Caneta Azul'}]
    >>> filtrar_por_nome([p1, p2], 'preto')
    [{'nome': 'Lapis Preto'}]
    >>> filtrar_por_nome([p1, p2], 'borracha')
    []
    """
    return list(filter(
        lambda p: termo.lower() in p.get('nome', '').lower(),
        produtos,
    ))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - usou list comprehension + if [item for item in ... if cond]
#   (resolve, mas o exercício pede filter())
# - acessou p['preco'] direto (KeyError se a chave faltar; .get(..., 0)
#   trata o produto "quebrado" sem estourar)
# - na busca por nome, comparou sem .lower() (busca virava
#   case sensitive, contrariando o caso-insensitive pedido)