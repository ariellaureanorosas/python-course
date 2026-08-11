"""
EXERCÍCIO 06 - @staticmethod: funções utilitárias dentro da classe

Tópicos: @staticmethod, method vs classmethod vs staticmethod
Aulas: 139-140

Um método estático é uma função comum que vive DENTRO da classe:
não recebe self nem cls, não acessa atributos do objeto nem da classe.
Use para validações e cálculos utilitários ligados ao domínio da classe.

1. Classe `Conexao`:
   - `__init__(self, host: str) -> None`
     - Guarda `self.host` e inicializa `self.usuario = None`
   - `@staticmethod _credenciais_validas(usuario: str, senha: str) -> bool`
     - Retorna True se usuario tiver 3+ caracteres E senha tiver 6+
     - É "privada" por convenção (underscore), usada só internamente
   - `@classmethod criar_com_credenciais(cls, host: str, usuario: str, senha: str) -> 'Conexao'`
     - Usa o método estático para validar
     - Se inválidas, levanta ValueError('Credenciais inválidas')
     - Se válidas, cria a Conexao com cls(host), define o usuário e retorna

Comportamento esperado:
    Conexao.criar_com_credenciais('localhost', 'ana', 'senha123')
    # Conexao(host='localhost', usuario='ana')
    Conexao.criar_com_credenciais('localhost', 'an', '123')
    # ValueError: Credenciais inválidas

Dica: depois de criar a instância com cls(host), atribua usuario,
como faria com uma instância normal: conexao.usuario = usuario.
"""


class Conexao:
    def __init__(self, host: str) -> None:
        ...

    @staticmethod
    def _credenciais_validas(usuario: str, senha: str) -> bool:
        ...

    @classmethod
    def criar_com_credenciais(
        cls,
        host: str,
        usuario: str,
        senha: str,
    ) -> 'Conexao':
        ...

    def __repr__(self) -> str:
        ...