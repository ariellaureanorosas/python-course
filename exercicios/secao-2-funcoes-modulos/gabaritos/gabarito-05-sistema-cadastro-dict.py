"""
Gabarito 05 - Sistema de Cadastro com Dict
"""
from copy import deepcopy


def criar_pessoa(nome: str, idade: int, email: str) -> dict:
    """Cria um dicionário representando uma pessoa.

    Exemplo:
        >>> criar_pessoa("Ana", 25, "ana@email.com")
        {'nome': 'Ana', 'idade': 25, 'email': 'ana@email.com'}
    """
    return {
        "nome": nome,
        "idade": idade,
        "email": email,
    }


def atualizar_pessoa(pessoa: dict, **dados) -> dict:
    """Atualiza os dados de uma pessoa usando update() e retorna uma cópia.

    Exemplo:
        >>> p = criar_pessoa("Ana", 25, "ana@email.com")
        >>> atualizar_pessoa(p, idade=26, email="ana.nova@email.com")
        {'nome': 'Ana', 'idade': 26, 'email': 'ana.nova@email.com'}
    """
    pessoa_atualizada = deepcopy(pessoa)
    pessoa_atualizada.update(dados)
    return pessoa_atualizada


def listar_chaves(pessoa: dict) -> list:
    """Retorna uma lista das chaves do dicionário.

    Exemplo:
        >>> p = criar_pessoa("Ana", 25, "ana@email.com")
        >>> listar_chaves(p)
        ['nome', 'idade', 'email']
    """
    return list(pessoa.keys())
