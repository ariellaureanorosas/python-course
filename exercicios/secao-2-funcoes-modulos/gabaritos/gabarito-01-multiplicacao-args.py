"""
Gabarito EXERCÍCIO 01 - Função de Multiplicação com *args

Raciocínio sênior
-----------------
*args reúne todos os argumentos posicionais em uma tupla — a validação
percorre essa tupla e o reduce acumula o produto. O valor inicial 1.0
é o "elemento neutro" da multiplicação: é o que garante que *args vazio
devolva 1.0 (nenhum argumento = produto vazio = 1.0).
Alternativas descartadas: laço for com acumulador e loop aninhado —
funciona, mas reduce expressa exatamente "acumular um produto" sem
estado mutável; validação dentro do reduce (lambda enxuto) esconderia
o erro de tipo no meio do cálculo.
"""

from functools import reduce


def multiplicar(*args: float) -> float:
    """Multiplica todos os argumentos recebidos.

    Parametros
    ----------
    *args : float
        Valores a serem multiplicados.

    Returns
    -------
    float
        Produto de todos os argumentos. Retorna 1.0 se nenhum
        for passado.

    Raises
    ------
    TypeError
        Se algum argumento não for int ou float.

    Exemplos
    --------
    >>> multiplicar(2, 3, 4)
    24.0
    >>> multiplicar()
    1.0
    >>> multiplicar(5.0)
    5.0
    """
    for numero in args:
        if not isinstance(numero, (int, float)):
            raise TypeError(
                f"Argumento inválido: {numero!r}. "
                "Todos os argumentos devem ser int ou float."
            )

    return reduce(lambda a, b: a * b, args, 1.0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(multiplicar(2, 3, 4))
    print(multiplicar())
    print(multiplicar(5.0))

# Onde você provavelmente divergiu:
# - fez um for com multiplicacao = 1.0 e acumulou — funciona, mas o
#   init 1.0 no reduce é o "elemento neutro" da multiplicação e a
#   leitura fica declarativa
# - não validou os tipos antes do reduce (aqui a validação ocorre
#   ANTES, porque o reduce com lambda curto não tem onde encaixar o
#   erro de forma legível)
# - retornou int quando não passou nada (0 em vez de 1.0 — o produto
#   vazio é 1.0, não 0)