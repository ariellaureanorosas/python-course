"""
Gabarito EXERCÍCIO 21 - Sets: Primeiro Duplicado e Operações

Raciocínio sênior
-----------------
O set de "vistos" transforma a busca de repetidos de O(n²) para
O(n): `item in set` custa O(1) (tabela hash, anotação 05) contra
O(n) de `item in lista`. A função devolve na PRIMEIRA repetição —
o return dentro do for é uma saída antecipada. elementos_duplicados
reusa o mesmo padrão, mas acumula em um segundo set (que também
evita repetir o repetido). palavras_em_comum é a interseção de
conjuntos: `set1 & set2` entrega exatamente "o que está nos dois"
sem nenhum loop manual.

Alternativas descartadas: `lista.count()` em loop (quadrático);
comprehension com `in` (mais lento e menos legível que &).
"""


def primeiro_duplicado(lista: list) -> int | None:
    """Devolve o primeiro elemento repetido da lista, ou None.

    Parâmetros
    ----------
    lista : list
        Lista de valores a varrer.

    Retorna
    -------
    int | None
        Primeiro valor que já havia aparecido, ou None.

    Exemplos
    --------
    >>> primeiro_duplicado([3, 5, 1, 3, 7])
    3
    >>> primeiro_duplicado([1, 2, 3]) is None
    True
    """
    vistos: set = set()
    for item in lista:
        if item in vistos:
            return item
        vistos.add(item)
    return None


def elementos_duplicados(lista: list) -> set:
    """Devolve o set de TODOS os elementos que aparecem mais de uma vez.

    Parâmetros
    ----------
    lista : list
        Lista de valores a inspecionar.

    Retorna
    -------
    set
        Elementos repetidos (sem duplicar no próprio retorno).

    Exemplos
    --------
    >>> elementos_duplicados([1, 2, 1, 3, 2])
    {1, 2}
    >>> elementos_duplicados([1, 2, 3])
    set()
    """
    vistos: set = set()
    repetidos: set = set()
    for item in lista:
        if item in vistos:
            repetidos.add(item)
        vistos.add(item)
    return repetidos


def palavras_em_comum(texto1: str, texto2: str) -> set:
    """Devolve as palavras presentes nos dois textos (interseção).

    Parâmetros
    ----------
    texto1 : str
        Primeiro texto, palavras separadas por espaço.
    texto2 : str
        Segundo texto, palavras separadas por espaço.

    Retorna
    -------
    set
        Palavras que aparecem nos dois textos.

    Exemplos
    --------
    >>> palavras_em_comum("oi cafe", "cafe leite")
    {'cafe'}
    >>> palavras_em_comum("a b", "c d")
    set()
    """
    return set(texto1.split()) & set(texto2.split())


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(primeiro_duplicado([3, 5, 1, 3, 7]))
    print(primeiro_duplicado([1, 2, 3]))
    print(elementos_duplicados([1, 2, 1, 3, 2]))
    print(palavras_em_comum("oi cafe", "cafe leite"))

# Onde você provavelmente divergiu:
# - usou lista de "vistos" (O(n) no `in`) — o set é o ponto da aula
# - checou `lista.count(item) > 1` dentro do loop (O(n²) total)
# - no primeiro_duplicado, retornou o item ANTES de marcar como visto
# - na interseção, fez loops manuais em vez de `set1 & set2`
# - usou `{}` pensando em set vazio no retorno (cria dict!)
#   — `set()` como aqui