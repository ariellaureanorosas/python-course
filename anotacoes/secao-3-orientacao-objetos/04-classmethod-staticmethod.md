# @classmethod e @staticmethod

## Quando você vai usar isso?
Quando a criação do objeto tem um "jeito pronto" (uma pessoa com 50 anos, uma conexão com credenciais, uma data "de hoje") você usa `@classmethod` como fábrica (factory). E quando existe uma função utilitária que pertence ao domínio da classe, mas não precisa do objeto nem da classe — validação de CPF, conversão de moeda — você usa `@staticmethod`.

## Modelo mental
`@classmethod` é o atendente da loja: recebe o pedido (`cls`) e fabrica o produto com configuração pronta — e serve clientes de qualquer tipo daquela loja (até sublojas). `@staticmethod` é o totem de autoatendimento: cumpre a função sem saber quem é você nem qual loja — só recebe os dados e devolve o resultado.

## Em uma linha
`@classmethod` recebe `cls` (a classe) e é usado para fábricas e acesso a dados da classe; `@staticmethod` não recebe nada além dos argumentos e é usado para utilitários que não tocam no estado.

## Na prática

### Caso simples
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome):     # ← cls em vez de self
        return cls(nome, 50)              # ← FÁBRICA: cria já pronta

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls(None, idade)

p = Pessoa.criar_com_50_anos('Maria')     # ← chamada NA CLASSE
print(p.idade)                            # ← 50
```

### Com variação
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @staticmethod
    def preco_com_imposto(preco, imposto):  # ← sem self, sem cls
        return preco * (1 + imposto)

    @staticmethod
    def _eh_preco_valido(preco):            # ← privado por convenção
        return preco > 0

    @classmethod
    def criar_validado(cls, nome, preco):
        if not cls._eh_preco_valido(preco):
            raise ValueError(f'Preço inválido: {preco}')
        return cls(nome, preco)

print(Produto.preco_com_imposto(100.0, 0.1))  # ← 110.0 (via classe)
print(Produto.criar_validado('Camiseta', 49.90))  # ← produto
# ← staticmethod também funciona pela instância, mas não precisa dela
```

### Em uso real
```python
from datetime import date

class Compra:
    def __init__(self, cliente, valor, data):
        self.cliente = cliente
        self.valor = valor
        self.data = data

    @classmethod
    def de_hoje(cls, cliente, valor):
        return cls(cliente, valor, date.today())   # ← fábrica com data pronta

    @staticmethod
    def formatar_reais(valor):
        return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

print(Compra.de_hoje('Ana', 129.90))        # ← data = hoje
print(Compra.formatar_reais(129.90))        # ← 'R$ 129,90'
```

## O que NÃO fazer
```python
# ← ERRADO: @staticmethod que precisaria de self ou cls
class A:
    ARQUIVO = 'dados.txt'

    @staticmethod
    def get_arquivo():        # ← quer acessar A.ARQUIVO
        return ARQUIVO        # ← NameError!
# ← o certo: @classmethod com cls (ou acessar A.ARQUIVO direto)

# ← ERRADO: @classmethod usado como se fosse factory para td empresa
class Pedido:
    @classmethod
    def calcular(cls, a, b):   # ← não usa cls, não fabrica nada
        return a + b
# ← o certo: @staticmethod — classmethod é para quem PRECISA da classe

# ← ERRADO: chamar cls() esperando um objeto pré-existente
def __init__(self, nome):
    self.nome = nome

@classmethod
def criar(cls, nome):
    return cls(nome)      # ← cls() É o construtor — está certo assim!
```

## Por que Python funciona assim?
O decorator é açúcar sintático: `criar_com_50_anos = classmethod(criar_com_50_anos)` e `preco_com_imposto = staticmethod(preco_com_imposto)`. O `staticmethod` devolve a função "pelada": chamar `Produto.preco_com_imposto(...)` ou `produto.preco_com_imposto(...)` executa a mesma função, sem injeção de argumento. O `classmethod` devolve um descritor que injeta a CLASSE como primeiro argumento (não a instância!) — e por isso funciona também quando chamado numa subclasse: `cls` será a subclasse, e `cls(...)` cria objetos da subclasse correta.

## Conexões
- Você já usou esse padrão quando: chamou `dict.fromkeys(...)`, `set.fromkeys?` — métodos de classe nativos do Python
- Aparece também em: `datetime.date.today()` (factory), ORMs (Django `objects.create(...)`), `Enum` e dataclasses (geradores automáticos)
- Diferente de: método de instância (recebe `self`, mexe no objeto), property (controla acesso a atributo), decorator comum (modifica funções, não é feito para fábricas)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre o primeiro parâmetro de `@classmethod` e o de `@staticmethod`?
2. Escreva uma classe `Data` com um `@classmethod` `de_hoje()` e um `@staticmethod` `bissexto(ano)`.
3. Por que `cls(...)` dentro de um `@classmethod` funciona também em uma subclasse?

---

**Frase-âncora:** O classmethod é a fábrica que recebe a classe e fabrica; o staticmethod é o totem que só calcula — sem saber de quem nem de quê.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14