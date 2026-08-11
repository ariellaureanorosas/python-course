"""
Gabarito EXERCÍCIO 29 - Cópia rasa e profunda

Raciocínio sênior
-----------------
A distinção da aula 102: copiar o TOPO é barato e instantâneo
(copy.copy), mas os itens aninhados continuam sendo as MESMAS
referências — mexer neles vaza para a original. Aumentar preços de
produtos em um dict aninhado (ou números dentro de listas de listas)
exige copy.deepcopy: só ela recria a estrutura em cascata. Em
aumentar_filhos a função NUNCA toca os objetos recebidos — clona
primeiro, transforma a cópia e devolve. Quem chamou continua com a
matriz intocada, o contrato de "função sem efeito colateral".

Alternativas descartadas: comprehension com [x + valor for ...] —
funcionaria para um nível, mas esconderia a lição do deepcopy e
quebraria em estruturas mais profundas.
"""

import copy


def clonar_rasa(origem: list) -> list:
    """Copia o topo da lista (itens aninhados continuam compartilhados).

    Parâmetros
    ----------
    origem : list
        Lista a clonar.

    Retorna
    -------
    list
        Novo container de topo.

    Exemplos
    --------
    >>> clonar_rasa([1, 2, 3])
    [1, 2, 3]
    """
    return copy.copy(origem)


def clonar_profunda(origem: list) -> list:
    """Recria a lista e todos os seus itens aninhados.

    Parâmetros
    ----------
    origem : list
        Lista a clonar, com qualquer profundidade.

    Retorna
    -------
    list
        Cópia totalmente independente.

    Exemplos
    --------
    >>> clonar_profunda([[1], [2]])
    [[1], [2]]
    """
    return copy.deepcopy(origem)


def aumentar_filhos(matriz: list, valor: int) -> list:
    """Devolve cópia profunda com `valor` somado a cada número.

    A matriz recebida não é modificada.

    Parâmetros
    ----------
    matriz : list
        Lista de listas de números.
    valor : int
        Quantia a somar em cada elemento.

    Retorna
    -------
    list
        Nova matriz com os elementos aumentados.

    Exemplos
    --------
    >>> original = [[1, 2], [3, 4]]
    >>> aumentar_filhos(original, 10)
    [[11, 12], [13, 14]]
    >>> original
    [[1, 2], [3, 4]]
    """
    nova: list = copy.deepcopy(matriz)
    for linha in nova:
        for indice in range(len(linha)):
            linha[indice] += valor
    return nova


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    original = [[1, 2], [3, 4]]
    print(aumentar_filhos(original, 10))
    print(original)

# Onde você provavelmente divergiu:
# - usou `.copy()` (shallow) em aumentar_filhos: o `+=` na linha
#   interna vazaria para a matriz original
# - usou copy.copy onde precisava de deepcopy (teste: crie uma
#   cópia rasa, altere matriz[0][0] e veja a original mudar)
# - no doctest, inverteu a ordem: checou original ANTES de ver a
#   cópia — o estado intocado é parte da prova
# - somou `valor` diretamente na matriz recebida (efeito colateral
#   que o enunciado proíbe)
# - esqueceu do módulo copy e tentou deepcopy sem import