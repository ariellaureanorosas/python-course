# Pitfall: Parâmetro Padrão Mutável

## Quando você vai usar isso?
Sempre que escrever `def funcao(x, lista=[])` — ou dict, set ou qualquer mutável — e a função for chamada mais de uma vez. O bug não aparece na primeira chamada: ele se acumula silenciosamente entre chamadas. É o erro número 1 de quem migra de outra linguagem para Python.

## Modelo mental
O valor padrão é um objeto ÚNICO criado na hora em que a função é DEFINIDA — não na hora em que ela é chamada. Uma lista padrão é uma caixa que vai sendo repartida entre TODAS as chamadas que não passam a lista: cada chamada enfia mais um item na mesma caixa.

## Em uma linha
Nunca use coleção mutável como padrão; use `None` como sentinela e crie a coleção dentro da função.

## Na prática

### Caso simples — o bug

```python
def adicionar_cliente(nome, lista=[]):
    lista.append(nome)
    return lista

adicionar_cliente("Luiz")    # ← ['Luiz']  — ok na 1ª chamada
adicionar_cliente("Ana")     # ← ['Luiz', 'Ana']  ← o "Luiz" CONTINUA lá!
```

### Com variação — a correção (aula 124)

```python
def adicionar_cliente(nome, lista=None):
    if lista is None:          # ← sentinela: "não me passaram lista"
        lista = []             # ← cria uma NOVA a cada chamada
    lista.append(nome)
    return lista

cliente1 = adicionar_cliente("Luiz")     # ← ['Luiz']
cliente2 = adicionar_cliente("Helena")   # ← ['Helena']  — caixas separadas
adicionar_cliente("Ariel", cliente1)     # ← ['Luiz', 'Ariel'] — reuso explícito
```

### Em uso real — por que o padrão não é reavaliado

```python
import time

def registrar(tarefa, historico=[]):
    historico.append((tarefa, time.time()))
    return historico

# Python cria [ ] UMA única vez, na definição da função, e o mantém
# em função.__defaults__:
registrar.__defaults__   # ← ([]) — a MESMA lista depois de varias chamadas!
```

## O que NÃO fazer

```python
def f(x, d={}):      # ← dict mutável como padrão: MESMO bug
    d[x] = len(d)
    return d

def g(x, s=set()):   # ← set idem
    s.add(x)
    return s

# A correção é igual para todos: None sentinela + criar dentro.
# Imutáveis (str, int, tuple, None) como padrão são 100% seguros —
# a tuple () é o único "vazio" seguro como padrão, mas é raro.
```

## Por que Python funciona assim?
Os padrões são avaliados UMA vez, no momento da definição (é a semântica de `def`: tudo no cabeçalho, inclusive os padrões, é executado ali). Como listas são mutáveis (nota 09 da Seção 1), qualquer append dentro da função altera o próprio objeto que ficou gravado em `__defaults__` — e a próxima chamada "herda" o estado. O `None` quebra o ciclo porque ele é imutável e único: a função precisa passar pelo `if lista is None` para criar uma lista NOVA por chamada.

## Conexões
- Você já usou esse padrão quando: closures com estado (nota 03) sofrem do mesmo problema se usarem mutável compartilhado
- Aparece também em: `datetime.datetime.now` como padrão (outro pitfall: congela o horário da definição), testes unitários que acumulam mocks
- Diferente de: parâmetros posicionais/nomeados comuns (nota 16) — o problema aqui é o VALOR padrão, não o mecanismo de passagem

---

## Teste de recuperação — responda sem olhar para cima

1. Explique POR QUE `def f(x, lista=[])` compartilha a lista entre chamadas.
2. Reescreva a função do jeito correto, sem tocar no comportamento esperado.
3. O que há de errado com `def f(x, d={})`? Vale para set também?

---

**Frase-âncora:** "Padrão mutável é avaliado uma vez: use None sentinela."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14