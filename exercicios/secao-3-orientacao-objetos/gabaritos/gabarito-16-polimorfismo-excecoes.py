"""
Gabarito EXERCÍCIO 16 - Polimorfismo e Exceções Customizadas

Raciocínio sênior
-----------------
Notificacao é um contrato abstrato: quem consome SÓ conhece o
conceito "envia" (notificar(chamada polimórfica). Cada canal
(Email, SMS) implementa o próprio enviar — a função notificar
funciona para qualquer canal sem mudar (Liskov: subclasses são
substituíveis pela base).
Exceção customizada herda Exception e carrega o CONTEXTO no
construtor (saldo real e tentativa) — a mensagem nasce dos dados,
não de texto fixo. tentar_sacar RELANÇA com raise ... from erro:
preserva a causa original (encadeamento de contexto — o log não
perde o "porquê").
"""

from abc import ABC, abstractmethod


class Notificacao(ABC):
    """Contrato de notificacao: subclasses implementam enviar()."""

    def __init__(self, mensagem: str) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        """Envia a notificacao pelo canal da subclasse."""


class NotificacaoEmail(Notificacao):
    """Notificacao entregue por e-mail."""

    def enviar(self) -> bool:
        """Envia via e-mail e confirma o envio.

        Exemplos:
        >>> NotificacaoEmail('Bem-vindo!').enviar()
        Enviando e-mail: Bem-vindo!
        True
        """
        print(f'Enviando e-mail: {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):
    """Notificacao entregue por SMS."""

    def enviar(self) -> bool:
        """Envia via SMS e confirma o envio.

        Exemplos:
        >>> NotificacaoSMS('Promoção').enviar()
        Enviando SMS: Promoção
        True
        """
        print(f'Enviando SMS: {self.mensagem}')
        return True


def notificar(notificacao: Notificacao) -> bool:
    """Dispara qualquer notificacao sem conhecer a implementacao (Liskov).

    Exemplos:
    >>> notificar(NotificacaoEmail('Olá!'))
    Enviando e-mail: Olá!
    True
    """
    return notificacao.enviar()


class SaldoInsuficienteError(Exception):
    """Excecao do dominio bancario: tentativa de sacar mais do que existe."""

    def __init__(self, saldo: float, valor: float) -> None:
        self.saldo = saldo
        self.valor = valor
        super().__init__(
            f'Saldo insuficiente: R$ {saldo:.2f} '
            f'(tentativa de R$ {valor:.2f})'
        )


class Conta:
    """Conta simples com saque validado por excecao customizada."""

    def __init__(self, saldo: float = 0.0) -> None:
        self._saldo = saldo

    def sacar(self, valor: float) -> float:
        """Saca e retorna o valor, ou levanta SaldoInsuficienteError.

        Raises:
            SaldoInsuficienteError: Se o valor exceder o saldo.

        Exemplos:
        >>> conta = Conta(10.0)
        >>> conta.sacar(4.0)
        4.0
        >>> try:
        ...     conta.sacar(20.0)
        ... except SaldoInsuficienteError as erro:
        ...     str(erro)
        'Saldo insuficiente: R$ 6.00 (tentativa de R$ 20.00)'
        """
        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)

        self._saldo -= valor
        return valor


def tentar_sacar(conta: Conta, valor: float) -> float | None:
    """Tenta sacar e relanca o erro para a camada superior.

    Exemplos:
    >>> conta = Conta(10.0)
    >>> tentar_sacar(conta, 4.0)
    4.0
    >>> tentar_sacar(conta, 20.0)
    Traceback (most recent call last):
    ...
    RuntimeError: Falha no saque
    """
    try:
        return conta.sacar(valor)
    except SaldoInsuficienteError as erro:
        raise RuntimeError('Falha no saque') from erro


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - fez notificar() testar o tipo (isinstance) em vez de delegar
#   com polimorfismo (cada canal sabe enviar; o dispatcher não
#   precisa conhecer os canais)
# - levantou ValueError genérico em vez da exceção customizada
#   (quem captura "SaldoInsuficienteError" distingue do resto;
#   ValueError vira tudo igual)
# - relançou o erro SEM o "from erro" (raise RuntimeError(...) só)
#   — perde o contexto original "SaldoInsuficienteError"; o from
#   encadeia e o depurador vê a causa raiz
# - usou mensagem fixa sem os valores reais (a mensagem com saldo
#   e tentativa é que torna depurável)