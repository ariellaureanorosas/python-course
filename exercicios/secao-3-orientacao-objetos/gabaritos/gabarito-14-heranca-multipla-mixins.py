"""
Gabarito EXERCÍCIO 14 - Herança Múltipla e Mixins

Raciocínio sênior
-----------------
Mixin é uma classe PEQUENA que entrega uma HABILIDADE (LogPrint,
LogFile) sem pretender ser uma entidade — o nome *Mixin diz isso.
O Smartphone ganha log em arquivo apenas herdando LogFileMixin;
trocar para LogPrintMixin muda o canal sem tocar no smartphone
(composição de habilidades).
Nos __init__ com herança múltipla, cada pai inicializa o próprio
estado: Eletronico via super(), LogFileMixin.init explícito —
não dá para confiar no super() sozinho (MRO pula o mixin).
A base Log define log() que delega em _log() (template method):
cada mixin implementa só _log, e o chamador usa log().
Alternativas descartadas: herança única com if dentro do log
(quebra o princípio open/closed); log como função solta importada.
"""

import os
import tempfile


class Log:
    """Contrato dos mixins de log: log() delega para _log()."""

    def _log(self, mensagem: str) -> None:
        """Metodo que cada mixin deve implementar."""
        raise NotImplementedError('Método _log deve ser implementado')

    def log(self, mensagem: str) -> None:
        """Registra uma mensagem usando o _log do mixin concreto."""
        self._log(mensagem)


class LogPrintMixin(Log):
    """Mixin que registra no terminal."""

    def _log(self, mensagem: str) -> None:
        """Imprime a mensagem no terminal.

        Exemplos:
        >>> LogPrintMixin().log('Registro impresso')
        Registro impresso
        """
        print(mensagem)


class LogFileMixin(Log):
    """Mixin que registra em arquivo."""

    def __init__(self, caminho_arquivo: str = 'log.txt') -> None:
        self.caminho_arquivo = caminho_arquivo

    def _log(self, mensagem: str) -> None:
        """Grava a mensagem em arquivo no modo append.

        Exemplos:
        >>> tmp = tempfile.mktemp(suffix='.log')
        >>> LogFileMixin(tmp)._log('Registro em arquivo')
        >>> with open(tmp, 'r', encoding='utf-8') as arquivo:
        ...     arquivo.read()
        'Registro em arquivo\\n'
        >>> os.remove(tmp)
        """
        with open(self.caminho_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{mensagem}\n')


class Eletronico:
    """Classe base para aparelhos eletronicos."""

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Eletronico('TV')
        Eletronico(nome='TV')
        """
        return f'Eletronico(nome={self.nome!r})'


class Smartphone(Eletronico, LogFileMixin):
    """Smartphone: heranca multipla (eletronico + mixin de log em arquivo)."""

    def __init__(self, nome: str, caminho_arquivo: str = 'log.txt') -> None:
        super().__init__(nome)
        LogFileMixin.__init__(self, caminho_arquivo)

    def ligar(self) -> str:
        """Liga o smartphone e registra a acao no arquivo de log.

        Exemplos:
        >>> tmp = tempfile.mktemp(suffix='.log')
        >>> sp = Smartphone('Galaxy', tmp)
        >>> sp.ligar()
        'Smartphone Galaxy ligado'
        >>> with open(tmp, 'r', encoding='utf-8') as arquivo:
        ...     arquivo.read()
        'Smartphone Galaxy ligado\\n'
        >>> os.remove(tmp)
        """
        mensagem = f'Smartphone {self.nome} ligado'
        self.log(mensagem)
        return mensagem


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - esqueceu LogFileMixin.__init__(self, caminho) no Smartphone —
#   o mixin fica sem caminho_arquivo e abre 'log.txt' do diretório
#   atual (estado não inicializado em herança múltipla)
# - implementou a escrita do log dentro do Smartphone (duplicação —
#   o mixin é o reuso; o Smartphone só usa self.log())
# - usou super().__init__ para os DOIS pais (o MRO chama Eletronico
#   e LogFile fica de fora; é preciso init explícito)