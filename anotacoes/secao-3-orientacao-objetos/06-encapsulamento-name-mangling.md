# Encapsulamento e name mangling (_ e __)

## Quando você vai usar isso?
Quando você quer sinalizar o grau de confiança dos atributos: público (posso mexer), protegido (`_` — uso interno, não mexa), privado (`__` — nem tente). Também é o momento de entender o que o `__` faz de verdade: ele RENOMEIA o atributo para evitar conflitos em herança — isso é o name mangling.

## Modelo mental
São placas de acesso, não fechaduras: `atributo` é o corredor público; `_atributo` é a área com placa "apenas funcionários" (elevador social em Python: a placa é respeitada por quem é educado); `__atributo` é o cofre com nome trocado — Python muda a etiqueta para `_Classe__atributo`, então quem procura `__atributo` fora da classe não encontra nada.

## Em uma linha
Em Python, encapsulamento é convenção: `nome` é público, `_nome` é protegido (por convenção) e `__nome` é "privado" via name mangling — o Python renomeia para `_Classe__nome` e acessar pela etiqueta original dá AttributeError.

## Na prática

### Caso simples
```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular      # ← público: leitura e escrita livres
        self.__saldo = saldo_inicial  # ← "privado": só os métodos mexem

    @property
    def saldo(self):                # ← porta de LEITURA controlada
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError('Valor deve ser positivo')
        self.__saldo += valor       # ← dentro da classe: nome normal

conta = ContaBancaria('Ana', 100.0)
print(conta.saldo)                  # ← 100.0 via property
# print(conta.__saldo)              # ← AttributeError!
print(vars(conta))                  # ← {'titular': 'Ana', '_ContaBancaria__saldo': 100.0}
```

### Com variação
```python
class Produto:
    def __init__(self, nome):
        self.__nome = nome          # ← privado

    @property
    def nome(self):
        return self.__nome

p = Produto('Camiseta')
# p.__nome                          # ← AttributeError (etiqueta trocada)
print(p._Produto__nome)             # ← 'Camiseta' — name mangling na prática
# ← porém é COERÇÃO, não segurança: saber o nome não justifica usar
```

### Em uso real
```python
class Pedido:
    def __init__(self):
        self.__itens = []           # ← estado interno que ninguém edita por fora

    def adicionar(self, item):
        self.__itens.append(item)

    def listar(self):
        return list(self.__itens)   # ← devolve CÓPIA: quem chama não muda o interno

pedido = Pedido()
pedido.adicionar('Camiseta')
print(pedido.listar())              # ← ['Camiseta']
# pedido.__itens                    # ← AttributeError — protegido de verdade
```

## O que NÃO fazer
```python
# ← ERRADO: acreditar que __ é segurança de verdade
p._Produto__nome = 'Hackeado'       # ← funciona! mangling é convenção
# ← o certo: trust the convention — coloque __ para NÃO DEIXAR NINGUÉM MEXER

# ← ERRADO: usar __ em classe que será HERDADA
class Base:
    def __init__(self):
        self.__valor = 10           # ← vira _Base__valor

class Filho(Base):
    def __init__(self):
        super().__init__()
        self.__valor = 20           # ← vira _Filho__valor — OUTRO atributo!
# ← o certo: _valor (uma cópia só, acessível na hierarquia)

# ← CUIDADO: acessar _atributo de outro objeto "de passagem"
print(outra_conta._saldo)           # ← funciona, mas fura o encapsulamento
# ← o certo: property pública E métodos da própria classe para mexer
```

## Por que Python funciona assim?
No momento da definição, o compilador reescreve `self.__nome` para `self._Classe__nome` (com o nome da classe onde o atributo foi escrito). Isso existe para resolver o problema real de nomeação em hierarquias: um atributo `__valor` da base não colide com outro `__valor` do filho, porque cada um vira `_Base__valor` e `_Filho__valor`. Não há "private" de verdade em Python — a linguagem escolheu confiança e clareza (Zen: "explicit is better than implicit" e "we are all consenting adults"). O `_` simples é só anotação cultural: ferramentas (IDE, lint) respeitam, Python não.

## Conexões
- Você já usou esse padrão quando: viu `_private` e `__dunder__` em bibliotecas — `__repr__` é "reservado", `_foo` é "interno", métodos de classes do Django como `_meta`
- Aparece também em: name mangling em herança (aula 148), `vars()`/`__dict__` mostrando os nomes reescritos, pydantic com campos "privados"
- Diferente de: property (controla acesso de forma elegante), herança (reuso — e é onde o `__` evita colisão), atributo público simples (sem barreira alguma)

---

## Teste de recuperação — responda sem olhar para cima

1. Para onde vai o nome de `self.__saldo` escrito dentro da classe `ContaBancaria`?
2. Escreva uma classe `Cofre` com `__senha` e métodos `abrir()`/`fechar()` que usam a senha internamente.
3. Por que `__` existe para herança e não para "proteção absoluta"?

---

**Frase-âncora:** Python não tranca portas — troca a etiqueta (mangling) e confia na placa (`_`): encapsulamento é contrato entre adultos.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14