"""
Gabarito EXERCÍCIO 07 - Property (Getter Somente Leitura)

Raciocínio sênior
-----------------
O atributo "de verdade" vive com _ (_cor) e a property expõe uma
LEITURA controlada sem permitir escrita: caneta.cor = 'Verde'
falharia (AttributeError) porque não há setter. O caller lê como
atributo (caneta.cor, sem parênteses) — a property esconde que há
lógica por trás, e o código de fora nunca percebe se o valor é
guardado direto ou calculado: essa é a vantagem do getter.
Quando o enunciado pedir "somente leitura", a receita é: atributo
com _ no __init__ + @property que só retorna.
Alternativas descartadas: métodos get_cor()/set_cor() estilo Java
(em Python, property é o idioma; métodos get_ são estrangeirismo).
"""


class Caneta:
    """Caneta com propriedades de leitura (getters) e atributos com _."""

    def __init__(self, cor: str, modelo: str) -> None:
        self._cor = cor
        self._modelo = modelo

    @property
    def cor(self) -> str:
        """Retorna a cor da caneta (somente leitura).

        Exemplos:
        >>> caneta = Caneta('Azul', 'Bic')
        >>> caneta.cor
        'Azul'
        """
        return self._cor

    @property
    def modelo(self) -> str:
        """Retorna o modelo da caneta (somente leitura).

        Exemplos:
        >>> caneta = Caneta('Azul', 'Bic')
        >>> caneta.modelo
        'Bic'
        """
        return self._modelo

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Caneta('Azul', 'Bic')
        Caneta(cor='Azul', modelo='Bic')
        """
        return f'Caneta(cor={self._cor!r}, modelo={self._modelo!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - expôs self.cor direto sem o _ interno (aí o atributo fica
#   gravável por fora — o enunciado pede somente leitura)
# - criou get_cor()/set_cor() no estilo Java (em Python o idioma
#   é @property: leitura igual a atributo, sem parênteses)
# - esqueceu o @property e deixou o atributo público gravável