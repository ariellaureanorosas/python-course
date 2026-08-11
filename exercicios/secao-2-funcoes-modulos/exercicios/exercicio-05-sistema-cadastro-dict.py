"""
EXERCÍCIO 05 - Sistema de Cadastro com Dict

Tópicos: criação de dict, update(), keys(), **kwargs

Crie três funções:

1. `criar_pessoa(nome: str, idade: int, email: str) -> dict`
   - Retorna um dict com as chaves 'nome', 'idade', 'email'

2. `atualizar_pessoa(pessoa: dict, **dados) -> dict`
   - Usa o método update() para atualizar os dados da pessoa
   - Retorna o dict atualizado

3. `listar_chaves(pessoa: dict) -> list`
   - Retorna uma lista das chaves do dict usando keys()

Comportamento esperado:
    p1 = criar_pessoa("Ana", 25, "ana@email.com")
    p2 = atualizar_pessoa(p1, idade=26)
    listar_chaves(p2)   # ['nome', 'idade', 'email']

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def criar_pessoa(nome: str, idade: int, email: str) -> dict:
    ...


def atualizar_pessoa(pessoa: dict, **dados) -> dict:
    ...


def listar_chaves(pessoa: dict) -> list:
    ...


if __name__ == "__main__":
    p1 = criar_pessoa("Ana", 25, "ana@email.com")
    p2 = atualizar_pessoa(p1, idade=26)
    print(p2)
    print(listar_chaves(p2))