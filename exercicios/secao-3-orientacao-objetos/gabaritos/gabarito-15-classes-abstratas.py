"""
Gabarito EXERCÍCIO 15 - Classes Abstratas (ABC)

Raciocínio sênior
-----------------
Uma classe abstrata é um CONTRATO: @abstractmethod define o QUE
toda subclasse deve implementar (processar, preco) sem importar o
COMO. Conseguência do design: é impossível instanciar Pagamento()
— TypeError na hora; o Python impõe o contrato em vez de confiar
no programador. Subclasse que esquecer o método também não
instancia (falha cedo, não tarde).
Propriedade abstrata usa a ordem @property POR CIMA de
@abstractmethod — a subclasse implementa a property e o acesso
virar preco (sem parênteses) igual a atributo. O cliente do
código trata todas as subclasses igualmente (polimorfismo
garantido pelo contrato).
"""

from abc import ABC, abstractmethod


class Pagamento(ABC):
    """Contrato de pagamento: subclasses implementam processar()."""

    @abstractmethod
    def processar(self) -> str:
        """Processa o pagamento na forma definida pela subclasse."""


class PagamentoCartao(Pagamento):
    """Pagamento com cartao de determinada bandeira."""

    def __init__(self, bandeira: str) -> None:
        self.bandeira = bandeira

    def processar(self) -> str:
        """Processa o pagamento no cartao.

        Exemplos:
        >>> PagamentoCartao('Visa').processar()
        'Pagamento com cartão Visa processado'
        """
        return f'Pagamento com cartão {self.bandeira} processado'


class PagamentoPix(Pagamento):
    """Pagamento instantaneo via Pix."""

    def processar(self) -> str:
        """Processa o pagamento via Pix.

        Exemplos:
        >>> PagamentoPix().processar()
        'Pagamento via Pix processado'
        """
        return 'Pagamento via Pix processado'


class Produto(ABC):
    """Contrato de produto: subclasses expoem o preco como property."""

    @property
    @abstractmethod
    def preco(self) -> float:
        """Preco do produto (property abstrata)."""


class Frutas(Produto):
    """Produto concreto com preco em property."""

    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self._preco = preco

    @property
    def preco(self) -> float:
        """Retorna o preco da fruta.

        Exemplos:
        >>> Frutas('Banana', 4.50).preco
        4.5
        """
        return self._preco


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - herdou de object ou não usou ABC (abstrato de verdade só
#   existe com ABC/abstractmethod; sem ele instanciaria Pagamento)
# - organizou @abstractmethod POR CIMA de @property (a ordem
#   invertida quebra — o decorator abstrato precisa ser o externo)
# - implementou processar() com pass na base em vez de
#   @abstractmethod (contrato fraco: subclasse pode "esquecer"
#   e ninguém avisa)