"""
Gabarito EXERCÍCIO 09 - Encapsulamento e Name Mangling

Raciocínio sênior
-----------------
__saldo (dois underscores) dispara o name mangling: por fora
vira _ContaBancaria__saldo — sinal claro de "não mexa aqui" e
proteção real contra escrita acidental por atributo solto. Mas o
Python não ESCOENDE privacidade de verdade — o que garante a
invariante (nunca negativar) são os métodos depositar/sacar com
validação. O saldo é exposto por @property só para LEITURA:
leitura livre, escrita controlada. Validar duas coisas distintas
(positivo E limite) com duas mensagens separadas é bom erro:
depurar sabe qual regra foi violada.
"""


class ContaBancaria:
    """Conta com saldo privado (name mangling) e operacoes validadas."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        self.titular = titular
        self.__saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        """Retorna o saldo atual (leitura permitida por fora).

        Exemplos:
        >>> conta = ContaBancaria('Ana', 100.0)
        >>> conta.saldo
        100.0
        """
        return self.__saldo

    def depositar(self, valor: float) -> None:
        """Adiciona valor ao saldo privado.

        Raises:
            ValueError: Se o valor nao for positivo.

        Exemplos:
        >>> conta = ContaBancaria('Ana', 100.0)
        >>> conta.depositar(50.0)
        >>> conta.saldo
        150.0
        >>> conta.depositar(-5.0)
        Traceback (most recent call last):
        ...
        ValueError: Valor deve ser positivo
        """
        if valor <= 0:
            raise ValueError('Valor deve ser positivo')

        self.__saldo += valor

    def sacar(self, valor: float) -> None:
        """Subtrai valor do saldo privado.

        Raises:
            ValueError: Se o valor nao for positivo ou exceder o saldo.

        Exemplos:
        >>> conta = ContaBancaria('Ana', 100.0)
        >>> conta.sacar(30.0)
        >>> conta.saldo
        70.0
        >>> conta.sacar(200.0)
        Traceback (most recent call last):
        ...
        ValueError: Saldo insuficiente
        """
        if valor <= 0:
            raise ValueError('Valor deve ser positivo')
        if valor > self.__saldo:
            raise ValueError('Saldo insuficiente')

        self.__saldo -= valor


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - usou _saldo (um _) em vez de __saldo: o enunciado pedia name
#   mangling (dois _); um _ é só convenção, __ é o que o Python
#   renomeia de verdade
# - deixou conta.saldo = 100 gravar por fora (sem property ou com
#   atributo público, o saldo vira "qualquer um pode setar")
# - juntou as duas validações numa mensagem genérica ("valor
#   inválido") — dois erros distintos merecem duas mensagens