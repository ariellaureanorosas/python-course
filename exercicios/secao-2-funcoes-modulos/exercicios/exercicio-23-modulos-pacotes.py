"""
EXERCÍCIO 23 - Módulo Próprio com __main__ e __all__

Tópicos: import, __name__, __main__, __all__, modularização

Transforme este arquivo em um módulo reutilizável:

1. Defina `somar(a: int, b: int) -> int` e `multiplicar(a: int, b: int)
   -> int` com testes doctest na docstring (padrão do repositório).

2. Defina a lista `__all__ = ["somar", "multiplicar"]` no topo:
   é ela que controla o que um eventual `from ... import *`
   exportaria (ouça a anotação 09).

3. O código "demo" (prints) deve rodar SOMENTE quando o arquivo for
   executado diretamente — proteja-o com
   `if __name__ == "__main__":`. Ao ser IMPORTADO por outro módulo,
   nada deve ser impresso.

Comportamento esperado:
    python exercicio-23-modulos-pacotes.py
    # → demo: 5, 20  e os doctests passam
    python -m doctest exercicio-23-modulos-pacotes.py
    # → os testes rodam e o demo NÃO imprime nada de extra

Dica: __name__ vale "__main__" só quando o arquivo é executado
diretamente; sob import, vale o nome do módulo.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def somar(a: int, b: int) -> int:
    ...


def multiplicar(a: int, b: int) -> int:
    ...