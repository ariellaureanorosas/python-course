"""
Gabarito EXERCÍCIO 20 - Sistema de Biblioteca (Capstone)

Raciocínio sênior
-----------------
O capstone amarra OOP: ABC como contrato (ItemBiblioteca força
tipo/calcular_multa em cada item), nome mangling em todo estado
interno (__titulo, __saldo de livros...), property para leitura
controlada (emprestimos devolve CÓPIA da lista — sem isso o
caller adicionaria/removeria empréstimos por fora), herança
(Livro/Revista/Cliente) e composição (Biblioteca TEM itens e
clientes; Emprestimo TEM um item).
A multa é POLIMÓRFICA: Biblioteca/Emprestimo chamam
item.calcular_multa(dias) sem saber se é Livro ou Revista — cada
item calcula a própria. datas são resolvidas com datetime +
timedelta (prazo de devolução = hoje + prazo_dias).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date, timedelta


class ItemBiblioteca(ABC):
    """Item acervo da biblioteca: contrato com tipo e calculo de multa."""

    def __init__(self, titulo: str) -> None:
        self.__titulo = titulo

    @property
    def titulo(self) -> str:
        """Retorna o titulo do item.

        Exemplos:
        >>> Livro('O Cortiço').titulo
        'O Cortiço'
        """
        return self.__titulo

    @property
    @abstractmethod
    def tipo(self) -> str:
        """Tipo do item (Livro, Revista, ...)."""

    @abstractmethod
    def calcular_multa(self, dias_atraso: int) -> float:
        """Calcula a multa proporcional aos dias de atraso."""

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Livro('O Cortiço')
        Livro(titulo='O Cortiço')
        """
        return f'{self.__class__.__name__}(titulo={self.titulo!r})'


class Livro(ItemBiblioteca):
    """Livro: multa de R$ 2,00 por dia de atraso."""

    @property
    def tipo(self) -> str:
        """Retorna o tipo do item.

        Exemplos:
        >>> Livro('O Cortiço').tipo
        'Livro'
        """
        return 'Livro'

    def calcular_multa(self, dias_atraso: int) -> float:
        """Multiplica dias de atraso por 2.

        Exemplos:
        >>> Livro('O Cortiço').calcular_multa(3)
        6.0
        """
        return dias_atraso * 2.0


class Revista(ItemBiblioteca):
    """Revista: multa de R$ 1,00 por dia de atraso."""

    @property
    def tipo(self) -> str:
        """Retorna o tipo do item.

        Exemplos:
        >>> Revista('Superinteressante').tipo
        'Revista'
        """
        return 'Revista'

    def calcular_multa(self, dias_atraso: int) -> float:
        """Multiplica dias de atraso por 1.

        Exemplos:
        >>> Revista('Superinteressante').calcular_multa(3)
        3.0
        """
        return dias_atraso * 1.0


