"""
Gabarito EXERCÍCIO 32 - Documentando Código (docstrings)

Raciocínio sênior
-----------------
A docstring é o contrato do código: quem lê o help() nunca mais
abre a implementação para saber o que a funcao faz. Aqui ela vem
duplamente a servico: explica PARA humanos e testa COM Python —
os exemplos `>>>` dentro da docstring sao executados pelo doctest,
entao docstring desatualizada vira erro de teste, nao "explicacao
solta". O z=None documenta o argumento opcional (mesma assinatura
da aula 169); sem ele, multiplica(2, 3, 4) retornaria apenas x*y —
o segundo exemplo da docstring pega exatamente esse suposto bug.
Na classe, classmethod e property ganham docstrings proprioas
porque sao consumidores diferentes do mesmo objeto: a IDE mostra
a docstring da property no autocomplete. ASCII nos exemplos evita
falha de codificacao no doctest.
"""

from __future__ import annotations


def soma(x: float, y: float) -> float:
    """Soma dois numeros.

    Exemplos:
    >>> soma(1, 2)
    3
    >>> soma(-1, 1)
    0
    """
    return x + y


def subtracao(x: float, y: float) -> float:
    """Subtrai o segundo numero do primeiro.

    Exemplos:
    >>> subtracao(5, 2)
    3
    """
    return x - y


def multiplica(x: float, y: float, z: float | None = None) -> int | float:
    """Multiplica x e y; se z for enviado, multiplica x, y e z.

    Exemplos:
    >>> multiplica(2, 3)
    6
    >>> multiplica(2, 3, 4)
    24

    :param x: Primeiro fator.
    :param y: Segundo fator.
    :param z: Fator opcional; se None, multiplica apenas x e y.
    :return: Produto dos fatores informados.
    """
    if z is None:
        return x * y
    return x * y * z


class Pessoa:
    """Representa uma pessoa com nome e idade.

    Exemplos:
    >>> Pessoa('Ana', 30).saudacao()
    'Ola, meu nome e Ana'
    >>> Pessoa('Ana', 30).nome_e_idade
    'Ana tem 30 anos'
    """

    def __init__(self, nome: str, idade: int) -> None:
        """Inicializa uma instancia.

        :param nome: Nome da pessoa.
        :param idade: Idade da pessoa.
        """
        self.nome = nome
        self.idade = idade

    def saudacao(self) -> str:
        """Retorna uma saudacao com o nome da pessoa.

        Exemplos:
        >>> Pessoa('Bia', 22).saudacao()
        'Ola, meu nome e Bia'
        """
        return f"Ola, meu nome e {self.nome}"

    @classmethod
    def anonimo(cls) -> Pessoa:
        """Cria uma pessoa sem identidade conhecida.

        Exemplos:
        >>> Pessoa.anonimo().nome
        'Anonimo'
        """
        return cls("Anonimo", 0)

    @staticmethod
    def mensagem_fixa() -> str:
        """Retorna uma mensagem fixa da classe.

        Exemplos:
        >>> Pessoa.mensagem_fixa()
        'Este e um metodo estatico'
        """
        return "Este e um metodo estatico"

    @property
    def nome_e_idade(self) -> str:
        """Combina nome e idade em uma frase.

        Exemplos:
        >>> Pessoa('Cadu', 45).nome_e_idade
        'Cadu tem 45 anos'
        """
        return f"{self.nome} tem {self.idade} anos"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Onde você provavelmente divergiu:
# - escreveu um comentario `# soma dois numeros` dentro do corpo no
#   lugar da docstring (o help() nao mostra nada)
# - esqueceu o `z=None` na assinatura de multiplica e a docstring
#   dos tres fatores nao bate com o comportamento real
# - usou acentos nos nomes dos exemplos ('Anônimo'/'Saudação') e o
#   doctest falhou por codificacao — prefira ASCII nos dados
# - nao documentou classmethod/property: eles tambem merecem
#   docstring propria (sao consumidos pela IDE e pelo autocomplete)
# - sobre a "docstring de modulo de 1 linha": o cabecalho deste
#   arquivo (primeira string do modulo) cumpre o papel