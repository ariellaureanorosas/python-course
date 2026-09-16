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

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def log_execucao(func: Callable[..., object]) -> Callable[..., object]: ...
