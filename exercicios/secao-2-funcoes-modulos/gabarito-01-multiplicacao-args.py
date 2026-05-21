"""
Gabarito 01 - Função de Multiplicação com *args
"""


def multiplicar(*args: float) -> float:
    """Multiplica todos os argumentos recebidos.

    Se nenhum argumento for passado, retorna 1.0.

    Exemplos:
        >>> multiplicar(2, 3, 4)
        24.0
        >>> multiplicar()
        1.0
        >>> multiplicar(5.0)
        5.0
    """
    total = 1.0
    for numero in args:
        total *= numero
    return total
