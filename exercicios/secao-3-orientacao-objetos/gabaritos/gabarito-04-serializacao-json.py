"""
Gabarito EXERCÍCIO 04 - Serialização JSON

Raciocínio sênior
-----------------
JSON só entende tipos nativos; um objeto Pessoa não é nativo. O
padrão é converter em uma ponta (vars(self) -> dict) e reconstruir
na outra (Pessoa(**dicionario) — o inverso do vars). As duas
funções são ESPELHADAS: salvar_pessoas serializa, carregar_pessoas
desserializa; a ida e a volta preservam os dados.
ensure_ascii=False + encoding='utf-8' preserva nomes acentuados
("João" não vira \\uXXXX). pathlib.Path como aceito no tipo
(caminho: str | Path) permite os dois jeitos de passar caminho.
Alternativas descartadas: pickle (binário, não legível — o
enunciado pede JSON); json.dumps manual com append de linhas.
"""

import json
import os
import tempfile
from pathlib import Path


class Pessoa:
    """Pessoa serializavel para JSON via vars()."""

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def para_dicionario(self) -> dict[str, str | int]:
        """Converte os atributos de instancia em dicionario.

        Exemplos:
        >>> Pessoa('Maria', 30).para_dicionario()
        {'nome': 'Maria', 'idade': 30}
        """
        return vars(self)

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Pessoa('Maria', 30)
        Pessoa(nome='Maria', idade=30)
        """
        return f'Pessoa(nome={self.nome!r}, idade={self.idade})'


def salvar_pessoas(caminho: str | Path, pessoas: list[Pessoa]) -> None:
    """Salva uma lista de pessoas em arquivo JSON.

    Parametros:
        caminho: Caminho do arquivo de saida.
        pessoas: Lista de pessoas a persistir.

    Exemplos:
    >>> tmp = tempfile.mktemp(suffix='.json')
    >>> salvar_pessoas(tmp, [Pessoa('Maria', 30), Pessoa('João', 25)])
    >>> carregar_pessoas(tmp)
    [Pessoa(nome='Maria', idade=30), Pessoa(nome='João', idade=25)]
    >>> os.remove(tmp)
    """
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(
            [pessoa.para_dicionario() for pessoa in pessoas],
            arquivo,
            indent=2,
            ensure_ascii=False,
        )


def carregar_pessoas(caminho: str | Path) -> list[Pessoa]:
    """Carrega uma lista de pessoas de um arquivo JSON.

    Parametros:
        caminho: Caminho do arquivo JSON.

    Returns:
        Lista de pessoas reconstruidas com Pessoa(**dicionario).

    Exemplos:
    >>> tmp = tempfile.mktemp(suffix='.json')
    >>> with open(tmp, 'w', encoding='utf-8') as arquivo:
    ...     json.dump([{'nome': 'Ana', 'idade': 40}], arquivo)
    >>> carregar_pessoas(tmp)
    [Pessoa(nome='Ana', idade=40)]
    >>> os.remove(tmp)
    """
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    return [Pessoa(**pessoa) for pessoa in dados]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - guardou as pessoas como listas soltas no JSON em vez do dict
#   de cada uma (json.dump([pessoa.para_dicionario() ...]))
# - esqueceu ensure_ascii=False — "João" vira \u00c3\u00a3... no
#   arquivo (ilegível para humanos, e o doctest quebra)
# - reconstruiu com Pessoa(nome=dados['nome'], ...) — chato e
#   frágil; Pessoa(**pessoa) espalha o dict e acompanha o construtor