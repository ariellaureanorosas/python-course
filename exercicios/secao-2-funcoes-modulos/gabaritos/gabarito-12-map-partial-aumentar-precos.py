"""
Gabarito EXERCÍCIO 12 - Map com partial para Aumentar Preços

Raciocínio sênior
-----------------
partial(aumentar, percentual=percentual) "congela" o percentual
e devolve uma função de um argumento só — exatamente o que map()
precisa receber. Essa é a ponte entre "função de dois parâmetros"
e "map espera função de um parâmetro".
aplicar_descontos usa lambda dentro de map() quando a lógica é
pontual e única (não vale a pena criar uma função nomeada).
Nenhuma função altera a lista original — map retorna iterator,
list() materializa a nova lista.
Alternativas descartadas: list comprehension em aplicar_aumento
(o exercício pede map + partial), função separada para desconto
(lambda pontual é o equilíbrio sênior).
"""

from functools import partial


def aumentar(preco: float, percentual: float) -> float:
    """Aplica percentual de aumento sobre o preco e retorna novo valor.

    Parametros
    ----------
    preco : float
        Valor original.
    percentual : float
        Percentual de aumento (ex: 10 para 10%%).

    Returns
    -------
    float
        Preco com aumento.

    Exemplos
    --------
    >>> aumentar(100.0, 10.0)
    110.0
    >>> aumentar(50.0, 50.0)
    75.0
    """
    return round(preco * (1 + percentual / 100), 2)


def aplicar_aumento(
    precos: list[float],
    percentual: float,
) -> list[float]:
    """Retorna nova lista com mesmo percentual de aumento em todos.

    Usa functools.partial para fixar o percentual e map() para
    aplicar a função parcial a cada preço.

    Parametros
    ----------
    precos : list[float]
        Lista de precos originais.
    percentual : float
        Percentual de aumento.

    Returns
    -------
    list[float]
        Lista de precos com aumento.

    Exemplos
    --------
    >>> aplicar_aumento([100.0, 200.0, 50.0], 10.0)
    [110.0, 220.0, 55.0]
    >>> aplicar_aumento([], 10.0)
    []
    """
    return list(map(partial(aumentar, percentual=percentual), precos))


def aplicar_descontos(
    precos: list[float],
) -> list[float]:
    """Retorna nova lista com descontos progressivos conforme faixa.

    Regras:
    - Preco <= 50: 5%% de desconto
    - Preco <= 100: 10%% de desconto
    - Preco > 100: 15%% de desconto

    Parametros
    ----------
    precos : list[float]
        Lista de precos originais.

    Returns
    -------
    list[float]
        Lista de precos com desconto.

    Exemplos
    --------
    >>> aplicar_descontos([50.0, 100.0, 200.0])
    [47.5, 90.0, 170.0]
    >>> aplicar_descontos([33.33])
    [31.66]
    >>> aplicar_descontos([])
    []
    """
    return [round(p * 0.95, 2) if p <= 50 else (
        round(p * 0.90, 2) if p <= 100 else round(p * 0.85, 2)
    ) for p in precos]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - passou aumentar(preco, percentual) direto ao map (map entrega
#   APENAS o elemento — a função deve receber um único argumento;
#   o partial é a ponte)
# - escreveu lambda p: p * 1.1 em aplicar_aumento (equivalente, mas
#   o exercício pede explicitamente partial)
# - multiplicou preco * (1 + percentual) esquecendo '/ 100'
#   (10% virava 11x o preço)