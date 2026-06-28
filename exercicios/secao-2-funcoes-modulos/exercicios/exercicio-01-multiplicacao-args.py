"""
Exercício 01 - Função de Multiplicação com *args

Crie uma função `multiplicar(*args: float) -> float` que:
- Receba uma quantidade variável de números
- Retorne a multiplicação de todos eles
- Se nenhum argumento for passado, retorne 1.0

Tópicos da aula: *args, return, parâmetros, type hints
"""

from functools import reduce

ERRO = "O input não é um dado"


def multiplicar(*args: float) -> float:
    for numero in args:
        if not isinstance(numero, (int, float)):
            raise TypeError(ERRO)
    return reduce(lambda a, b: a * b, args, 1.0)


if __name__ == "__main__":
    print(multiplicar(2, 3, 4))
    print(multiplicar())
    print(multiplicar("a"))
    print(multiplicar(5.0))
