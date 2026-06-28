"""
Exercício 04 - Closure Multiplicador

Crie uma função `criar_multiplicador(multiplicador: int)` que:
- Receba um inteiro multiplicador
- Retorne uma função que recebe um número e retorna número * multiplicador

Exemplo:
    dobro = criar_multiplicador(2)
    dobro(5) -> 10

Tópicos da aula: closure, parâmetros, return de função
"""


def criar_multiplicador(multiplicador: int):
    def multiplicacao(numero: int) -> int:
        return numero * multiplicador

    return multiplicacao


if __name__ == "__main__":
    multiplo_dois = criar_multiplicador(2)
    print(multiplo_dois(3))
