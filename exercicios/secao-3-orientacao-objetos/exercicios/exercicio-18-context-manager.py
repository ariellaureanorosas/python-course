"""
EXERCÍCIO 18 - Context managers: with + __enter__ + __exit__

Tópicos: context manager, __enter__, __exit__, duck typing, with
Aulas: 158-160

Um context manager garante limpeza automática mesmo com erro no meio:
ao sair do `with`, o __exit__ roda SEMPRE. Você já usa isso com o
open() — agora vai implementar o seu próprio.

1. Classe `ArquivoSeguro`:
   - `__init__(self, caminho: str, modo: str = 'r') -> None`
   - `__enter__(self) -> 'ArquivoSeguro'`
     - Abre o arquivo com open(caminho, modo, encoding='utf-8'),
       guarda em self.arquivo e retorna self
   - `__exit__(self, exc_type, exc_val, exc_tb) -> bool`
     - Fecha self.arquivo se estiver aberto
     - Retorna False (não suprime exceções)
   - `ler(self) -> str` retorna self.arquivo.read()
   - `escrever(self, texto: str) -> None` faz self.arquivo.write(texto)

2. Variante com função geradora (aula 160):
   - Função `abrir_arquivo(caminho: str, modo: str = 'r')`
     - Decorada com @contextmanager de contextlib
     - Abre o arquivo, usa try/finally com yield no meio
     - O yield devolve o arquivo para dentro do with

Comportamento esperado:
    with ArquivoSeguro('teste.txt', 'w') as arquivo:
        arquivo.escrever('Olá mundo')
    with abrir_arquivo('teste.txt') as arquivo:
        print(arquivo.ler())  # 'Olá mundo'

Import: from contextlib import contextmanager
"""

from contextlib import contextmanager

from types import TracebackType


class ArquivoSeguro:
    def __init__(self, caminho: str, modo: str = 'r') -> None:
        ...

    def __enter__(self) -> 'ArquivoSeguro':
        ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        ...

    def ler(self) -> str:
        ...

    def escrever(self, texto: str) -> None:
        ...


@contextmanager
def abrir_arquivo(caminho: str, modo: str = 'r'):
    ...