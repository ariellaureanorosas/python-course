"""
Gabarito EXERCÍCIO 11 - Agregação

Raciocínio sênior
-----------------
Agregação = o todo TEM partes, mas as partes vivem SEM o todo:
o Produto é criado fora do Carrinho e continua existindo se o
carrinho sumir (remover() só desliga a associação). O carrinho
adiciona/remove a MESMA referência — nunca uma cópia.
listar() devolve list(self._produtos): uma CÓPIA da lista — se
devolver a lista interna, o caller pode adicionar/remover
produtos sem passar pelos métodos (furando o encapsulamento).
total como @property calcula na hora (sum generator) em vez de
guardar um total que pode desatualizar.
"""


class Produto:
    """Produto que existe independentemente de qualquer carrinho."""

    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Produto('Camiseta', 49.90)
        Produto(nome='Camiseta', preco=49.9)
        """
        return f'Produto(nome={self.nome!r}, preco={self.preco})'


class CarrinhoDeCompras:
    """Carrinho que agrega produtos (partes vivem fora do todo)."""

    def __init__(self) -> None:
        self._produtos: list[Produto] = []

    def adicionar(self, produto: Produto) -> None:
        """Adiciona um produto ao carrinho.

        Exemplos:
        >>> carrinho = CarrinhoDeCompras()
        >>> carrinho.adicionar(Produto('Camiseta', 49.90))
        >>> len(carrinho.listar())
        1
        """
        self._produtos.append(produto)

    def remover(self, produto: Produto) -> None:
        """Remove um produto do carrinho (list.remove).

        Exemplos:
        >>> camiseta = Produto('Camiseta', 49.90)
        >>> carrinho = CarrinhoDeCompras()
        >>> carrinho.adicionar(camiseta)
        >>> carrinho.remover(camiseta)
        >>> carrinho.listar()
        []
        """
        self._produtos.remove(produto)

    def limpar(self) -> None:
        """Esvazia o carrinho.

        Exemplos:
        >>> carrinho = CarrinhoDeCompras()
        >>> carrinho.adicionar(Produto('Camiseta', 49.90))
        >>> carrinho.limpar()
        >>> carrinho.listar()
        []
        """
        self._produtos.clear()

    def listar(self) -> list[Produto]:
        """Retorna uma copia da lista de produtos.

        Exemplos:
        >>> carrinho = CarrinhoDeCompras()
        >>> carrinho.adicionar(Produto('Camiseta', 49.90))
        >>> carrinho.listar()
        [Produto(nome='Camiseta', preco=49.9)]
        """
        return list(self._produtos)

    @property
    def total(self) -> float:
        """Retorna a soma dos precos dos produtos.

        Exemplos:
        >>> carrinho = CarrinhoDeCompras()
        >>> carrinho.adicionar(Produto('Camiseta', 49.90))
        >>> carrinho.adicionar(Produto('Calça', 89.90))
        >>> carrinho.total
        139.8
        """
        return sum(produto.preco for produto in self._produtos)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - devolveu self._produtos direto em listar() — quem chamar pode
#   mexer na lista sem passar por adicionar()/remover()
#   (encapsulamento furado); list() copia e protege
# - criou o Produto dentro de adicionar (composição) — na
#   agregação as partes nascem fora e são INJETADAS
# - guardou self.total no momento da adição (desatualiza se
#   remover; property calcula sempre na hora)