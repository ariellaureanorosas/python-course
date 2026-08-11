"""
EXERCÍCIO 27 - Descrever com singledispatch (avançado)

Tópicos: functools.singledispatch
Aulas: 129-177 (avançado)

`functools.singledispatch` implementa polimorfismo por TIPO do
primeiro argumento em funções: a função base (decorada com
@singledispatch) trata o caso genérico e cada `.register(tipo)`
agrega um comportamento especializado. Chamou com um tipo sem
registro? Cai no default. Nada de if/elif de isinstance.

1. Função `descrever`:
   - `@singledispatch def descrever(valor) -> str`:
     - Retorna `f'generico: {valor}'` (caso default)
   - `@descrever.register(int)`:
     - Retorna `f'numero {valor}'`
   - `@descrever.register(str)`:
     - Retorna `f'texto: {valor}'`
   - `@descrever.register(list)`:
     - Retorna `f'lista com {len(valor)} itens'`
   - `@descrever.register(dict)`:
     - Retorna `f'dict com {len(valor)} chaves'`

Comportamento esperado (fluxo de uso):
    descrever(42)  # 'numero 42'
    descrever('oi')  # 'texto: oi'
    descrever([1, 2, 3])  # 'lista com 3 itens'
    descrever({'a': 1})  # 'dict com 1 chaves'
    descrever(3.14)  # 'generico: 3.14'  (float não registrado)

Observações:
  - A função decorada com @singledispatch ganha o atributo
    `.register` usado para anexar as variações
  - O despacho atende subclasses também: passar um bool (subclasse
    de int) chama a versão de int
  - A mensagem é case de demo: mantenha as frases simples (sem
    acento) para a saída de doctest ficar exata
"""

from functools import singledispatch


@singledispatch
def descrever(valor) -> str:
    ...


@descrever.register(int)
def _descrever_int(valor: int) -> str:
    ...


@descrever.register(str)
def _descrever_str(valor: str) -> str:
    ...


@descrever.register(list)
def _descrever_list(valor: list) -> str:
    ...


@descrever.register(dict)
def _descrever_dict(valor: dict) -> str:
    ...