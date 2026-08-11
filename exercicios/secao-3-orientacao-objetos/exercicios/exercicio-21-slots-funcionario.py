"""
EXERCÍCIO 21 - Slots em Funcionario (memoria)

Tópicos: __slots__
Aulas: 129-177 (memoria)

Classes normais guardam cada atributo de instância num dicionário
`__dict__` (flexível, mas custoso em memória). Com `__slots__`,
o Python troca o dicionário por um descritor fixo por atributo:
o consumo cai e atributos novos são proibidos — o erro aparece na
hora, em vez de virar bug silencioso meses depois.

1. Classe `Funcionario` (não herda de nada):
   - `__slots__ = ('nome', 'salario')`
   - `__init__(self, nome: str, salario: float) -> None`
     guarda os dois atributos
   - `aumento_salario(self, percentual: float) -> None`
     aplica `salario += salario * percentual / 100`
   - `__repr__(self) -> str` retornando
     `Funcionario(nome='Ana', salario=3000.0)`

Comportamento esperado (fluxo de uso):
    f = Funcionario('Ana', 3000.0)
    f.nome  # 'Ana'
    f.aumento_salario(10)
    f.salario  # 3300.0
    hasattr(f, '__dict__')  # False (slots ocupam lugar do dicionário)
    f.cargo = 'x'  # AttributeError: atributo não declarado nos slots

Observações:
  - `__slots__` é um atributo de CLASSE: uma tupla de nomes,
    declarada no corpo da classe (não no __init__)
  - Sem herança, `__slots__` vale direto; se herdar, a classe
    filha precisa declarar os próprios slots (o `__dict__` só
    some se toda a cadeia usar __slots__)
  - O erro ao atribuir atributo fora dos slots é `AttributeError`
"""


class Funcionario:
    __slots__ = ('nome', 'salario')

    def __init__(self, nome: str, salario: float) -> None:
        ...

    def aumento_salario(self, percentual: float) -> None:
        ...

    def __repr__(self) -> str:
        ...