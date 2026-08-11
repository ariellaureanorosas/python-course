"""
EXERCÍCIO 13 - Herança, super() e sobreposição de métodos

Tópicos: herança, super(), override (sobreposição), polimorfismo básico
Aulas: 148

Herança é "é um": Carro É UM Veiculo. A subclasse herda atributos e
métodos da superclasse, pode ADICIONAR os seus e SOBREPOR (override)
métodos herdados — chamando o original via super() quando precisar.

1. Classe `Veiculo`:
   - `__init__(self, marca: str, modelo: str) -> None`
   - `descricao(self) -> str` retorna '<marca> <modelo>'
   - `mover(self) -> str` retorna 'O veículo está se movendo'
   - `__repr__(self) -> str` retornando Veiculo(marca='...', modelo='...')

2. Classe `Carro(Veiculo)`:
   - `__init__(self, marca: str, modelo: str, portas: int) -> None`
     - Chama super().__init__(marca, modelo) — NÃO repita a atribuição
     - Guarda `self.portas`
   - `mover(self) -> str` retorna '<resultado de super().mover()> sobre 4 rodas'

3. Classe `Moto(Veiculo)`:
   - `__init__(self, marca: str, modelo: str, cilindradas: int) -> None`
     - Chama super().__init__(marca, modelo) e guarda `self.cilindradas`
   - `mover(self) -> str` retorna '<resultado de super().mover()> sobre 2 rodas'

Comportamento esperado:
    carro = Carro('Fiat', 'Uno', 4)
    carro.descricao()   # 'Fiat Uno'
    carro.mover()       # 'O veículo está se movendo sobre 4 rodas'
    carro.portas        # 4

Dica: super().__init__(...) executa o __init__ da classe pai, evitando
duplicar a linha `self.marca = marca`.
"""


class Veiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        ...

    def descricao(self) -> str:
        ...

    def mover(self) -> str:
        ...

    def __repr__(self) -> str:
        ...


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        ...

    def mover(self) -> str:
        ...


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cilindradas: int) -> None:
        ...

    def mover(self) -> str:
        ...