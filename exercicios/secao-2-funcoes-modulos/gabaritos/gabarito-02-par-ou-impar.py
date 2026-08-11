"""
Gabarito EXERCÍCIO 02 - Função Par ou Ímpar

Raciocínio sênior
-----------------
O gabarito protege o contrato com isinstance() ANTES de calcular:
um erro de tipo é capturado na porta de entrada, com mensagem clara,
em vez de quebrar o programa no meio (por exemplo, texto % 2 dessa
maneira nem executaria). O ternário devolve "Par" ou "Ímpar" — o
valor exato pedido no enunciado.
Alternativas descartadas: try/except em volta do cálculo (esconde o
erro e força erro genérico); bool como retorno (o enunciado pede str).
"""

ERRO_TIPO = "O argumento deve ser um inteiro"


def par_ou_impar(numero: int) -> str:
    """Retorna 'Par' ou 'Ímpar' conforme o número.

    Parametros
    ----------
    numero : int
        Número inteiro a ser classificado.

    Returns
    -------
    str
        'Par' se o número for par, 'Ímpar' se for ímpar.

    Raises
    ------
    TypeError
        Se o argumento não for int.

    Exemplos
    --------
    >>> par_ou_impar(6)
    'Par'
    >>> par_ou_impar(7)
    'Ímpar'
    >>> par_ou_impar(0)
    'Par'
    """
    if not isinstance(numero, int):
        raise TypeError(ERRO_TIPO)
    return "Par" if numero % 2 == 0 else "Ímpar"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(par_ou_impar(6))
    print(par_ou_impar(7))

# Onde você provavelmente divergiu:
# - retornou "PAR"/"IMPAR" em maiúsculas (o enunciado pede
#   "Par"/"Ímpar" com a capitalização exata)
# - converteu float para int silenciosamente (par_ou_impar(2.0) deve
#   levantar TypeError — aqui o contrato é rigoroso)
# - usou try/except no cálculo em vez de validar o tipo antes