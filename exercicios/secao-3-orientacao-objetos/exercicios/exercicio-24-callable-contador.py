"""
EXERCÍCIO 24 - Contador com __call__ (callables)

Tópicos: __call__
Aulas: 129-177 (callable-objeto)

Implementar `__call__` torna a INSTÂNCIA chamável como uma função:
`c()` executa `c.__call__()`. É o que distingue instâncias que
guardam estado de funções puras — o contador dessa classe é um
exemplo clássico: a contagem vive no objeto e avança a cada
chamada, sem variáveis globais.

1. Classe `Contador`:
   - `__init__(self, inicio: int = 0) -> None`
     guarda `self.valor = inicio`
   - `__call__(self) -> int`
     incrementa `self.valor` em 1 e RETORNA o novo valor
   - `__repr__(self) -> str` retornando `Contador(valor=6)`

Comportamento esperado (fluxo de uso):
    c = Contador(5)
    c()  # 6 (incrementou e retornou)
    c()  # 7
    c.valor  # 7 (estado vive no objeto)
    callable(c)  # True (instância é chamável)
    d = Contador()
    d()  # 1 (começa em 0)

Observações:
  - A assinatura de `__call__` define como a instância é invocada:
    se precisar de argumentos, basta adicioná-los na assinatura
  - `callable(objeto)` retorna True justamente quando `__call__`
    existe na classe
  - O estado persiste entre chamadas porque ele mora no próprio
    objeto (cada instância tem seu próprio valor)
"""


class Contador:
    def __init__(self, inicio: int = 0) -> None:
        ...

    def __call__(self) -> int:
        ...

    def __repr__(self) -> str:
        ...