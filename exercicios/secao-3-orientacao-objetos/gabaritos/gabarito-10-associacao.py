"""
Gabarito EXERCÍCIO 10 - Associação entre Objetos

Raciocínio sênior
-----------------
Associação = dois objetos que se CONHECEM mas têm ciclos de vida
independentes: a ferramenta existe sem o escritor (crio a caneta
sozinha) e o escritor existe sem ferramenta (None no início).
O "@ferramenta.setter" recebe o OUTRO OBJETO (não um valor bruto):
o relacionamento se representa guardando a referência. O tipo
FerramentaDeEscrever | None documenta "pode não ter" já na
assinatura. escrever() delega à ferramenta (self.__ferramenta.
escrever()) — delegação é o coração do design orientado a objetos.
Alternativas descartadas: herança (a caneta NÃO É UM escritor);
composição (a caneta não pertence ao escritor — ela sobrevive).
"""


class FerramentaDeEscrever:
    """Ferramenta utilizada por um escritor (vive independente dele)."""

    def __init__(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nome(self) -> str:
        """Retorna o nome da ferramenta.

        Exemplos:
        >>> FerramentaDeEscrever('Caneta Bic').nome
        'Caneta Bic'
        """
        return self.__nome

    def escrever(self) -> str:
        """Retorna o texto produzido pela ferramenta.

        Exemplos:
        >>> FerramentaDeEscrever('Caneta Bic').escrever()
        'Caneta Bic está escrevendo'
        """
        return f'{self.__nome} está escrevendo'


class Escritor:
    """Escritor que pode usar (ou nao) uma ferramenta de escrever."""

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__ferramenta: FerramentaDeEscrever | None = None

    @property
    def nome(self) -> str:
        """Retorna o nome do escritor.

        Exemplos:
        >>> Escritor('Machado de Assis').nome
        'Machado de Assis'
        """
        return self.__nome

    @property
    def ferramenta(self) -> FerramentaDeEscrever | None:
        """Retorna a ferramenta atual (None se nao tiver).

        Exemplos:
        >>> escritor = Escritor('Machado de Assis')
        >>> escritor.ferramenta
        """
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta: FerramentaDeEscrever | None) -> None:
        """Define a ferramenta de trabalho (associacao com outro objeto)."""
        self.__ferramenta = ferramenta

    def escrever(self) -> str:
        """Escreve usando a ferramenta, se houver uma.

        Exemplos:
        >>> escritor = Escritor('Machado de Assis')
        >>> escritor.escrever()
        'Machado de Assis precisa de uma ferramenta'
        >>> caneta = FerramentaDeEscrever('Caneta Bic')
        >>> escritor.ferramenta = caneta
        >>> escritor.escrever()
        'Machado de Assis está escrevendo com Caneta Bic está escrevendo'
        """
        if self.__ferramenta is None:
            return f'{self.__nome} precisa de uma ferramenta'

        return f'{self.__nome} está escrevendo com {self.__ferramenta.escrever()}'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - fez a caneta nascer dentro do escritor (composição) — a
#   associação pede que os objetos vivam independentes (criar a
#   caneta fora e INJETAR via setter)
# - usou herança (Fer CanetaEspecial(Escritor)) — associação é
#   "tem um", herança é "é um"; caneta NÃO é um escritor
# - retornou o nome da ferramenta direto em escrever() em vez de
#   delegar à própria ferramenta (a ferramenta sabe como escrever)