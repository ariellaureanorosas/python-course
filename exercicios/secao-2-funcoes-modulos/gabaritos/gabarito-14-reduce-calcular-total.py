"""
Gabarito EXERCÍCIO 14 - Reduce para Calcular Total

Raciocínio sênior
-----------------
reduce() acumula: a função lambda recebe o acumulador (acc) e o
próximo item, e o valor inicial 0.0 garante que lista vazia retorna
0.0. No caso do desconto, a redução aplica o percentual no PREÇO de
cada item ANTES de somar — a regra de negócio vive no acumulador.
A alternativa com sum() + generator expression é a "versão
pitônica" preferida na prática (reduce é mais verboso e menos
legível para somatórios simples) — o exercício pede reduzido e o
gabarito entrega os dois, mostrando a troca entre eles.
"""

from functools import reduce


def calcular_total_estoque(
    produtos: list[dict],
) -> float:
    """Retorna soma de preco * quantidade de todos os produtos.

    Usa reduce() com acumulador iniciado em 0.0.

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicionarios de produtos.

    Returns
    -------
    float
        Valor total do estoque.

    Exemplos
    --------
    >>> p1 = {'preco': 10.0, 'quantidade': 3}
    >>> p2 = {'preco': 5.0, 'quantidade': 2}
    >>> calcular_total_estoque([p1, p2])
    40.0
    >>> calcular_total_estoque([])
    0.0
    """
    return reduce(
        lambda acc, p: acc + p['preco'] * p['quantidade'],
        produtos,
        0.0,
    )


def calcular_total_sum(
    produtos: list[dict],
) -> float:
    """Retorna soma de preco * quantidade com sum e generator.

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicionarios de produtos.

    Returns
    -------
    float
        Valor total do estoque.

    Exemplos
    --------
    >>> p1 = {'preco': 10.0, 'quantidade': 3}
    >>> p2 = {'preco': 5.0, 'quantidade': 2}
    >>> calcular_total_sum([p1, p2])
    40.0
    >>> calcular_total_sum([])
    0.0
    """
    return float(sum(p['preco'] * p['quantidade'] for p in produtos))


def calcular_total_com_desconto(
    produtos: list[dict],
    desconto: float,
) -> float:
    """Retorna total do estoque aplicando desconto percentual no preco.

    O desconto (ex: 10 para 10%) incide sobre o preco de cada
    produto individualmente.

    Parametros
    ----------
    produtos : list[dict]
        Lista de dicionarios de produtos.
    desconto : float
        Percentual de desconto.

    Returns
    -------
    float
        Valor total com desconto.

    Raises
    ------
    ValueError
        Se o desconto for negativo.

    Exemplos
    --------
    >>> p1 = {'preco': 100.0, 'quantidade': 1}
    >>> p2 = {'preco': 200.0, 'quantidade': 1}
    >>> calcular_total_com_desconto([p1, p2], 10.0)
    270.0
    >>> calcular_total_com_desconto([], 10.0)
    0.0
    """
    if desconto < 0:
        raise ValueError('Desconto nao pode ser negativo')

    return reduce(
        lambda acc, p: acc + (p['preco'] * (1 - desconto / 100)) * p['quantidade'],
        produtos,
        0.0,
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - esqueceu o valor inicial do reduce (sem o 0.0, uma lista vazia
#   quebra com TypeError)
# - somou o desconto no TOTAL em vez de aplicá-lo no preco de cada
#   produto (100 + 200 = 300 → 270 aqui; com desconto no total
#   daria o mesmo para preços iguais, mas difere quando variam)
# - não validou desconto negativo (um bug silencioso de -10% viraria
#   um "aumento")