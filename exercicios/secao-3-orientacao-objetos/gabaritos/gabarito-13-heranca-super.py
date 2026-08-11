"""
Gabarito EXERCÍCIO 13 - Herança e super()

Raciocínio sênior
-----------------
super() tem duas funções: inicializar o estado herdado
(super().__init__(marca, modelo) — sem isso o Carro não teria
marca) e REUTILIZAR comportamento da base (super().mover() +
" sobre 4 rodas" — especialização: a base diz o núcleo, a
subclasse incrementa). Carro e Moto herdam descricao/__repr__
sem reescrever (código compartilhado); só mover é sobrescrito.
O polimorfismo aparece pronto aqui: uma lista [Carro, Moto]
chama .mover() de cada um sem saber o tipo (cada objeto decide).
Alternativas descartadas: copiar o __init__ da base dentro das
subclasses (duplicação); moto/carro sem super() duplicando mover.
"""


class Veiculo:
    """Classe base (pai) da hierarquia de veiculos."""

    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo

    def descricao(self) -> str:
        """Retorna 'marca modelo'.

        Exemplos:
        >>> Veiculo('Fiat', 'Uno').descricao()
        'Fiat Uno'
        """
        return f'{self.marca} {self.modelo}'

    def mover(self) -> str:
        """Retorna o comportamento padrao de movimento.

        Exemplos:
        >>> Veiculo('Fiat', 'Uno').mover()
        'O veículo está se movendo'
        """
        return 'O veículo está se movendo'

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Veiculo('Fiat', 'Uno')
        Veiculo(marca='Fiat', modelo='Uno')
        """
        return f'Veiculo(marca={self.marca!r}, modelo={self.modelo!r})'


class Carro(Veiculo):
    """Carro herda de Veiculo e especializa o movimento."""

    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self.portas = portas

    def mover(self) -> str:
        """Override: aproveita a base via super() e adiciona detalhe.

        Exemplos:
        >>> Carro('Fiat', 'Uno', 4).mover()
        'O veículo está se movendo sobre 4 rodas'
        >>> Carro('Fiat', 'Uno', 4).portas
        4
        """
        return f'{super().mover()} sobre 4 rodas'


class Moto(Veiculo):
    """Moto herda de Veiculo e especializa o movimento."""

    def __init__(self, marca: str, modelo: str, cilindradas: int) -> None:
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def mover(self) -> str:
        """Override: aproveita a base via super() e adiciona detalhe.

        Exemplos:
        >>> Moto('Honda', 'CG', 160).mover()
        'O veículo está se movendo sobre 2 rodas'
        """
        return f'{super().mover()} sobre 2 rodas'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - esqueceu super().__init__(marca, modelo) no Carro — instância
#   sem marca/modelo (AttributeError ou estado vazio)
# - sobrescreveu descricao() nas subclasses em vez de herdar
#   (duplicou código que a base já entrega)
# - reescreveu mover() inteiro na subclasse sem super() (perdeu o
#   comportamento base; a especialização é base + detalhe)