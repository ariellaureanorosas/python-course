CORES_VALIDAS: tuple[str, ...] = ('Azul', 'Vermelha', 'Preta')


"""
Gabarito EXERCÍCIO 08 - Property com Setter Validando

Raciocínio sênior
-----------------
O setter é o GUARDIÃO da invariante: toda escrita passa por ele,
inclusive a do próprio __init__ (self.cor = cor chama o setter —
a validação roda UMA vez para criar e para alterar). Por isso o
atributo interno é _cor e o nome público é o mesmo sem _.
CORES_VALIDAS como constante de módulo em caixa alta: a lista de
cores é dado de domínio único, fonte de verdade para o setter.
Alternativas descartadas: validar só no setter e criar com
self._cor = cor no __init__ (um objeto inválido já nasceria sem
passar pela regra); validar com if em cada ponto de escrita.
"""


class Caneta:
    """Caneta cuja cor somente muda para valores validos (via setter)."""

    def __init__(self, cor: str) -> None:
        self.cor = cor  # passa pelo setter: valida tambem na criacao

    @property
    def cor(self) -> str:
        """Retorna a cor da caneta.

        Exemplos:
        >>> caneta = Caneta('Azul')
        >>> caneta.cor
        'Azul'
        """
        return self._cor

    @cor.setter
    def cor(self, nova_cor: str) -> None:
        """Altera a cor validando contra CORES_VALIDAS.

        Raises:
            ValueError: Se a cor nao estiver em CORES_VALIDAS.

        Exemplos:
        >>> caneta = Caneta('Azul')
        >>> caneta.cor = 'Vermelha'
        >>> caneta.cor
        'Vermelha'
        >>> caneta.cor = 'Roxa'
        Traceback (most recent call last):
        ...
        ValueError: Cor inválida: Roxa
        """
        if nova_cor not in CORES_VALIDAS:
            raise ValueError(f'Cor inválida: {nova_cor}')

        self._cor = nova_cor

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Caneta('Azul')
        Caneta(cor='Azul')
        """
        return f'Caneta(cor={self._cor!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - guardou self._cor = cor no __init__ (sem passar pelo setter) —
#   criava Caneta('Roxa') sem erro; a invariante precisa valer
#   desde o nascimento
# - esqueceu o @cor.setter e implementou muda_cor() (quebra a
#   chamada caneta.cor = 'Vermelha' que o enunciado pede)
# - hardcodou as cores dentro do setter em vez de constante de
#   módulo (mudou o catálogo, teve que caçar no código)