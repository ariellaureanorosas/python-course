"""
Exercício 05 - Sistema de Cadastro com Dict

Crie três funções:

1. `criar_pessoa(nome: str, idade: int, email: str) -> dict`
   - Retorna um dict com as chaves 'nome', 'idade', 'email'

2. `atualizar_pessoa(pessoa: dict, **dados) -> dict`
   - Usa o método update() para atualizar os dados da pessoa
   - Retorna o dict atualizado

3. `listar_chaves(pessoa: dict) -> list`
   - Retorna uma lista das chaves do dict usando keys()

Tópicos da aula: criação de dict, update(), keys(), deepcopy, **kwargs
"""

from copy import deepcopy


def criar_pessoa(nome: str, idade: int, email: str) -> dict:
    return dict(nome=nome, idade=idade, email=email)


def atualizar_pessoa(pessoa: dict, **dados) -> dict:
    copia = deepcopy(pessoa)
    copia.update(dados)
    return copia


def listar_chaves(pessoa: dict) -> list:
    return list(pessoa.keys())


if __name__ == "__main__":
    p1 = criar_pessoa("Ana", 25, "ana@email.com")
    p2 = atualizar_pessoa(p1, idade=26, email="ana.nova@email.com")
    print(p2)
    print(listar_chaves(p2))
