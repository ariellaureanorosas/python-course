"""
Gabarito EXERCÍCIO 31 - functools.lru_cache (Memoização)

Raciocínio sênior
-----------------
A memoização troca memória por tempo: funções PURAS (mesma entrada ↵
mesma saída, sem efeito colateral) podem ser cacheadas com segurança.
O decorator envolve a função e guarda num dict interno o par
(argumentos → resultado). maxsize=None ignora limites; maxsize=128
mantém os 128 itens mais recentemente usados (LRU) e descarta o
resto. No fatorial é dramático: fatorial(5) recalcula uma árvore
inteira de chamadas; na segunda chamada com o mesmo n, o resultado
sai pronto do cache — cache_info() é o painel que prova: hits (veio
do cache) vs misses (calculou).

Alternativas descartadas: cache manual com dict global (o decorator
já gerencia invalidação e limite); bundas de força como functools
de memoização implementada à mão.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fatorial(n: int) -> int:
    """Calcula n! com memoização (maxsize ilimitado).

    Parâmetros
    ----------
    n : int
        Número inteiro não negativo.

    Retorna
    -------
    int
        Fatorial de n.

    Exemplos
    --------
    >>> fatorial(5)
    120
    >>> fatorial(0)
    1
    """
    if n <= 1:
        return 1
    return n * fatorial(n - 1)


@lru_cache(maxsize=128)
def potencia(base: int, expoente: int) -> int:
    """Calcula base ** expoente com memoização (cache limitado).

    Parâmetros
    ----------
    base : int
        Número a elevar.
    expoente : int
        Expoente inteiro não negativo.

    Retorna
    -------
    int
        base elevado a expoente.

    Exemplos
    --------
    >>> potencia(2, 10)
    1024
    >>> potencia(3, 2)
    9
    """
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(fatorial(5))
    print(fatorial(5))
    print(potencia(2, 10))
    print(potencia(2, 10))
    print(fatorial.cache_info())

# Onde você provavelmente divergiu:
# - usou maxsize=0 — isso DESLIGA o cache (0 itens cabem)
# - decorou sem parênteses: @lru_cache (erro: função, não decorator
#   chamável — precisa ser @lru_cache(...))
# - cacheou função com efeito colateral (só FUNÇÕES PURAS podem ser
#   memoizadas com segurança)
# - esqueceu que fatorial chama fatorial: o cache nas chamadas
#   recursivas é o que acelera fatorial(5) de verdade
# - tentou acessar .cache_info() sem ter chamado a função antes
#   (o atributo só existe após o decorator configurar a função)