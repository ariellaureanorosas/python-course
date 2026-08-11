"""
EXERCÍCIO 19 - Dataclasses: classes de dados com código automático

Tópicos: @dataclass, field, default_factory, frozen, order, asdict
Aulas: 172-175

Dataclass = classe voltada a dados: __init__, __repr__ e __eq__ são
gerados automaticamente. frozen=True torna imutável; order=True
habilita comparações (<, >, sorted); field controla cada atributo.

1. Classe `Produto` com @dataclass(frozen=True, order=True):
   - `nome: str`
   - `preco: float`
   - `categorias: list[str]` com field(default_factory=list, repr=False)
     - default_factory evita compartilhar a MESMA lista entre instâncias
     - repr=False esconde categorias no __repr__ (fica mais legível)

2. Classe `Pedido` com @dataclass(frozen=True):
   - `numero: int`
   - `produtos: list[Produto]` com field(default_factory=list)
   - `@property total(self) -> float` (soma dos preços dos produtos)

3. Utilidades (aula 174):
   - Use asdict(pedido) para converter em dicionário
   - Use astuple(pedido) para converter em tupla

Comportamento esperado:
    caneta = Produto('Caneta', 3.50)
    caderno = Produto('Caderno', 12.90)
    pedido = Pedido(1, [caneta, caderno])
    pedido.total            # 16.4
    caneta < caderno        # True (order=True gera comparações)
    Produto('Caneta', 3.50) == Produto('Caneta', 3.50)  # True (__eq__ automático)
    caneta.categorias.append('Papelaria')  # FrozenInstanceError

Import: from dataclasses import dataclass, field, asdict, astuple
"""

from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Produto:
    nome: str
    preco: float
    categorias: list[str] = field(default_factory=list, repr=False)


@dataclass(frozen=True)
class Pedido:
    numero: int
    produtos: list[Produto] = field(default_factory=list)

    @property
    def total(self) -> float:
        ...