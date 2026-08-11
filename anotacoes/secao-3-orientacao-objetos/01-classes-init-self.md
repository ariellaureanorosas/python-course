# Classes (__init__ e self)

## Quando você vai usar isso?
Você precisa guardar dados que andam SEMPRE juntos (nome + sobrenome, x + y, produto + preço) e quer que eles carreguem junto um comportamento (nome_completo(), distancia()). Em vez de duas listas paralelas ou dicionários soltos, você cria uma classe e cada objeto é uma "ficha preenchida".

## Modelo mental
Classe é a forminha de biscoito: ela define o formato, mas não é biscoito. Cada instância é um biscoito feito com a forminha, com os seus próprios ingredientes. O `__init__` é a ficha que roda na hora de preencher cada biscoito — é onde você diz "todo objeto criado vai ter nome e sobrenome".

## Em uma linha
Classe define o molde com `__init__` (construtor) que recebe os dados; `self` é o próprio objeto, usado para guardar e acessar os atributos de cada instância.

## Na prática

### Caso simples
```python
class Pessoa:                    # ← PascalCase, sempre com letra maiúscula
    def __init__(self, nome, sobrenome):
        # ← roda AUTOMATICAMENTE na criação; self é o objeto novo
        self.nome = nome         # ← guarda o valor no objeto
        self.sobrenome = sobrenome

    def nome_completo(self):     # ← método: função que age sobre o objeto
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('Maria', 'Silva')    # ← __init__ roda aqui
p2 = Pessoa('João', 'Santos')
print(p1.nome_completo())  # ← 'Maria Silva'
print(p2.nome_completo())  # ← 'João Santos'
```

### Com variação
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def com_desconto(self, percentual):
        # ← método pode usar os atributos do próprio objeto
        return self.preco * (1 - percentual / 100)

camiseta = Produto('Camiseta', 49.90)
print(camiseta.com_desconto(10))  # ← 44.91

# ← self é passado implicitamente — as duas chamadas abaixo são iguais:
camiseta.com_desconto(10)            # açúcar sintático
Produto.com_desconto(camiseta, 10)   # a forma real por baixo
```

### Em uso real
```python
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):          # ← representação para depuração (aula 155)
        return f'Cliente(nome={self.nome!r}, email={self.email!r})'

clientes = [
    Cliente('Ana', 'ana@email.com'),
    Cliente('Bia', 'bia@email.com'),
]
print(clientes)  # ← sem __repr__: <__main__.Cliente object at 0x...>
```

## O que NÃO fazer
```python
# ← ERRADO: esquecer self no primeiro parâmetro
class Pessoa:
    def __init__(nome, sobrenome):   # ← sem self → TypeError na criação
        self.nome = nome

# ← ERRADO: "inventar" atributos fora do __init__
p = Pessoa('Maria', 'Silva')
p.telefone = '(11) 99999-0000'   # ← funciona, mas cada objeto pode ter
# ← conjuntos de atributos diferentes → código imprevisível

# ← ERRADO: guardar dados em variável local em vez do atributo
def __init__(self, nome):
    nome = nome                  # ← some ao fim do __init__, objeto fica vazio!
```

## Por que Python funciona assim?
`self` não é uma palavra reservada especial: é apenas o PRIMEIRO parâmetro, e Python passa o próprio objeto nele na chamada `p.metodo()`. O `__init__` não é um construtor de verdade — isso é o `__new__` (aula 157) — ele é o inicializador que roda logo após o objeto existir, para preencher a ficha. Por isso `__init__` retorna `None` sempre e você nunca dá `return` nele.

## Conexões
- Você já usou esse padrão quando: criou um dict com as mesmas chaves sempre (`{'nome': ..., 'idade': ...}`) — era uma classe "anônima"
- Aparece também em: dataclasses (geram `__init__` automaticamente), NamedTuple, Django models (cada `class Produto(models.Model)` é uma tabela)
- Diferente de: dicionário (armazena sem comportamento validado), `lambda` (função sem estado), função pura (mesma entrada, mesma saída, sem memória)

---

## Teste de recuperação — responda sem olhar para cima

1. O que acontece sem o parâmetro `self` em um método de instância?
2. Escreva uma classe `Retangulo` com `__init__(largura, altura)` e um método `area()`.
3. Por que `p1.metodo()` e `Pessoa.metodo(p1)` fazem a mesma coisa?

---

**Frase-âncora:** Classe é o molde, instância é o biscoito, e `self` é a mão do biscoito para mexer nos próprios ingredientes.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14