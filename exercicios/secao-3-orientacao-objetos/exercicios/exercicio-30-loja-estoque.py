"""
EXERCÍCIO 30 - Controle de Estoque da Loja (integrador)

Tópicos: ABC, polimorfismo, composição
Aulas: 129-177 (integrador)

`Produto` é um contrato ABSTRATO (ABC): todo produto tem preço de
venda, mas cada categoria calcula o seu do seu jeito
(polimorfismo). O `Estoque` COMPÕE produtos (dicionário
produto -> quantidade) e opera sobre eles SEM nunca saber o tipo
concreto — chama apenas `produto.preco_venda`, que cada subclasse
responde.

1. Classe `Produto(ABC)`:
   - `__init__(self, nome: str, preco_custo: float) -> None`:
     - Guarda `self.__nome` e `self.__preco_custo`
   - `@property nome -> str`
   - `@property preco_custo -> float`
   - `@property @abstractmethod preco_venda(self) -> float`
   - `__repr__(self) -> str` retornando
     `Eletronico(nome='Mouse', preco_custo=40.0)`
     (use `self.__class__.__name__` para o nome da classe)

2. Classe `Eletronico(Produto)`:
   - `@property preco_venda` retornando `self.preco_custo * 1.5`

3. Classe `Alimento(Produto)`:
   - `@property preco_venda` retornando `self.preco_custo * 1.2`

4. Classe `Estoque`:
   - `__init__(self) -> None` iniciando
     `self.__itens: dict[Produto, int] = {}`
   - `adicionar(self, produto: Produto, quantidade: int = 1) -> None`:
     - Se `quantidade <= 0`: `raise ValueError('quantidade deve ser positiva')`
     - Acumula a quantidade no dicionário
   - `retirar(self, produto: Produto, quantidade: int = 1) -> float`:
     - Se o produto não existe: `raise KeyError(produto)`
     - Se `self.__itens[produto] < quantidade`:
       `raise ValueError('quantidade indisponível')`
     - Reduz a quantidade e retorna `produto.preco_venda * quantidade`
     - Se a quantidade chegou a zero, remove a chave do dicionário
   - `@property itens -> dict[Produto, int]` (devolve CÓPIA)
   - `valor_estoque(self) -> float` retornando
     `sum(p.preco_venda * q for p, q in self.__itens.items())`
   - `__repr__(self) -> str` retornando `Estoque(quantidade=N)`
     (N = total de unidades em estoque)

Comportamento esperado (fluxo de uso):
    mouse = Eletronico('Mouse', 40.0)
    mouse.preco_venda  # 60.0  (40 * 1.5)
    arroz = Alimento('Arroz', 10.0)
    estoque = Estoque()
    estoque.adicionar(mouse, 2)
    estoque.adicionar(arroz, 5)
    estoque.valor_estoque()  # 180.0  (60*2 + 12*5)
    estoque.retirar(mouse, 1)  # 60.0
    estoque.itens  # cópia: len 2 e quantidade do mouse == 1
    estoque.retirar(mouse, 99)  # ValueError: quantidade indisponível
    estoque.retirar(Eletronico('Teclado', 50.0), 1)  # KeyError
    Estoque().adicionar(mouse, 0)  # ValueError: quantidade deve ser positiva

Observações:
  - `Produto` define `__eq__`/`__hash__`? NÃO: a identidade do
    objeto é a chave natural do dicionário (igualdade por endereço)
  - O ABC impede instanciar `Produto` diretamente
    (TypeError: Can't instantiate abstract class)
  - `Estoque` não usa os tipos concretos em momento algum: só o
    contrato `preco_venda` — adicionar uma categoria nova não muda
    o Estoque (polimorfismo + Liskov)
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, nome: str, preco_custo: float) -> None:
        ...

    @property
    def nome(self) -> str:
        ...

    @property
    def preco_custo(self) -> float:
        ...

    @property
    @abstractmethod
    def preco_venda(self) -> float:
        ...

    def __repr__(self) -> str:
        ...


class Eletronico(Produto):
    @property
    def preco_venda(self) -> float:
        ...


class Alimento(Produto):
    @property
    def preco_venda(self) -> float:
        ...


class Estoque:
    def __init__(self) -> None:
        ...

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        ...

    def retirar(self, produto: Produto, quantidade: int = 1) -> float:
        ...

    @property
    def itens(self) -> dict[Produto, int]:
        ...

    def valor_estoque(self) -> float:
        ...

    def __repr__(self) -> str:
        ...