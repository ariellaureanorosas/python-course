"""
EXERCÍCIO 23 - Descritor Campo (acesso validado)

Tópicos: descritores
Aulas: 129-177 (descritores)

Um descritor é um objeto que intercepta o acesso a atributos da
classe onde está declarado: os métodos `__get__`/`__set__` rodam
em toda leitura e escrita, permitindo validação centralizada.
Com descritores, uma classe do tamanho de `Pessoa` ganha checagem
de tipo sem reescrever getter/setter para cada atributo.

1. Classe `Campo` (descritor de dados):
   - `__init__(self, tipo: type = object)` guarda `self.tipo = tipo`
   - `__set_name__(self, owner: type, nome: str) -> None`
     guarda o nome do atributo em `self.nome = nome`
   - `__get__(self, instancia, owner)`:
     - Se `instancia is None`, retorna o próprio descritor
     - Senão, retorna `instancia.__dict__.get(self.nome)`
   - `__set__(self, instancia, valor)`:
     - Se `not isinstance(valor, self.tipo)`:
       `raise TypeError(f'{self.nome} deve ser {self.tipo.__name__}')`
     - Senão: `instancia.__dict__[self.nome] = valor`

2. Classe `Pessoa`:
   - Atributos de classe `nome = Campo(str)` e `idade = Campo(int)`
   - `__init__(self, nome: str, idade: int) -> None`
     atribui via `self.nome`/`self.idade` (passa pelo `__set__`)
   - `__repr__(self) -> str` retornando `Pessoa(nome='Ana', idade=30)`

Comportamento esperado (fluxo de uso):
    p = Pessoa('Ana', 30)
    p.nome  # 'Ana'
    p.nome = 'Bia'  # válido, mundo gira
    p.nome = 123  # TypeError: nome deve ser str
    p.idade = 'trinta'  # TypeError: idade deve ser int

Observações:
  - Descritor só intercepta atributos de CLASSE que implementam
    `__get__`/`__set__`; o valor vivo fica no `__dict__` da instância
  - `__set_name__` roda automaticamente quando a classe é criada e
    entrega o nome usado no corpo da classe (evita duplicação)
  - Um descritor com `__set__` é chamado de "descritor de dados" e
    tem prioridade sobre o `__dict__` da instância
"""


class Campo:
    def __init__(self, tipo: type = object) -> None:
        ...

    def __set_name__(self, owner: type, nome: str) -> None:
        ...

    def __get__(self, instancia, owner):
        ...

    def __set__(self, instancia, valor) -> None:
        ...


class Pessoa:
    nome = Campo(str)
    idade = Campo(int)

    def __init__(self, nome: str, idade: int) -> None:
        ...

    def __repr__(self) -> str:
        ...