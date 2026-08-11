"""
EXERCÍCIO 01 - Classes, __init__ e self

Tópicos: class, __init__, self, atributos de instância, métodos
Aulas: 129-130

Crie a classe `Pessoa`, o primeiro contato com programação orientada
a objetos: uma classe é o molde e as instâncias são os objetos criados
a partir dela.

1. Classe `Pessoa`:
   - `__init__(self, nome: str, sobrenome: str) -> None`
     - Recebe nome e sobrenome e guarda como atributos de instância
     - Atributos: `self.nome`, `self.sobrenome`
   - `nome_completo(self) -> str`
     - Retorna o nome e o sobrenome separados por um espaço
   - `__repr__(self) -> str`
     - Retorna Pessoa(nome='...', sobrenome='...') para depuração

Comportamento esperado:
    p = Pessoa('Maria', 'Silva')
    p.nome_completo()  # 'Maria Silva'
"""


class Pessoa:
    def __init__(self, nome: str, sobrenome: str) -> None:
        ...

    def nome_completo(self) -> str:
        ...

    def __repr__(self) -> str:
        ...