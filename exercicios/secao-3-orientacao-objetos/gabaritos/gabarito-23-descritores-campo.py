"""
Gabarito EXERCÍCIO 23 - Descritor Campo (acesso validado)

Raciocínio sênior
-----------------
O descritor concentra a validacao de tipo num unico lugar:
`__set__` so libera a escrita se `isinstance(valor, self.tipo)`
passar, senao levanta TypeError com o nome do atributo — e a
classe `Pessoa` ganha checagem sem escrever setter para cada
campo. `__set_name__` roda na criacao da classe e grava o nome do
atributo (evita o segundo parametro redundante e a magica de
string). O valor vivo fica no `__dict__` da instancia, nunca no
descritor (senao todos os objetos compartilhariam o mesmo valor).
`__get__` devolve o proprio descritor quando `instancia is None`
(acesso via classe, usado por introspeccao) e o valor do dict
quando ha instancia; o `__init__` de Pessoa passa por `self.nome`
e `self.idade` justamente para cair no `__set__` e validar ate a
construcao.
"""

from __future__ import annotations


class Campo:
    """Descritor de dados que valida o tipo na atribuicao.

    Exemplos:
    >>> p = Pessoa('Ana', 30)
    >>> p.nome
    'Ana'
    >>> p.nome = 'Bia'
    >>> p.nome
    'Bia'
    >>> p.nome = 123
    Traceback (most recent call last):
    ...
    TypeError: nome deve ser str
    >>> p.idade = 'trinta'
    Traceback (most recent call last):
    ...
    TypeError: idade deve ser int
    """

    def __init__(self, tipo: type = object) -> None:
        self.tipo = tipo

    def __set_name__(self, owner: type, nome: str) -> None:
        self.nome = nome

    def __get__(self, instancia, owner):
        if instancia is None:
            return self
        return instancia.__dict__.get(self.nome)

    def __set__(self, instancia, valor) -> None:
        if not isinstance(valor, self.tipo):
            raise TypeError(f'{self.nome} deve ser {self.tipo.__name__}')
        instancia.__dict__[self.nome] = valor


class Pessoa:
    """Pessoa com campos validados pelo descritor Campo.

    Exemplos:
    >>> p = Pessoa('Ana', 30)
    >>> p
    Pessoa(nome='Ana', idade=30)
    """

    nome = Campo(str)
    idade = Campo(int)

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Pessoa('Ana', 30)
        Pessoa(nome='Ana', idade=30)
        """
        return f'Pessoa(nome={self.nome!r}, idade={self.idade!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - guardou o valor dentro do proprio descritor (self.valor = valor):
#   descritor e atributo de CLASSE — todas as instancias dividiriam
#   o mesmo dado; o certo e gravar no __dict__ da instancia
# - validou com type(valor) is self.tipo, que rejeita subclasses
#   legitimas (ex.: bool e int); isinstance e a checagem correta
# - esqueceu o `__set_name__` e pediu o nome na mao (`Campo('nome',
#   str)`) — ou guardou um nome errado em atributos reutilizados
# - no __get__ retornou instancia.__dict__[self.nome], que levanta
#   KeyError antes da primeira atribuicao; .get() devolve None