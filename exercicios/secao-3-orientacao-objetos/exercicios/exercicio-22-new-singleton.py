"""
EXERCÍCIO 22 - Configuracao Singleton (padrão de projeto)

Tópicos: __new__
Aulas: 129-177 (padrão de projeto)

Singletons garantem uma única instância da classe em todo o
processo — útil para configurações globais, conexões e caches.
O truque clássico é interceptar a criação com `__new__`: ele roda
ANTES de `__init__` e decide se cria a instância ou devolve a já
existente. O `__init__` também precisa de proteção, senão ele roda
de novo a cada chamada e sobrescreve a configuração original.

1. Classe `Configuracao`:
   - Atributos de classe `_instancia = None` e `_inicializada = False`
   - `__new__(cls, *args, **kwargs)`: o `*args, **kwargs` absorve os
     argumentos que o `__init__` receberia (ex.: `Configuracao('outro', 9000)`)
     - Se `cls._instancia is None`, cria com `super().__new__(cls)`
       e guarda em `cls._instancia`
     - Senão, retorna a instância já existente
   - `__init__(self, host: str = 'localhost', porta: int = 8000) -> None`:
     - Só aplica os valores se `type(self)._inicializada` for False
     - Depois seta `type(self)._inicializada = True`
   - `__repr__(self) -> str` retornando
     `Configuracao(host='localhost', porta=8000)`

Comportamento esperado (fluxo de uso):
    c1 = Configuracao()
    c2 = Configuracao()
    c1 is c2  # True (mesma instância)
    c1.host  # 'localhost'
    c1.porta  # 8000
    c3 = Configuracao('outro', 9000)
    c3 is c1  # True (não criou nada novo)
    c1.host  # continua 'localhost' (o __init__ foi bloqueado)
    c1.porta  # continua 8000

Observações:
  - `__new__` recebe a classe como primeiro argumento; `super().__new__(cls)`
    é quem de fato aloca o objeto na memória
  - `__init__` recebe SELF já criado; proteja-o com a flag de classe
    para ele não reconfigurar a instância nas chamadas seguintes
  - Teste a identidade com `is` (não `==`)
"""


class Configuracao:
    _instancia = None
    _inicializada = False

    def __new__(cls, *args, **kwargs) -> 'Configuracao':
        ...

    def __init__(self, host: str = 'localhost', porta: int = 8000) -> None:
        ...

    def __repr__(self) -> str:
        ...