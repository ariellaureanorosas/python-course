# Generators

## Quando você vai usar isso?
Precisa processar 10 milhões de registros de um arquivo CSV mas não quer travar o computador tentando alocar uma lista gigante na memória. Ou quer um fluxo de dados que produza valores sob demanda (lazy evaluation).

## Modelo mental
Generator é uma esteira que só liga quando alguém pega a peça. Diferente de uma lista (prateleira com tudo empilhado), o generator produz cada item na hora que você pede — e esquece depois.

## Em uma linha
Generator produz valores um de cada vez sob demanda sem armazenar tudo na memória — lazy evaluation.

## Na prática

### Caso simples
```python
# ← Generator Expression: igual list comprehension mas com parênteses
gen = (n**2 for n in range(1000000))  # ← ( ) em vez de [ ]

# ← Só ocupa ~200 bytes independente do range
soma = sum(gen)  # ← processa um por um, nunca aloca a lista inteira
```

### Com variação
```python
# ← Generator Function com yield — pausa e retoma
def contador(maximo):
    n = 0
    while n < maximo:
        yield n       # ← pausa aqui, retorna n, depois continua
        n += 1

for valor in contador(5):
    print(valor)      # ← 0, 1, 2, 3, 4 — um de cada vez

# ← yield from — delega para outro generator
def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()  # ← terceiriza a produção para gen1
    yield 3

list(gen2())  # ← [1, 2, 3]
```

### Em uso real
```python
# ← Processar linhas de arquivo gigante sem carregar tudo
def linhas_arquivo(caminho):
    with open(caminho) as f:
        for linha in f:       # ← f já é iterável linha por linha
            yield linha.strip()

# ← Consome uma linha por vez — memória constante
for linha in linhas_arquivo("dados.csv"):
    if "erro" in linha:
        print(linha)

# ← Comparação de memória
import sys
lista = [n for n in range(1000000)]  # ← ~8 MB — aloca tudo
gen = (n for n in range(1000000))    # ← ~200 bytes — não aloca nada
```

## O que NÃO fazer
```python
# ← ERRADO: converter generator em lista sem necessidade — perde a vantagem
gen = (x**2 for x in range(1000000))
lista = list(gen)       # ← acabou com a memória, matou o propósito

# ← ERRADO: reutilizar generator — ele se esgota
gen = (x for x in range(3))
list(gen)  # ← [0, 1, 2]
list(gen)  # ← [] — vazio, generator já consumido

# ← O erro real: generator é iterável de uso único, não uma coleção
```

## Por que Python funciona assim?
Funções com `yield` viram generators porque Python transforma o frame da função num objeto iterator. Quando encontra `yield`, congela o estado local (variáveis, ponteiro de execução) e retorna o valor. Na próxima chamada de `next()`, restaura o frame e continua de onde parou. `yield from` é syntactic sugar que expande `for item in subgen: yield item` — otimizado em C. A economia de memória vem de não alocar o iterável inteiro: cada item é produzido, processado e descartado.

## Conexões
- Você já usou esse padrão quando: usou `range()` — que é um generator, não uma lista
- Aparece também em: `open()` retorna um iterator de linhas, `csv.reader` também é lazy
- Diferente de: List Comprehension `[x for x]` — aloca tudo na hora, eager

---

## Teste de recuperação — responda sem olhar para cima

1. O que significa "lazy evaluation" em generators?
2. Escreva uma generator function que produza números pares infinitos.
3. Qual a diferença de memória entre `sum([x for x in range(10**6)])` e `sum(x for x in range(10**6))`?

---

**Frase-âncora:** Generator produz sob demanda, não armazena — memória constante.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
