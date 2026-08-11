"""
Gabarito EXERCÍCIO 03 - Atributos de Classe e de Instância

Raciocínio sênior
-----------------
Atributo de classe (ano_atual) é dado COMPARTILHADO: um só valor
para todas as instâncias, acessível por Aluno.ano_atual. Atributo
de instância (nome, idade) é dado PARTICULAR de cada objeto.
ano_nascimento usa self.__class__.ano_atual — explicitamente a
CLASSE (não a instância) — porque o valor está na classe; assim,
se uma subclasse mudar o ano, o cálculo acompanha.
vars() é a forma canônica de "ver o dict interno" da instância;
Aluno(**dados) espalha o dict no construtor — a ponte entre
dicionário e objeto (e o inverso de vars()).
Alternativas descartadas: hardcode 2026 dentro do método (perde a
fonte única de verdade — se o ano mudar, muda em um lugar só).
"""


class Aluno:
    """Aluno com atributo de classe (ano_atual) e de instancia (nome, idade)."""

    ano_atual: int = 2026

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self) -> int:
        """Calcula o ano de nascimento usando o atributo de classe.

        Exemplos:
        >>> aluno = Aluno('Ana', 20)
        >>> aluno.ano_nascimento()
        2006
        """
        return self.__class__.ano_atual - self.idade

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Aluno('Ana', 20)
        Aluno(nome='Ana', idade=20)
        """
        return f'Aluno(nome={self.nome!r}, idade={self.idade})'


def instancia_do_dicionario(dados: dict[str, str | int]) -> Aluno:
    """Constroi um Aluno expandindo o dicionario com **.

    Exemplos:
    >>> instancia_do_dicionario({'nome': 'Ana', 'idade': 20})
    Aluno(nome='Ana', idade=20)
    """
    return Aluno(**dados)


def atributos_do_objeto(aluno: Aluno) -> dict:
    """Retorna apenas os atributos de instancia com vars().

    Exemplos:
    >>> atributos_do_objeto(Aluno('Ana', 20))
    {'nome': 'Ana', 'idade': 20}
    """
    return vars(aluno)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - usou self.ano_atual em vez de self.__class__.ano_atual (na
#   prática dá o mesmo... até uma subclasse mudar o atributo da
#   classe — aí self.__class__ acompanha, self não)
# - criou ano_atual dentro do __init__ (vira atributo de
#   instância; o enunciado pede atributo de classe)
# - tentou reconstruir o objeto com dict fixo em vez de
#   Aluno(**dados) (espalhar o dict é o padrão de "dict -> objeto")