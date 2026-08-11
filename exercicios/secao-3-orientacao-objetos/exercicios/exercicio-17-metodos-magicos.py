"""
EXERCÍCIO 17 - Métodos especiais (dunder): __str__, __repr__, __add__, __gt__

Tópicos: dunder methods, __repr__ vs __str__, sobrecarga de operadores
Aulas: 155-156

Métodos especiais (dunder = double underscore) definem como Python
interage com seus objetos: print usa __str__, o REPL usa __repr__,
o + usa __add__ e o > usa __gt__.

1. Classe `Ponto`:
   - `__init__(self, x: int, y: int) -> None`
   - `__repr__(self) -> str` retorna 'Ponto(<x>, <y>)'  (para devs)
   - `__str__(self) -> str` retorna '(<x>, <y>)'  (para usuários)
   - `__add__(self, outro: 'Ponto') -> 'Ponto'`
     - Retorna um NOVO Ponto com a soma das coordenadas
   - `__gt__(self, outro: 'Ponto') -> bool`
     - True se a distância da origem deste ponto for maior que a do outro
   - `distancia_da_origem(self) -> float`
     - Raiz quadrada de (x**2 + y**2), ou seja, (x**2 + y**2) ** 0.5

Comportamento esperado:
    p1 = Ponto(1, 2)
    p2 = Ponto(3, 4)
    p1 + p2          # Ponto(4, 6)  — usa __add__ e print usa __str__
    print(p1)        # (1, 2)
    repr(p1)         # 'Ponto(1, 2)'
    Ponto(3, 4) > Ponto(1, 1)  # True — usa __gt__

Observação: com __gt__ implementado, sorted() e max() funcionam
automaticamente em listas de Ponto.
"""


class Ponto:
    def __init__(self, x: int, y: int) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def __add__(self, outro: 'Ponto') -> 'Ponto':
        ...

    def __gt__(self, outro: 'Ponto') -> bool:
        ...

    def distancia_da_origem(self) -> float:
        ...