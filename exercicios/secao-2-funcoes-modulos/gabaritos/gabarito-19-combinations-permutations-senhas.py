from itertools import combinations, permutations
from copy import deepcopy


def gerar_combinacoes(
    caracteres: list[str],
    tamanho: int,
    /,
) -> list[tuple[str, ...]]:
    """Retorna combinacoes dos caracteres (ordem nao importa).

    Parametros:
        caracteres: Lista de caracteres disponiveis.
        tamanho: Comprimento de cada combinacao.

    Returns:
        Lista de tuplas com combinacoes.

    Raises:
        ValueError: Se tamanho maior que numero de caracteres.

    Exemplos:
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
    /,
) -> list[tuple[str, ...]]:
    """Retorna permutacoes dos caracteres (ordem importa).

    Parametros:
        caracteres: Lista de caracteres disponiveis.
        tamanho: Comprimento de cada permutacao.

    Returns:
        Lista de tuplas com permutacoes.

    Raises:
        ValueError: Se tamanho maior que numero de caracteres.

    Exemplos:
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
    /,
) -> dict[str, int | float]:
    """Retorna dicionario comparativo entre combinacoes e permutacoes.

    Usa generator expressions para contar sem materializar listas intermediarias.

    Parametros:
        caracteres: Lista de caracteres disponiveis.
        tamanho: Comprimento das senhas.

    Returns:
        Dicionario com estatisticas.

    Exemplos:
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
    /,
) -> list[str]:
    """Retorna combinacoes que incluem todos os caracteres obrigatorios.

    Parametros:
        obrigatorios: Caracteres obrigatorios em todas as senhas.
        opcionais: Caracteres opcionais.
        tamanho: Comprimento total de cada senha.

    Returns:
        Lista de strings com senhas geradas (combinacoes sem repeticoes).

    Raises:
        ValueError: Se tamanho < len(obrigatorios) ou se houver caracteres
                    duplicados entre obrigatorios e opcionais.

    Exemplos:
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
