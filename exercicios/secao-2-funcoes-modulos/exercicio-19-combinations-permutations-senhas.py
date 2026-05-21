"""
EXERCÍCIO 19 - combinations/permutations em Senhas

Tópicos: itertools.combinations, itertools.permutations
Aula: 111

Crie funções que usam combinations e permutations do itertools para
gerar possibilidades de senhas.

1. Função `gerar_combinacoes(caracteres: list[str], tamanho: int) -> list[tuple[str, ...]]`
   - Usa itertools.combinations para gerar todas as combinações de `caracteres`
     com comprimento `tamanho`
   - Retorna como lista de tuplas

2. Função `gerar_permutacoes(caracteres: list[str], tamanho: int) -> list[tuple[str, ...]]`
   - Usa itertools.permutations para gerar todas as permutações de `caracteres`
     com comprimento `tamanho`
   - Retorna como lista de tuplas

3. Função `comparar_possibilidades(caracteres: list[str], tamanho: int) -> dict`
   - Gera combinações e permutações para o mesmo conjunto
   - Retorna um dicionário com:
     {
         "caracteres": len(caracteres),
         "tamanho": tamanho,
         "combinacoes": quantidade,
         "permutacoes": quantidade,
         "razao": permutacoes / combinacoes (ou 0 se não houver combinações)
     }

4. Função `gerar_senhas_com_fixas(
       obrigatorios: list[str],
       opcionais: list[str],
       tamanho: int,
   ) -> list[str]`
   - Dados caracteres obrigatórios (que devem estar em todas as senhas)
     e opcionais, gere todas as combinações de tamanho `tamanho` que
     INCLUEM todos os obrigatórios
   - Ex: obrigatorios=['A','B'], opcionais=['1','2'], tamanho=3
     -> combinações de 3 elementos de ['A','B','1','2'] que sempre têm A e B
   - Dica: combinação total de todos, depois filtre as que contêm todos os obrigatórios
"""

from itertools import combinations, permutations


def gerar_combinacoes(
    caracteres: list[str],
    tamanho: int,
) -> list[tuple[str, ...]]:
    ...


def gerar_permutacoes(
    caracteres: list[str],
    tamanho: int,
) -> list[tuple[str, ...]]:
    ...


def comparar_possibilidades(
    caracteres: list[str],
    tamanho: int,
) -> dict:
    ...


def gerar_senhas_com_fixas(
    obrigatorios: list[str],
    opcionais: list[str],
    tamanho: int,
) -> list[str]:
    ...
