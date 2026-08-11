"""
Gabarito EXERCÍCIO 21 - Slots em Funcionario (memoria)

Raciocínio sênior
-----------------
A classe declara `__slots__ = ('nome', 'salario')` no corpo, o que
faz o Python substituir o `__dict__` de cada instância por um par
de descritores de slots: menos memória por objeto e atributos
inesperados viram AttributeError no momento da atribuição (bug
silencioso vira erro explícito). O `__init__` apenas preenche os
dois slots; `aumento_salario` lê e reescreve `self.salario` com o
cálculo percentual, que deve ser feito em float para não truncar
(3000.0 * 10 / 100 = 300.0). Como não há herança, o `__slots__`
vale direto (herança exigiria slots em cada nível da cadeia até
que o `__dict__` desaparecesse de vez). O `__repr__` usa `!r` para
cercar o nome com aspas simples, e `hasattr(f, '__dict__')` por
si só já prova a ausência do dicionário (e não retorna um
descritor falso — o atributo simplesmente não existe).
"""

from __future__ import annotations


class Funcionario:
    """Funcionario com slots: memoria enxuta e atributos fixos.

    Exemplos:
    >>> f = Funcionario('Ana', 3000.0)
    >>> f.nome
    'Ana'
    >>> f.salario
    3000.0
    >>> hasattr(f, '__dict__')
    False
    >>> f.cargo = 'x'
    Traceback (most recent call last):
    ...
    AttributeError: 'Funcionario' object has no attribute 'cargo' and no __dict__ for setting new attributes
    """

    __slots__ = ('nome', 'salario')

    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    def aumento_salario(self, percentual: float) -> None:
        """Aplica aumento percentual ao salario.

        Exemplos:
        >>> f = Funcionario('Ana', 3000.0)
        >>> f.aumento_salario(10)
        >>> f.salario
        3300.0
        """
        self.salario += self.salario * percentual / 100

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Funcionario('Ana', 3000.0)
        Funcionario(nome='Ana', salario=3000.0)
        """
        return f'Funcionario(nome={self.nome!r}, salario={self.salario!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - esqueceu os parenteses: `__slots__ = 'nome', 'salario'` funciona,
#   mas a tupla explicita documenta a intencao (evita confusao com string)
# - declarou `__slots__` dentro do __init__ (so vale no corpo da classe,
#   no momento da definicao do tipo)
# - usou `salario * (1 + percentual / 100)` e conferiu 3300 vs 3300.0:
#   o valor permanece float porque a base ja e float — o doctest exige
#   a saida exata 3300.0
# - tentou ler `f.__dict__` antes do hasattr (so existe em classes sem
#   slots; aqui o erro AttributeError jah e a prova de que nao existe)