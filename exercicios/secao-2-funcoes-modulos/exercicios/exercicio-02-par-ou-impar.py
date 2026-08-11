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


def par_ou_impar(numero: int) -> str:
    ...


if __name__ == "__main__":
    print(par_ou_impar(6))
    print(par_ou_impar(7))