"""
EXERCÍCIO 29 - Sistema de Reservas do Hotel (integrador)

Tópicos: associação, encapsulamento, validação
Aulas: 129-177 (integrador)

Três classes que se relacionam por ASSOCIAÇÃO: a Reserva conecta
um Cliente a um Quarto. Encapsulamento com name mangling em todo
estado interno, properties para leitura e VALIDAÇÃO no construtor
e nos métodos que mudam estado (reservar um quarto ocupado e criar
reserva com dias <= 0 devem falhar com ValueError).

1. Classe `Quarto`:
   - `__init__(self, numero: int, preco_diaria: float) -> None`:
     - Guarda `self.__numero`, `self.__preco_diaria` e
       `self.__disponivel = True`
   - `@property numero -> int`
   - `@property preco_diaria -> float`
   - `@property disponivel -> bool`
   - `reservar(self) -> None`:
     - Se `not self.__disponivel`: `raise ValueError('Quarto já está ocupado')`
     - Senão: `self.__disponivel = False`
   - `liberar(self) -> None`: `self.__disponivel = True`
   - `__repr__(self) -> str` retornando
     `Quarto(numero=101, preco_diaria=100.0, disponivel=True)`

2. Classe `Cliente`:
   - `__init__(self, nome: str) -> None`:
     - Guarda `self.__nome` e `self.__reservas: list[Reserva] = []`
   - `@property nome -> str`
   - `adicionar_reserva(self, reserva: Reserva) -> None`
   - `@property reservas -> list[Reserva]` (devolve CÓPIA da lista)
   - `__repr__(self) -> str` retornando `Cliente(nome='Ana')`

3. Classe `Reserva`:
   - `__init__(self, cliente: Cliente, quarto: Quarto, dias: int) -> None`:
     - Se `dias <= 0`: `raise ValueError('dias deve ser positivo')`
     - Chama `quarto.reservar()` (se ocupado, o ValueError propaga)
     - Guarda `self.__cliente`, `self.__quarto`, `self.__dias`
     - Registra a reserva no cliente (`cliente.adicionar_reserva(self)`)
   - `@property total -> float` retornando
     `self.__quarto.preco_diaria * self.__dias`
   - `cancelar(self) -> None` chamando `self.__quarto.liberar()`
   - `__repr__(self) -> str` retornando
     `Reserva(cliente=Cliente(nome='Ana'), quarto=Quarto(numero=101, preco_diaria=100.0, disponivel=False), dias=3)`

Comportamento esperado (fluxo de uso):
    ana = Cliente('Ana')
    quarto = Quarto(101, 100.0)
    reserva = Reserva(ana, quarto, 3)
    reserva.total  # 300.0
    quarto.disponivel  # False (o quarto ficou ocupado)
    Reserva(ana, quarto, 2)  # ValueError: Quarto já está ocupado
    reserva.cancelar()
    quarto.disponivel  # True (liberado de volta)
    ana.reservas  # [Reserva(cliente=..., quarto=..., dias=3)]
    Reserva(ana, quarto, 0)  # ValueError: dias deve ser positivo

Observações:
  - `Cliente` referencia `Reserva` antes dela ser definida: use
    `from __future__ import annotations` (as anotações viram
    strings e só são resolvidas em tempo de execução, se precisar)
  - A validação de `dias` vem ANTES de reservar o quarto: uma
    reserva inválida não pode sujar o estado do quarto
  - `reservas` devolve cópia; sem isso, quem lê poderia adicionar
    reservas falsas na lista interna do cliente
"""

from __future__ import annotations


class Quarto:
    def __init__(self, numero: int, preco_diaria: float) -> None:
        ...

    @property
    def numero(self) -> int:
        ...

    @property
    def preco_diaria(self) -> float:
        ...

    @property
    def disponivel(self) -> bool:
        ...

    def reservar(self) -> None:
        ...

    def liberar(self) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Cliente:
    def __init__(self, nome: str) -> None:
        ...

    @property
    def nome(self) -> str:
        ...

    def adicionar_reserva(self, reserva: Reserva) -> None:
        ...

    @property
    def reservas(self) -> list[Reserva]:
        ...

    def __repr__(self) -> str:
        ...


class Reserva:
    def __init__(self, cliente: Cliente, quarto: Quarto, dias: int) -> None:
        ...

    @property
    def total(self) -> float:
        ...

    def cancelar(self) -> None:
        ...

    def __repr__(self) -> str:
        ...