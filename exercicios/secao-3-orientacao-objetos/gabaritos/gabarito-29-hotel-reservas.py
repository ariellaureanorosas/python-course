"""
Gabarito EXERCÍCIO 29 - Sistema de Reservas do Hotel (associação)

Raciocínio sênior
-----------------
A associação nasce no construtor da Reserva: ela recebe Cliente e
Quarto, reserva o quarto (efeito colateral validado) e se registra
no cliente (as duas pontas ficam conectadas com um unico ponto de
criacao). A ordem de validacao importa: dias <= 0 sai ANTES de
quarto.reservar(), senao uma reserva invalida sujaria o estado do
quarto. Encapsulamento em tudo (name mangling + properties), e a
property reservas devolve CÓPIA — quem le a lista nao pode injetar
reservas falsas no cliente. O cancelamento delega ao quarto
(liberar) e o total e DERIVADO (preco * dias), nunca armazenado, o
que elimina estado duplicado para divergir.
"""

from __future__ import annotations


class Quarto:
    """Quarto com flag de disponibilidade protegida por property."""

    def __init__(self, numero: int, preco_diaria: float) -> None:
        self.__numero = numero
        self.__preco_diaria = preco_diaria
        self.__disponivel = True

    @property
    def numero(self) -> int:
        """Retorna o numero do quarto.

        Exemplos:
        >>> Quarto(101, 100.0).numero
        101
        """
        return self.__numero

    @property
    def preco_diaria(self) -> float:
        """Retorna o preco da diaria.

        Exemplos:
        >>> Quarto(101, 100.0).preco_diaria
        100.0
        """
        return self.__preco_diaria

    @property
    def disponivel(self) -> bool:
        """True se o quarto esta livre para reserva.

        Exemplos:
        >>> Quarto(101, 100.0).disponivel
        True
        """
        return self.__disponivel

    def reservar(self) -> None:
        """Ocupa o quarto; levanta erro se ja estiver ocupado.

        Raises:
            ValueError: Se o quarto ja esta ocupado.

        Exemplos:
        >>> quarto = Quarto(101, 100.0)
        >>> quarto.reservar()
        >>> quarto.disponivel
        False
        >>> quarto.reservar()
        Traceback (most recent call last):
        ...
        ValueError: Quarto já está ocupado
        """
        if not self.__disponivel:
            raise ValueError('Quarto já está ocupado')
        self.__disponivel = False

    def liberar(self) -> None:
        """Devolve o quarto ao estado disponivel."""
        self.__disponivel = True

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Quarto(101, 100.0)
        Quarto(numero=101, preco_diaria=100.0, disponivel=True)
        """
        return (
            f'Quarto(numero={self.numero}, '
            f'preco_diaria={self.preco_diaria}, '
            f'disponivel={self.disponivel})'
        )


class Cliente:
    """Cliente do hotel: acumula as reservas feitas em seu nome."""

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__reservas: list[Reserva] = []

    @property
    def nome(self) -> str:
        """Retorna o nome do cliente.

        Exemplos:
        >>> Cliente('Ana').nome
        'Ana'
        """
        return self.__nome

    def adicionar_reserva(self, reserva: Reserva) -> None:
        """Vincula uma reserva ao cliente."""
        self.__reservas.append(reserva)

    @property
    def reservas(self) -> list[Reserva]:
        """Retorna uma copia da lista de reservas.

        Exemplos:
        >>> Cliente('Ana').reservas
        []
        """
        return list(self.__reservas)

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Cliente('Ana')
        Cliente(nome='Ana')
        """
        return f'Cliente(nome={self.__nome!r})'


class Reserva:
    """Reserva ligando cliente e quarto: valida, reserva e totaliza."""

    def __init__(self, cliente: Cliente, quarto: Quarto, dias: int) -> None:
        if dias <= 0:
            raise ValueError('dias deve ser positivo')
        quarto.reservar()
        self.__cliente = cliente
        self.__quarto = quarto
        self.__dias = dias
        cliente.adicionar_reserva(self)

    @property
    def total(self) -> float:
        """Custo total da estadia (diaria * dias) — sempre derivado.

        Exemplos:
        >>> ana = Cliente('Ana')
        >>> quarto = Quarto(101, 100.0)
        >>> reserva = Reserva(ana, quarto, 3)
        >>> reserva.total
        300.0
        """
        return self.__quarto.preco_diaria * self.__dias

    def cancelar(self) -> None:
        """Cancela a reserva liberando o quarto.

        Exemplos:
        >>> ana = Cliente('Ana')
        >>> quarto = Quarto(101, 100.0)
        >>> reserva = Reserva(ana, quarto, 3)
        >>> reserva.cancelar()
        >>> quarto.disponivel
        True
        """
        self.__quarto.liberar()

    def __repr__(self) -> str:
        """Representacao textual completa para depuracao.

        Exemplos:
        >>> ana = Cliente('Ana')
        >>> quarto = Quarto(101, 100.0)
        >>> reserva = Reserva(ana, quarto, 3)
        >>> ana.reservas
        [Reserva(cliente=Cliente(nome='Ana'), quarto=Quarto(numero=101, preco_diaria=100.0, disponivel=False), dias=3)]
        >>> Reserva(ana, quarto, 0)
        Traceback (most recent call last):
        ...
        ValueError: dias deve ser positivo
        """
        return (
            f'Reserva(cliente={self.__cliente!r}, '
            f'quarto={self.__quarto!r}, dias={self.__dias})'
        )


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - validou dias DEPOIS de quarto.reservar() (reserva invalida
#   marcava o quarto como ocupado; a validacao tem que vir antes)
# - devolveu self.__reservas na property (o caller podia adicionar
#   reservas falsas; list(...) corta a referencia)
# - guardou o total como atributo self.__total (estado duplicado:
#   se o quarto mudasse de preco, o total divergiria; preco * dias
#   é sempre derivado na leitura)
# - replicou a validacao "quarto ocupado" dentro da Reserva com
#   if quarto.disponivel — a regra é UNICA e mora em quarto.reservar();
#   a Reserva so chama e deixa o ValueError propagar
# - esqueceu o from __future__ import annotations e usou a classe
#   Reserva antes de definida (a anotacao em Cliente quebraria em
#   tempo de definicao sem ele)