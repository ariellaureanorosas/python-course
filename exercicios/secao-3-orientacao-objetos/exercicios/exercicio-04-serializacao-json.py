"""
EXERCÍCIO 04 - Serializando instâncias para JSON e de volta

Tópicos: vars(), json.dump, json.load, Path, expandir com **
Aulas: 137

Serializar = transformar um objeto em texto (JSON) para salvar em
arquivo. Desserializar = reconstruir o objeto a partir do texto.
Use `vars(instancia)` para obter o dicionário de atributos e
`Pessoa(**dados)` para reconstruir.

1. Classe `Pessoa`:
   - `__init__(self, nome: str, idade: int) -> None`
   - `__repr__(self) -> str` retornando Pessoa(nome='...', idade=...)
   - `para_dicionario(self) -> dict[str, str | int]` retornando vars(self)

2. Função `salvar_pessoas(caminho: str | Path, pessoas: list[Pessoa]) -> None`
   - Abre o arquivo em modo escrita com encoding='utf-8'
   - Grava a lista de dicionários com json.dump(indent=2, ensure_ascii=False)

3. Função `carregar_pessoas(caminho: str | Path) -> list[Pessoa]`
   - Abre o arquivo em modo leitura com encoding='utf-8'
   - Lê a lista de dicionários com json.load
   - Reconstrói cada Pessoa com Pessoa(**dicionario)

Formato do arquivo:
    [
      {"nome": "Maria", "idade": 30},
      {"nome": "João", "idade": 25}
    ]

Dica: use open() ou Path.read_text()/write_text() com json.loads/json.dumps.
"""

from pathlib import Path


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        ...

    def para_dicionario(self) -> dict[str, str | int]:
        ...

    def __repr__(self) -> str:
        ...


def salvar_pessoas(caminho: str | Path, pessoas: list[Pessoa]) -> None:
    ...


def carregar_pessoas(caminho: str | Path) -> list[Pessoa]:
    ...