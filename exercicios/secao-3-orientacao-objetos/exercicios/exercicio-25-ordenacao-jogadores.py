"""
EXERCÍCIO 25 - Ordenação de Jogadores (comparação rica)

Tópicos: comparação rica, functools.total_ordering
Aulas: 129-177 (comparacao-rica)

`sorted()`, `max()` e `min()` precisam comparar objetos entre si.
A comparação rica são os métodos `__eq__`, `__lt__`, `__le__`,
`__gt__`, `__ge__` e `__ne__`. Escrever os seis é tedioso — o
decorador `@total_ordering` deriva os que faltam a partir de
`__eq__` e `__lt__` sozinhos.

1. Classe `Jogador` decorada com `@total_ordering`:
   - `__init__(self, nome: str, pontos: int) -> None`
     guarda os dois atributos
   - `__eq__(self, outro) -> bool`
     True se `self.__class__ is type(outro)` E nome e pontos iguais
   - `__lt__(self, outro) -> bool`
     True se pontos menor; em caso de empate, compara por nome
     (desempate alfabético)
   - `__repr__(self) -> str` retornando `Jogador('Ana', 50)`

Comportamento esperado (fluxo de uso):
    jogadores = [
        Jogador('Ana', 50),
        Jogador('Bia', 80),
        Jogador('Cadu', 60),
    ]
    sorted(jogadores)  # [Jogador('Ana', 50), Jogador('Cadu', 60), Jogador('Bia', 80)]
    max(jogadores)  # Jogador('Bia', 80)
    min(jogadores)  # Jogador('Ana', 50)
    Jogador('Ana', 50) == Jogador('Ana', 50)  # True
    Jogador('Bia', 80) > Jogador('Ana', 50)  # True (via total_ordering)

Observações:
  - `@total_ordering` vem de `functools` e exige `__eq__` + pelo
    menos `__lt__` (ou `__le__`); o resto é derivado
  - Comparar com outro tipo: retorne False (ou NotImplemented) —
    senão `sorted` misturado com números quebra
  - Sem o desempate por nome, jogadores com pontos iguais ficam
    em ordem arbitrária dentro do sorted
"""

from functools import total_ordering


@total_ordering
class Jogador:
    def __init__(self, nome: str, pontos: int) -> None:
        ...

    def __eq__(self, outro) -> bool:
        ...

    def __lt__(self, outro) -> bool:
        ...

    def __repr__(self) -> str:
        ...