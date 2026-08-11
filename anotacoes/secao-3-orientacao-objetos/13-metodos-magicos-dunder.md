# Métodos especiais (dunder) — __str__, __repr__, __add__, __gt__

## Quando você vai usar isso?
Toda vez que quer que Python saiba como falar do seu objeto: `print(obj)`, `repr(obj)`, `obj + outro`, `obj > outro`, `sorted(lista_de_objetos)`. Sem esses métodos, o Python responde com `<__main__.Ponto object at 0x000001...>` (inútil) e `+`/`>` explodem com TypeError. Implementá-los é o que torna a classe "cidadã de primeira classe" na linguagem.

## Modelo mental
São os manuais de instrução que o Python consulta embaixo da mesa: quando você escreve `print(p)`, Python não "sabe" imprimir Ponto — ele pergunta ao próprio Ponto via `__str__`: "como você quer que eu te mostre?". Quando escreve `a + b`, ele pergunta ao `a`: `type(a).__add__(a, b)`. Os operadores são só açúcar sintático para esses métodos.

## Em uma linha
`__str__` é a cara para usuários (print), `__repr__` é a cara para devs (REPL, listas, f'{x!r}'), `__add__`/`__gt__`/`__eq__` fazem `+`, `>` e `==` funcionarem com seus objetos — e é bom SEMPRE ter `__repr__` antes de tudo.

## Na prática

### Caso simples
```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Ponto({self.x}, {self.y})'   # ← o que um dev espera ver

    def __str__(self):
        return f'({self.x}, {self.y})'        # ← o que um usuário lê

p = Ponto(1, 2)
print(p)          # ← (1, 2)      → usa __str__
repr(p)           # ← 'Ponto(1, 2)' → usa __repr__
print(f'{p!r}')   # ← Ponto(1, 2)  → !r força o __repr__
```

### Com variação (operadores)
```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Ponto({self.x}, {self.y})'

    def __add__(self, outro):           # ← a + b → a.__add__(b)
        return Ponto(self.x + outro.x, self.y + outro.y)

    def distancia_da_origem(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __gt__(self, outro):            # ← a > b → a.__gt__(b)
        return self.distancia_da_origem() > outro.distancia_da_origem()

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
print(p1 + p2)          # ← Ponto(4, 6)
print(Ponto(3, 4) > Ponto(1, 1))   # ← True
```

### Em uso real (ordenar objetos)
```python
import random

pontos = [Ponto(random.randint(0, 5), random.randint(0, 5)) for _ in range(5)]
ordenados = sorted(pontos)     # ← sorted usa __gt__ (ou __lt__)
maior = max(pontos)            # ← max também!
print(maior)
# ← só porque Ponto sabe se comparar, sorted/max/min funcionam de graça
```

## O que NÃO fazer
```python
# ← ERRADO: __str__ sem __repr__ — metade do "manual" faltando
def __str__(self):
    return f'({self.x}, {self.y})'
# ← print(self) ok, mas listas/REPL continuam mostrando <object at...>

# ← ERRADO: __add__ que MUTA o objeto (operações devem devolver novo)
def __add__(self, outro):
    self.x += outro.x            # ← mudou o original sem avisar!
    return self
# ← p1 + p2 deveria deixar p1 intacto — devolva um objeto NOVO

# ← CUIDADO: __eq__ sem __hash__ consistente
def __eq__(self, outro):
    return self.x == outro.x and self.y == outro.y
# ← se igualdade é por VALOR, um objeto mutável com __eq__ vira
# ← uma chave de dict perigosa; pesquise __hash__ antes de usar em sets
```

## Por que Python funciona assim?
Toda operação que parece mágica é uma chamada de método: `a + b` tenta `type(a).__add__(a, b)` e, se não existir/retornar NotImplemented, tenta `type(b).__radd__(b, a)`; `print` chama `str()`, que chama `__str__` (e o fallback é `repr` se só houver `__repr__`); o `==` padrão, quando `__eq__` não existe, compara por IDENTIDADE de objeto (dois objetos iguais em valor são !=). Por isso classes de dados (dataclasses) geram `__eq__`, `__repr__`, `__lt__` automaticamente — é o mesmo protocolo por baixo.

## Conexões
- Você já usou esse padrão quando: usou `len(lista)` (protocolo `__len__`), `d['chave']` (`__getitem__`), `for i in itens` (`__iter__`/`__next__` — aula 177)
- Aparece também em: comparadores de `sorted`/`max`/`min`, `f'{x!r}'` em logs, context managers (`__enter__`/`__exit__` — aula 158), `__call__` (aula 164)
- Diferente de: `__init__` (configura o objeto, não fala dele), `@property` (calcula atributo, não opera), métodos normais (precisam de chamada explícita com parênteses)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual método o `print()` usa e qual o REPL usa para exibir um objeto?
2. Escreva uma classe `Dinheiro` com `__repr__`, `__add__` e `__gt__`.
3. O que acontece com `a + b` se `a` não tiver `__add__` e `b` não tiver `__radd__`?

---

**Frase-âncora:** Operadores e prints são perguntas disfarçadas: o Python pergunta ao seu objeto, e os dunders são as respostas.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14