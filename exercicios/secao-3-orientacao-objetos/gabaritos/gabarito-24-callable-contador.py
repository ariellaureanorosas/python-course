"""
Gabarito EXERCÍCIO 24 - Contador com __call__ (callables)

Raciocínio sênior
-----------------
A classe vira um callable porque `__call__` redefine o protocolo
de invocacao: `c()` executa `c.__call__()` e o estado da contagem
vive no atributo `self.valor` — entre chamadas nada se perde,
porque cada instancia carrega seu proprio contador. O retorno de
`__call__` deve ser o valor JAH incrementado (o fluxo esperado e
6, 7, 7...), e o `__repr__` precisa espelhar o momento exato do
estado para os doctests: `Contador(valor=6)`. O default `inicio=0`
cobre o segundo cenário (`Contador()` chama a 1 numa instancia
fresca), e a funcao embutida `callable` devolve True justamente
porque a classe possui `__call__` — a prova concisa de que o
objeto pode ser usado como funcao.
"""

from __future__ import annotations


class Contador:
    """Contador chamavel: cada chamada incrementa e devolve o valor.

    Exemplos:
    >>> c = Contador(5)
    >>> c()
    6
    >>> c()
    7
    >>> c.valor
    7
    >>> callable(c)
    True
    >>> c
    Contador(valor=7)
    """

    def __init__(self, inicio: int = 0) -> None:
        self.valor = inicio

    def __call__(self) -> int:
        """Incrementa o valor em 1 e retorna o novo valor.

        Exemplos:
        >>> c = Contador()
        >>> c()
        1
        """
        self.valor += 1
        return self.valor

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Contador(5)
        Contador(valor=5)
        """
        return f'Contador(valor={self.valor!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - retornou o valor ANTES de incrementar (o contrato pede o novo
#   valor: 6 na primeira chamada a partir de 5)
# - usou uma variavel global no lugar do atributo (com instancias
#   diferentes o contador vazaria; o estado tem que estar no objeto)
# - esqueceu o default `inicio=0` e quebrou o segundo cenario
# - no doctest esperou `0` na primeira chamada de um Contador()
#   (a sequencia e começa em 0 e a chamada devolve 1)