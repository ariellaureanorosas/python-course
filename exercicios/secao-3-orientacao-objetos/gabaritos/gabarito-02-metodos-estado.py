"""
Gabarito EXERCÍCIO 02 - Métodos e Estado

Raciocínio sênior
-----------------
O estado (filmando, fotos_tiradas) nasce no __init__ e só muda
por métodos que NOMEIAM a ação (filmar, parar_de_filmar,
fotografar). A classe é a dona do estado: o caller não seta
camera.filmando = True diretamente — ele pede para a câmera agir.
As guardas (if/return) tornam os métodos idempotentes: chamar
duas vezes não corrompe o estado.
Alternativas descartadas: fotos_tiradas sem contador (o gerador
de "Foto 1", "Foto 2" nasce do contador de estado).
"""


class Camera:
    """Camera que mantém estado interno de filmagem e contagem de fotos."""

    def __init__(self, marca: str) -> None:
        self.marca = marca
        self.filmando = False
        self.fotos_tiradas = 0

    def filmar(self) -> str:
        """Inicia a filmagem, se a camera estiver parada.

        Exemplos:
        >>> camera = Camera('Nikon')
        >>> camera.filmar()
        'Nikon começou a filmar'
        >>> camera.filmar()
        'Nikon já está filmando'
        """
        if self.filmando:
            return f'{self.marca} já está filmando'

        self.filmando = True
        return f'{self.marca} começou a filmar'

    def parar_de_filmar(self) -> str:
        """Para a filmagem, se a camera estiver filmando.

        Exemplos:
        >>> camera = Camera('Nikon')
        >>> camera.parar_de_filmar()
        'Nikon não está filmando'
        >>> camera.filmar()
        'Nikon começou a filmar'
        >>> camera.parar_de_filmar()
        'Nikon parou de filmar'
        """
        if not self.filmando:
            return f'{self.marca} não está filmando'

        self.filmando = False
        return f'{self.marca} parou de filmar'

    def fotografar(self) -> str:
        """Tira uma foto e incrementa o contador, se nao estiver filmando.

        Exemplos:
        >>> camera = Camera('Nikon')
        >>> camera.filmar()
        'Nikon começou a filmar'
        >>> camera.fotografar()
        'Não é possível fotografar enquanto filma'
        >>> camera.parar_de_filmar()
        'Nikon parou de filmar'
        >>> camera.fotografar()
        'Foto 1 capturada'
        >>> camera.fotografar()
        'Foto 2 capturada'
        """
        if self.filmando:
            return 'Não é possível fotografar enquanto filma'

        self.fotos_tiradas += 1
        return f'Foto {self.fotos_tiradas} capturada'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - deixou o caller mutar o estado direto (camera.filmando = True
#   fora da classe) — o encapsulamento do estado é o ponto
# - esqueceu a guarda em fotografar (tirava foto enquanto filmava;
#   o enunciado proíbe)
# - usou else com if/return desnecessário (o guard clause do
#   gabarito é mais legível e evita aninhamento)