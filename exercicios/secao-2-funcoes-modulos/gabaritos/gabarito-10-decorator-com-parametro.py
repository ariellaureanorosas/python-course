"""
Gabarito EXERCÍCIO 10 - Decorator com Parâmetro (nível de log)

Raciocínio sênior
-----------------
Decorator COM parâmetro é uma fábrica de decorators: log(nivel)
executa na hora da chamada, valida o nível (fail fast) e RETORNA
o decorador de verdade. Por isso a assinatura tem três níveis:
log(nivel) -> decorador(func) -> wrapper(*args). A validação
acontece ANTES de decorar — um nível inválido é rejeitado no
momento da definição da função decorada, não na primeira chamada.
O wrapper usa @wraps pelas mesmas razões do exercício 09, e os
níveis validos são uma tupla constante (imutável por contrato).
"""

from functools import wraps

NIVEIS_VALIDOS = ("INFO", "WARNING", "ERROR")


def log(nivel: str):
    """Cria um decorator de log com o nível fixado.

    Parametros
    ----------
    nivel : str
        Um dos níveis: 'INFO', 'WARNING' ou 'ERROR'.

    Returns
    -------
    Callable
        Decorator que envolvem a função-alvo.

    Raises
    ------
    ValueError
        Se o nível não for um dos três válidos.

    Exemplos
    --------
    >>> @log("INFO")
    ... def somar(a: int, b: int) -> int:
    ...     return a + b
    >>> somar(2, 3)
    [INFO] Executando somar ((2, 3), {})
    5
    >>> log("DEBUG")
    Traceback (most recent call last):
    ...
    ValueError: Nível inválido: 'DEBUG'. Use um de ('INFO', 'WARNING', 'ERROR')
    """
    if nivel not in NIVEIS_VALIDOS:
        raise ValueError(
            f"Nível inválido: '{nivel}'. Use um de {NIVEIS_VALIDOS}"
        )

    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'[{nivel}] Executando {func.__name__} ({args}, {kwargs})')
            return func(*args, **kwargs)
        return wrapper
    return decorador


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    @log("INFO")
    def multiplicar(a: int, b: int) -> int:
        return a * b

    print(multiplicar(4, 5))

# Onde você provavelmente divergiu:
# - fez a validação do nível DENTRO do wrapper (validaria a cada
#   chamada, não na definição; aqui é fail fast)
# - esqueceu um nível da tupla de retorno (sem o return decorador, a
#   chamada @log("INFO") devolve uma função em vez de um decorator)
# - não validou o nível (log("INVALIDO") era aceito silenciosamente)