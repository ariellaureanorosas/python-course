ERRO_TIPO = "O argumento deve ser um número inteiro"


def par_ou_impar(numero: int) -> str:
    if not isinstance(numero, int):
        raise TypeError(ERRO_TIPO)
    return "Par" if numero % 2 == 0 else "Ímpar"


if __name__ == "__main__":
    print(par_ou_impar(7))
