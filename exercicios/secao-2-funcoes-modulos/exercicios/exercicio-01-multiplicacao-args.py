"""
EXERCÍCIO 01 - Função de Multiplicação com *args

Tópicos: *args, return, parâmetros, type hints, validação

Crie a função `multiplicar(*args: float) -> float` que:

1. Receba uma quantidade variável de números
2. Retorne a multiplicação de todos eles
3. Se nenhum argumento for passado, retorne 1.0

Comportamento esperado:
    multiplicar(2, 3, 4)   # 24
    multiplicar()          # 1.0
    multiplicar(5.0)       # 5.0

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def multiplicar(*args: float) -> float:
    ...


if __name__ == "__main__":
    print(multiplicar(2, 3, 4))
    print(multiplicar())
    print(multiplicar(5.0))