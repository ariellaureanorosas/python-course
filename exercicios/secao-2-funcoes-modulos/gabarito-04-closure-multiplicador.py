"""
Gabarito 04 - Closure Multiplicador
"""


def criar_multiplicador(multiplicador: int):
    """Retorna uma função que multiplica qualquer número pelo multiplicador.

    Exemplos:
        >>> dobro = criar_multiplicador(2)
        >>> dobro(5)
        10
        >>> triplo = criar_multiplicador(3)
        >>> triplo(4)
        12
    """
    def multiplicar(numero: int) -> int:
        return numero * multiplicador

    return multiplicar
