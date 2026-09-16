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

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def log(nivel: str) -> Callable[..., object]: ...
