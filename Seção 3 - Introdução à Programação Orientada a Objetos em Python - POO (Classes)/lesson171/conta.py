import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia: int = agencia
        self.conta: int = conta
        self.saldo: float = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        pass

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f"(DEPÓSITO {valor})")
        return self.saldo

    def detalhes(self, msg: str = "") -> None:
        print(f"O seu saldo é: {self.saldo:.2f} {msg}")
        print("-" * 10)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"{self.agencia!r}, {self.conta!r}, {self.saldo!r}"
        return f"{class_name} {attrs}"


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque: float = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo

        print("Não foi possivel sacar o valor desejado")
        self.detalhes(msg=f"(SAQUE NEGADO {valor})")
        return self.saldo


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, conta: int, saldo: float = 0, limite: float = 0
    ) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite: float = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque: float = self.saldo - valor
        limite_maximo: float = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(msg=f"(SAQUE {valor})")
            return self.saldo

        print("Não foi possivel sacar o valor desejado")
        print(f"Seu limite é, {self.limite:.2f}")
        self.detalhes(msg=f"(SAQUE NEGADO {valor})")
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"{self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r}"
        return f"{class_name} {attrs}"


if __name__ == "__main__":
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.depositar(10)
    cp1.sacar(5)
    print("#")
    cc1 = ContaCorrente(111, 222, 0, 1)
    cc1.depositar(10)
    cc1.sacar(20)
