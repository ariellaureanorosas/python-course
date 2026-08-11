"""
EXERCÍCIO 29 - Cópia rasa e profunda

Tópicos: copy.copy, copy.deepcopy, estruturas aninhadas, anotação 22

Implemente três funções:

1. `clonar_rasa(origem: list) -> list`
   - Usa copy.copy: devolve lista nova no topo, mas itens
     aninhados continuam COMPARTILHADOS com a original.

2. `clonar_profunda(origem: list) -> list`
   - Usa copy.deepcopy: devolve uma estrutura totalmente nova —
     mudar a cópia não afeta a original em nenhum nível.

3. `aumentar_filhos(matriz: list, valor: int) -> list`
   - Recebe uma lista de listas de números e devolve uma cópia
     PROFUNDA com `valor` somado a cada número. A matriz original
     deve permanecer intocada (o padrão da aula 102).

Comportamento esperado:
    aumentar_filhos([[1, 2], [3, 4]], 10)
    # [[11, 12], [13, 14]] e a matriz original continua [[1, 2], [3, 4]]

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def clonar_rasa(origem: list) -> list:
    ...


def clonar_profunda(origem: list) -> list:
    ...


def aumentar_filhos(matriz: list, valor: int) -> list:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    original = [[1, 2], [3, 4]]
    print(aumentar_filhos(original, 10))
    print(original)