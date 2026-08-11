"""
Gabarito EXERCÍCIO 04 - Closure Multiplicador

Raciocínio sênior
-----------------
O mesmo padrão do exercício 03: a fábrica fixa multiplicador no
closure e devolve uma função nova. Testar com dobro e triplo
mostra que closures distintos coexistem sem interferência — cada
função criada tem seu próprio "estado congelado".
Alternativas descartadas: função com dois parâmetros
(multiplicar(n, m) — não é closure; o enunciado pede explicitamente
que criar_multiplicador RETORNE uma função).
"""


def criar_multiplicador(multiplicador: int):
    """Retorna uma função que multiplica um número pelo multiplicador.

    Parametros
    ----------
    multiplicador : int
        Fator fixado no closure.

    Returns
    -------
    Callable[[int], int]
        Função que recebe um número e retorna número * multiplicador.

    Exemplos
    --------
    >>> dobro = criar_multiplicador(2)
    >>> dobro(5)
    10
    >>> dobro(0)
    0
    >>> triplo = criar_multiplicador(3)
    >>> triplo(4)
    12
    """
    def multiplicar(numero: int) -> int:
        return numero * multiplicador
    return multiplicar


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    dobro = criar_multiplicador(2)
    print(dobro(5))

# Onde você provavelmente divergiu:
# - definiu function interna com o mesmo nome da externa
#   (multiplicador → multiplicar dentro), o que gera dobra de nomes
#   e confusão na leitura; aqui a interna é multiplicar e a externa
#   criar_multiplicador
# - esqueceu o return da função interna (retornou o resultado da
#   multiplicação em vez de retornar a função)
# - testou apenas um multiplicador (dobro e triplo mostram que os
#   closures são independentes)