class Pessoa:
    """Pessoa generica com nome protegido por property."""

    def __init__(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nome(self) -> str:
        """Retorna o nome da pessoa.

        Exemplos:
        >>> Pessoa('Ana').nome
        'Ana'
        """
        return self.__nome

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Pessoa('Ana')
        Pessoa(nome='Ana')
        """
        return f'{self.__class__.__name__}(nome={self.nome!r})'


class Cliente(Pessoa):
    """Cliente da biblioteca: pessoa que acumula emprestimos."""

    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.__emprestimos: list[Emprestimo] = []

    @property
    def emprestimos(self) -> list[Emprestimo]:
        """Retorna uma copia da lista de emprestimos do cliente.

        Exemplos:
        >>> Cliente('Ana').emprestimos
        []
        """
        return list(self.__emprestimos)

    def registrar_emprestimo(self, emprestimo: Emprestimo) -> None:
        """Vincula um emprestimo ao cliente."""
        self.__emprestimos.append(emprestimo)


class Emprestimo:
    """Emprestimo de um item: controla devolucao e multa por atraso."""

    def __init__(self, item: ItemBiblioteca, prazo_dias: int = 7) -> None:
        self.__item = item
        self.__data_devolucao = date.today() + timedelta(days=prazo_dias)
        self.__devolvido = False

    @property
    def item(self) -> ItemBiblioteca:
        """Retorna o item emprestado.

        Exemplos:
        >>> Emprestimo(Livro('O Cortiço')).item
        Livro(titulo='O Cortiço')
        """
        return self.__item

    @property
    def esta_atrasado(self) -> bool:
        """True se o item ainda nao foi devolvido apos o prazo.

        Exemplos:
        >>> Emprestimo(Livro('O Cortiço')).esta_atrasado
        False
        >>> Emprestimo(Livro('O Cortiço'), prazo_dias=-1).esta_atrasado
        True
        """
        return not self.__devolvido and date.today() > self.__data_devolucao

    def devolver(self) -> float | None:
        """Devolve o item e retorna a multa, se houver atraso.

        Exemplos:
        >>> Emprestimo(Livro('O Cortiço')).devolver()
        >>> Emprestimo(Livro('O Cortiço'), prazo_dias=-1).devolver()
        2.0
        >>> Emprestimo(Revista('Superinteressante'), prazo_dias=-1).devolver()
        1.0
        """
        self.__devolvido = True
        dias_atraso = (date.today() - self.__data_devolucao).days

        if dias_atraso > 0:
            return self.__item.calcular_multa(dias_atraso)
        return None

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Emprestimo(Livro('O Cortiço'))
        Emprestimo(item=Livro(titulo='O Cortiço'))
        """
        return f'Emprestimo(item={self.__item!r})'


class Biblioteca:
    """Biblioteca: agrega itens e clientes e controla emprestimos."""

    def __init__(self) -> None:
        self.__itens: list[ItemBiblioteca] = []
        self.__clientes: list[Cliente] = []

    @property
    def itens(self) -> list[ItemBiblioteca]:
        """Retorna uma copia do acervo.

        Exemplos:
        >>> biblioteca = Biblioteca()
        >>> biblioteca.itens
        []
        """
        return list(self.__itens)

    @property
    def clientes(self) -> list[Cliente]:
        """Retorna uma copia da lista de clientes.

        Exemplos:
        >>> biblioteca = Biblioteca()
        >>> biblioteca.clientes
        []
        """
        return list(self.__clientes)

    def cadastrar_item(self, item: ItemBiblioteca) -> None:
        """Adiciona um item ao acervo."""
        self.__itens.append(item)

    def cadastrar_cliente(self, cliente: Cliente) -> None:
        """Adiciona um cliente a biblioteca."""
        self.__clientes.append(cliente)

    def emprestar(self, item: ItemBiblioteca, cliente: Cliente) -> Emprestimo:
        """Cria um emprestimo e o registra no cliente.

        Exemplos:
        >>> biblioteca = Biblioteca()
        >>> livro = Livro('O Cortiço')
        >>> ana = Cliente('Ana')
        >>> emprestimo = biblioteca.emprestar(livro, ana)
        >>> emprestimo.item
        Livro(titulo='O Cortiço')
        >>> ana.emprestimos
        [Emprestimo(item=Livro(titulo='O Cortiço'))]
        """
        emprestimo = Emprestimo(item)
        cliente.registrar_emprestimo(emprestimo)
        return emprestimo


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - devolveu a lista interna __emprestimos direto na property (o
#   caller podia mutá-la; list() copia e preserva o encapsulamento)
# - calculou a multa com um if no Emprestimo ("if isinstance(item,
#   Livro)...") — quebra o polimorfismo; cada item já sabe sua multa
# - usou datetime.now() vs date.today() misturados ou esqueceu
#   timedelta na devolução (a conta de dias atraso depende do
#   mesmo "hoje" do prazo)
# - cadastrou lista de empréstimos como atributo de classe (seta o
#   mesmo emprestimo em todos os clientes — é __init__ da instância)