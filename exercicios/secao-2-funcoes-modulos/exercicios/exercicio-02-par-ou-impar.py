"""
EXERCÍCIO 02 - Função Par ou Ímpar

Tópicos: isinstance(), return, type hints, raise

Crie a função `par_ou_impar(numero: int) -> str` que:

1. Receba um número inteiro
2. Valide o tipo do argumento com isinstance()
3. Se não for int, levante um TypeError com a mensagem
   "O argumento deve ser um inteiro"
4. Retorne a string "Par" se o número for par, ou "Ímpar" se for ímpar

Comportamento esperado:
    par_ou_impar(6)   # 'Par'
    par_ou_impar(7)   # 'Ímpar'

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

ERRO_TIPO = "O argumento deve ser válido"


def par_ou_impar(numero: object) -> str:
    if not isinstance(numero, int):
        raise TypeError(ERRO_TIPO)
    return "par" if numero % 2 == 0 else "impar"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(par_ou_impar(6))
    print(par_ou_impar(7))
