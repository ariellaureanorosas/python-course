"""
EXERCÍCIO 08 - @property + @setter com validação

Tópicos: @property, @setter, validação de entrada, convenção _atributo
Aulas: 142

O @setter permite VALIDAR e CONTROLAR a escrita do atributo: em vez
de `caneta.cor = 'qualquer_coisa'` sem restrição, toda mudança passa
pelo setter, que pode recusar valores inválidos.

1. Constantes:
   - `CORES_VALIDAS: tuple[str, ...] = ('Azul', 'Vermelha', 'Preta')`

2. Classe `Caneta`:
   - `__init__(self, cor: str) -> None`
     - Armazena em `self._cor` — use o PRÓPRIO setter dentro do __init__
       (atribua via `self.cor = cor` para já validar na criação)
   - `@property cor(self) -> str`
     - Retorna `self._cor`
   - `@cor.setter cor(self, nova_cor: str) -> None`
     - Se a cor NÃO estiver em CORES_VALIDAS, levanta
       ValueError('Cor inválida: <cor>')
     - Caso contrário, atualiza `self._cor`
   - `__repr__(self) -> str` retornando Caneta(cor='...')

Comportamento esperado:
    caneta = Caneta('Azul')            # ok
    caneta.cor = 'Vermelha'            # ok
    caneta.cor = 'Roxa'                # ValueError: Cor inválida: Roxa
    Caneta('Roxa')                     # ValueError na criação também!

Dica: chamar `self.cor = cor` dentro do __init__ executa o setter,
então a validação vale para a criação E para mudanças futuras.
"""

CORES_VALIDAS: tuple[str, ...] = ('Azul', 'Vermelha', 'Preta')


class Caneta:
    def __init__(self, cor: str) -> None:
        ...

    @property
    def cor(self) -> str:
        ...

    @cor.setter
    def cor(self, nova_cor: str) -> None:
        ...

    def __repr__(self) -> str:
        ...