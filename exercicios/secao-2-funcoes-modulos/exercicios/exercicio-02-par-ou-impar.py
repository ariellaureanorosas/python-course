"""
Exercício 02 - Função Par ou Ímpar

Crie uma função `par_ou_impar(numero: int) -> str` que:
- Receba um número inteiro
- Retorne a string "Par" se o número for par, ou "Ímpar" se for ímpar
- Valide o tipo do argumento com isinstance()
- Se não for int, levante um TypeError com a mensagem "O argumento deve ser um inteiro"

Tópicos da aula: isinstance(), return, type hints, raise
"""

ERRO = "o input não é um número"


def par_ou_impar(numero: int) -> str:
    if not isinstance(numero, int):
        raise TypeError(ERRO)
    return "PAR" if numero % 2 == 0 else "IMPAR"


if __name__ == "__main__":
    print(par_ou_impar(6))

if __name__ == "__main__":
    print(par_ou_impar(7))
