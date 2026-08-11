"""
Gabarito EXERCÍCIO 12 - Composição

Raciocínio sênior
-----------------
Composição = a parte NÃO EXISTE sem o todo: o Endereco nasce
DENTRO do Cliente (Endereco(...) no __init__) e morre com ele.
O cliente não recebe um endereço pronto — ele CONSTRÓI o próprio.
Composição é o relacionamento mais forte: ciclo de vida atado.
Na associação (exercício 10) a parte é injetada e sobrevive; na
composição a parte é criada dentro e não tem vida própria — a
pergunta "quem cria?" separa os dois conceitos. O __init__ do
Cliente não recebe um Endereco e sim os DADOS dele (rua, numero,
cidade) — é a classe do todo que decide quando montar a parte.
"""


class Endereco:
    """Endereco que nasce DENTRO do cliente (composicao)."""

    def __init__(self, rua: str, numero: int, cidade: str) -> None:
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Endereco('Rua das Flores', 123, 'São Paulo')
        Endereco(rua='Rua das Flores', numero=123, cidade='São Paulo')
        """
        return (
            f'Endereco(rua={self.rua!r}, numero={self.numero}, '
            f'cidade={self.cidade!r})'
        )


class Cliente:
    """Cliente que possui um Endereco proprio e exclusivo."""

    def __init__(self, nome: str, rua: str, numero: int, cidade: str) -> None:
        self.nome = nome
        self.endereco = Endereco(rua, numero, cidade)  # composicao

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Cliente('Maria', 'Rua das Flores', 123, 'São Paulo')
        Cliente(nome='Maria', endereco=Endereco(rua='Rua das Flores', numero=123, cidade='São Paulo'))
        """
        return f'Cliente(nome={self.nome!r}, endereco={self.endereco!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - recebeu o Endereco pronto no __init__ (isso é ASSOCIAÇÃO:
#   a parte chega de fora; na composição o todo constrói)
# - criou o endereço fora e passou por setter — mesma confusão
#   agregar/compor: o teste é "a parte sobrevive sem o todo?"
# - deixou endereco público gravável (cliente.endereco = outro —
#   no gabarito o endereço nasce no construtor e não muda)