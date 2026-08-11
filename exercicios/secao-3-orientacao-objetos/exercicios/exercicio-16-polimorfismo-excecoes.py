"""
EXERCÍCIO 16 - Polimorfismo e exceção customizada

Tópicos: polimorfismo, Liskov (SOLID), herança de Exception, raise
Aulas: 153-154

Polimorfismo: mesmas assinaturas de método, comportamentos diferentes.
A função `notificar` aceita QUALQUER subclasse de Notificacao — ela
não precisa saber qual é. E exceções podem ser criadas por você,
herdando de Exception, para deixar os erros do seu domínio explícitos.

1. Classe `Notificacao(ABC)`:
   - `__init__(self, mensagem: str) -> None`
   - `@abstractmethod enviar(self) -> bool`

2. Classe `NotificacaoEmail(Notificacao)`:
   - `enviar(self) -> bool` imprime 'Enviando e-mail: <mensagem>'
     e retorna True

3. Classe `NotificacaoSMS(Notificacao)`:
   - `enviar(self) -> bool` imprime 'Enviando SMS: <mensagem>'
     e retorna True

4. Função `notificar(notificacao: Notificacao) -> bool`:
   - Apenas executa notificacao.enviar() e retorna o resultado
   - Funciona com qualquer implementação (polimorfismo)

5. Classe `SaldoInsuficienteError(Exception)`:
   - `__init__(self, saldo: float, valor: float)`
     - Chama super().__init__ com a mensagem
       'Saldo insuficiente: R$ <saldo> (tentativa de R$ <valor>)'
       usando :.2f na formatação

6. Classe `Conta`:
   - `__init__(self, saldo: float = 0.0) -> None` guarda `self._saldo`
   - `sacar(self, valor: float) -> float`
     - Se valor > saldo, levanta SaldoInsuficienteError(self._saldo, valor)
     - Senão, subtrai e RETORNA o valor sacado

Comportamento esperado:
    notificar(NotificacaoEmail('Bem-vindo!'))  # 'Enviando e-mail: Bem-vindo!' → True
    notificar(NotificacaoSMS('Promoção'))      # 'Enviando SMS: Promoção' → True
    conta = Conta(10.0)
    conta.sacar(20.0)  # SaldoInsuficienteError: Saldo insuficiente: R$ 10.00 (tentativa de R$ 20.00)
"""

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem: str) -> None:
        ...

    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        ...


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        ...


def notificar(notificacao: Notificacao) -> bool:
    ...


class SaldoInsuficienteError(Exception):
    def __init__(self, saldo: float, valor: float) -> None:
        ...


class Conta:
    def __init__(self, saldo: float = 0.0) -> None:
        ...

    def sacar(self, valor: float) -> float:
        ...