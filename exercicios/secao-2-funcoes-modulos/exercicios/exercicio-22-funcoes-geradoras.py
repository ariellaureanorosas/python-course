"""
EXERCÍCIO 22 - Funções Geradoras (yield)

Tópicos: generator, yield, yield from, generator expression

Implemente três funções geradoras:

1. `pares_ate(limite: int) -> Iterator[int]`
   - Função geradora com yield: devolve todos os pares de 0 até
     limite (inclusive).

2. `ao_quadrado(fonte: list) -> Iterator[int]`
   - Função geradora: devolve n ** 2 para cada n da fonte.

3. `concatenar(geradores: list) -> Iterator[int]`
   - Usa `yield from` para repassar, um a um, os itens de CADA
     gerador da lista, na ordem.

4. Bônus: no __main__, crie uma generator expression
   `dobrados = (n * 2 for n in range(5))` e exiba-a com list().

Comportamento esperado:
    list(pares_ate(6))             # [0, 2, 4, 6]
    list(ao_quadrado([1, 2, 3]))   # [1, 4, 9]
    list(concatenar([pares_ate(2), pares_ate(4)]))  # [0, 2, 0, 2, 4]

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

from typing import Iterator


def pares_ate(limite: int) -> Iterator[int]:
    ...


def ao_quadrado(fonte: list) -> Iterator[int]:
    ...


def concatenar(geradores: list) -> Iterator[int]:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(list(pares_ate(6)))
    print(list(ao_quadrado([1, 2, 3])))
    print(list(concatenar([pares_ate(2), pares_ate(4)])))

    dobrados = (n * 2 for n in range(5))
    print(list(dobrados))