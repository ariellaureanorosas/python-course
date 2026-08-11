"""
EXERCÍCIO 32 - Documentando Código (docstrings)

Tópicos: docstrings, documentação, doctest
Aulas: 169 (docstrings-documentacao)

A docstring é a primeira string após a definição — vira o `__doc__`
do objeto e é o que o `help()` e as IDEs exibem. Documentar bem é
escrever o CONTRATO: o que a função faz, parâmetros, retorno — e
exemplos que podem ser executados com `doctest`.

1. Função `soma(x, y)`:
   - type hints `(x: float, y: float) -> float`
   - docstring: resumo em 1 linha + exemplos executáveis:
       >>> soma(1, 2)
       3
       >>> soma(-1, 1)
       0
   - retorna `x + y`

2. Função `subtracao(x, y)`:
   - type hints `(x: float, y: float) -> float`
   - docstring com exemplo: `subtracao(5, 2)` → `3`
   - retorna `x - y`

3. Função `multiplica(x, y, z=None)`:
   - type hints `(x: float, y: float, z: float | None = None) -> int | float`
   - docstring VÁRIAS linhas documentando o parâmetro opcional:
       >>> multiplica(2, 3)
       6
       >>> multiplica(2, 3, 4)
       24
   - sem `z`: retorna `x * y`; com `z`: retorna `x * y * z`

4. Classe `Pessoa` com docstring no estilo Google:
   - módulo: docstring de 1 linha no topo do arquivo
   - classe: docstring explicando o que representa
   - `__init__(self, nome: str, idade: int)`: docstring com `:param`
   - `saudacao(self) -> str`: retorna `f"Ola, meu nome e {self.nome}"`
     e docstring com exemplo:
       >>> Pessoa('Ana', 30).saudacao()
       'Ola, meu nome e Ana'
   - `@classmethod anonimo(cls) -> 'Pessoa'`: retorna `cls('Anonimo', 0)`
   - `@staticmethod mensagem_fixa() -> str`: retorna
     `'Este e um metodo estatico'`
   - `@property nome_e_idade -> str`: retorna
     `f"{self.nome} tem {self.idade} anos"` com exemplo:
       >>> Pessoa('Ana', 30).nome_e_idade
       'Ana tem 30 anos'

Comportamento esperado (fluxo de uso):
    soma(1, 2)            # 3
    subtracao(5, 2)       # 3
    multiplica(2, 3)      # 6
    multiplica(2, 3, 4)   # 24
    Pessoa('Ana', 30).saudacao()      # 'Ola, meu nome e Ana'
    Pessoa.anonimo().nome             # 'Anonimo'
    Pessoa('Ana', 30).nome_e_idade    # 'Ana tem 30 anos'

Observações:
  - Docstring NÃO é comentário: use três aspas logo após `def`/`class`
  - Os exemplos dentro da docstring (`>>>`) rodam com doctest —
    escreva docstrings testáveis
  - Use nomes ASCII nos dados e nos exemplos (aula 169 usa 'Anônimo',
    mas o doctest compara bytes — evite acentos)
"""


def soma(x: float, y: float) -> float:
    ...


def subtracao(x: float, y: float) -> float:
    ...


def multiplica(x: float, y: float, z: float | None = None) -> int | float:
    ...


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        ...

    def saudacao(self) -> str:
        ...

    @classmethod
    def anonimo(cls) -> "Pessoa":
        ...

    @staticmethod
    def mensagem_fixa() -> str:
        ...

    @property
    def nome_e_idade(self) -> str:
        ...