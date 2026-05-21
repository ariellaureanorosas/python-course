from itertools import zip_longest
from copy import deepcopy


def combinar_listas(
    nomes: list[str],
    idades: list[int],
    /,
) -> list[str]:
    """Retorna lista formatada combinando nomes e idades com zip.

    A funcao nao modifica as listas originais.

    Parametros:
        nomes: Lista de nomes.
        idades: Lista de idades.

    Returns:
        Lista de strings no formato 'Nome tem X anos'.

    Exemplos:
    >>> combinar_listas(['Ana', 'Joao'], [25, 30])
    ['Ana tem 25 anos', 'Joao tem 30 anos']
    >>> combinar_listas(['Maria'], [40])
    ['Maria tem 40 anos']
    """
    return [
        f'{nome} tem {idade} anos'
        for nome, idade in zip(nomes, idades)
    ]


def combinar_listas_desiguais(
    nomes: list[str],
    idades: list[int],
    /,
    *,
    preenchimento: int = 0,
) -> list[str]:
    """Retorna lista combinando listas de tamanhos diferentes com zip_longest.

    A funcao nao modifica as listas originais.

    Parametros:
        nomes: Lista de nomes.
        idades: Lista de idades.
        preenchimento: Valor numerico substituto para indices faltantes.

    Returns:
        Lista de strings no formato 'Nome tem X anos'.

    Exemplos:
    >>> combinar_listas_desiguais(['Ana', 'Joao', 'Carla'], [25, 30])
    ['Ana tem 25 anos', 'Joao tem 30 anos', 'Carla tem 0 anos']
    >>> combinar_listas_desiguais(['Ana', 'Joao'], [25], preenchimento=18)
    ['Ana tem 25 anos', 'Joao tem 18 anos']
    """
    return [
        f'{nome} tem {idade} anos'
        for nome, idade in zip_longest(
            nomes, idades, fillvalue=preenchimento
        )
    ]


def combinar_tres_listas(
    nomes: list[str],
    idades: list[int],
    cidades: list[str],
    /,
) -> list[str]:
    """Retorna lista formatada combinando tres listas com zip.

    A funcao nao modifica as listas originais.

    Parametros:
        nomes: Lista de nomes.
        idades: Lista de idades.
        cidades: Lista de cidades.

    Returns:
        Lista de strings 'Nome tem X anos e mora em Cidade'.

    Exemplos:
    >>> combinar_tres_listas(['Ana'], [25], ['SP'])
    ['Ana tem 25 anos e mora em SP']
    """
    return [
        f'{nome} tem {idade} anos e mora em {cidade}'
        for nome, idade, cidade in zip(nomes, idades, cidades)
    ]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
