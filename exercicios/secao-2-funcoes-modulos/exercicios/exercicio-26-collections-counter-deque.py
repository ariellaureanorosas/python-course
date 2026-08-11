"""
EXERCÍCIO 26 - collections: Counter, defaultdict e deque

Tópicos: collections.Counter, collections.defaultdict,
         collections.deque, anotação 18

Implemente quatro funções:

1. `contar_palavras(texto: str) -> Counter`
   - Separa por espaços e conta as ocorrências de cada palavra
     com collections.Counter.

2. `top_palavras(texto: str, n: int) -> list`
   - Usa .most_common(n) do Counter — devolve a lista dos n pares
     (palavra, quantidade) mais frequentes.

3. `agrupar_por_inicial(palavras: list) -> dict`
   - Usa defaultdict(list) para agrupar as palavras pela PRIMEIRA
     letra — sem if existe/append manual. Devolve dict normal.

4. `ultimos_itens(itens: list, n: int) -> list`
   - Usa deque(maxlen=n): o deque descarta sozinho os mais antigos
     quando estoura o limite. Devolve list(deque).

Comportamento esperado:
    contar_palavras("bola gato bola")          # Counter({'bola': 2, 'gato': 1})
    top_palavras("a b a c a b", 2)             # [('a', 3), ('b', 2)]
    agrupar_por_inicial(["bola", "gato", "banana"])
    # {'b': ['bola', 'banana'], 'g': ['gato']}
    ultimos_itens([1, 2, 3, 4, 5], 3)          # [3, 4, 5]

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

from collections import Counter, defaultdict, deque


def contar_palavras(texto: str) -> Counter:
    ...


def top_palavras(texto: str, n: int) -> list:
    ...


def agrupar_por_inicial(palavras: list) -> dict:
    ...


def ultimos_itens(itens: list, n: int) -> list:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(contar_palavras("bola gato bola"))
    print(top_palavras("a b a c a b", 2))
    print(agrupar_por_inicial(["bola", "gato", "banana"]))
    print(ultimos_itens([1, 2, 3, 4, 5], 3))