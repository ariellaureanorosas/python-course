"""
EXERCÍCIO 31 - functools.lru_cache (Memoização)

Tópicos: functools.lru_cache, cache_info, anotação 18

Implemente duas funções DECORADAS com lru_cache:

1. `fatorial(n: int) -> int`
   - Decorada com @lru_cache(maxsize=None): a segunda chamada com o
     mesmo n vem do cache, sem recalcular.

2. `potencia(base: int, expoente: int) -> int`
   - Decorada com @lru_cache(maxsize=128) — o caso do maxsize finito:
     quando o cache estoura, os itens menos usados saem.

3. No __main__, chame fatorial(5) duas vezes, chame potencia(2, 10)
   duas vezes e exiba `fatorial.cache_info()` — o relatório mostra
   quantas chamadas vieram do cache (hits) e quantas calcularam
   (misses).

Comportamento esperado:
    fatorial(5)        # 120
    potencia(2, 10)    # 1024
    # após 2x fatorial(5): CacheInfo(hits=1, misses=1, maxsize=None, currsize=...)

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def fatorial(n: int) -> int:
    ...


def potencia(base: int, expoente: int) -> int:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(fatorial(5))
    print(fatorial(5))
    print(potencia(2, 10))
    print(potencia(2, 10))
    print(fatorial.cache_info())