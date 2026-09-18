"""
Exercício 09 - Decorator de Log

Crie um decorator `@log_execucao` que:
- Imprima "Executando [nome_da_funcao] com argumentos ([args], [kwargs])"
- Execute a função decorada
- Imprima "Resultado: [resultado]"
- Retorne o resultado da função
- Use @wraps de functools para preservar os metadados da função

Tópicos da aula: decorators, @wraps, *args, **kwargs, print
"""

from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def log_execucao(func: Callable[..., object]) -> Callable[..., object]:
    @wraps(func)
    def wraper(*args: object, **kwargs: object) -> None:
        print(f"executando a função {func.__name__} com os argumentos {args, kwargs}")
        execucao = func(*args, **kwargs)
        print(f"resultado: {execucao}")

    return wraper


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    @log_execucao
    def somar(*args: int) -> int:
        return sum(args)

    somar(3, 3)
