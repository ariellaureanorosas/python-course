# collections e functools — Ferramentas de containers e funções

## Quando você vai usar isso?
Quando o dicionário padrão não basta: precisa de um dict com valor padrão (`defaultdict`), de um dict que conta ocorrências (`Counter`), de uma fila dupla (`deque`) ou de uma tupla nomeada que documenta campos (`namedtuple`). Em funções, quando você quer fixar argumentos (`partial`), acumular resultados (`lru_cache`) ou gerar comparações completas (`total_ordering`).

## Modelo mental
O módulo `collections` é a caixa de ferramentas de estruturas de dados prontas — você não precisa reinventar um dict com padrão, uma contagem ou uma fila. O módulo `functools` é a caixa de ferramentas de funções — ele edita funções: fixa argumentos, memoiza, completa comparações e compõe decoradores.

## Em uma linha
`collections` entrega estruturas prontas (`Counter`, `defaultdict`, `deque`, `namedtuple`); `functools` entrega ferramentas para transformar funções (`partial`, `lru_cache`, `wraps`, `reduce`).

## Na prática

### Caso simples

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter: conta ocorrencias (texto, listas, palavras)
frase = 'banana'
contagem = Counter(frase)
print(contagem)                # Counter({'a': 3, 'n': 2, 'b': 1})
print(contagem.most_common(1)) # [('a', 3)]

# defaultdict: dict que cria o valor padrao ao acessar
agrupado = defaultdict(list)
agrupado['python'].append('funcao')   # chave nova vira [] automaticamente

# deque: fila eficiente nos dois lados
fila = deque([1, 2, 3])
fila.appendleft(0)             # adiciona a esquerda em O(1)
print(fila)                    # deque([0, 1, 2, 3])

# namedtuple: tupla com campos nomeados
Ponto = namedtuple('Ponto', ['x', 'y'])
p = Ponto(3, 4)
print(p.x, p.y)                # 3 4
```

### Com variação

```python
from functools import partial, lru_cache, total_ordering

# partial: fixa argumentos de uma funcao
from math import pow
quadrado = partial(pow, exp=2)      # fixa o expoente em 2
print(quadrado(5))                  # 25.0

# lru_cache: memoizacao (guarda resultados ja calculados)
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))                      # 12586269025 (rapido, sem recalc)

# total_ordering: completa comparacoes a partir de == e <
@total_ordering
class Item:
    def __init__(self, preco):
        self.preco = preco
    def __eq__(self, outro):
        return self.preco == outro.preco
    def __lt__(self, outro):
        return self.preco < outro.preco
    def __repr__(self):
        return f'Item({self.preco})'

print(Item(5) <= Item(10))          # True (deriva de == e <)
```

### Em uso real

```python
from collections import Counter

# relatorio rapido de log: quais erros mais aparecem?
linhas_log = ['ERRO: rede', 'OK', 'ERRO: rede', 'ERRO: disco']
c = Counter(linhas_log)
print(c.most_common(2))             # [('ERRO: rede', 2), ('OK', 1)]

# cache de biblioteca: consumir API uma vez e reusar
from functools import lru_cache

@lru_cache(maxsize=128)
def buscar_usuario(usuario_id: int) -> dict:
    ...  # num projeto real: chamada HTTP/banco
    return {'id': usuario_id}
```

## O que NÃO fazer

```python
# NAO conte ocorrencias com dict manual quando Counter resolve
# d = {}
# for letra in frase:
#     d[letra] = d.get(letra, 0) + 1
# funciona, mas Counter e declarativo: "conta isso pra mim"

# NAO use lru_cache em funcoes com efeitos colaterais
@lru_cache
# def registrar_venda(...):   se a funcao grava em arquivo/banco,
# memoizar reexecucoes esconderia efeitos que precisam ocorrer

# NAO use namedtuple quando objetos com comportamento sao melhores:
# classes simples com metodos (ex.: Ponto com distancia()) sao mais
# expressivas do que tuplas nomeadas sem metodos.
```

## Por que Python funciona assim?
O Python preza o princípio baterias incluídas: os módulos da stdlib são as peças mais usadas da comunidade, validadas por anos de uso real. `collections` reúne estruturas que em muitas linguagens exigem implementação manual (fila dupla, dict com padrão, contador); `functools` reúne padrões funcionais que em Python clássico exigiam boilerplate (fixar argumento virava lambda; memoizar virava dict manual). Eles existem para você escrever menos código e mais intenção.

## Conexões

- Você já usou esse padrão quando: fez `d.get(chave, 0) + 1` para contar — `Counter` é a versão declarativa; e quando escreveu `lambda x: f(x, 10)` — `partial` fixa esse argumento.
- Isso se conecta com: `itertools` (combinações, permutações, agrupamentos — o irmão de `collections` para iteráveis), `typing` (`namedtuple` e `defaultdict` têm versões tipadas), e `json`/`csv` (contagens e agrupamentos aparecem em análise de dados).
- Isso te prepara para: análise de dados (pandas trabalha com conceitos de `Counter`/`deque`), web scraping (contagem de frequência de termos), e cache de performance em APIs.

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `Counter` e um dict comum ao contar ocorrências?
2. O que `functools.partial` faz com uma função que recebe 2 argumentos?
3. Quando NÃO usar `lru_cache`?

---

**Frase-âncora:** *Baterias incluídas: antes de reescrever uma estrutura ou um padrão, procure na stdlib — `collections` e `functools` já resolveram.*
**Nível:** Intermediário
**Revisão sugerida:** 30 dias