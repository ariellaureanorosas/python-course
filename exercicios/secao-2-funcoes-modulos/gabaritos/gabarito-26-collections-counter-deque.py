"""
Gabarito EXERCÍCIO 26 - collections: Counter, defaultdict e deque

Raciocínio sênior
-----------------
Counter é o dict "já contado": em vez de `if palavra in dict:
dict[palavra] += 1 else: dict[palavra] = 1`, uma linha `Counter(texto
.split())`. most_common(n) devolve os n pares ordenados por
frequência — a operação mais pedida em análise de texto. O
defaultdict(list) elimina o "if grupo não existe: cria lista" antes
de cada append — o fábrica é chamada automaticamente para chaves
novas. deque(maxlen=n) é a fila de tamanho fixo: o item mais antigo
SAI sozinho quando a fila estoura — perfeito para "últimos N eventos"
sem gerenciar a remoção na mão.

Alternativas descartadas: dict + if/else manual (o exercício é
justamente matar esse boilerplate); list box de tamanho fixo com pop(0)
(O(n) por pop — deque é O(1) nos dois lados).
"""

from collections import Counter, defaultdict, deque


def contar_palavras(texto: str) -> Counter:
    """Conta as ocorrências de cada palavra do texto.

    Parâmetros
    ----------
    texto : str
        Texto com palavras separadas por espaço.

    Retorna
    -------
    Counter
        Palavra → quantidade de ocorrências.

    Exemplos
    --------
    >>> contar_palavras("bola gato bola")
    Counter({'bola': 2, 'gato': 1})
    """
    return Counter(texto.split())


def top_palavras(texto: str, n: int) -> list:
    """Devolve os n pares (palavra, quantidade) mais frequentes.

    Parâmetros
    ----------
    texto : str
        Texto com palavras separadas por espaço.
    n : int
        Quantos itens devolver.

    Retorna
    -------
    list
        Lista de tuplas ordenadas por frequência decrescente.

    Exemplos
    --------
    >>> top_palavras("a b a c a b", 2)
    [('a', 3), ('b', 2)]
    """
    return contar_palavras(texto).most_common(n)


def agrupar_por_inicial(palavras: list) -> dict:
    """Agrupa as palavras pela primeira letra.

    Parâmetros
    ----------
    palavras : list
        Lista de strings.

    Retorna
    -------
    dict
        Letra inicial → lista de palavras (dict comum, sem
        comportamento de default fora da função).

    Exemplos
    --------
    >>> agrupar_por_inicial(["bola", "gato", "banana"])
    {'b': ['bola', 'banana'], 'g': ['gato']}
    """
    grupos: defaultdict = defaultdict(list)
    for palavra in palavras:
        grupos[palavra[0]].append(palavra)
    return dict(grupos)


def ultimos_itens(itens: list, n: int) -> list:
    """Devolve os n últimos itens, descartando os mais antigos.

    Parâmetros
    ----------
    itens : list
        Sequência fonte.
    n : int
        Tamanho fixo da janela.

    Retorna
    -------
    list
        Os n últimos itens na ordem original.

    Exemplos
    --------
    >>> ultimos_itens([1, 2, 3, 4, 5], 3)
    [3, 4, 5]
    """
    return list(deque(itens, maxlen=n))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(contar_palavras("bola gato bola"))
    print(top_palavras("a b a c a b", 2))
    print(agrupar_por_inicial(["bola", "gato", "banana"]))
    print(ultimos_itens([1, 2, 3, 4, 5], 3))

# Onde você provavelmente divergiu:
# - contou com dict + if/else manual (3 linhas por incremento)
# - chamou .most_common() e depois ordenou de novo (já vem ordenado)
# - no agrupamento, fez `if chave in d: d[chave].append(...) else:
#   d[chave] = [...palavra]` — o defaultdict é exatamente isso
# - retornou o defaultdict cru em vez de dict() (o default "vaza"
#   para quem usa a função)
# - para os últimos itens, fez lista[-n:] sem o aspecto "janela que
#   descarta a chegarem itens NOVOS" — esse é o deque