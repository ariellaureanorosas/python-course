# __new__ e o padrão singleton (a parteira da instância)

## Quando você vai usar isso?
Quando você precisa controlar o MOMENTO e a FORMA da criação do objeto — não apenas configurá-lo depois de pronto. O exemplo clássico é o singleton: uma classe com NO MÁXIMO uma instância em todo o programa (configuração global, conexão de banco, logger, cache de serviço). Como `__new__` é o método que CRIA o objeto (roda antes do `__init__`), é nele que vive qualquer regra do tipo "quantas instâncias podem existir". Fora singleton e fábricas com cache, `__new__` é raro — a maioria dos casos resolve com classe normal.

## Modelo mental
`__new__` é a parteira: é ela quem FAZ NASCER o bebê (aloca a instância crua). `__init__` é a mãe: dá o nome e veste as roupinhas (configura os atributos). A parteira trabalha antes, a mãe depois — sempre nessa ordem. Se a parteira for gulosa e já tiver um bebê no cofre (`_instancia`), ela ENTREGA O MESMO bebê de novo e o `__init__` até chora pra configurar, mas ninguém nasce de novo. Singleton é exatamente essa parteira com cofre: a primeira chamada `Configuracao()` nasce; todas as outras recebem a mesma criança.

## Em uma linha
`__new__` cria e retorna a instância antes de `__init__` configurá-la; o singleton guarda a primeira instância numa variável da classe (`_instancia`) e devolve SEMPRE a mesma.

## Na prática

### Caso simples (ordem: __new__ antes de __init__)
```python
class Numero:
    def __new__(cls, valor):
        print('__new__: criando a instância')
        instancia = super().__new__(cls)   # ← aloca o objeto cru
        return instancia                   # ← SEMPRE retornar a instância

    def __init__(self, valor):
        print('__init__: configurando')
        self.valor = valor

n = Numero(10)
# ← __new__: criando a instância
# ← __init__: configurando
print(n.valor)               # ← 10
```

### Com variação (singleton com guard de inicialização)
```python
class Configuracao:
    _instancia = None        # ← o cofre da parteira
    _inicializada = False    # ← guard: configura SOMENTE na primeira chamada

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if not self._inicializada:      # ← sem isso, o 2º __init__ apagaria tudo
            self.tema = 'claro'
            self._inicializada = True

c1 = Configuracao()
c1.tema = 'escuro'
c2 = Configuracao()
print(c1 is c2)              # ← True — a MESMA instância
print(c2.tema)               # ← 'escuro' — não foi resetado pelo 2º __init__
```

### Em uso real (cache de instâncias via __new__)
```python
class Usuario:
    _cache = {}              # ← parteira com memória: um Usuario por id

    def __new__(cls, id_, nome):
        if id_ in cls._cache:
            return cls._cache[id_]      # ← devolve o que já existia
        instancia = super().__new__(cls)
        cls._cache[id_] = instancia
        return instancia

    def __init__(self, id_, nome):
        self.id_ = id_
        self.nome = nome

u1 = Usuario(1, 'Ana')
u2 = Usuario(1, 'Ana')
print(u1 is u2)              # ← True — mesmo objeto do cache
print(len(Usuario._cache))   # ← 1

# ── Thread-safety: o `if cls._instancia is None` NÃO é atômico ─────────
# Duas threads podem passar a checagem ao mesmo tempo e criar 2 instâncias
# (corrida clássica). Soluções: criar a instância com antecedência (eager),
# usar threading.Lock em volta, ou... aceitar se a inicialização é única
# e o dano é zero.

# ── Alternativa simples: um MÓDULO já é um singleton ──────────────────
# # config.py
# TEMA = 'claro'            # ← um import por processo: todos leem o mesmo
# # uso.py
# from config import TEMA   # ← sem classe, sem __new__, sem cofre
```

## O que NÃO fazer
```python
# ← ERRADO: esquecer o return no __new__ — a instância morre no nascedouro
def __new__(cls):
    super().__new__(cls)        # ← descarta o resultado → retorna None
# n = MinhaClasse()             # ← n é None! (silencioso e bizarro)
# ← o certo: `return super().__new__(cls)` SEMPRE

# ← ERRADO: __init__ retornando um valor
def __init__(self):
    self.x = 1
    return 'pronto'             # ← TypeError: __init__() should return None
# ← o certo: sem return (None implícito) ou `return` puro

# ← ERRADO: singleton sem o guard _inicializada — estado apagado na 2ª chamada
class Configuracao:
    _instancia = ...
    def __init__(self):
        self.tema = 'claro'     # ← c2 = Configuracao() voltaria a 'claro'
# ← o certo: flag _inicializada (ou configurar fora do __init__)

# ← ERRADO: usar __new__ para VALIDAR dados — validação é do __init__/setter
def __new__(cls, idade):
    if idade < 0:
        raise ValueError(...)   # ← funciona, mas entulha a parteira
# ← o certo: __new__ só decide COMO criar; validar no __init__
```

## Por que Python funciona assim?
Chamar `Classe()` executa `type.__call__`, que orquestra: primeiro chama `Classe.__new__(cls, ...)` — retorno esperado: uma instância — e só DEPOIS, se ela for instância de `Classe` (ou subclasse), chama `Classe.__init__(instancia, ...)`. Detalhe poderoso: se `__new__` retornar uma instância de OUTRA classe, o `__init__` é PULADO — é assim que `int.__new__` devolve inteiros do cache e `__init__` nem roda. Por isso o singleton funciona: a checagem e o reuso acontecem antes do benefício (configuração), e o `__init__`, que roda em TODA chamada, precisa do guard `_inicializada` para não reconfigurar. E por ser `staticmethod` implícito, `__new__` recebe `cls` (a classe), não a instância — porque instância ainda não existe.

## Conexões
- Você já usou esse padrão quando: chamou `int(5)` (o int devolve do CACHE de inteiros pequenos via `__new__`; por isso `int(5) is int(5)` pode dar `True`) e quando comparou `x is y` de singletons nativos como `True`, `None` e `NotImplemented`
- Aparece também em: metaclasses (o `__call__` que executa `__new__` é da metaclasse), ORMs com identity map (uma linha do banco = uma instância), `functools.lru_cache` (mesma ideia, para resultados), kits de DI (injeção de dependência) que garantem um único service
- Diferente de: `@classmethod` fábrica (`Pessoa.com_nome(...)` cria uma instância NORMAL — não controla quantas existem), módulo Python (singleton de graça, sem classe), `__init_subclass__` (age na criação da CLASSE, não da instância)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a ordem exata de execução entre `__new__` e `__init__`? E o que acontece se `__new__` retorna um objeto de OUTRA classe?
2. Escreva um singleton `Log` com `__new__` que devolve sempre a mesma instância.
3. Por que o singleton precisa do guard `_inicializada`? (O que o segundo `__init__` faria sem ele?)

---

**Frase-âncora:** `__new__` é a parteira que decide se nasce um bebê novo ou se entrega o mesmo de sempre — o `__init__` só configura o que já nasceu.
**Nível:** Avançado
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14