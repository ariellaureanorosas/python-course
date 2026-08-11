"""
Gabarito EXERCÍCIO 28 - Tabuada Iterável (iteradores em POO)

Raciocínio sênior
-----------------
O protocolo de iteracao pede duas respostas: __iter__ (quem
fornece o iterador) e __next__ (o proximo valor ou StopIteration).
Fazer a propria instancia ser o iterador (return self) concentra o
estado em __atual, mas cria uma responsabilidade extra: quando o
fluxo esgota, o ponteiro PRECISA voltar a zero no mesmo ramo do
StopIteration — so assim list(t) de novo devolve a sequencia
completa (iterador com "reset implicito"). A multiplicacao usa o
valor JA incrementado (1..vezes), o que elimina a condicao "a
primeira chamada retorna 0": a tabuada comeca em numero * 1 e nao
em numero * 0.
"""

from __future__ import annotations


class Tabuada:
    """Tabuada iteravel: percorre numero * 1 ate numero * vezes."""

    def __init__(self, numero: int, vezes: int = 10) -> None:
        self.__numero = numero
        self.__vezes = vezes
        self.__atual = 0

    def __iter__(self) -> Tabuada:
        """Devolve o proprio objeto (ele e o iterador).

        Exemplos:
        >>> iter(Tabuada(3, 3)) is not None
        True
        """
        return self

    def __next__(self) -> int:
        """Devolve o proximo multiplo ou sinaliza o fim da iteracao.

        Exemplos:
        >>> list(Tabuada(5))
        [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        >>> list(Tabuada(3, 3))
        [3, 6, 9]
        >>> list(Tabuada(7, 0))
        []
        >>> t = iter(Tabuada(2, 2))
        >>> next(t)
        2
        >>> next(t)
        4
        >>> next(t)
        Traceback (most recent call last):
        ...
        StopIteration
        >>> list(t)
        [2, 4]
        """
        if self.__atual >= self.__vezes:
            self.__atual = 0
            raise StopIteration

        self.__atual += 1
        return self.__numero * self.__atual


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - retornou numero * self.__atual ANTES de incrementar (a tabuada
#   comecava em 0; incremente e depois multiplique)
# - testou `== self.__vezes` em vez de `>=` (a sequencia perdia o
#   ultimo multiplo; `>=` cobre o caso vezes=0 tambem)
# - nao fez o reset de __atual no StopIteration (o iterador
#   esgotava para sempre; list(t) devolvia [] na segunda passada)
# - implementou __iter__ devolvendo iter(range(...)) — valido se
#   forcasse a iteracao por for, mas o enunciado pede "a instancia
#   e o iterador" (return self) e o doctest next(t) exige isso