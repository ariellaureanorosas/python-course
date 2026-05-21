"""
GABARITO 19 - combinations/permutations em Senhas
"""

from itertools import combinations, permutations


def gerar_combinacoes(
    caracteres: list[str],
    tamanho: int,
) -> list[tuple[str, ...]]:
    """Gera combinações de caracteres no tamanho especificado.

    Combinações ignoram ordem (A,B) == (B,A).

    Args:
        caracteres: Lista de caracteres disponíveis.
        tamanho: Comprimento de cada combinação.

    Returns:
        Lista de tuplas com combinações.
    """
    return list(combinations(caracteres, tamanho))


def gerar_permutacoes(
    caracteres: list[str],
    tamanho: int,
) -> list[tuple[str, ...]]:
    """Gera permutações de caracteres no tamanho especificado.

    Permutações consideram ordem (A,B) != (B,A).

    Args:
        caracteres: Lista de caracteres disponíveis.
        tamanho: Comprimento de cada permutação.

    Returns:
        Lista de tuplas com permutações.
    """
    return list(permutations(caracteres, tamanho))


def comparar_possibilidades(
    caracteres: list[str],
    tamanho: int,
) -> dict:
    """Compara o número de combinações vs permutações.

    Args:
        caracteres: Lista de caracteres disponíveis.
        tamanho: Comprimento das senhas.

    Returns:
        Dicionário com estatísticas comparativas.
    """
    n_comb = len(list(combinations(caracteres, tamanho)))
    n_perm = len(list(permutations(caracteres, tamanho)))
    return {
        'caracteres': len(caracteres),
        'tamanho': tamanho,
        'combinacoes': n_comb,
        'permutacoes': n_perm,
        'razao': n_perm / n_comb if n_comb > 0 else 0,
    }


def gerar_senhas_com_fixas(
    obrigatorios: list[str],
    opcionais: list[str],
    tamanho: int,
) -> list[str]:
    """Gera combinações que incluem todos os caracteres obrigatórios.

    Args:
        obrigatorios: Caracteres que devem estar em todas as senhas.
        opcionais: Caracteres opcionais.
        tamanho: Comprimento total das senhas.

    Returns:
        Lista de strings com senhas geradas.
    """
    todos = obrigatorios + opcionais
    conjunto_obrigatorios = set(obrigatorios)
    return [
        ''.join(comb)
        for comb in combinations(todos, tamanho)
        if conjunto_obrigatorios.issubset(comb)
    ]
