"""
Gabarito EXERCÍCIO 30 - Controle de Estoque da Loja (ABC + polimorfismo)

Raciocínio sênior
-----------------
Produto(ABC) fixa o contrato preco_venda sem ditar o calculo: o
Estoque conhece só o contrato e delega a conta a cada subclasse
(polimorfismo — inserir categoria nova não muda uma linha do
Estoque). O dicionario usa Produto como chave por IDENTIDADE (sem
__eq__/__hash__ customizados, a igualdade é por endereço, então
dois "Mouse" distintos são produtos distintos). Retirar devolve o
VALOR monetário (preco_venda * qtd), deriva o preço do produto —
nunca guardado no Estoque — e remove a chave ao zerar para o
inventário nunca ter "linha morta". A property itens devolve CÓPIA
e o repr resume o estoque pelo total de unidades, sem vazar o
dicionário interno.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Produto(ABC):
    """Contrato de produto: nome, custo e preco de venda derivado."""

    def __init__(self, nome: str, preco_custo: float) -> None:
        self.__nome = nome
        self.__preco_custo = preco_custo

    @property
    def nome(self) -> str:
        """Retorna o nome do produto.

        Exemplos:
        >>> Eletronico('Mouse', 40.0).nome
        'Mouse'
        """
        return self.__nome

    @property
    def preco_custo(self) -> float:
        """Retorna o preco de custo.

        Exemplos:
        >>> Eletronico('Mouse', 40.0).preco_custo
        40.0
        """
        return self.__preco_custo

    @property
    @abstractmethod
    def preco_venda(self) -> float:
        """Preco final de venda; cada categoria calcula o seu."""

    def __repr__(self) -> str:
        """Representacao textual com o nome real da classe.

        Exemplos:
        >>> Eletronico('Mouse', 40.0)
        Eletronico(nome='Mouse', preco_custo=40.0)
        >>> Alimento('Arroz', 10.0)
        Alimento(nome='Arroz', preco_custo=10.0)
        """
        return (
            f'{self.__class__.__name__}('
            f'nome={self.nome!r}, preco_custo={self.preco_custo})'
        )


class Eletronico(Produto):
    """Produto eletronico com margem de 50% sobre o custo."""

    @property
    def preco_venda(self) -> float:
        """Aplica a margem do eletronico.

        Exemplos:
        >>> Eletronico('Mouse', 40.0).preco_venda
        60.0
        """
        return self.preco_custo * 1.5


class Alimento(Produto):
    """Alimento com margem de 20% sobre o custo."""

    @property
    def preco_venda(self) -> float:
        """Aplica a margem do alimento.

        Exemplos:
        >>> Alimento('Arroz', 10.0).preco_venda
        12.0
        """
        return self.preco_custo * 1.2


class Estoque:
    """Estoque da loja: mapeia produto (por identidade) a quantidade."""

    def __init__(self) -> None:
        self.__itens: dict[Produto, int] = {}

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        """Acumula quantidade do produto no estoque.

        Raises:
            ValueError: Se a quantidade informada nao for positiva.

        Exemplos:
        >>> estoque = Estoque()
        >>> estoque.adicionar(Eletronico('Mouse', 40.0), 2)
        >>> estoque
        Estoque(quantidade=2)
        >>> estoque.adicionar(Eletronico('Mouse', 40.0), 0)
        Traceback (most recent call last):
        ...
        ValueError: quantidade deve ser positiva
        """
        if quantidade <= 0:
            raise ValueError('quantidade deve ser positiva')
        self.__itens[produto] = self.__itens.get(produto, 0) + quantidade

    def retirar(self, produto: Produto, quantidade: int = 1) -> float:
        """Retira unidades e devolve o valor (preco_venda * qtd).

        Raises:
            KeyError: Se o produto nao consta no estoque.
            ValueError: Se a quantidade pedida exceder a disponivel.

        Exemplos:
        >>> mouse = Eletronico('Mouse', 40.0)
        >>> estoque = Estoque()
        >>> estoque.adicionar(mouse, 2)
        >>> estoque.retirar(mouse, 1)
        60.0
        >>> estoque.retirar(mouse, 99)
        Traceback (most recent call last):
        ...
        ValueError: quantidade indisponível
        >>> estoque.retirar(Eletronico('Teclado', 50.0), 1)
        Traceback (most recent call last):
        ...
        KeyError: Eletronico(nome='Teclado', preco_custo=50.0)
        """
        if produto not in self.__itens:
            raise KeyError(produto)
        if self.__itens[produto] < quantidade:
            raise ValueError('quantidade indisponível')

        self.__itens[produto] -= quantidade
        if self.__itens[produto] == 0:
            del self.__itens[produto]
        return produto.preco_venda * quantidade

    @property
    def itens(self) -> dict[Produto, int]:
        """Retorna uma copia do mapeamento interno.

        Exemplos:
        >>> mouse = Eletronico('Mouse', 40.0)
        >>> arroz = Alimento('Arroz', 10.0)
        >>> estoque = Estoque()
        >>> estoque.adicionar(mouse, 2)
        >>> estoque.adicionar(arroz, 5)
        >>> estoque.itens
        {Eletronico(nome='Mouse', preco_custo=40.0): 2, Alimento(nome='Arroz', preco_custo=10.0): 5}
        >>> estoque.retirar(mouse, 1)
        60.0
        >>> len(estoque.itens)
        2
        >>> estoque.itens[mouse]
        1
        """
        return dict(self.__itens)

    def valor_estoque(self) -> float:
        """Valor total do estoque somando preco_venda * quantidade.

        Exemplos:
        >>> mouse = Eletronico('Mouse', 40.0)
        >>> arroz = Alimento('Arroz', 10.0)
        >>> estoque = Estoque()
        >>> estoque.adicionar(mouse, 2)
        >>> estoque.adicionar(arroz, 5)
        >>> estoque.valor_estoque()
        180.0
        """
        return sum(p.preco_venda * q for p, q in self.__itens.items())

    def __repr__(self) -> str:
        """Representacao textual resumida em total de unidades.

        Exemplos:
        >>> Estoque()
        Estoque(quantidade=0)
        """
        return f'Estoque(quantidade={sum(self.__itens.values())})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - devolveu o dict interno na property itens (quem lia podia
#   zerar ou inflar o estoque; dict() copia o mapeamento)
# - não removeu a chave ao zerar a quantidade (o produto virava
#   linha morta e retirar mais 1 devolvia KeyError? não — o if de
#   "quantidade indisponível" tratava; mas o inventário engana)
# - definiu __eq__/__hash__ em Produto (quebraria a identidade que
#   o enunciado pede como chave do dicionário)
# - usou isinstance no Estoque para escolher margem (o próprio
#   produto já sabe o preco_venda — duplicar a regra em dois
#   lugares é o caminho para a regra divergir)
# - validou a quantidade na retirada DEPOIS de subtrair (o estado
#   ficaria negativo; valide antes de mutar)