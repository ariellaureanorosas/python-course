"""
Gabarito 10 - Decorator com Parâmetro (nível de log)
"""
from functools import wraps


def log(nivel: str):
    """Decorator que exibe o nível de log antes de executar a função.

    Níveis válidos: "INFO", "WARNING", "ERROR".

    Exemplo:
        >>> @log("INFO")
        ... def somar(a, b):
        ...     return a + b
        >>> somar(2, 3)
        [INFO] Executando somar ((2, 3), {})
        5
    """
    niveis_validos = ("INFO", "WARNING", "ERROR")

    if nivel not in niveis_validos:
        raise ValueError(
            f"Nível inválido: '{nivel}'. Use um de {niveis_validos}"
        )

    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{nivel}] Executando {func.__name__} ({args}, {kwargs})")
            return func(*args, **kwargs)

        return wrapper

    return decorador
