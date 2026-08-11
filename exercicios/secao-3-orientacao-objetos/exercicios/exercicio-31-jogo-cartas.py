"""
EXERCÍCIO 31 - Jogo de Cartas (capstone)

Tópicos: __slots__, comparação rica, iterável, composição
Aulas: 129-177 (capstone)

O exercício final amarra os tópicos avançados da seção numa
única modelagem: `Carta` usa `__slots__` (memória enxuta para
muitas instâncias), comparação rica com `@total_ordering`
(ordenar cartas/hands), e `Baralho` COMPÕE 52 cartas e é
iterável/indeXável (protocolos de coleção: `__len__`,
`__getitem__`, `__iter__`).

1. Classe `Carta`:
   - `__slots__ = ('numero', 'naipe')`
   - `__init__(self, numero: int, naipe: str) -> None`:
     - Valida `numero` em 1..13 e `naipe` em
       ('copas', 'ouros', 'paus', 'espadas'); senão `ValueError`
   - `__repr__(self) -> str` retornando `Carta(7, 'ouros')`
   - `__eq__(self, outro) -> bool`:
     - Mesma classe, mesmo numero e mesmo naipe
   - `__lt__(self, outro) -> bool`:
     - Compara por numero; empate desempata pelo naipe na ordem
       copas < ouros < paus < espadas (use uma TUPLA ordenada de naipes)
   - Decorada com `@total_ordering` (deriva >, <=, >= de == e <)
   - NÃO defina `__hash__` (não há dict/set de Carta no problema)

2. Classe `Baralho`:
   - `__init__(self) -> None`: composição —
     `self.__cartas = [Carta(n, naipe) for n in range(1, 14) for naipe in (...)]`
     (52 cartas em ordem fixa: números crescentes; naipes na ordem da tupla)
   - `__len__(self) -> int` retornando 52
   - `__getitem__(self, indice: int) -> Carta` delegando para `self.__cartas[indice]`
   - `__iter__(self)` retornando `iter(self.__cartas)`
   - `embaralhar(self) -> None` chamando `random.shuffle(self.__cartas)`
   - `@property cartas -> list[Carta]` (devolve CÓPIA)
   - `__repr__(self) -> str` retornando `Baralho(cartas=52)`

Comportamento esperado (fluxo de uso):
    baralho = Baralho()
    len(baralho)  # 52
    baralho[0]  # Carta(1, 'copas')
    baralho[-1]  # Carta(13, 'espadas')
    sorted(baralho)[:3]  # [Carta(1, 'copas'), Carta(1, 'ouros'), Carta(1, 'paus')]
    Carta(7, 'ouros') > Carta(5, 'espadas')  # True
    Carta(7, 'ouros') == Carta(7, 'ouros')  # True
    hasattr(Carta(1, 'copas'), '__dict__')  # False (__slots__ ativo)
    random.seed(0)
    baralho.embaralhar()
    sorted(baralho)[0]  # Carta(1, 'copas') (ordenação restaura o mínimo)

Observações:
  - `__slots__` troca o `__dict__` por descritores de atributo
    fixos: menos memória por instância, mas atributos fora da lista
    falham com AttributeError
  - `@total_ordering` exige `__eq__` + PELO MENOS uma comparação
    (`__lt__`) e completa o restante
  - Importe `import random` e `from functools import total_ordering`
  - Só `__lt__` basta para `sorted()`; `>` e `>=` vêm do
    total_ordering; nunca defina `__lt__` que não seja coerente
    com `__eq__` (transitividade, simetria)
"""

import random
from functools import total_ordering


@total_ordering
class Carta:
    __slots__ = ('numero', 'naipe')

    def __init__(self, numero: int, naipe: str) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __eq__(self, outro: object) -> bool:
        ...

    def __lt__(self, outro: Carta) -> bool:
        ...


class Baralho:
    def __init__(self) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, indice: int) -> Carta:
        ...

    def __iter__(self):
        ...

    def embaralhar(self) -> None:
        ...

    @property
    def cartas(self) -> list[Carta]:
        ...

    def __repr__(self) -> str:
        ...