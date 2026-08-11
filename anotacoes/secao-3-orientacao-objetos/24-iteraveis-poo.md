# Classes iteráveis e iteradores (__iter__, __next__, StopIteration)

## Quando você vai usar isso?
Quando você tem uma sequência no seu domínio que merece ser percorrida no `for`: uma tabuada, os números de Fibonacci, as páginas de um documento, os clientes de uma fila. Também quando você quer que o seu objeto seja aceito por `list()`, `tuple()`, `enumerate()`, `zip()` — tudo isso só sabe uma coisa: pedir o `__iter__` e consumir com `__next__` até o `StopIteration`.

## Modelo mental
Iterável é a PIZZA inteira; iterador é a PESSOA comendo fatia por fatia. A pizza (iterável) pode ser comida quantas vezes quiser — cada `for` ganha um prato novo; mas quem está comendo (o iterador) ESGOTA: quando come a última fatia, o prato fica vazio e não volta atrás. O `for` é o garçom: pergunta "tem mais?" e, quando o prato grita `StopIteration`, encerra a refeição — você nunca vê a gritaria, o `for` engole.

## Em uma linha
Iterável é quem fornece `__iter__` (a "máquina de iteradores"); iterador é quem implementa `__next__` e levanta `StopIteration` quando acaba — e o `for`, `list()`, `enumerate` e `zip` consomem qualquer um dos dois.

## Na prática

### Caso simples (iterador manual com __next__)
```python
class Tabuada:
    def __init__(self, numero, limite=10):
        self.numero = numero
        self.limite = limite
        self.atual = 0          # ← ESTADO da iteração vive no objeto

    def __iter__(self):
        return self             # ← devolve a si mesmo: iterável e iterador

    def __next__(self):
        self.atual += 1
        if self.atual > self.limite:
            raise StopIteration      # ← avisa o for: acabou!
        return self.numero * self.atual

for resultado in Tabuada(7):
    print(resultado)            # ← 7, 14, 21, ..., 70 (uma passada só)
print(list(Tabuada(7)))         # ← [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```

### Com variação (iterável separado do iterador — pode repetir)
```python
class Numeros:
    def __init__(self, limite):
        self.limite = limite

    def __iter__(self):          # ← entrega um iterador NOVO a cada vez
        return iter(range(1, self.limite + 1))

n = Numeros(3)
print(list(n))                   # ← [1, 2, 3]
print(list(n))                   # ← [1, 2, 3] — de novo! iterável não esgota
# ← a PIZZA sobra; quem esgota é o iterador de cada for
```

### Em uso real (__iter__ como gerador com yield)
```python
class Fibonacci:
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def __iter__(self):
        # ← gerador (Seção 2): yield vira um iterador embutido
        # ← o estado (a, b) mora na GERAÇÃO, não no objeto
        a, b = 0, 1
        for _ in range(self.quantidade):
            yield a              # ← pausa e entrega; continua na próxima volta
            a, b = b, a + b

fib = Fibonacci(7)
print(list(fib))                 # ← [0, 1, 1, 2, 3, 5, 8]
print(list(zip(fib, 'abcdefg'))) # ← [] — ESGOTOU na passada anterior!
# ← iterador é de uma passada só; recrie a instância para novo ciclo

# iter() e next() na mão:
t = iter(Tabuada(2, limite=2))   # ← iter() chama __iter__
print(next(t))                   # ← 2
print(next(t))                   # ← 4
# print(next(t))                 # ← StopIteration (agora você vê a gritaria)
```

## O que NÃO fazer
```python
# ← ERRADO: iterável que não esgota, mas usa estado global compartilhado
class Fila:
    def __init__(self, itens):
        self.itens = itens
        self.i = 0               # ← estado na CLASSE errada: fila única

    def __iter__(self):
        return self

    def __next__(self):          # ← dois fors disputam o MESMO índice
        ...
# ← o certo: cada chamada de __iter__ devolve um iterador INDEPENDENTE
# ← (objeto novo, ou yield → gerador novo; dois fors em paralelo)

# ← ERRADO: esquecer o StopIteration — o for nunca termina
def __next__(self):
    if self.atual >= self.limite:
        return None              # ← for continua pedindo... loop infinito!
# ← o certo: raise StopIteration quando acabou (None É um valor válido)

# ← ERRADO: achar que o iterador dá duas passadas
iterador = iter(Tabuada(3))
print(list(iterador))            # ← [3, 6, 9, ...]
print(list(iterador))            # ← [] — gasto na primeira passada!
# ← o certo: guardar o ITERÁVEL e pedir iter() de novo para cada passada
```

## Por que Python funciona assim?
O `for` é um protocolo de duas etapas: primeiro ele chama `iter(objeto)`, que resolve `type(objeto).__iter__` — se existir, retorna um iterador; se não, Python tenta o fallback da iteração por índices (`__getitem__` de 0 em diante, até `IndexError`). Depois ele fica chamando `next(iterador)` (o `__next__`) até escutar `StopIteration` — que é uma exceção de CONTROLE, capturada silenciosamente pelo próprio `for`. Um gerador (`yield`) é só um iterador que a linguagem construiu para você: a função vira uma máquina de estados que pausa no `yield` e retoma na próxima chamada de `next()` — por isso `__iter__` com `yield` entrega um iterador novo e independente a cada chamada, sem você gerenciar o estado na mão.

## Conexões
- Você já usou esse padrão quando: fez `for x in lista` — `list` é iterável; e `enumerate`, `zip` e `list()` no seu código consumindo qualquer iterável
- Aparece também em: geradores da Seção 2 (`yield`), compreensões de lista (chamam o protocolo por baixo), `collections.abc` (`Iterable`, `Iterator`, `Sequence`), `map`/`filter` (retornam iteradores que esgotam)
- Diferente de: `__getitem__` + `IndexError` (protocolo antigo, sem `__iter__` — funciona no `for` mas não em `iter()` explícito), `Sequence` (iterável COM índices e `len`, como `list`), iterador vs gerador (gerador É um iterador, criado por função, sem classe)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença conceitual entre iterável e iterador, e o que o `StopIteration` sinaliza?
2. Escreva a classe `Tabuada` com `__iter__` e `__next__` manuais que pare de forma correta.
3. Por que um iterador só dá UMA passada, e como `yield` resolve esse problema na prática?

---

**Frase-âncora:** A pizza não esgota; o prato, sim — entregue um prato novo a cada `for`, e `StopIteration` é o "acabou".
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14