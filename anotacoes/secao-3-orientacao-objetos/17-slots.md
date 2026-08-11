# __slots__ (memória sob controle)

## Quando você vai usar isso?
Quando sua classe vai gerar MILHARES ou milhões de instâncias e a memória importa — cada objeto comum carrega um `__dict__` (um dicionário inteiro) que responde por boa parte do peso. Ou quando você quer uma classe-ESTRUTURA (um record), com conjunto fixo e conhecido de atributos: slots trava o formato e corta o custo. Também é útil quando atributos criados ao acaso são bug (tipografia `p.z = 3` que ninguém pediu): com slots, isso explode com `AttributeError` na hora, em vez de sobreviver escondido.

## Modelo mental
Um objeto comum é uma mochila aberta: cabe qualquer coisa dentro (`obj.atributo_novo = 1` sempre funciona), mas a mochila (o `__dict__`) pesa e não tem portas para travar. `__slots__` troca a mochila por um guarda-roupa com GAVETAS FIXAS: as gavetas (`x`, `y`) existem, são rápidas e acessadas direto — mas ninguém pendura uma prateleira nova no meio. Tentou (`p.z = 3`)? O guarda responde: `AttributeError`.

## Em uma linha
`__slots__ = ('x', 'y')` declara quais atributos a instância pode ter e elimina o `__dict__` — menos memória, acesso na mesma velocidade e erro em qualquer atributo fora da lista.

## Na prática

### Caso simples
```python
class Ponto:
    __slots__ = ('x', 'y')      # ← só existem essas duas gavetas

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Ponto(2, 3)
print(p.x, p.y)                 # ← 2 3
print(p.__slots__)              # ← ('x', 'y')
# p.z = 5                       # ← AttributeError: 'Ponto' object has no attribute 'z'
# print(p.__dict__)             # ← AttributeError: não existe __dict__!
```

### Com variação (herança: slots se somam)
```python
class PontoComCor(Ponto):
    __slots__ = ('cor',)        # ← somou a gaveta da subclasse

pc = PontoComCor(1, 1, 'azul')
print(pc.x, pc.cor)             # ← 1 azul

class PontoSolto(Ponto):        # ← subclasse SEM __slots__
    pass                        # ← a mochila volta! ganha __dict__ de novo

s = PontoSolto(1, 2)
print(hasattr(s, '__dict__'))   # ← True — herdar sem slots recria o dicionário
s.z = 42                        # ← e atributo livre volta a funcionar
```

### Em uso real (muitas instâncias + medindo a diferença)
```python
import sys

class Ponto:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Ponto({self.x}, {self.y})'

pontos = [Ponto(i, i * 2) for i in range(100_000)]
print(len(pontos))                       # ← 100000
print(pontos[-1])                        # ← Ponto(99999, 199998)

class PontoComDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(sys.getsizeof(Ponto(1, 1)))             # ← 32  (sem __dict__)
print(sys.getsizeof(PontoComDict(1, 1)))      # ← 48  (com __dict__)
# ← em 100 mil instâncias: ~1,6 MB a menos — e sem dicionário, o cache
# de atributos do interpretador trabalha melhor

# Obs.: precisa de referência fraca (weakref)? Declare __weakref__ também.
class Aluno:
    __slots__ = ('_nome', '__weakref__')      # ← libera weakref.ref(instancia)
    def __init__(self, nome):
        self._nome = nome
```

## O que NÃO fazer
```python
# ← ERRADO: esquecer slots na SUBCLASSE — todo o lucro se perde
class PontoHerdado(Ponto):
    pass                        # ← cada instância volta a ter __dict__
# ← o certo: repetir __slots__ em CADA nível da hierarquia

# ← ERRADO: declarar __dict__ dentro de __slots__ achando que ainda ganha
class Trapacero:
    __slots__ = ('x', '__dict__')   # ← a mochila entra pela porta dos fundos
# ← o certo: slots sem __dict__, ou dicionário simples sem slots

# ← CUIDADO: nome com DOIS underscores é name mangling (vira _Classe__nome)
class Segredo:
    __slots__ = ('__senha',)        # ← internamente: _Segredo__senha
    def __init__(self, senha):
        self.__senha = senha        # ← ok aqui (mangling aplicado dos dois lados)
# Segredo('abc').__senha            # ← AttributeError: nem parece que existe
# ← o certo: para slots, prefira UM underscore (_senha) e evite a confusão

# ← CUIDADO: dar valor padrão no corpo da classe com slots dá Shared Memory
# class Ponto:
#     __slots__ = ('x', 'y')
#     x = 1                 # ← não: cai na classe, não por instância
# ← o certo: inicializar sempre no __init__ (ou usar descritor)
```

## Por que Python funciona assim?
Toda classe criada com `class` ganha, por padrão, o `__dict__` para as instâncias — foi assim desde sempre, por flexibilidade. Quando você escreve `__slots__`, no momento da DEFINIÇÃO da classe o interpretador calcula o tamanho fixo da instância e cria, para cada nome da lista, um `member_descriptor` na classe (é por isso que `Ponto.x` existe e é acessível antes de qualquer instância — slots são descritores! é o mesmo mecanismo do `@property` passando por `__get__`/`__set__`). A economia vem de dois lugares: sem `__dict__` (dicionário de ~1/3 do peso total de um objeto) e com acesso direto pelo offset calculado, sem passar por hash. Na herança, os descritores dos slots do pai continuam na classe filha (por isso se "somam"); mas se a filha não declara `__slots__`, ela recebe o `__dict__` padrão de volta. E `__weakref__` precisa ser declarado porque sem `__dict__` não existe onde guardar a referência fraca.

## Conexões
- Você já usou esse padrão quando: usou `@dataclass(slots=True)` sem saber — o decorator só aplica `__slots__` por baixo; e quando acessou `Ponto.x` na classe (os slots são descritores, como property)
- Aparece também em: dataclasses (`@dataclass(slots=True)`, Python 3.10+), Pydantic (`model_config = ConfigDict(slots=True)`), ORMs como SQLAlchemy e Django (classes de tabela com campos fixos), classes do próprio CPython (muitas são slots para economizar memória)
- Diferente de: `@dataclass` (gera `__init__`/`__repr__`, não trava atributos), `namedtuple` (tupla imutável, sem métodos), `__getattr__` (objeto ABERTO: intercepta qualquer atributo inexistente — o oposto de travar o formato), `__dict__` padrão (flexível, porém pesado)

---

## Teste de recuperação — responda sem olhar para cima

1. O que acontece se você tenta criar um atributo fora da lista de `__slots__`? E por que `p.__dict__` também falha?
2. Sua subclasse herda `__slots__` do pai mas NÃO declara os seus. O que ela ganha de volta e como corrigir?
3. Por que é preciso declarar `__weakref__` entre os slots para usar `weakref.ref()`? E o que o name mangling faz com `__senha`?

---

**Frase-âncora:** `__slots__` troca a mochila aberta por gavetas fixas: menos peso, e o `AttributeError` avisa antes que o atributo errado sobreviva.
**Nível:** Avançado
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14