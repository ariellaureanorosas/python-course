"""
EXERCÍCIO 28 - Tabuada Iterável (avançado)

Tópicos: iteradores em POO
Aulas: 129-177 (avançado)

Um objeto iterável em POO implementa `__iter__` (devolve o
iterador) e, quando ele próprio é o iterador, também `__next__` —
o protocolo da iteração. `for`, `list()` e `sorted` consomem o
objeto até ele levantar `StopIteration`. O truque do exercício é o
RESET: ao esgotar, o iterador volta ao ponteiro inicial, então o
mesmo objeto pode ser re-iterado.

1. Classe `Tabuada`:
   - `__init__(self, numero: int, vezes: int = 10) -> None`:
     - Guarda `self.__numero`, `self.__vezes` e `self.__atual = 0`
   - `__iter__(self) -> Tabuada` retornando `return self`
     (a instância é o próprio iterador)
   - `__next__(self) -> int`:
     - Se `self.__atual >= self.__vezes`:
       - Zera `self.__atual` (reset para re-iteração)
       - Levanta `StopIteration`
     - Senão:
       - Incrementa `self.__atual` e retorna `self.__numero * self.__atual`
       (multiplica pelo valor JÁ incrementado: começa em numero * 1)

Comportamento esperado (fluxo de uso):
    list(Tabuada(5))      # [5, 10, 15, 20, ..., 50]
    list(Tabuada(3, 3))   # [3, 6, 9]
    t = iter(Tabuada(2, 2))
    next(t)  # 2
    next(t)  # 4
    next(t)  # StopIteration (e o reset permite list(t) de novo)

Observações:
  - Um iterador esgotado NÃO reinicia sozinho: o reset manual no
    ramo do StopIteration é o que permite `list(t)` de novo
  - Retornar `self` em `__iter__` exige que o objeto carregue o
    estado da iteração (`__atual`)
  - Dica de robustez: se `vezes` for 0, a tabuada é vazia
"""


class Tabuada:
    def __init__(self, numero: int, vezes: int = 10) -> None:
        ...

    def __iter__(self) -> Tabuada:
        ...

    def __next__(self) -> int:
        ...