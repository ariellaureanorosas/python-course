"""
EXERCÍCIO 03 - Atributos de classe vs atributos de instância

Tópicos: atributos de classe, atributos de instância, vars(), dict
Aulas: 135-136

Atributos de classe pertencem ao molde (classe) e são compartilhados
por todas as instâncias; atributos de instância pertencem a cada objeto.
Use ambos na classe `Aluno` e pratique a introspecção com vars()/__dict__.

1. Classe `Aluno`:
   - Atributo de classe `ano_atual: int = 2026`
   - `__init__(self, nome: str, idade: int) -> None`
     - Guarda nome e idade como atributos de instância
   - `ano_nascimento(self) -> int`
     - Calcula ano_atual - idade (acesse o atributo de classe)
   - `__repr__(self) -> str`
     - Retorna Aluno(nome='...', idade=...)

2. Função `instancia_do_dicionario(dados: dict[str, str | int]) -> Aluno`
   - Constrói um Aluno a partir de um dicionário usando expandir com **
   - Exemplo: instancia_do_dicionario({'nome': 'Ana', 'idade': 20})

3. Função `atributos_do_objeto(aluno: Aluno) -> dict`
   - Retorna vars(aluno), ou seja, apenas os atributos de instância

Comportamento esperado:
    aluno = Aluno('Ana', 20)
    aluno.ano_nascimento()  # 2006
    atributos_do_objeto(aluno)  # {'nome': 'Ana', 'idade': 20}
"""


class Aluno:
    ano_atual: int = 2026

    def __init__(self, nome: str, idade: int) -> None:
        ...

    def ano_nascimento(self) -> int:
        ...

    def __repr__(self) -> str:
        ...


def instancia_do_dicionario(dados: dict[str, str | int]) -> Aluno:
    ...


def atributos_do_objeto(aluno: Aluno) -> dict:
    ...