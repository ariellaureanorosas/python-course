"""
Gabarito EXERCÍCIO 25 - Ordenação de Jogadores (comparação rica)

Raciocínio sênior
-----------------
Decorar com `@total_ordering` deixa o __lt__ como unica regra de
ordem e deriva o resto (incluindo o `>` usado no doctest) a
partir de __eq__ + __lt__. O __eq__ exige mesma classe E nome e
pontos iguais, pois `==` entre objetos de tipos diferentes nao
faz sentido. O __lt__ compara pontos e, em empate, recorre ao
nome como desempate determinístico — sem isso o sorted devolveria
ordem arbitrária (dependente do hash) para jogadores com a mesma
pontuacao. Retornar False (em vez de NotImplemented) para outro
tipo preserva o comportamento seguro no sorted. Nomes ASCII nos
doctests garantem saidas fidedignas ao repr.
"""

from __future__ import annotations

from functools import total_ordering


@total_ordering
class Jogador:
    """Jogador ordenavel por pontos (desempate por nome).

    Exemplos:
    >>> jogadores = [
    ...     Jogador('Ana', 50),
    ...     Jogador('Bia', 80),
    ...     Jogador('Cadu', 60),
    ... ]
    >>> sorted(jogadores)
    [Jogador('Ana', 50), Jogador('Cadu', 60), Jogador('Bia', 80)]
    >>> max(jogadores)
    Jogador('Bia', 80)
    >>> min(jogadores)
    Jogador('Ana', 50)
    >>> Jogador('Bia', 80) > Jogador('Ana', 50)
    True
    >>> Jogador('Ana', 50) == Jogador('Ana', 50)
    True
    >>> Jogador('Ana', 50) == Jogador('Bia', 80)
    False
    """

    def __init__(self, nome: str, pontos: int) -> None:
        self.nome = nome
        self.pontos = pontos

    def __eq__(self, outro) -> bool:
        """True se o outro jogador tiver nome e pontos iguais.

        Exemplos:
        >>> Jogador('Ana', 50) == Jogador('Ana', 50)
        True
        >>> Jogador('Ana', 50) == Jogador('Bia', 50)
        False
        """
        if not isinstance(outro, Jogador):
            return False
        return self.nome == outro.nome and self.pontos == outro.pontos

    def __lt__(self, outro) -> bool:
        """True se este jogador tiver menos pontos; empate por nome.

        Exemplos:
        >>> Jogador('Cadu', 60) < Jogador('Bia', 80)
        True
        >>> Jogador('Bia', 80) < Jogador('Cadu', 60)
        False
        """
        if not isinstance(outro, Jogador):
            return False
        if self.pontos != outro.pontos:
            return self.pontos < outro.pontos
        return self.nome < outro.nome

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Jogador('Ana', 50)
        Jogador('Ana', 50)
        """
        return f'Jogador({self.nome!r}, {self.pontos!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - implementou os 6 metodos de comparacao na mao (o decorator
#   @total_ordering deriva os que faltam a partir de __eq__ + __lt__)
# - no __eq__ aceitou tipos diferentes ou comparou por referencia
#   (a regra exige mesma classe E nome/pontos iguais)
# - esqueceu o desempate por nome no empate de pontos: jogadores com
#   60 pontos ficariam em ordem arbitraria dentro do sorted
# - usou nomes com acento nos exemplos (ex.: 'Cadu') e viu o repr
#   do doctest falhar por codificacao — prefira ASCII nos dados)