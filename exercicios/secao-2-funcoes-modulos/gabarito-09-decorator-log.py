"""
Gabarito 09 - Decorator de Log
"""
from functools import wraps


def log_execucao(func):
    """Decorator que loga a execução de uma função com seus argumentos e resultado.

    Exemplo:
        >>> @log_execucao
        ... def somar(a, b):
        ...     return a + b
        >>> somar(3, 5)
        Executando somar com argumentos ((3, 5), {})
        Resultado: 8
        8
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__} com argumentos ({args}, {kwargs})")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado

    return wrapper
