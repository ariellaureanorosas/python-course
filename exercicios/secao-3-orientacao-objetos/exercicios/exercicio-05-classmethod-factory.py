"""
EXERCÍCIO 05 - @classmethod e factory methods

Tópicos: @classmethod, cls, factory methods (métodos fábrica)
Aulas: 138

Um factory method é um método de classe que fabrica instâncias com
configurações prontas. Ele recebe `cls` (a própria classe) e chama
`cls(...)` para criar o objeto — assim funciona até em subclasses.

1. Classe `Pessoa`:
   - `__init__(self, nome: str | None, idade: int) -> None`
     - nome pode ser None (pessoa sem nome registrado)
   - `__repr__(self) -> str` retornando Pessoa(nome='...', idade=...)
   - `@classmethod criar_com_50_anos(cls, nome: str) -> 'Pessoa'`
     - Retorna cls(nome, 50) — uma pessoa fabricada com 50 anos
   - `@classmethod criar_sem_nome(cls, idade: int) -> 'Pessoa'`
     - Retorna cls(None, idade) — uma pessoa sem nome

Comportamento esperado:
    Pessoa.criar_com_50_anos('Maria')  # Pessoa(nome='Maria', idade=50)
    Pessoa.criar_sem_nome(30)          # Pessoa(nome=None, idade=30)

Dica: o primeiro parâmetro de um classmethod se chama `cls`, e serve
para chamar `cls(...)` em vez de `Pessoa(...)`.
"""


class Pessoa:
    def __init__(self, nome: str | None, idade: int) -> None:
        ...

    def __repr__(self) -> str:
        ...

    @classmethod
    def criar_com_50_anos(cls, nome: str) -> 'Pessoa':
        ...

    @classmethod
    def criar_sem_nome(cls, idade: int) -> 'Pessoa':
        ...