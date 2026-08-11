"""
Gabarito EXERCÍCIO 22 - Configuracao Singleton (padrão de projeto)

Raciocínio sênior
-----------------
O singleton depende de estagios: `__new__` roda antes de `__init__`
e decide a identidade — se `cls._instancia` ainda for None, aloca
com `super().__new__(cls)` e guarda a referencia na classe; nas
chamadas seguintes devolve a mesma instancia sem alocar nada. O
`__init__` nao pode rodar de novo, senao `Configuracao('outro',
9000)` sobrescreveria host/porta da instancia unica — por isso a
flag de classe `_inicializada` bloqueia a reconfiguracao (o gasto
do `__init__` em chamadas subsequentes e inocuo, mas o estado
original precisa sobreviver). As leituras sao diretas (nao ha
property neste exercicio), o `__repr__` espelha o estado real com
`!r`, e a prova final `c1 is c2` usa identidade, nao igualdade.
"""

from __future__ import annotations


class Configuracao:
    """Configuracao global unica (singleton por __new__).

    Exemplos:
    >>> c1 = Configuracao()
    >>> c2 = Configuracao()
    >>> c1 is c2
    True
    >>> c1.host
    'localhost'
    >>> c1.porta
    8000
    >>> c3 = Configuracao('outro', 9000)
    >>> c3 is c1
    True
    >>> c1.host
    'localhost'
    >>> c1.porta
    8000
    >>> c1
    Configuracao(host='localhost', porta=8000)
    """

    _instancia = None
    _inicializada = False

    def __new__(cls, *args, **kwargs) -> Configuracao:
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, host: str = 'localhost', porta: int = 8000) -> None:
        if not type(self)._inicializada:
            self.host = host
            self.porta = porta
            type(self)._inicializada = True

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Configuracao()
        Configuracao(host='localhost', porta=8000)
        """
        return f'Configuracao(host={self.host!r}, porta={self.porta!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - esqueceu a flag `_inicializada`: sem ela o __init__ roda de novo
#   a cada chamada e `Configuracao('outro', 9000)` apaga a config
#   original da instancia unica
# - checou `self._inicializada` em vez de `type(self)._inicializada`
#   (funciona aqui, mas em heranca a flag da classe filha seria ignorada)
# - comparou com `==` no teste em vez de `is` (o teste correto do
#   singleton e a identidade de objeto)
# - esqueceu o return dentro do if no __new__ e retornou None
#   implicitamente em alguma regra (aqui o else e desnecessario,
#   mas o return unico e obrigatorio)