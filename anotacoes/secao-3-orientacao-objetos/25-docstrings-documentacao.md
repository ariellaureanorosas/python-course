# Docstrings e documentação de código

## Quando você vai usar isso?
Toda vez que outra pessoa (ou você daqui a 3 meses) precisar entender o que uma função, classe ou módulo faz SEM ler a implementação inteira. O `help()` do terminal, o `pydoc`, as IDEs e o autocomplete exibem a docstring na hora — ela é a "etiqueta" oficial do seu código. É o tema da aula 169: comentários contam o porquê, docstrings documentam o contrato (o que faz, parâmetros, retorno).

## Modelo mental
Comentário (`#`) é o bilhete grudado na parede ao lado do código — fala do "como" num trecho específico. Docstring (`"""..."""`) é o rótulo afixado na própria função/classes/módulo — fala do "o quê" e acompanha a assinatura para sempre, aparecendo no `help()` e nas IDEs. Função sem docstring é produto sem etiqueta: funcional, mas ninguém sabe como consumir.

## Em uma linha
Docstring é a primeira string após a definição (`def`/`class`/módulo) e vira o `__doc__` do objeto: uma linha para resumir, várias linhas para detalhar — o que documenta NUNCA é um comentário solto no meio do corpo.

## Na prática

### Caso simples — função com docstring de uma linha

```python
def soma(x: float, y: float) -> float:
    """Soma dois números."""
    return x + y
```

### Com variação — docstring de várias linhas com parâmetros e retorno

```python
def multiplica(x: float, y: float, z: float | None = None) -> int | float:
    """Multiplica x e y; se z for enviado, multiplica x, y e z.

    :param x: Primeiro fator
    :param y: Segundo fator
    :param z: Fator opcional
    :return: Produto dos fatores informados
    """
    if z is None:
        return x * y
    return x * y * z

help(multiplica)   # ← o interpretador exibe a docstring no terminal
```

### Em uso real — documentando classes, métodos e módulos

```python
"""Exemplos de documentação (docstrings) em classes Python"""


class MinhaClasse:
    """Classe exemplo que demonstra docstrings em classe, métodos
    e propriedade."""

    variavel_de_classe: str = "Valor da classe"

    def __init__(self, nome: str, idade: int) -> None:
        """Inicializa uma instância.

        :param nome: Nome da pessoa
        :param idade: Idade da pessoa
        """
        self.nome = nome
        self.idade = idade

    def metodo_instancia(self) -> str:
        """Retorna uma saudação com o nome da pessoa."""
        return f"Olá, meu nome é {self.nome}"

    @classmethod
    def metodo_classe(cls) -> str:
        """Retorna o valor da variável de classe."""
        return cls.variavel_de_classe

    @staticmethod
    def metodo_estatico() -> str:
        """Retorna uma mensagem fixa."""
        return "Este é um método estático"

    @property
    def nome_e_idade(self) -> str:
        """Combina nome e idade em uma frase."""
        return f"{self.nome} tem {self.idade} anos"
```

- **Docstring de módulo** (uma linha): `"""O que seu módulo faz"""`
- **Docstring de módulo** (várias linhas): primeira linha resume, as seguintes detalham
- O `help()` mostra a docstring do módulo, das classes e dos métodos — o que a IDE mostra
  no autocomplete também vem daqui

## O que NÃO fazer

```python
# ← ERRADO: comentário no lugar de docstring (ou vice-versa)
def soma(x, y):
    # soma dois numeros            # ← some quando a assinatura muda
    return x + y

# ← ERRADO: docstring que MENTE (diz + quando faz -)
def soma(x, y):
    """Subtrai y de x."""
    return x - y

# ← ERRADO: docstring genérica que não agrega
def soma(x, y):
    """Função de soma."""
    return x + y
# ← o certo: dizer o contrato real: parâmetros, retorno e edge cases
```

## Por que Python funciona assim?
Toda definição (`def`, `class`, módulo) guarda a primeira string do corpo como atributo `__doc__`: nada é "interpretado" — a string fica armazenada no objeto. O `help()` apenas formata `__doc__` para o terminal, e as IDEs fazem o mesmo para o autocomplete. Como `print(obj.__doc__)` funciona para qualquer objeto, a docstring acaba sendo também um contrato consultável em tempo de execução — é por isso que bibliotecas sérias documentam tudo, e é o que os gabaritos deste repositório usam para embutir exemplos testáveis (doctest).

## Conexões
- Você já usou esse padrão quando: viu `help(len)` ou o tooltip da IDE exibir a descrição de uma função
- Aparece também em: `doctest` (gabaritos deste repo!), `pydoc` (gera HTML da documentação), Sphinx
- Diferente de: comentários `#` (nota 01 — "porquê" local, não contrato), docstring de módulo vs de função, type hints (nota Type Hints — declaram TIPOS, docstring declara COMPORTAMENTO)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre docstring e comentário `#`?
2. Diferencie docstring de uma linha de docstring de várias linhas — quando usar cada uma?
3. Escreva a docstring de `multiplica(x, y, z=None)` com `:param` e `:return`.

---

**Frase-âncora:** "Comentário explica a linha; docstring documenta o contrato — e o `help()` devolve tudo na hora."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14