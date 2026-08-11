# Dataclasses

## Quando você vai usar isso?
Quando a classe é quase só dados + um pouco de comportamento — Produto(nome, preco), Pedido(numero, itens), Usuario(email, nome). Em vez de escrever `__init__`, `__repr__`, `__eq__` na mão (muito boilerplate), o `@dataclass` gera tudo. É o padrão sênior para 90% das classes de dados no Python moderno (PEP 557).

## Modelo mental
É a montadora de carros: você entrega a lista de peças (os campos tipados) e ela produz o carro completo — `__init__` (motor), `__repr__` (placa descritiva), `__eq__` (conferir se dois carros são iguais por valor). as opções `frozen=True` (carro blindado: nada muda depois de sair da fábrica), `order=True` (direção que sabe comparar) e `field` (peças opcionais com fábrica própria).

## Em uma linha
`@dataclass` gera `__init__`, `__repr__` e `__eq__` a partir dos campos tipados; `frozen=True` congela (imutável); `order=True` habilita comparações e `sorted`; `field(default_factory=...)` cria uma coleção NOVA para cada instância.

## Na prática

### Caso simples
```python
from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float

p1 = Produto('Caneta', 3.50)
p2 = Produto('Caneta', 3.50)
print(p1)                    # ← Produto(nome='Caneta', preco=3.5)  (repr grátis)
print(p1 == p2)              # ← True  (eq por VALOR, não por identidade)
# ← sem dataclass: precisaria de 12 linhas de métodos manuais
```

### Com variação (frozen + order + field)
```python
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Produto:
    nome: str
    preco: float
    categorias: list[str] = field(default_factory=list, repr=False)
    # ← default_factory: CADA instância ganha a própria lista
    # ← repr=False: categorias não poluem o repr (que é usado em logs)

caneta = Produto('Caneta', 3.50)
caderno = Produto('Caderno', 12.90)
print(caneta < caderno)      # ← True (order=True gera __lt__ etc.)
print(repr(caneta))          # ← Produto(nome='Caneta', preco=3.5) — sem a lista
# caneta.nome = 'Lápis'      # ← FrozenInstanceError! congelado
```

### Em uso real (asdict + astuple)
```python
from dataclasses import asdict, astuple, dataclass, field

@dataclass(frozen=True)
class Pedido:
    numero: int
    produtos: list[Produto] = field(default_factory=list)

    @property
    def total(self):                     # ← comportamento junto dos dados
        return sum(p.preco for p in self.produtos)

pedido = Pedido(1, [caneta, caderno])
print(pedido.total)                      # ← 16.4
print(asdict(pedido))
# ← {'numero': 1, 'produtos': [{'nome': 'Caneta', 'preco': 3.5, 'categorias': []}, ...]}
print(astuple(pedido))
# ← (1, [Produto(nome='Caneta', preco=3.5), ...])
# ← caminho natural para JSON/serialização (aula 137)
```

## O que NÃO fazer
```python
# ← ERRADO: lista como default direto — compartilha a MESMA lista!
@dataclass
class Carrinho:
    itens: list = []          # ← perigo: TODO carrinho nasce com esta lista

c1 = Carrinho()
c2 = Carrinho()
c1.itens.append('Camiseta')
print(c2.itens)               # ← ['Camiseta'] — vazamento clássico!
# ← o certo: field(default_factory=list)

# ← ERRADO: frozen=True "às cegas" para quem vai mutar bastante
@dataclass(frozen=True)
class Carrinho:
    itens: list = field(default_factory=list)
    def adicionar(self, item):
        self.itens.append(item)   # ← CONSEGUE (a lista é mutável),
        # ← mas a INTENÇÃO de frozen era imutabilidade total
# ← o certo: congelar quando o objeto deve mesmo ser de valor

# ← CUIDADO: dataclass não é para tudo — mandar classes com lógica
# ← complexa de negócio e herança profunda para dataclass fica espremido
# ← o certo: dataclass para DADOS; classe comum para COMPORTAMENTO
```

## Por que Python funciona assim?
O `@dataclass` é um decorator que analisa as anotações de tipo do corpo da classe e GERA métodos (`__init__`, `__repr__`, `__eq__`, e com `order=True` também `__lt__`, `__le__`, `__gt__`, `__ge__` — via uma tupla de campos especial). `field()` controla o comportamento de cada campo: `default_factory` é chamado POR INSTÂNCIA (o que resolve o problema da lista compartilhada), `repr=False` um campo que não aparece, `init=False` um campo calculado (aula 173). `asdict`/`astuple` percorrem recursivamente os campos — por isso aninham dicionários. E `frozen` gera um `__setattr__` que levanta `FrozenInstanceError`.

## Conexões
- Você já usou esse padrão quando: substituiu classes cheias de `self.x = x` e métodos de comparação manuais
- Aparece também em: pydantic (validação além da classe de dados), NamedTuple (tupla imutável com nomes — aula 176), JSON/serialização via asdict
- Diferente de: NamedTuple (imutável por TUPLA, sem métodos de negócio), classe normal com `__init__` manual (boilerplate), dict (sem tipo, sem repr organizado, sem comportamento)

---

## Teste de recuperação — responda sem olhar para cima

1. O que `@dataclass` gera automaticamente a partir dos campos?
2. Escreva uma dataclass `Livro` com `titulo`, `autor` e `categorias: list` segura contra compartilhamento.
3. Por que `field(default_factory=list)` é obrigatório em vez de `= []`?

---

**Frase-âncora:** Dataclass é a montadora de classes de dados: entrega os campos, recebe init, repr e eq sem escrever uma linha de boilerplate.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14