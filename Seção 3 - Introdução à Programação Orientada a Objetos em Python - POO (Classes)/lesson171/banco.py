import conta
import pessoa


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoa.Pessoa] | None = None,
        contas: list[conta.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print("A conta é do cliente", True)
            return True
        print("_checa_se_conta_e_do_cliente", False)
        return False

    def autenticar(self, cliente: pessoa.Pessoa, conta: conta.Conta):
        return (
            self._checa_agencia(conta)
            and self._checa_cliente(cliente)
            and self._checa_conta(conta)
            and self._checa_se_conta_e_do_cliente(cliente, conta)
        )

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"{self.agencias!r}, {self.contas!r}, {self.clientes!r}"
        return f"{class_name} {attrs}"


if __name__ == "__main__":
    c1 = pessoa.Cliente("Ariel", 19)
    cc1 = conta.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoa.Cliente("Maria", 18)
    cp1 = conta.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.agencias.extend([111, 222])
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    print(banco)

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        print(c1.conta)
