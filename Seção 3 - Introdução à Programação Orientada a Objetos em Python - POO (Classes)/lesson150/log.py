# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"


class Log:
    def _log(self, msg):
        raise NotImplementedError("Implementei o log")

    def erro(self, msg):
        return self._log(f"Erro: {msg}")

    def sucesso(self, msg):
        return self._log(f"Sucesso: {msg}")


class LogFileMixin(Log):
    def _log(self, msg):
        mensagem_formatada = f"{msg} {self.__class__.__name__}"
        print("Salvando no log:", mensagem_formatada)
        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(mensagem_formatada)
            arquivo.write("\n")


class LogPrintMixin(Log):
    def _log(self, msg):
        mensagem_formatada = f"{msg} {self.__class__.__name__}"
        print(mensagem_formatada)
