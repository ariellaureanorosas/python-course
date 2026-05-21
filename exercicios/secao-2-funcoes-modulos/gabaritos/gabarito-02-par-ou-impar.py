"""
Gabarito 02 - Função Par ou Ímpar
"""


def par_ou_impar(numero: int) -> str:
    """Retorna 'Par' se o número for par, 'Ímpar' caso contrário.

    Valida o tipo do argumento com isinstance().

    Exemplos:
        >>> par_ou_impar(2)
        'Par'
        >>> par_ou_impar(3)
        'Ímpar'
        >>> par_ou_impar(0)
        'Par'
    """
    if not isinstance(numero, int):
        raise TypeError("O argumento deve ser um inteiro")

    if numero % 2 == 0:
        return "Par"

    return "Ímpar"
