"""
Exercício 10 - Decorator com Parâmetro (nível de log)

Crie um decorator `@log(nivel: str)` que:
- Aceite os níveis "INFO", "WARNING" ou "ERROR"
- Exiba a mensagem no formato: "[NIVEL] Executando [nome] ([args], [kwargs])"
- Se o nível não for um dos três válidos, levante ValueError
- Use @wraps de functools

Exemplo:
    @log("INFO")
    def somar(a, b):
        return a + b

    somar(2, 3)  # imprime: [INFO] Executando somar ((2, 3), {})

Tópicos da aula: decorators com parâmetros, @wraps, *args, **kwargs, raise
"""

from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

NIVEIS_VALIDOS = ("INFO", "WARNING", "ERROR")


def log(nivel: str) -> Callable[[Callable[..., object]], Callable[..., object]]:
    if nivel not in NIVEIS_VALIDOS:
        msg: str = f"Nível inválido: {nivel}. Use um dos {NIVEIS_VALIDOS}"
        raise ValueError(msg)

    def decorator(func: Callable[..., object]) -> Callable[..., object]:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            print(f"[{nivel}] Executando {func.__name__} ({args}, {kwargs})")
            return func(*args, **kwargs)

        return wrapper

    return decorator


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    @log("INFO")
    def multiplicar(a: int, b: int) -> int:
        return a * b

    print(multiplicar(4, 5))
