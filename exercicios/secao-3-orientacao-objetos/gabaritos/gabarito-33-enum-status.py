"""
Gabarito EXERCÍCIO 33 - Status de Pedido com Enum (enum/metaclasses)

Raciocínio sênior
-----------------
O status e um conjunto FECHADO de estados: Enum modela isso de
forma exata, enquanto strings soltas ('pago', 'Pago', 'pago ')
seriam N estados compativeis que o == não distingue. auto() garante
valores sequenciais sem voce numerar na mao. A maquina de estados
vira dois metodos: `avancar` percorre a lista de membros pelo indice
(itens de Enum sao ordenados como definidos), e `cancelar` so
funciona do estado inicial — estados nao transicionaveis devolvem
False em vez de levantar, preservando o fluxo do chamador que decide
o que mostrar. O repr usa `PedidoStatus.{status.name}` porque o
repr de membro (`<PedidoStatus.PAGO: 2>`) e util para log, mas o
repr do pedido precisa ser legivel por humanos.
"""

from __future__ import annotations

from enum import Enum, auto


class PedidoStatus(Enum):
    """Estados possiveis de um pedido.

    Exemplos:
    >>> PedidoStatus.PAGO.name
    'PAGO'
    >>> PedidoStatus.PAGO.value
    2
    >>> [membro.name for membro in PedidoStatus]
    ['PENDENTE', 'PAGO', 'ENVIADO', 'ENTREGUE', 'CANCELADO']
    """

    PENDENTE = auto()
    PAGO = auto()
    ENVIADO = auto()
    ENTREGUE = auto()
    CANCELADO = auto()


class Pedido:
    """Pedido com maquina de estados guiada por Enum.

    Exemplos:
    >>> p = Pedido(1)
    >>> p.status
    <PedidoStatus.PENDENTE: 1>
    >>> p.pagar()
    True
    >>> p.pagar()
    False
    >>> p.status.name
    'PAGO'
    >>> p.avancar()
    >>> p.status.name
    'ENVIADO'
    >>> p.avancar()
    >>> p.avancar()
    Traceback (most recent call last):
        ...
    ValueError: pedido nao pode avancar
    >>> repr(p)
    'Pedido(1, PedidoStatus.ENTREGUE)'
    """

    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.status = PedidoStatus.PENDENTE

    def pagar(self) -> bool:
        """Marca como pago se o pedido ainda nao foi pago.

        Exemplos:
        >>> p = Pedido(1)
        >>> p.pagar()
        True
        >>> p.pagar()
        False
        >>> p.status == PedidoStatus.PAGO
        True
        """
        if self.status is not PedidoStatus.PENDENTE:
            return False
        self.status = PedidoStatus.PAGO
        return True

    def cancelar(self) -> bool:
        """Cancela o pedido somente enquanto esta pendente.

        Exemplos:
        >>> c = Pedido(2)
        >>> c.cancelar()
        True
        >>> c.cancelar()
        False
        >>> c.status.name
        'CANCELADO'
        """
        if self.status is not PedidoStatus.PENDENTE:
            return False
        self.status = PedidoStatus.CANCELADO
        return True

    def avancar(self) -> None:
        """Avança uma etapa da entrega; estados finais nao avancam.

        Exemplos:
        >>> p = Pedido(1)
        >>> p.avancar()
        >>> p.status.name
        'PAGO'
        >>> p.avancar()
        >>> p.avancar()
        >>> p.status.name
        'ENTREGUE'
        """
        if self.status in (PedidoStatus.ENTREGUE, PedidoStatus.CANCELADO):
            raise ValueError("pedido nao pode avancar")
        membros = list(PedidoStatus)
        self.status = membros[list(PedidoStatus).index(self.status) + 1]

    def __repr__(self) -> str:
        return f"Pedido({self.numero}, PedidoStatus.{self.status.name})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Onde você provavelmente divergiu:
# - comparou status por string ('PAGO' == self.status.name) em vez de
#   usar o membro do Enum — o == por string é onde o bug mora
# - numerou os valores na mao (PENDENTE = 0 etc.) em vez de auto():
#   a ordem fica implícita e você renumera ao inserir um estado novo
# - em `avancar` avançou com `+ 1` sem estacar nos estados finais e
#   estourou IndexError em vez de ValueError com mensagem clara
# - no cancelar usou `!= PedidoStatus.PENDENTE` e aceitou cancelar
#   pedido já pago (no fluxo esperado só PENDENTE é cancelável)
# - o repr devolveu "<PedidoStatus.PAGO: 2>" (repr do membro) em vez
#   de algo legível como "Pedido(1, PedidoStatus.PAGO)"