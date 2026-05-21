"""
Gabarito 03 - Closure para Criar Saudação
"""


def criar_saudacao(saudacao: str):
    """Retorna uma função que saúda uma pessoa com a saudação fornecida.

    Exemplos:
        >>> saudar = criar_saudacao("Olá")
        >>> saudar("João")
        'Olá João'
        >>> criar_saudacao("Bom dia")("Maria")
        'Bom dia Maria'
    """
    def saudar(nome: str) -> str:
        return f"{saudacao} {nome}"

    return saudar
