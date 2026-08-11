"""
EXERCÍCIO 21 - Sets: Primeiro Duplicado e Operações

Tópicos: set, in, interseção, anotação 05

Implemente três funções:

1. `primeiro_duplicado(lista: list) -> int | None`
   - Percorre a lista e devolve o PRIMEIRO elemento que já tinha
     aparecido antes (use um set de "vistos" — o `item in set` é
     O(1)). Devolve None se não houver nenhum duplicado.

2. `elementos_duplicados(lista: list) -> set`
   - Devolve um SET com TODOS os elementos que aparecem mais de
     uma vez (pode reusar a lógica da função anterior).

3. `palavras_em_comum(texto1: str, texto2: str) -> set`
   - Separa cada texto por espaços, transforma em sets e devolve a
     INTERSEÇÃO — palavras que estão nos dois textos.

Comportamento esperado:
    primeiro_duplicado([3, 5, 1, 3, 7])     # 3
    primeiro_duplicado([1, 2, 3])           # None
    elementos_duplicados([1, 2, 1, 3, 2])   # {1, 2}
    palavras_em_comum("oi cafe", "cafe leite")  # {'cafe'}

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def primeiro_duplicado(lista: list) -> int | None:
    ...


def elementos_duplicados(lista: list) -> set:
    ...


def palavras_em_comum(texto1: str, texto2: str) -> set:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(primeiro_duplicado([3, 5, 1, 3, 7]))
    print(primeiro_duplicado([1, 2, 3]))
    print(elementos_duplicados([1, 2, 1, 3, 2]))
    print(palavras_em_comum("oi cafe", "cafe leite"))