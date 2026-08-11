"""
EXERCÍCIO 09 - Encapsulamento e name mangling (atributos __privados)

Tópicos: encapsulamento, name mangling (_Classe__atributo), convenções
Aulas: 143

Em Python, encapsulamento é por CONVENÇÃO:
  - public: nome normal (atributo)
  - protected: _nome (apenas convenção, ainda acessível)
  - private: __nome → Python renomeia para _Classe__nome (name mangling)

O name mangling impede conflito de nomes entre classes da mesma
hierarquia: fora da classe, `__saldo` não existe; existe
`_ContaBancaria__saldo`.

1. Classe `ContaBancaria`:
   - `__init__(self, titular: str, saldo_inicial: float = 0.0) -> None`
     - Guarda `self.titular` e `self.__saldo = saldo_inicial`
   - `@property saldo(self) -> float`
     - Retorna `self.__saldo` (leitura por fora é permitida)
   - `depositar(self, valor: float) -> None`
     - Se valor <= 0, levanta ValueError('Valor deve ser positivo')
     - Soma ao saldo privado
   - `sacar(self, valor: float) -> None`
     - Se valor <= 0, levanta ValueError('Valor deve ser positivo')
     - Se valor > saldo, levanta ValueError('Saldo insuficiente')
     - Subtrai do saldo privado

Comportamento esperado:
    conta = ContaBancaria('Ana', 100.0)
    conta.saldo              # 100.0 (via property)
    conta.depositar(50.0)
    conta.saldo              # 150.0
    conta.sacar(200.0)       # ValueError: Saldo insuficiente
    conta.__saldo            # AttributeError — o nome foi "manglado"!
    conta._ContaBancaria__saldo  # 150.0 (é assim que Python guarda)
"""


class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        ...

    @property
    def saldo(self) -> float:
        ...

    def depositar(self, valor: float) -> None:
        ...

    def sacar(self, valor: float) -> None:
        ...