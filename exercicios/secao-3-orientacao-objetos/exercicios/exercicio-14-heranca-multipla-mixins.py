"""
EXERCÍCIO 14 - Herança múltipla e mixins (logando ações)

Tópicos: herança múltipla, MRO, mixins, NotImplementedError como contrato
Aulas: 149-150

Mixins são classes pequenas que adicionam um comportamento reutilizável
(grandes chances de você usá-los dentro de outra classe). A classe
principal herda de várias: Smartphone É UM Eletronico E ACEITA o
comportamento de Log.

1. Classe `Log` (base dos mixins):
   - `_log(self, mensagem: str) -> None` levanta NotImplementedError
   - `log(self, mensagem: str) -> None` chama self._log(mensagem)
   - O `log()` é o contrato público; cada mixin implementa o `_log()`

2. Classe `LogPrintMixin(Log)`:
   - `_log(self, mensagem: str) -> None` que imprime a mensagem

3. Classe `LogFileMixin(Log)`:
   - `__init__(self, caminho_arquivo: str = 'log.txt')`
   - `_log(self, mensagem: str) -> None` que grava a mensagem + '\n'
     no arquivo em modo append ('a') com encoding='utf-8'

4. Classe `Eletronico`:
   - `__init__(self, nome: str) -> None`
   - `__repr__(self) -> str` retornando Eletronico(nome='...')

5. Classe `Smartphone(Eletronico, LogFileMixin)`:
   - `__init__(self, nome: str, caminho_arquivo: str = 'log.txt')`
     - Chama super().__init__(nome) e super().__init__(caminho_arquivo):
       o primeiro super().__init__ chama Eletronico.__init__ (MRO),
       o segundo precisa de `LogFileMixin.__init__(self, caminho_arquivo)`
   - `ligar(self) -> str`:
     - Monta 'Smartphone <nome> ligado'
     - Registra com self.log(mensagem)
     - Retorna a mensagem

Comportamento esperado:
    sp = Smartphone('Galaxy')
    sp.ligar()   # 'Smartphone Galaxy ligado'  → e grava no log.txt
    Smartphone.mro()  # ordem: Smartphone, Eletronico, LogFileMixin, Log, object

Dica: super() segue o MRO (Method Resolution Order). Para chamar um
__init__ específico de outro ramo, use Classe.__init__(self, ...).
"""


class Log:
    def _log(self, mensagem: str) -> None:
        ...

    def log(self, mensagem: str) -> None:
        ...


class LogPrintMixin(Log):
    def _log(self, mensagem: str) -> None:
        ...


class LogFileMixin(Log):
    def __init__(self, caminho_arquivo: str = 'log.txt') -> None:
        ...

    def _log(self, mensagem: str) -> None:
        ...


class Eletronico:
    def __init__(self, nome: str) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Smartphone(Eletronico, LogFileMixin):
    def __init__(self, nome: str, caminho_arquivo: str = 'log.txt') -> None:
        ...

    def ligar(self) -> str:
        ...