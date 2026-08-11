# Comparação rica de objetos (__lt__, __eq__ e total_ordering)

## Quando você vai usar isso?
Quando os seus objetos precisam ser ORDENADOS — `sorted()`, `max()`, `min()`, `<`, `>` — e ordenar pelo endereço de memória não faz sentido. Você define "o que é maior" no domínio: o jogador com mais pontos, o produto mais caro, a tarefa mais antiga. Também quando precisa comparar igualdade com significado (`==` entre dois objetos deve olhar os campos, não a identidade).

## Modelo mental
Operadores são métodos disfarçados: `a < b` é só açúcar sintático para `a.__lt__(b)`. Quando o Python resolve `sorted(jogadores)`, ele pergunta para os próprios objetos "você é menor que este aqui?" — como pessoas numa fila sendo perguntadas uma a uma "você deixa esse passar na frente?". Se os objetos respondem, a fila (a ordenação) acontece; se não respondem, Python reclama com `TypeError`.

## Em uma linha
Implemente `__lt__` (+ `__eq__`) para dar ordem e igualdade ao seu objeto; `functools.total_ordering` preenche o resto dos operadores sozinho.

## Na prática

### Caso simples (__lt__ por pontos)
```python
class Jogador:
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    def __lt__(self, outro):
        # ← o único operador que sorted()/max()/min() PRECISAM
        return self.pontos < outro.pontos

    def __repr__(self):
        return f'{self.nome} ({self.pontos})'

jogadores = [Jogador('Ana', 10), Jogador('Bia', 20), Jogador('Caio', 5)]
print(sorted(jogadores))        # ← [Caio (5), Ana (10), Bia (20)]
print(max(jogadores))           # ← Bia (20)
print(min(jogadores))           # ← Caio (5)
print(jogadores[0] < jogadores[1])   # ← True
```

### Com variação (__eq__ + total_ordering)
```python
from functools import total_ordering

@total_ordering   # ← a partir de __lt__ E __eq__, gera <=, >, >=
class Jogador:
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    def __lt__(self, outro):
        return self.pontos < outro.pontos

    def __eq__(self, outro):
        return self.pontos == outro.pontos

    def __repr__(self):
        return f'{self.nome} ({self.pontos})'

print(Jogador('Ana', 10) >= Jogador('Bia', 5))   # ← True (gerado!)
print(Jogador('Ana', 10) == Jogador('Zé', 10))    # ← True (igualdade por pontos)
```

### Em uso real (ranking com desempate)
```python
from functools import total_ordering

@total_ordering
class Jogador:
    def __init__(self, nome, pontos, partidas):
        self.nome = nome
        self.pontos = pontos
        self.partidas = partidas

    def __lt__(self, outro):
        # ← desempate: menos partidas fica na frente
        return (self.pontos, -self.partidas) < (outro.pontos, -outro.partidas)

    def __eq__(self, outro):
        return (self.pontos, self.partidas) == (outro.pontos, outro.partidas)

    def __repr__(self):
        return f'{self.nome}: {self.pontos} pts em {self.partidas} jogos'

# ← sorted() compara tupla a tupla, igual string/literal comparam
print(sorted([Jogador('Ana', 10, 8), Jogador('Bia', 10, 5)]))
# ← [Bia: 10 pts em 5 jogos, Ana: 10 pts em 8 jogos] — empate em pontos,
# ← menos partidas primeiro
```

## O que NÃO fazer
```python
# ← ERRADO: esquecer __hash__ ao criar __eq__
class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def __eq__(self, outro):      # ← definir __eq__ ANULA o __hash__ herdado!
        return self.nome == outro.nome

j = Jogador('Ana')
# print(hash(j))                  # ← TypeError: unhashable type: 'Jogador'
# print(j in {Jogador('Ana')})    # ← também quebra (set/dict usam hash)
# ← o certo: se precisa de igualdade E hash, defina __hash__ também,
# ← baseado NOS MESMOS campos de __eq__
# ← o certo (rápido): __hash__ = hash(self.nome)

# ← ERRADO: __eq__ comparando com tipo errado sem proteção
def __eq__(self, outro):
    return self.pontos < outro.pontos   # ← se outro for None ou str, AttributeError
# ← o certo: if not isinstance(outro, Jogador): return NotImplemented
# ← (NotImplemented deixa o Python tentar o operador do outro lado)

# ← ERRADO: escrever os 6 operadores na mão
def __le__(self, o): return self.pontos <= o.pontos
def __gt__(self, o): return self.pontos > o.pontos    # ← repetição que
def __ge__(self, o): return self.pontos >= o.pontos   # ← total_ordering evita
# ← o certo: @total_ordering + __lt__ + __eq__
```

## Por que Python funciona assim?
Comparação em Python é resolução de DUPLO despacho: `a < b` chama `type(a).__lt__(a, b)` e, se isso devolver `NotImplemented`, tenta `type(b).__gt__(b, a)` — por isso os operadores são "reflexos" uns dos outros. `sorted()`, `max()` e `min()` só conhecem o protocolo: para ordenar, basta `__lt__` responder `True/False` (equivalente ao método `compareTo` de outras linguagens). `total_ordering` não é mágica: é um decorator que INSPEciona a classe e injeta os operadores que faltam, derivando-os de `__lt__` e `__eq__` (menos eficiente que escrever na mão para casos extremos, mas correto). E `__eq__` sem `__hash__` deixa o objeto `unhashable` porque o contrato do Python exige que objetos iguais tenham o MESMO hash — ele prefere proibir o hash a arriscar quebrar essa regra.

## Conexões
- Você já usou esse padrão quando: chamou `sorted()` numa lista de strings — `str` implementa `__lt__` por ordem alfabética, e `datetime` e `Decimal` também
- Aparece também em: `dataclass` (gera `__eq__`/`__lt__` automaticamente se você pedir `order=True`), `collections.abc` (o protocolo `Ordered`), `heapq` (usa `__lt__` para heap)
- Diferente de: `__eq__`/`__hash__` padrão (comparação por IDENTIDADE — dois objetos separados nunca são iguais), `total_ordering` vs escrever todos os operadores (o decorator é mais curto, a mão é mais rápido), sobrecarga de operador em C++/Java (lá o tipo é fixo na compilação; aqui é resolvido em tempo de execução)

---

## Teste de recuperação — responda sem olhar para cima

1. Quais dois dunders uma classe precisa para funcionar com `sorted()`, `max()` e `min()`?
2. Escreva `@total_ordering` com `__lt__` e `__eq__` para uma classe `Produto` ordenada por `preco`.
3. Por que definir `__eq__` sem `__hash__` torna o objeto `unhashable`?

---

**Frase-âncora:** Seus objetos ganham ordem quando você responde por eles: "este é menor que aquele, este é igual àquele" — o resto dos operadores Python deriva.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14