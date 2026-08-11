"""
Gabarito EXERCÍCIO 27 - Descrever com singledispatch (functools.singledispatch)

Raciocínio sênior
-----------------
Em vez de uma funcao cheia de if/elif isinstance (que quebra a
cada tipo novo), singledispatch registra UM COMPORTAMENTO por tipo
e deixa o despacho com o interpretador: descrever() so conhece o
conceito "descrever"; cada registro (int, str, list, dict) tem a
propria forma. Tipo sem registro (3.14) cai na funcao base — esse
é o contrato do default: SEMPRE existe um caso generico valido,
entao a funcao nunca explode para tipos desconhecidos. Subclasses
herdam o registro do ancestral (bool cai em int), o que mantem
Liskov sem registros extras.
"""

from __future__ import annotations

from functools import singledispatch


@singledispatch
def descrever(valor) -> str:
    """Descreve qualquer valor: caso generico quando nao ha registro.

    Exemplos:
    >>> descrever(3.14)
    'generico: 3.14'
    >>> descrever(True)
    'numero True'
    """
    return f'generico: {valor}'


@descrever.register(int)
def _descrever_int(valor: int) -> str:
    """Descreve um inteiro.

    Exemplos:
    >>> descrever(42)
    'numero 42'
    """
    return f'numero {valor}'


@descrever.register(str)
def _descrever_str(valor: str) -> str:
    """Descreve um texto.

    Exemplos:
    >>> descrever('oi')
    'texto: oi'
    """
    return f'texto: {valor}'


@descrever.register(list)
def _descrever_list(valor: list) -> str:
    """Descreve uma lista pela quantidade de itens.

    Exemplos:
    >>> descrever([1, 2, 3])
    'lista com 3 itens'
    """
    return f'lista com {len(valor)} itens'


@descrever.register(dict)
def _descrever_dict(valor: dict) -> str:
    """Descreve um dicionario pela quantidade de chaves.

    Exemplos:
    >>> descrever({'a': 1})
    'dict com 1 chaves'
    """
    return f'dict com {len(valor)} chaves'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - escreveu if isinstance(valor, int): ... elif isinstance(valor,
#   str): ... e adicionaria mais um elif a cada tipo novo (o
#   singledispatch cresce por registro, o if cresce por gambiarra)
# - decorou TODAS as funcoes com @singledispatch em vez de usar a
#   .register da base (registros anexados = despacho unico)
# - esqueceu o caso default e matou o contrato do generico (tipo
#   desconhecido deveria ter saida, nao quebrar)
# - usou nome de funcao publica para os registros (por convencao
#   eles sao privados: _descrever_int etc. — so a "fachada"
#   descrever() é importada/exposta)