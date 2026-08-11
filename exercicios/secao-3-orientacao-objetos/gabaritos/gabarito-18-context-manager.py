"""
Gabarito EXERCÍCIO 18 - Context Managers

Raciocínio sênior
-----------------
Dois jeitos oficiais de implementar: a CLASSE com __enter__/
__exit__ e o DECORADOR @contextmanager sobre um gerador. No
__exit__ assinatura completa: recebe a exceção (se houver) e
retorna False para NÃO suprimir — o erro continua propagando
(o with não muda o comportamento em erro, só garante cleanup).
Limpeza via finally no gerador: garante close() mesmo com
exceção dentro do bloco (a classe garante igual via __exit__).
Alternativas descartadas: fechar na mão no corpo do programa
(repetia close() em todo caminho; com with é automático).
"""

import os
import tempfile
from contextlib import contextmanager
from types import TracebackType


class ArquivoSeguro:
    """Context manager que garante o fechamento do arquivo."""

    def __init__(self, caminho: str, modo: str = 'r') -> None:
        self.caminho = caminho
        self.modo = modo
        self.arquivo = None

    def __enter__(self) -> 'ArquivoSeguro':
        """Abre o arquivo ao entrar no bloco with.

        Exemplos:
        >>> tmp = tempfile.mktemp(suffix='.txt')
        >>> with ArquivoSeguro(tmp, 'w') as arquivo:
        ...     arquivo.escrever('Olá mundo')
        """
        self.arquivo = open(self.caminho, self.modo, encoding='utf-8')
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        """Fecha o arquivo ao sair do with; nao suprime excecoes."""
        if self.arquivo is not None:
            self.arquivo.close()
        return False

    def ler(self) -> str:
        """Le o conteudo inteiro do arquivo aberto.

        Exemplos:
        >>> tmp = tempfile.mktemp(suffix='.txt')
        >>> with ArquivoSeguro(tmp, 'w') as arquivo:
        ...     arquivo.escrever('Olá mundo')
        >>> with ArquivoSeguro(tmp) as arquivo:
        ...     arquivo.ler()
        'Olá mundo'
        >>> os.remove(tmp)
        """
        return self.arquivo.read()

    def escrever(self, texto: str) -> None:
        """Grava o texto no arquivo aberto."""
        self.arquivo.write(texto)


@contextmanager
def abrir_arquivo(caminho: str, modo: str = 'r'):
    """Context manager equivalente, feito com funcao geradora.

    Exemplos:
    >>> tmp = tempfile.mktemp(suffix='.txt')
    >>> with abrir_arquivo(tmp, 'w') as arquivo:
    ...     arquivo.write('Olá mundo')
    9
    >>> with abrir_arquivo(tmp) as arquivo:
    ...     arquivo.read()
    'Olá mundo'
    >>> os.remove(tmp)
    """
    arquivo = open(caminho, modo, encoding='utf-8')
    try:
        yield arquivo
    finally:
        arquivo.close()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - esqueceu __exit__ e implementou só __enter__ (TypeError no
#   with; o protocolo exige os dois)
# - retornou True no __exit__ para "tratar" a exceção — isso
#   SUPRIME o erro e esconde bugs; False deixa propagar
# - escreveu __exit__ sem os 3 parâmetros posicionais (a
#   assinatura (exc_type, exc_val, exc_tb) é o contrato do with;
#   nomes diferentes funcionam, parametros faltando não)