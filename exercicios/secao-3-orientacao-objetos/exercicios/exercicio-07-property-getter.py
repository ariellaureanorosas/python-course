"""
EXERCÍCIO 07 - @property: getter pythônico

Tópicos: @property, getter, atributos com _ (protected por convenção)
Aulas: 141

@property transforma um método em atributo de leitura: quem usa a classe
escreve `caneta.cor` e NÃO `caneta.cor()`. É o getter pythônico.

1. Classe `Caneta`:
   - `__init__(self, cor: str, modelo: str) -> None`
     - Guarda internamente em `self._cor` e `self._modelo` (com _)
   - `@property cor(self) -> str`
     - Retorna `self._cor`
   - `@property modelo(self) -> str`
     - Retorna `self._modelo`
   - `__repr__(self) -> str` retornando Caneta(cor='...', modelo='...')

Comportamento esperado:
    caneta = Caneta('Azul', 'Bic')
    caneta.cor   # 'Azul'  (sem parênteses!)
    caneta.modelo  # 'Bic'
    caneta.cor = 'Vermelha'  # AttributeError: sem setter, é só leitura

Observações:
  - O atributo real é `_cor`; `cor` é a "porta de entrada" criada
    pelo property. NUNCA acesse `_cor` fora da classe.
  - Sem um @setter, a propriedade é somente leitura.
"""


class Caneta:
    def __init__(self, cor: str, modelo: str) -> None:
        ...

    @property
    def cor(self) -> str:
        ...

    @property
    def modelo(self) -> str:
        ...

    def __repr__(self) -> str:
        ...