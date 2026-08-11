"""
Gabarito EXERCÍCIO 01 - Classes, __init__ e self

Raciocínio sênior
-----------------
__init__ NÃO cria o objeto: ele inicializa o estado da instância
já criada. Por isso todo atributo que a classe precisa nasce
dentro dele — criar atributo fora (p.idade = 20 depois) quebra o
contrato da classe e confunde quem lê.
__repr__ é a representação para o DESENVOLVEDOR (depuração);
__str__ é para o usuário final. Aqui só o repr é necessário — e é
ele que o doctest captura.
Alternativas descartadas: nome_completo com concatenação manual
(" ".join além do necessário); __init__ sem default preservando
estado (o estado nasce no construtor, não fora).
"""


class Pessoa:
    """Representa uma pessoa com nome e sobrenome."""

    def __init__(self, nome: str, sobrenome: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_completo(self) -> str:
        """Retorna o nome e o sobrenome separados por um espaco.

        Exemplos:
        >>> p = Pessoa('Maria', 'Silva')
        >>> p.nome_completo()
        'Maria Silva'
        """
        return f'{self.nome} {self.sobrenome}'

    def __repr__(self) -> str:
        """Representacao facil de ler para depuracao.

        Exemplos:
        >>> Pessoa('Maria', 'Silva')
        Pessoa(nome='Maria', sobrenome='Silva')
        """
        return f'Pessoa(nome={self.nome!r}, sobrenome={self.sobrenome!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - usou __str__ onde o enunciado pedia __repr__ (ou os dois
#   idênticos — o doctest quebra, pois print usa __str__ e o
#   repr do console usa __repr__)
# - criou self.idade fora do __init__ ("p = Pessoa('Maria');
#   p.idade = 20") — estado espalhado em vez de nascer no
#   construtor
# - esqueceu o !r no __repr__ (repr é sobre precisão, não beleza:
#   '{self.nome!r}' mostra as aspas, '{self.nome}' não)