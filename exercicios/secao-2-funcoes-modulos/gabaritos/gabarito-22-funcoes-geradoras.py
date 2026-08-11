"""
Gabarito EXERCÍCIO 22 - Funções Geradoras (yield)

Raciocínio sênior
-----------------
Uma função com `yield` é uma fábrica de geradores: ela não executa
nada até o primeiro next() — diferentemente de uma lista, que já
nasce pronta. Por isso cada função devolve o gerador SEM materializar
nada; o `list(...)` no chamador é quem "queima" tudo. `yield from`
existe exatamente para repassar os itens de outro iterável sem
escrever `for x in g: yield x` — ele delega o protocolo de iteração
inteiro. O generator expression `(n * 2 for n in range(5))` é o
irmão preguiçoso da list comprehension: mesmo efeito, memória O(1).

Alternativas descartadas: listas retornadas (perde a preguiça);
comprehension em pares_ate (o estilo com yield mostra o protocolo).
"""

from typing import Iterator


def pares_ate(limite: int) -> Iterator[int]:
    """Gera os números pares de 0 até limite (inclusive).

    Parâmetros
    ----------
    limite : int
        Limite superior (inclusivo).

    Retorna
    -------
    Iterator[int]
        Pares em ordem crescente.

    Exemplos
    --------
    >>> list(pares_ate(6))
    [0, 2, 4, 6]
    >>> list(pares_ate(1))
    [0]
    """
    for n in range(limite + 1):
        if n % 2 == 0:
            yield n


def ao_quadrado(fonte: list) -> Iterator[int]:
    """Gera n ** 2 para cada n da fonte, na ordem.

    Parâmetros
    ----------
    fonte : list
        Lista de números.

    Retorna
    -------
    Iterator[int]
        Quadrados, um por item.

    Exemplos
    --------
    >>> list(ao_quadrado([1, 2, 3]))
    [1, 4, 9]
    """
    for n in fonte:
        yield n ** 2


def concatenar(geradores: list) -> Iterator[int]:
    """Repassa, um a um, os itens de cada gerador da lista.

    Parâmetros
    ----------
    geradores : list
        Lista de iteráveis em sequência.

    Retorna
    -------
    Iterator[int]
        Itens de todos os geradores, na ordem dada.

    Exemplos
    --------
    >>> list(concatenar([pares_ate(2), pares_ate(4)]))
    [0, 2, 0, 2, 4]
    """
    for gerador in geradores:
        yield from gerador


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(list(pares_ate(6)))
    print(list(ao_quadrado([1, 2, 3])))
    print(list(concatenar([pares_ate(2), pares_ate(4)])))

    dobrados = (n * 2 for n in range(5))
    print(list(dobrados))

# Onde você provavelmente divergiu:
# - usou return em vez de yield (a função deixaria de ser geradora)
# - chamou o gerador duas vezes esperando "recomeçar"
#   (gerador é de uso único — recrie ou materialize com list())
# - usou yield g dentro de concatenar (entrega o gerador INTEIRO
#   como item; o certo é yield from g)
# - esqueceu de incluir o limite na varredura de pares_ate