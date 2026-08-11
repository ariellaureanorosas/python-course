"""
Gabarito EXERCÍCIO 17 - Métodos Mágicos (Dunder)

Raciocínio sênior
-----------------
Cada dunder é um contrato COM o interpretador: + chama __add__,
> chama __gt__, print chama __str__, console/REPL chama __repr__.
A dupla __str__/__repr__ tem papéis distintos — usuário vs
desenvolvedor — e só é coerente quando as saídas diferem.
__add__ retorna um NOVO Ponto (imutabilidade funcional: somar
não altera os operandos) — mesma regra do int. __gt__ reutiliza
a distância em vez de duplicar a comparação (fonte única de
verdade). Cada dunder reusa o método de domínio em vez de
reescrever a lógica.
"""


class Ponto:
    """Ponto 2D com operadores por meio de metodos especiais (dunder)."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Representacao para desenvolvedores (REPL, listas, etc).

        Exemplos:
        >>> Ponto(1, 2)
        Ponto(1, 2)
        """
        return f'Ponto({self.x}, {self.y})'

    def __str__(self) -> str:
        """Representacao amigavel para usuarios (print).

        Exemplos:
        >>> print(Ponto(1, 2))
        (1, 2)
        """
        return f'({self.x}, {self.y})'

    def __add__(self, outro: 'Ponto') -> 'Ponto':
        """Soma coordenada a coordenada e retorna um NOVO ponto.

        Exemplos:
        >>> Ponto(1, 2) + Ponto(3, 4)
        Ponto(4, 6)
        """
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __gt__(self, outro: 'Ponto') -> bool:
        """True se este ponto estiver mais distante da origem.

        Exemplos:
        >>> Ponto(3, 4) > Ponto(1, 1)
        True
        >>> Ponto(1, 1) > Ponto(3, 4)
        False
        """
        return self.distancia_da_origem() > outro.distancia_da_origem()

    def distancia_da_origem(self) -> float:
        """Distancia euclidiana ate a origem (0, 0).

        Exemplos:
        >>> Ponto(3, 4).distancia_da_origem()
        5.0
        """
        return (self.x**2 + self.y**2) ** 0.5


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - mutou o próprio ponto em __add__ (p.x += outro.x) em vez de
#   retornar um NOVO Ponto — quebra a semântica esperada de +
# - escreveu __gt__ comparando (x, y) direto (a regra pedida é
#   distância da origem; duplicar a fórmula em dois lugares
#   desatualiza um deles)
# - usou o MESMO texto em __str__ e __repr__ (print e REPL
#   não diferenciam; o gabarito usa exatamente para distinguir)