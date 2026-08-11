"""
EXERCÍCIO 25 - itertools.count e product

Tópicos: itertools.count, itertools.islice, itertools.product

Implemente duas funções:

1. `gerar_sequencia(start: int, step: int, quantidade: int) -> list`
   - Usa itertools.count(start, step) limitado por
     itertools.islice para devolver os `quantidade` primeiros
     números da sequência.

2. `combinar_opcoes(cores: list, tamanhos: list) -> list`
   - Usa itertools.product para devolver TODAS as combinações
     (cor, tamanho), na ordem que o product gera (primeiro o 1º
     argumento variando mais devagar).

Comportamento esperado:
    gerar_sequencia(10, 2, 4)   # [10, 12, 14, 16]
    combinar_opcoes(["p", "m"], ["A", "B"])
    # [('p', 'A'), ('p', 'B'), ('m', 'A'), ('m', 'B')]

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

from itertools import count, islice, product


def gerar_sequencia(start: int, step: int, quantidade: int) -> list:
    ...


def combinar_opcoes(cores: list, tamanhos: list) -> list:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(gerar_sequencia(10, 2, 4))
    print(combinar_opcoes(["p", "m"], ["A", "B"]))