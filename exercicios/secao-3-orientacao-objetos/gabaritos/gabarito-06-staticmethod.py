"""
Gabarito EXERCÍCIO 06 - Staticmethod e Classmethod

Raciocínio sênior
-----------------
O staticmethod é uma FUNÇÃO QUE NÃO PRECISA DE self NEM de cls:
_credenciais_validas só decide sobre o ARGUMENTO (usuario/senha),
não sobre o estado da conexão — por isso não recebe a instância.
Já criar_com_credenciais é classmethod: precisa de cls porque
CONSTRÓI a conexão (e devolveria a subclasse certa em herança).
A validação acontece ANTES de criar (fail fast): a fábrica é o
único caminho para criar conexão com credenciais, e é ela quem
garante o contrato.
O _ (undescore) em _credenciais_validas marca "uso interno" por
convenção — não é privado de verdade (isso não existe em Python).
Alternativas descartadas: staticmethod que retorna instância
(para isso existe classmethod); validação dentro do __init__
(quem criasse conexão direto burlaria a regra).
"""


class Conexao:
    """Conexao com metodo estatico de validacao e factory com classmethod."""

    def __init__(self, host: str) -> None:
        self.host = host
        self.usuario = None

    @staticmethod
    def _credenciais_validas(usuario: str, senha: str) -> bool:
        """Valida tamanho minimo de usuario e senha (metodo estatico).

        Exemplos:
        >>> Conexao._credenciais_validas('ana', 'senha123')
        True
        >>> Conexao._credenciais_validas('an', '123')
        False
        """
        return len(usuario) >= 3 and len(senha) >= 6

    @classmethod
    def criar_com_credenciais(
        cls,
        host: str,
        usuario: str,
        senha: str,
    ) -> 'Conexao':
        """Cria uma conexao validando as credenciais antes.

        Raises:
            ValueError: Se usuario ou senha forem invalidos.

        Exemplos:
        >>> Conexao.criar_com_credenciais('localhost', 'ana', 'senha123')
        Conexao(host='localhost', usuario='ana')
        >>> Conexao.criar_com_credenciais('localhost', 'an', '123')
        Traceback (most recent call last):
        ...
        ValueError: Credenciais inválidas
        """
        if not cls._credenciais_validas(usuario, senha):
            raise ValueError('Credenciais inválidas')

        conexao = cls(host)
        conexao.usuario = usuario
        return conexao

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Conexao('localhost')
        Conexao(host='localhost', usuario=None)
        """
        return f'Conexao(host={self.host!r}, usuario={self.usuario!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - usou classmethod para _credenciais_validas (não usa cls; virar
#   staticmethod elimina o parâmetro e deixa a intenção clara)
# - usou staticmethod para criar_com_credenciais (retorna cls(...);
#   sem cls, a fábrica fixaria a classe errada em herança)
# - validou credenciais só no setter posterior (criou a conexão
#   com dados inválidos e validou depois — fail fast é antes)