"""
EXERCÍCIO 12 - Composição: Cliente e Endereço

Tópicos: composição, ciclo de vida, objeto criado DENTRO do dono
Aulas: 146

Composição é a relação mais forte: a parte (Endereco) é criada DENTRO
do todo (Cliente) e não faz sentido sozinha. Se o Cliente morre,
o Endereco morre junto.

1. Classe `Endereco`:
   - `__init__(self, rua: str, numero: int, cidade: str) -> None`
   - `__repr__(self) -> str` retornando Endereco(rua='...', numero=..., cidade='...')

2. Classe `Cliente`:
   - `__init__(self, nome: str, rua: str, numero: int, cidade: str) -> None`
     - Guarda o nome
     - Cria o Endereco DENTRO do __init__ (composição!):
       `self.endereco = Endereco(rua, numero, cidade)`
   - `__repr__(self) -> str` retornando Cliente(nome='...', endereco=...)

Comportamento esperado:
    cliente = Cliente('Maria', 'Rua das Flores', 123, 'São Paulo')
    cliente.endereco  # Endereco(rua='Rua das Flores', numero=123, cidade='São Paulo')

Diferença fundamental:
  - Aqui o Endereco NUNCA é recebido pronto: ele nasce dentro do Cliente.
  - Se criar outro Cliente, ele ganha UM ENDEREÇO NOVO — nunca
    compartilhado com o primeiro.
"""


class Endereco:
    def __init__(self, rua: str, numero: int, cidade: str) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Cliente:
    def __init__(self, nome: str, rua: str, numero: int, cidade: str) -> None:
        ...

    def __repr__(self) -> str:
        ...