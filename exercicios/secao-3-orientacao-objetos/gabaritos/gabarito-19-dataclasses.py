"""
Gabarito EXERCÍCIO 19 - Dataclasses

Raciocínio sênior
-----------------
A dataclass GERA o boilerplate (__init__, __repr__, __eq__)
a partir das anotações de tipo — você declara os campos, ela
escreve a classe. frozen=True dá imutabilidade (como uma tupla
tipada: atribuir lança FrozenInstanceError); order=True gera
todas as comparações a partir da ordem dos campos.
field(default_factory=list) é OBRIGATÓRIO para valores mutáveis:
list = [] como default seria COMPARTILHADO entre instâncias
(péssima pegadinha). repr=False esconde o campo do repr.
total como @property calcula na hora, sem estado desatualizado.
Alternativas descartadas: dataclass sem frozen/order (o enunciado
pede comportamento de imutável e ordenável).
"""

from dataclasses import asdict, dataclass, field


@dataclass(frozen=True, order=True)
class Produto:
    """Produto imutavel e ordenavel, com categorias nao exibidas no repr."""

    nome: str
    preco: float
    categorias: list[str] = field(default_factory=list, repr=False)


@dataclass(frozen=True)
class Pedido:
    """Pedido imutavel que agrega produtos e calcula o total."""

    numero: int
    produtos: list[Produto] = field(default_factory=list)

    @property
    def total(self) -> float:
        """Soma dos precos dos produtos.

        Exemplos:
        >>> pedido = Pedido(1, [Produto('Caneta', 3.50), Produto('Caderno', 12.90)])
        >>> pedido.total
        16.4
        """
        return sum(produto.preco for produto in self.produtos)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - escreveu categorias: list[str] = [] — o MESMO list é
#   compartilhado por todas as instâncias (adicionar categoria num
#   produto apareceria nos outros); default_factory cria uma por
#   instância
# - esqueceu order=True/frozen=True (o enunciado pede produto
#   imutável e ordenável; sem isso default de dataclass)
# - guardou self.total no __init__ (property calcula na hora e
#   nunca desatualiza; além disso frozen não deixa setar depois)