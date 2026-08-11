"""
Gabarito EXERCÍCIO 31 - Jogo de Cartas (capstone: slots + ordenação + iterável)

Raciocínio sênior
-----------------
O capstone amarra os topicos avancados numa modelagem unica,
cada um resolvendo um problema real: __slots__ corta o __dict__
de cada Carta — num baralho real seriam milhares de instancias
(maos, historicos) e a economia de memoria por instancia vira
economia total (troca por atributos fixos e erro imediato em
typo). total_ordering + __eq__/__lt__ dao ORDEM total ao dominio:
numero desempata pelo indice da tupla de naipes (copas < ouros <
paus < espadas), e o decorador deriva >, <=, >= sem reescrever
logica (sorted() so usa __lt__). O Baralho COMPOE 52 Cartas e
implementa o protocolo de colecao (__len__/__getitem__/__iter__):
sendo iteravel e indexavel, ele recebe sorted(), baralho[0],
fatiamento e for de graca, alem de delegar o embaralhamento ao
random.shuffle sobre a LISTA interna — o pacote de cartas vira
uma colecao de verdade, nao um objeto que "tem" dados.
"""

from __future__ import annotations

import random
from collections.abc import Iterator
from functools import total_ordering


@total_ordering
class Carta:
    """Carta de baralho com slots e ordem total por numero/naipe."""

    __slots__ = ('numero', 'naipe')

    NAIPES = ('copas', 'ouros', 'paus', 'espadas')

    def __init__(self, numero: int, naipe: str) -> None:
        if numero not in range(1, 14):
            raise ValueError(f'numero deve estar entre 1 e 13: {numero}')
        if naipe not in self.NAIPES:
            raise ValueError(f'naipe invalido: {naipe}')
        self.numero = numero
        self.naipe = naipe

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Carta(7, 'ouros')
        Carta(7, 'ouros')
        """
        return f'Carta({self.numero}, {self.naipe!r})'

    def __eq__(self, outro: object) -> bool:
        """Igualdade por numero E naipe (mesma classe).

        Exemplos:
        >>> Carta(7, 'ouros') == Carta(7, 'ouros')
        True
        >>> Carta(7, 'ouros') == Carta(7, 'paus')
        False
        >>> Carta(14, 'ouros')
        Traceback (most recent call last):
        ...
        ValueError: numero deve estar entre 1 e 13: 14
        >>> Carta(1, 'pipa')
        Traceback (most recent call last):
        ...
        ValueError: naipe invalido: pipa
        """
        if not isinstance(outro, Carta):
            return NotImplemented
        return self.numero == outro.numero and self.naipe == outro.naipe

    def __lt__(self, outro: Carta) -> bool:
        """Ordena por numero; empate desempatado pelo naipe (tupla).

        Exemplos:
        >>> Carta(5, 'espadas') < Carta(7, 'ouros')
        True
        >>> Carta(7, 'ouros') < Carta(7, 'copas')
        False
        >>> sorted([Carta(7, 'paus'), Carta(1, 'espadas'), Carta(1, 'copas')])
        [Carta(1, 'copas'), Carta(1, 'espadas'), Carta(7, 'paus')]
        >>> Carta(7, 'ouros') > Carta(5, 'espadas')
        True
        >>> Carta(7, 'ouros') >= Carta(7, 'ouros')
        True
        >>> hasattr(Carta(1, 'copas'), '__dict__')
        False
        """
        if self.numero != outro.numero:
            return self.numero < outro.numero
        return self.NAIPES.index(self.naipe) < self.NAIPES.index(outro.naipe)


class Baralho:
    """Baralho padrao de 52 cartas: indexavel, iteravel e embaralhavel."""

    def __init__(self) -> None:
        self.__cartas = [
            Carta(n, naipe)
            for n in range(1, 14)
            for naipe in Carta.NAIPES
        ]

    def __len__(self) -> int:
        """Quantidade de cartas.

        Exemplos:
        >>> len(Baralho())
        52
        """
        return len(self.__cartas)

    def __getitem__(self, indice: int) -> Carta:
        """Delega a indexacao para a lista interna.

        Exemplos:
        >>> baralho = Baralho()
        >>> baralho[0]
        Carta(1, 'copas')
        >>> baralho[-1]
        Carta(13, 'espadas')
        >>> baralho[52]
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
        """
        return self.__cartas[indice]

    def __iter__(self) -> Iterator[Carta]:
        """Itera pelas cartas na ordem atual.

        Exemplos:
        >>> baralho = Baralho()
        >>> sorted(baralho)[:3]
        [Carta(1, 'copas'), Carta(1, 'ouros'), Carta(1, 'paus')]
        """
        return iter(self.__cartas)

    def embaralhar(self) -> None:
        """Embaralha a lista interna in-place.

        Exemplos:
        >>> import random
        >>> random.seed(0)
        >>> baralho = Baralho()
        >>> baralho.embaralhar()
        >>> len(baralho)
        52
        >>> sorted(baralho)[0]
        Carta(1, 'copas')
        """
        random.shuffle(self.__cartas)

    @property
    def cartas(self) -> list[Carta]:
        """Retorna uma copia da lista de cartas.

        Exemplos:
        >>> len(Baralho().cartas)
        52
        """
        return list(self.__cartas)

    def __repr__(self) -> str:
        """Representacao textual resumida em quantidade.

        Exemplos:
        >>> Baralho()
        Baralho(cartas=52)
        """
        return f'Baralho(cartas={len(self.__cartas)})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - definiu __hash__ junto com __eq__ (com slots e comparação rica,
#   o problema nao pede dict/set de Carta; definir __hash__ por
#   numero/naipe vazaria o contrato e deixaria a comparacao
#   incoerente com a identidade)
# - desempatou naipe com if/elif de strings em vez da TUPLA
#   ordenada (NAIPES.index() deriva a ordem de uma fonte unica)
# - implementou __lt__ usando a TUPLA DO ENUNCIADO? não — a ordem
#   copas < ouros < paus < espadas só existe porque a tupla é
#   declarada nessa ordem; reordena-la muda o jogo inteiro
# - esqueceu @total_ordering e escreveu >, <=, >= à mão (o
#   decorador deriva os tres do par __eq__/__lt__; duplicar
#   comparacao é onde simetria/transitividade divergem)
# - devolveu self.__cartas na property cartas (o caller podia
#   remover/duplicar cartas sem passar por embaralhar; list() isola)
# - usou random.seed() sem importar random antes no doctest (cada
#   doctest roda num namespace proprio; o import no topo da
#   module nao povoia o namespace do exemplo)