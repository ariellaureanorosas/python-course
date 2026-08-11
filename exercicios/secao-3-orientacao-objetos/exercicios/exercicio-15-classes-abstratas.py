"""
EXERCÍCIO 15 - Classes abstratas (ABC) e métodos abstratos

Tópicos: abc.ABC, @abstractmethod, contrato, property abstrata
Aulas: 151-152

Uma classe abstrata é um CONTRATO: define O QUE as subclasses devem
implementar, sem dizer COMO. Não pode ser instanciada — quem a herda
DEVE implementar os métodos abstratos, ou também vira abstrata.

1. Classe `Pagamento(ABC)`:
   - `@abstractmethod processar(self) -> str`
   - Corpo pode ser `...` (Ellipsis)

2. Classe `PagamentoCartao(Pagamento)`:
   - `__init__(self, bandeira: str) -> None`
   - `processar(self) -> str` retorna
     'Pagamento com cartão <bandeira> processado'

3. Classe `PagamentoPix(Pagamento)`:
   - `processar(self) -> str` retorna 'Pagamento via Pix processado'

4. Classe `Produto(ABC)`:
   - `@property @abstractmethod preco(self) -> float`
     - @property por fora, @abstractmethod por dentro (ordem importa)

5. Classe `Frutas(Produto)`:
   - `__init__(self, nome: str, preco: float) -> None`
   - Implementa `preco` como @property que retorna o preço

Comportamento esperado:
    Pagamento()          # TypeError: não pode instanciar classe abstrata
    PagamentoCartao('Visa').processar()  # 'Pagamento com cartão Visa processado'
    PagamentoPix().processar()           # 'Pagamento via Pix processado'
    Frutas('Banana', 4.50).preco         # 4.5

Import: from abc import ABC, abstractmethod
"""

from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def processar(self) -> str:
        ...


class PagamentoCartao(Pagamento):
    def __init__(self, bandeira: str) -> None:
        ...

    def processar(self) -> str:
        ...


class PagamentoPix(Pagamento):
    def processar(self) -> str:
        ...


class Produto(ABC):
    @property
    @abstractmethod
    def preco(self) -> float:
        ...


class Frutas(Produto):
    def __init__(self, nome: str, preco: float) -> None:
        ...

    @property
    def preco(self) -> float:
        ...