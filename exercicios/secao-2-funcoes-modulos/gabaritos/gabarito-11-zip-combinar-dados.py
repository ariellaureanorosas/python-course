"""
Gabarito EXERCÍCIO 11 - Zip para Combinar Dados

Raciocínio sênior
-----------------
zip() casa posição por posição e PARA no menor iterável — por isso
combinar_listas presume listas do mesmo tamanho. Quando os tamanhos
diferem, zip_longest() preenche o que falta com fillvalue (padrão 0).
Todas as funções retornam listas NOVAS (as originais não são
tocadas), e a formatação f-string centraliza a transformação.
Alternativas descartadas: loop com range(len(nomes)) (frágil com
tamanhos diferentes); enumerate sobre uma lista e índice na outra.
"""

from itertools import zip_longest


def combinar_listas(
    nomes: list[str],
    idades: list[int],
) -> list[str]:
    """Retorna lista formatada combinando nomes e idades com zip.

    A funcao nao modifica as listas originais.

    Parametros
    ----------
    nomes : list[str]
        Lista de nomes.
    idades : list[int]
        Lista de idades.

    Returns
    -------
    list[str]
        Lista de strings no formato 'Nome tem X anos'.

    Exemplos
    --------
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
    preenchimento: int = 0,
) -> list[str]:
    """Retorna lista combinando listas de tamanhos diferentes.

    Usa zip_longest() com fillvalue=preenchimento para cobrir os
    índices faltantes da menor lista.

    Parametros
    ----------
    nomes : list[str]
        Lista de nomes.
    idades : list[int]
        Lista de idades.
    preenchimento : int, opcional
        Valor numérico substituto para índices faltantes (padrão 0).

    Returns
    -------
    list[str]
        Lista de strings no formato 'Nome tem X anos'.

    Exemplos
    --------
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
) -> list[str]:
    """Retorna lista formatada combinando tres listas com zip.

    Parametros
    ----------
    nomes : list[str]
        Lista de nomes.
    idades : list[int]
        Lista de idades.
    cidades : list[str]
        Lista de cidades.

    Returns
    -------
    list[str]
        Lista de strings 'Nome tem X anos e mora em Cidade'.

    Exemplos
    --------
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

# Onde você provavelmente divergiu:
# - usou range(len(...)) + índice (quebra quando as listas têm
#   tamanhos diferentes)
# - usou zip() onde o zip_longest() era o correto (a mais curta
#   "corta" a lista maior em silêncio)
# - esqueceu o fillvalue (zip_longest preencheria com None e
#   "tem None anos" apareceria no print)