"""
EXERCÍCIO 26 - Relatório com Cache (avançado)

Tópicos: functools.cached_property
Aulas: 129-177 (avançado)

`functools.cached_property` transforma um método em propriedade
que calcula o valor UMA única vez: o resultado fica guardado no
`__dict__` da instância e as leituras seguintes são O(1), sem
recalcular. Perfeito para campos derivados caros (somatórios,
médias, agregações) sobre dados que não mudam.

1. Classe `Relatorio`:
   - `__init__(self, vendas: list[float]) -> None`:
     - Guarda `self.__vendas = list(vendas)` (CÓPIA defensiva —
       quem chamou não pode mutar o relatório por fora)
   - `@cached_property total(self) -> float`:
     - Retorna `sum(self.__vendas)`
   - `@cached_property media(self) -> float`:
     - Retorna `self.total / len(self.__vendas)` (reusa o cache do total)
   - `__repr__(self) -> str` retornando
     `Relatorio(vendas=[10.0, 20.0, 30.0])`

Comportamento esperado (fluxo de uso):
    r = Relatorio([10.0, 20.0, 30.0])
    r.total  # 60.0 (calcula e cacheia)
    r.total  # 60.0 (segunda leitura vem do __dict__ da instância)
    'total' in r.__dict__  # True (o cache fica no dicionário)
    del r.total
    r.total  # 60.0 (recalculado; o cache foi invalidado pelo del)

Observações:
  - A classe NÃO pode usar `__slots__`: `cached_property` depende
    do `__dict__` da instância para armazenar o valor
  - `media` chama `self.total`, não `sum` de novo — assim o total
    também não é recalculado
  - `del atributo` remove a entrada do `__dict__` e força o
    recálculo na próxima leitura
"""

from functools import cached_property


class Relatorio:
    def __init__(self, vendas: list[float]) -> None:
        ...

    @cached_property
    def total(self) -> float:
        ...

    @cached_property
    def media(self) -> float:
        ...

    def __repr__(self) -> str:
        ...