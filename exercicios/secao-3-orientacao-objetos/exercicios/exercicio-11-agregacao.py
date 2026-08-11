"""
EXERCÍCIO 11 - Agregação: Carrinho de Compras e Produtos

Tópicos: agregação, relação um-para-muitos, objetos independentes
Aulas: 145

Agregação é uma relação em que o TODO (carrinho) contém as PARTES
(produtos), mas as partes existem fora do todo: o mesmo Produto pode
estar em vários carrinhos ou em nenhum, e viver sozinho.

1. Classe `Produto`:
   - `__init__(self, nome: str, preco: float) -> None`
   - `__repr__(self) -> str` retornando Produto(nome='...', preco=...)

2. Classe `CarrinhoDeCompras`:
   - `__init__(self) -> None` inicia `self._produtos: list[Produto] = []`
   - `adicionar(self, produto: Produto) -> None`
   - `remover(self, produto: Produto) -> None` (use list.remove)
   - `limpar(self) -> None` (esvazia a lista)
   - `listar(self) -> list[Produto]` (retorna cópia da lista)
   - `@property total(self) -> float` (soma dos preços)

Comportamento esperado:
    camiseta = Produto('Camiseta', 49.90)
    calca = Produto('Calça', 89.90)
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar(camiseta)
    carrinho.adicionar(calca)
    carrinho.total   # 139.8
    carrinho.remover(camiseta)
    carrinho.total   # 89.9

Observação: o Produto continua existindo depois de removido —
é isso que diferencia agregação de composição.
"""


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        ...

    def __repr__(self) -> str:
        ...


class CarrinhoDeCompras:
    def __init__(self) -> None:
        ...

    def adicionar(self, produto: Produto) -> None:
        ...

    def remover(self, produto: Produto) -> None:
        ...

    def limpar(self) -> None:
        ...

    def listar(self) -> list[Produto]:
        ...

    @property
    def total(self) -> float:
        ...