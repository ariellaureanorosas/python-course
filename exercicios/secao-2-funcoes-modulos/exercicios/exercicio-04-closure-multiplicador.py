"""
EXERCÍCIO 04 - Closure Multiplicador

Tópicos: closure, parâmetros, return de função

Crie a função `criar_multiplicador(multiplicador: int)` que:

1. Receba um inteiro multiplicador
2. Retorne uma função que recebe um número e retorna
   número * multiplicador

Comportamento esperado:
    dobro = criar_multiplicador(2)
    dobro(5)   # 10

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def criar_multiplicador(multiplicador: int) -> Callable[[int], int]:
    def multiplicar(numero: int) -> int:
        return numero * multiplicador

    return multiplicar


if __name__ == "__main__":
    dobro = criar_multiplicador(2)
    print(dobro(5))
