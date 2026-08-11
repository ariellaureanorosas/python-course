"""
EXERCÍCIO 20 - Sistema de Biblioteca (integrador: 4 pilares da POO)

Tópicos: abstração, herança, encapsulamento, polimorfismo, composição/agregação
Aulas: 129-177 (integrador)

Projeto final da seção: um sistema de biblioteca que usa os quatro
pilares da POO. O diagrama conceitual:

    ItemBiblioteca (ABC)            Pessoa
        ├── Livro                     └── Cliente (1-N Emprestimo)
        └── Revista
    Emprestimo (liga ItemBiblioteca + Cliente + multa)
    Biblioteca (agrega itens e clientes, controla empréstimos)

1. Classe `ItemBiblioteca(ABC)`:
   - `__init__(self, titulo: str) -> None` guarda `self.__titulo`
   - `@property titulo -> str`
   - `@property @abstractmethod tipo -> str`
   - `@abstractmethod calcular_multa(self, dias_atraso: int) -> float`
   - `__repr__(self) -> str` retornando '<Classe>(titulo='...')'

2. Classe `Livro(ItemBiblioteca)`:
   - `tipo` retorna 'Livro'
   - `calcular_multa` retorna dias_atraso * 2.0

3. Classe `Revista(ItemBiblioteca)`:
   - `tipo` retorna 'Revista'
   - `calcular_multa` retorna dias_atraso * 1.0

4. Classe `Pessoa`:
   - `__init__(self, nome: str) -> None` guarda `self.__nome`
   - `@property nome -> str`
   - `__repr__(self) -> str` retornando 'Pessoa(nome='...')'

5. Classe `Cliente(Pessoa)`:
   - `__init__(self, nome: str) -> None` chama super().__init__ e
     inicia `self.__emprestimos: list[Emprestimo] = []`
   - `@property emprestimos -> list['Emprestimo']` (cópia da lista)
   - `registrar_emprestimo(self, emprestimo: 'Emprestimo') -> None`
   - `__repr__(self) -> str` retornando 'Cliente(nome='...')'

6. Classe `Emprestimo`:
   - `__init__(self, item: ItemBiblioteca, prazo_dias: int = 7) -> None`
     - Guarda o item e a data final = date.today() + timedelta(days=prazo_dias)
     - Inicia `self.__devolvido = False`
   - `@property item -> ItemBiblioteca`
   - `@property esta_atrasado -> bool`:
     - True se NÃO devolvido E date.today() > data final
   - `devolver(self) -> float | None`:
     - Marca como devolvido
     - Se houver atraso (dias inteiros), retorna
       item.calcular_multa(dias_atraso)
     - Senão retorna None

7. Classe `Biblioteca`:
   - `__init__(self) -> None` inicia `self.__itens: list[ItemBiblioteca] = []`
     e `self.__clientes: list[Cliente] = []`
   - `cadastrar_item(self, item: ItemBiblioteca) -> None`
   - `cadastrar_cliente(self, cliente: Cliente) -> None`
   - `emprestar(self, item: ItemBiblioteca, cliente: Cliente) -> Emprestimo`
     - Cria o Emprestimo, registra no cliente e retorna
   - `@property itens -> list[ItemBiblioteca]` (cópia da lista)
   - `@property clientes -> list[Cliente]` (cópia da lista)

Comportamento esperado (fluxo de uso):
    biblioteca = Biblioteca()
    livro = Livro('O Cortiço')
    cliente = Cliente('Ana')
    biblioteca.cadastrar_item(livro)
    biblioteca.cadastrar_cliente(cliente)
    emprestimo = biblioteca.emprestar(livro, cliente)
    emprestimo.esta_atrasado  # False (prazo de 7 dias a partir de hoje)
    multa = emprestimo.devolver()  # None (sem atraso)

Observações:
  - Use `from datetime import date, timedelta` e `from abc import ABC, abstractmethod`
  - `Emprestimo` é referenciado por `Cliente` antes de ser definido:
    use aspas na anotação ('Emprestimo') e defina depois — funciona
    porque as anotações só são avaliadas com `from __future__ import annotations`
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date, timedelta


class ItemBiblioteca(ABC):
    def __init__(self, titulo: str) -> None:
        ...

    @property
    def titulo(self) -> str:
        ...

    @property
    @abstractmethod
    def tipo(self) -> str:
        ...

    @abstractmethod
    def calcular_multa(self, dias_atraso: int) -> float:
        ...

    def __repr__(self) -> str:
        ...


class Livro(ItemBiblioteca):
    @property
    def tipo(self) -> str:
        ...

    def calcular_multa(self, dias_atraso: int) -> float:
        ...


class Revista(ItemBiblioteca):
    @property
    def tipo(self) -> str:
        ...

    def calcular_multa(self, dias_atraso: int) -> float:
        ...


class Pessoa:
    def __init__(self, nome: str) -> None:
        ...

    @property
    def nome(self) -> str:
        ...

    def __repr__(self) -> str:
        ...


class Cliente(Pessoa):
    def __init__(self, nome: str) -> None:
        ...

    @property
    def emprestimos(self) -> list[Emprestimo]:
        ...

    def registrar_emprestimo(self, emprestimo: Emprestimo) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Emprestimo:
    def __init__(self, item: ItemBiblioteca, prazo_dias: int = 7) -> None:
        ...

    @property
    def item(self) -> ItemBiblioteca:
        ...

    @property
    def esta_atrasado(self) -> bool:
        ...

    def devolver(self) -> float | None:
        ...


class Biblioteca:
    def __init__(self) -> None:
        ...

    def cadastrar_item(self, item: ItemBiblioteca) -> None:
        ...

    def cadastrar_cliente(self, cliente: Cliente) -> None:
        ...

    def emprestar(
        self,
        item: ItemBiblioteca,
        cliente: Cliente,
    ) -> Emprestimo:
        ...

    @property
    def itens(self) -> list[ItemBiblioteca]:
        ...

    @property
    def clientes(self) -> list[Cliente]:
        ...