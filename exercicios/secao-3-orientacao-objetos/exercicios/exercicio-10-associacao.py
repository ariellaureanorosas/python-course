"""
EXERCÍCIO 10 - Associação entre classes

Tópicos: associação, atributo privado __, @property + @setter
Aulas: 144

Associação é a relação mais simples entre objetos: uma classe
REFERENCIA outra, mas cada uma vive de forma independente — o
Escritor pode trocar de ferramenta, e a ferramenta existe mesmo
sem o escritor.

1. Classe `FerramentaDeEscrever`:
   - `__init__(self, nome: str) -> None` guarda `self.__nome`
   - `@property nome -> str`
   - `escrever(self) -> str` retorna '<nome> está escrevendo'

2. Classe `Escritor`:
   - `__init__(self, nome: str) -> None`
     - Guarda `self.__nome` e inicia `self.__ferramenta = None` (ainda sem ferramenta)
   - `@property nome -> str`
   - `@property ferramenta -> FerramentaDeEscrever | None`
   - `@ferramenta.setter ferramenta(ferramenta: FerramentaDeEscrever | None) -> None`
   - `escrever(self) -> str`:
     - Se não tiver ferramenta, retorna '<nome> precisa de uma ferramenta'
     - Se tiver, retorna '<nome> está escrevendo com <ferramenta que escreve>'

Comportamento esperado:
    escritor = Escritor('Machado de Assis')
    caneta = FerramentaDeEscrever('Caneta Bic')
    escrito = escritor.escrever()      # 'Machado de Assis precisa de uma ferramenta'
    escritor.ferramenta = caneta       # associação: referência a outro objeto
    escritor.escrever()                # 'Machado de Assis está escrevendo com Caneta Bic está escrevendo'
"""


class FerramentaDeEscrever:
    def __init__(self, nome: str) -> None:
        ...

    @property
    def nome(self) -> str:
        ...

    def escrever(self) -> str:
        ...


class Escritor:
    def __init__(self, nome: str) -> None:
        ...

    @property
    def nome(self) -> str:
        ...

    @property
    def ferramenta(self) -> 'FerramentaDeEscrever | None':
        ...

    @ferramenta.setter
    def ferramenta(self, ferramenta: 'FerramentaDeEscrever | None') -> None:
        ...

    def escrever(self) -> str:
        ...