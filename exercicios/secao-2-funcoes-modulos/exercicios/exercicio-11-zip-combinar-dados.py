"""
EXERCÍCIO 11 - Zip para Combinar Dados

Tópicos: zip, zip_longest (itertools.zip_longest)
Aulas: 110

Crie as funções abaixo usando zip() e itertools.zip_longest().

1. Função `combinar_listas(nomes: list[str], idades: list[int]) -> list[str]`
   - Recebe duas listas de mesmo tamanho
   - Usa zip() para combinar nome e idade
   - Retorna lista de strings no formato: "Nome tem X anos"

2. Função `combinar_listas_desiguais(nomes: list[str], idades: list[int],
   preenchimento: int = 0) -> list[str]`
   - Recebe duas listas de tamanhos POTENCIALMENTE diferentes
   - Usa zip_longest() para preencher valores faltantes com `preenchimento`
   - Retorna lista de strings no formato: "Nome tem X anos"

3. Função `combinar_tres_listas(nomes: list[str], idades: list[int],
   cidades: list[str]) -> list[str]`
   - Usa zip() para combinar TRÊS listas de mesmo tamanho
   - Retorna lista de strings no formato: "Nome tem X anos e mora em Cidade"
"""

from itertools import zip_longest


def combinar_listas(nomes: list[str], idades: list[int]) -> list[str]:
    return [
        f"{nome} tem {idade} anos" for nome, idade in zip(nomes, idades, strict=True)
    ]


def combinar_listas_desiguais(
    nomes: list[str],
    idades: list[int],
    preenchimento: int = 0,
) -> list[str]:
    return [
        f"{nome} tem {idade} anos"
        for nome, idade in zip_longest(nomes, idades, fillvalue=preenchimento)
    ]


def combinar_tres_listas(
    nomes: list[str],
    idades: list[int],
    cidades: list[str],
) -> list[str]:
    return [
        f"{nome} tem {idade} anos e mora em {cidade}"
        for nome, idade, cidade in zip(nomes, idades, cidades, strict=True)
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
