"""
Gabarito EXERCÍCIO 05 - Classmethod como Factory

Raciocínio sênior
-----------------
A fábrica (factory) centraliza CONFIGURAÇÕES PRONTAS de criação:
criar_com_50_anos e criar_sem_nome são nomes que explicam a
intenção, enquanto Pessoa(None, 50) esconderia o propósito.
O classmethod recebe cls e retorna cls(...) — NÃO Pessoa(...):
se uma subclasse herdar, a fábrica devolve a subclasse (esse é o
ponto do cls). O __init__ aceita nome: str | None porque a
fábrica gera pessoa sem nome (contrato explícito na tipagem).
Alternativas descartadas: staticmethod (não recebe cls e
devolveria a classe fixa); factory como função solta fora da classe.
"""


class Pessoa:
    """Pessoa com factory methods para criacao com configuracoes prontas."""

    def __init__(self, nome: str | None, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome: str) -> 'Pessoa':
        """Fabrica uma pessoa ja com 50 anos.

        Exemplos:
        >>> Pessoa.criar_com_50_anos('Maria')
        Pessoa(nome='Maria', idade=50)
        """
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade: int) -> 'Pessoa':
        """Fabrica uma pessoa sem nome registrado.

        Exemplos:
        >>> Pessoa.criar_sem_nome(30)
        Pessoa(nome=None, idade=30)
        """
        return cls(None, idade)

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Pessoa('Maria', 50)
        Pessoa(nome='Maria', idade=50)
        """
        return f'Pessoa(nome={self.nome!r}, idade={self.idade})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - escreveu return Pessoa(...) dentro do classmethod — com
#   herança, a subclasse chamaria a fábrica e receberia a classe
#   errada; cls resolve isso
# - usou staticmethod (não recebe cls; o retorno fixa a classe)
# - criou a configuração na mão em cada chamada
#   (Pessoa('Maria', 50) repetido) em vez de nomear a intenção
#   com a fábrica