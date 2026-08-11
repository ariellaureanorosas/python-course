"""
EXERCÍCIO 33 - Status de Pedido com Enum (enum/metaclasses)

Tópicos: Enum, auto(), máquina de estados simples
Aulas: 172 (enum-metaclasses)

`Enum` cria um conjunto FECHADO de constantes nomeadas: o status de
um pedido nunca pode ser uma string solta ('pago' vs 'Pago') — só
existem os membros definidos, com `.name` e `.value`. Uma máquina
de estados (pedido avançando PENDENTE → PAGO → ENVIADO → ENTREGUE)
é o uso clássico.

1. Enum `PedidoStatus(Enum)` com `auto()`:
   - membros na ordem: `PENDENTE`, `PAGO`, `ENVIADO`, `ENTREGUE`,
     `CANCELADO`

2. Classe `Pedido`:
   - `__init__(self, numero: int) -> None`: guarda `numero` e inicia
     `status = PedidoStatus.PENDENTE`
   - `pagar(self) -> bool`: se PENDENTE vira PAGO e retorna True;
     senão retorna False
   - `cancelar(self) -> bool`: se PENDENTE vira CANCELADO e retorna
     True; senão retorna False
   - `avancar(self) -> None`: anda uma etapa (PENDENTE→PAGO→ENVIADO→
     ENTREGUE); em ENTREGUE ou CANCELADO levanta
     `ValueError('pedido nao pode avancar')`
   - `__repr__(self) -> str`: `Pedido(1, PedidoStatus.PAGO)` (mostra
     `PedidoStatus.<nome>`)

Comportamento esperado (fluxo de uso):
    PedidoStatus.PAGO.name     # 'PAGO'
    PedidoStatus.PAGO.value    # 2  (auto() começa em 1)
    list(PedidoStatus)         # todos os membros na ordem definida

    p = Pedido(1)
    p.status                   # <PedidoStatus.PENDENTE: 1>
    p.pagar()                  # True
    p.pagar()                  # False (já pago)
    p.status.name              # 'PAGO'
    p.avancar()
    p.status.name              # 'ENVIADO'
    p.avancar()
    p.avancar()                # ValueError: pedido nao pode avancar
    repr(p)                    # 'Pedido(1, PedidoStatus.ENTREGUE)'

    c = Pedido(2)
    c.cancelar()               # True
    c.cancelar()               # False
    c.status.name              # 'CANCELADO'

Observações:
  - `auto()` atribui 1, 2, 3... na ordem dos membros
  - Comparar status SEMPRE pelo Enum (`p.status == PedidoStatus.PAGO`),
    nunca por string
  - O `repr` do Enum é `<PedidoStatus.PENDENTE: 1>` — use isso nos
    seus comentários de teste
"""

from enum import Enum, auto


class PedidoStatus(Enum):
    ...


class Pedido:
    def __init__(self, numero: int) -> None:
        ...

    def pagar(self) -> bool:
        ...

    def cancelar(self) -> bool:
        ...

    def avancar(self) -> None:
        ...

    def __repr__(self) -> str:
        ...