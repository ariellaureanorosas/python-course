"""
EXERCÍCIO 02 - Métodos de instância e manutenção de estado

Tópicos: métodos de instância, self, estado do objeto, atributos mutáveis
Aulas: 131-134

O objetivo é aprender que os métodos podem MUDAR o estado do objeto.
Crie a classe `Camera`, que mantém internamente se está filmando e
quantas fotos já foram tiradas.

1. Classe `Camera`:
   - `__init__(self, marca: str) -> None`
     - Guarda `self.marca` e inicializa `self.filmando = False` e
       `self.fotos_tiradas = 0`
   - `filmar(self) -> str`
     - Se já estiver filmando, retorna '<marca> já está filmando'
     - Caso contrário, liga o estado e retorna '<marca> começou a filmar'
   - `parar_de_filmar(self) -> str`
     - Se não estiver filmando, retorna '<marca> não está filmando'
     - Caso contrário, desliga o estado e retorna '<marca> parou de filmar'
   - `fotografar(self) -> str`
     - Se estiver filmando, retorna 'Não é possível fotografar enquanto filma'
     - Caso contrário, incrementa `fotos_tiradas` e retorna
       'Foto <n> capturada'

Comportamento esperado:
    camera = Camera('Nikon')
    camera.filmar()          # 'Nikon começou a filmar'
    camera.fotografar()      # 'Não é possível fotografar enquanto filma'
    camera.parar_de_filmar() # 'Nikon parou de filmar'
    camera.fotografar()      # 'Foto 1 capturada'
"""


class Camera:
    def __init__(self, marca: str) -> None:
        ...

    def filmar(self) -> str:
        ...

    def parar_de_filmar(self) -> str:
        ...

    def fotografar(self) -> str:
        ...