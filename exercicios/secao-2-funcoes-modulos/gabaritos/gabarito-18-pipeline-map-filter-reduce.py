"""
Gabarito EXERCÍCIO 18 - Combinar map/filter/reduce em Pipeline

Raciocínio sênior
-----------------
O pipeline lê da direita para a esquerda: filter(par) -> map(^2)
-> reduce(soma) em uma única expressão aninhada — cada função da
etapa anterior alimenta a seguinte sem listas intermediárias
(lazy até o reduce materializar).
processar_numeros_flexivel mostra o pipeline parametrizado:
pares/expoente viram os únicos pontos de decisão. A validação do
expoente (não pode ser negativo) protege o contrato ANTES do
cálculo. O predicado é tipado como Callable[[int], bool] — filter
espera exatamente isso, e a tipagem documenta o contrato.
Alternativas descartadas: for com acumulador (mais código, menos
composição); lambda anônimo sem nome em cada etapa (aqui o
predicado é nomeado em filtro para legibilidade).
"""

from collections.abc import Callable
from functools import reduce


def processar_numeros(
    numeros: list[int],
) -> int:
    """Retorna soma dos quadrados dos numeros pares (pipeline).

    Etapas: filter(pares) -> map(^2) -> reduce(soma).

    Parametros
    ----------
    numeros : list[int]
        Lista de inteiros.

    Returns
    -------
    int
        Soma dos quadrados dos numeros pares.

    Exemplos
    --------
    >>> processar_numeros([1, 2, 3, 4, 5])
    20
    >>> processar_numeros([])
    0
    >>> processar_numeros([1, 3, 5])
    0
    """
    return reduce(
        lambda acc, n: acc + n,
        map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numeros)),
        0,
    )


def processar_numeros_flexivel(
    numeros: list[int],
    *,
    pares: bool = True,
    expoente: int = 2,
) -> int:
    """Retorna soma dos numeros filtrados elevados ao expoente.

    Parametros
    ----------
    numeros : list[int]
        Lista de inteiros.
    pares : bool, opcional
        True filtra pares, False filtra impares (padrao True).
    expoente : int, opcional
        Expoente para elevar cada numero (padrao 2).

    Returns
    -------
    int
        Soma calculada.

    Raises
    ------
    ValueError
        Se o expoente for negativo.

    Exemplos
    --------
    >>> processar_numeros_flexivel([1, 2, 3, 4], pares=True, expoente=2)
    20
    >>> processar_numeros_flexivel([1, 2, 3, 4], pares=False, expoente=2)
    10
    >>> processar_numeros_flexivel([1, 2, 3], pares=True, expoente=3)
    8
    >>> processar_numeros_flexivel([], pares=True)
    0
    """
    if expoente < 0:
        raise ValueError('Expoente nao pode ser negativo')

    filtro: Callable[[int], bool] = (
        lambda n: n % 2 == 0
    ) if pares else (
        lambda n: n % 2 != 0
    )

    return reduce(
        lambda acc, n: acc + n,
        map(lambda n: n ** expoente, filter(filtro, numeros)),
        0,
    )


def processar_texto(
    palavras: list[str],
) -> list[str]:
    """Retorna lista com palavras de 3+ caracteres em maiusculas.

    Parametros
    ----------
    palavras : list[str]
        Lista de strings.

    Returns
    -------
    list[str]
        Lista filtrada com strings em maiusculas.

    Exemplos
    --------
    >>> processar_texto(['oi', 'mundo', 'a', 'Python'])
    ['MUNDO', 'PYTHON']
    >>> processar_texto(['a', 'bc', ''])
    []
    >>> processar_texto([])
    []
    """
    return list(map(
        str.upper,
        filter(lambda p: len(p) >= 3, palavras),
    ))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(processar_numeros([1, 2, 3, 4, 5]))
    print(processar_numeros_flexivel([1, 2, 3, 4], pares=False, expoente=3))
    print(processar_texto(['oi', 'mundo', 'a', 'Python']))

# Onde você provavelmente divergiu:
# - tipou o predicado como object (perde a informação de que filter
#   espera um chamável que recebe int e devolve bool — aqui é
#   Callable[[int], bool])
# - trocou a ordem do pipeline (map antes do filter soma os quadrados
#   dos ímpares também — a ordem muda o resultado)
# - não validou expoente negativo (fatorial de um número negativo
#   inválido em matemática básica: 2**-1 = 0.5, quebrando o int no
#   reduce)