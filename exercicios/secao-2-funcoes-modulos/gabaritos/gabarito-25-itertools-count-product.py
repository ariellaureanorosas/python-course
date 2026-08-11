"""
Gabarito EXERCÍCIO 25 - itertools.count e product

Raciocínio sênior
-----------------
`count(start, step)` é a versão ITERADOR do range infinito: ele só
termina porque o `islice` corta a sequência. islice(seq, n) pega os
n primeiros — é quem dá finitude ao infinito. `product(a, b)` é o
produto cartesiano: para CADA item de cores ele varre TODOS os
tamanhos, e o orderm que ele gera (primeiro argumento variando mais
devagar) é o padrão dos `for` aninhados — o produto cartesiano é
exatamente o aninhamento em uma linha.

Alternativas descartadas: loops aninhados manuais (product deixa a
intenção explícita e lida com N iteráveis); range(start, stop)
(termina — count+islice funciona para sequências infinitas).
"""

from itertools import count, islice, product


def gerar_sequencia(start: int, step: int, quantidade: int) -> list:
    """Devolve os `quantidade` primeiros números da sequência infinita.

    Parâmetros
    ----------
    start : int
        Primeiro número.
    step : int
        Passo da progressão.
    quantidade : int
        Quantos números devolver.

    Retorna
    -------
    list
        Lista com os primeiros termos.

    Exemplos
    --------
    >>> gerar_sequencia(10, 2, 4)
    [10, 12, 14, 16]
    >>> gerar_sequencia(0, 5, 3)
    [0, 5, 10]
    """
    return list(islice(count(start, step), quantidade))


def combinar_opcoes(cores: list, tamanhos: list) -> list:
    """Devolve todas as combinações (cor, tamanho).

    Parâmetros
    ----------
    cores : list
        Primeiro eixo do produto cartesiano.
    tamanhos : list
        Segundo eixo.

    Retorna
    -------
    list
        Tuplas (cor, tamanho) na ordem do product.

    Exemplos
    --------
    >>> combinar_opcoes(["p", "m"], ["A", "B"])
    [('p', 'A'), ('p', 'B'), ('m', 'A'), ('m', 'B')]
    """
    return list(product(cores, tamanhos))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(gerar_sequencia(10, 2, 4))
    print(combinar_opcoes(["p", "m"], ["A", "B"]))

# Onde você provavelmente divergiu:
# - usou range em vez de count: funciona para passos finitos, mas
#   count+islice é a ferramenta que não termina sozinha
# - fez o loop manual com next() até cansar (o islice já corta)
# - inverteu os operandos do product (a ordem do exemplo muda)
# - tentou list(count(10, 2)) — loop infinito! islice é obrigatório
# - esqueceu islice(counter, quantidade) — devolveu os 4 primeiros
#   com list(count(start, step)) direto, travando o script