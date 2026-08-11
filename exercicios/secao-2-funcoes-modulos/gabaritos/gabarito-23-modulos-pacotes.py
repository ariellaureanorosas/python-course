"""
Gabarito EXERCÍCIO 23 - Módulo Próprio com __main__ e __all__

Raciocínio sênior
-----------------
A separação "módulo importável × script executável" é o contrato de
qualquer arquivo Python reutilizável: o código de DEMONSTRAÇÃO fica
atrás do `if __name__ == "__main__":` para que importar não dispare
prints inesperados (efeito colateral ao importar é anti-contract).
O `__all__` é a LISTA DE EXPORTAÇÃO: `from ... import *` só traz os
nomes declarados ali — é também documentação, dizendo "esta é a API".
As funções carregam doctests exatamente como o resto do repositório:
o `python -m doctest arquivo.py` executa o arquivo como __main__,
então o guard entra, roda testmod() e os testes passam.

Observação do repositório: os arquivos usam hífen no nome (padrão
desta pasta), e nomes com hífen não podem ser alvo de import normal
— a lição de módulos vale no conceito; para importar de verdade,
renomeie ou use importlib (anotação 24).
"""

__all__ = ["somar", "multiplicar"]


def somar(a: int, b: int) -> int:
    """Soma dois inteiros.

    Parâmetros
    ----------
    a : int
        Primeira parcela.
    b : int
        Segunda parcela.

    Retorna
    -------
    int
        a + b.

    Exemplos
    --------
    >>> somar(2, 3)
    5
    """
    return a + b


def multiplicar(a: int, b: int) -> int:
    """Multiplica dois inteiros.

    Parâmetros
    ----------
    a : int
        Primeiro fator.
    b : int
        Segundo fator.

    Retorna
    -------
    int
        a * b.

    Exemplos
    --------
    >>> multiplicar(4, 5)
    20
    """
    return a * b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"Demo: {somar(2, 3)} e {multiplicar(4, 5)}")

# Onde você provavelmente divergiu:
# - deixou o print do demo FORA do guard: ao importar o módulo, o
#   demo imprimiria sem querer
# - não definiu __all__ (o import * exportaria nomes internos, como
#   _auxiliar, além das funções públicas)
# - usou `if __name__ == "exercicio-23-modulos-pacotes":` — o nome
#   correto do buildin é "__main__"
# - esqueceu o import doctest dentro do guard — testmod() sem import
#   levanta NameError