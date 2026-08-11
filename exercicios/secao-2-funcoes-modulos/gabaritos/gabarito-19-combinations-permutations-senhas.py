"""
Gabarito EXERCÍCIO 19 - combinations/permutations em Senhas

Raciocínio sênior
-----------------
combinations ignora ordem (['A','B'] == ['B','A']), permutations
considera — a comparação final (razao = permutações/combinacoes)
deixa o conceito visível: com n elementos e tamanho k, há k!
permutações para cada combinação.
gerar_senhas_com_fixas resolve com um filtro de subset: das
combinações totais, só as que CONTÊM todos os obrigatórios. Isso é
mais enxuto e mais correto que combinar manualmente obrigatórios +
escolhas — evita duplicação e cobre casos em que o conjunto
obrigatório interage com os opcionais.
A validação de tamanho é fail-fast: garante que combinations não
receba tamanho maior que o conjunto.
Alternativas descartadas: product() (com repetição — aqui a
semântica é sem repetição), loop manual de agrupamento.
"""

from itertools import combinations, permutations


def gerar_combinacoes(
    caracteres: list[str],
    tamanho: int,
) -> list[tuple[str, ...]]:
    """Retorna combinacoes dos caracteres (ordem nao importa).

    Parametros
    ----------
    caracteres : list[str]
        Lista de caracteres disponiveis.
    tamanho : int
        Comprimento de cada combinacao.

    Returns
    -------
    list[tuple[str, ...]]
        Lista de tuplas com combinacoes.

    Raises
    ------
    ValueError
        Se tamanho maior que numero de caracteres.

    Exemplos
    --------
    >>> gerar_combinacoes(['A', 'B', 'C'], 2)
    [('A', 'B'), ('A', 'C'), ('B', 'C')]
    >>> gerar_combinacoes(['A', 'B'], 3)
    Traceback (most recent call last):
    ...
    ValueError: Tamanho (3) maior que numero de caracteres (2)
    """
    if tamanho > len(caracteres):
        raise ValueError(
            f'Tamanho ({tamanho}) maior que numero de caracteres ({len(caracteres)})'
        )
    return list(combinations(caracteres, tamanho))


def gerar_permutacoes(
    caracteres: list[str],
    tamanho: int,
) -> list[tuple[str, ...]]:
    """Retorna permutacoes dos caracteres (ordem importa).

    Parametros
    ----------
    caracteres : list[str]
        Lista de caracteres disponiveis.
    tamanho : int
        Comprimento de cada permutacao.

    Returns
    -------
    list[tuple[str, ...]]
        Lista de tuplas com permutacoes.

    Raises
    ------
    ValueError
        Se tamanho maior que numero de caracteres.

    Exemplos
    --------
    >>> gerar_permutacoes(['A', 'B'], 2)
    [('A', 'B'), ('B', 'A')]
    >>> gerar_permutacoes(['A', 'B', 'C'], 2)
    [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    """
    if tamanho > len(caracteres):
        raise ValueError(
            f'Tamanho ({tamanho}) maior que numero de caracteres ({len(caracteres)})'
        )
    return list(permutations(caracteres, tamanho))


def comparar_possibilidades(
    caracteres: list[str],
    tamanho: int,
) -> dict[str, int | float]:
    """Retorna dicionario comparativo entre combinacoes e permutacoes.

    Usa generator expressions para contar sem materializar listas
    intermediarias.

    Parametros
    ----------
    caracteres : list[str]
        Lista de caracteres disponiveis.
    tamanho : int
        Comprimento das senhas.

    Returns
    -------
    dict[str, int | float]
        Dicionario com estatisticas.

    Exemplos
    --------
    >>> resultado = comparar_possibilidades(['A', 'B', 'C'], 2)
    >>> resultado['combinacoes']
    3
    >>> resultado['permutacoes']
    6
    >>> resultado['razao']
    2.0
    """
    if tamanho > len(caracteres):
        raise ValueError(
            f'Tamanho ({tamanho}) maior que numero de caracteres ({len(caracteres)})'
        )

    n_comb: int = sum(1 for _ in combinations(caracteres, tamanho))
    n_perm: int = sum(1 for _ in permutations(caracteres, tamanho))

    return {
        'caracteres': len(caracteres),
        'tamanho': tamanho,
        'combinacoes': n_comb,
        'permutacoes': n_perm,
        'razao': n_perm / n_comb if n_comb > 0 else 0.0,
    }


def gerar_senhas_com_fixas(
    obrigatorios: list[str],
    opcionais: list[str],
    tamanho: int,
) -> list[str]:
    """Retorna combinacoes que incluem todos os caracteres obrigatorios.

    Gera todas as combinacoes de `tamanho` a partir do conjunto
    (obrigatorios + opcionais) e filtra as que contêm todos os
    obrigatorios.

    Parametros
    ----------
    obrigatorios : list[str]
        Caracteres que devem aparecer em todas as senhas.
    opcionais : list[str]
        Caracteres opcionais.
    tamanho : int
        Comprimento total de cada senha.

    Returns
    -------
    list[str]
        Lista de strings com senhas geradas (sem repeticao).

    Raises
    ------
    ValueError
        Se tamanho for menor que o numero de obrigatorios.

    Exemplos
    --------
    >>> gerar_senhas_com_fixas(['A'], ['B', 'C'], 2)
    ['AB', 'AC']
    >>> gerar_senhas_com_fixas(['A', 'B'], ['C', 'D'], 3)
    ['ABC', 'ABD']
    """
    if len(obrigatorios) > tamanho:
        raise ValueError(
            f'Numero de caracteres obrigatorios ({len(obrigatorios)}) '
            f'excede o tamanho total ({tamanho})'
        )

    conjunto_obrigatorios: set[str] = set(obrigatorios)
    todos: list[str] = obrigatorios + opcionais

    return [
        ''.join(comb)
        for comb in combinations(todos, tamanho)
        if conjunto_obrigatorios.issubset(comb)
    ]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - usou product() — isso PERMITE repetição de caracteres
#   ('AA'), que não faz sentido numa senha gerada por
#   combinações; aqui combinations/permutations são sem repetição
# - esqueceu a validação de tamanho (combinations(['A','B'], 3)
#   devolvia lista vazia em silêncio em vez de avisar)
# - em gerar_senhas_com_fixas, montou combinações de obrigatórios +
#   opcionais manualmente (o subset filter é mais à prova de erro:
#   cobre automaticamente o caso tamanho == len(obrigatorios))
# - não chamou doctest.testmod() — o pattern dos gabaritos sem ele
#   não roda a bateria automática