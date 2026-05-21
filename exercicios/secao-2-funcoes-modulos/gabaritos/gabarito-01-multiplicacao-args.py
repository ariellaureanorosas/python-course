from functools import reduce


def multiplicar(*args: float) -> float:
    """Multiplica todos os argumentos recebidos.

    Args:
        *args: Valores a serem multiplicados.

    Returns:
        Produto de todos os argumentos. Retorna 1.0 se nenhum for passado.

    Raises:
        TypeError: Se algum argumento não for int ou float.

    Exemplos:
        >>> multiplicar(2, 3, 4)
        24.0
        >>> multiplicar()
        1.0
        >>> multiplicar(5.0)
        5.0
    """
    for numero in args:
        if not isinstance(numero, (int, float)):
            raise TypeError(
                f"Argumento inválido: {numero!r}. "
                "Todos os argumentos devem ser int ou float."
            )

    return reduce(lambda a, b: a * b, args, 1.0)


if __name__ == "__main__":
    print(multiplicar(2, 3, 4))
    print(multiplicar())
    print(multiplicar(5.0))
