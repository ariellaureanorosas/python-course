# Lambda e Comprehensions (List, Dict, Set)

## Quando você vai usar isso?
Precisa criar uma função rápida de usar uma vez só (tipo um filtro no sort) e não quer poluir o código com `def`. Ou quer construir uma lista/dict/set numa linha só em vez de um loop `for` com `append`.

## Modelo mental
Lambda é um post-it que você escreve e joga fora — existe só na hora que precisa. Comprehension é uma esteira de fábrica: entra um iterável, cada item passa por uma transformação, e opcionalmente um fiscal (if) barra alguns.

## Em uma linha
Lambda cria funções anônimas de uma expressão; comprehensions constroem coleções a partir de iteráveis com filtro e transformação.

## Na prática

### Caso simples
```python
# ← Lambda: função anônima para usar na hora
soma = lambda a, b: a + b       # ← define sem nome, joga numa variável
soma(2, 3)                      # ← 5 — usa como função normal

# ← List Comprehension: [expr for item in iteravel if condicao]
pares = [n for n in range(20) if n % 2 == 0]  # ← [0,2,4,...18]
```

### Com variação
```python
# ← Lambda com sort — chave de ordenação
pessoas = [("Ana", 30), ("João", 25)]
pessoas.sort(key=lambda p: p[1])  # ← key recebe função que extrai idade

# ← Dict Comprehension — transforma chaves e valores
quadrados = {n: n**2 for n in range(5)}  # ← {0:0, 1:1, 2:4, 3:9, 4:16}

# ← Set Comprehension — elimina duplicatas automaticamente
unicos = {n for n in [1, 1, 2, 2, 3]}   # ← {1, 2, 3}
```

### Em uso real
```python
# ← Filtrar e transformar dados de um dicionário com isinstance
dados = {"nome": "Ana", "idade": 30, "peso": 65.5, "ativo": True}
strings = {k: v for k, v in dados.items() if isinstance(v, str)}
# ← {'nome': 'Ana'} — só pares onde valor é string

# ← Comprehension aninhada = produto cartesiano
coordenadas = [(x, y) for x in range(3) for y in range(3)]
# ← [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
```

## O que NÃO fazer
```python
# ← ERRADO: usar lambda quando uma função normal é mais clara
# ← Lambdas são limitados a UMA expressão — não use com if/else complexos
calc = lambda x: x**2 if x > 0 else (x**3 if x < 0 else 0)  # ← ilegível

# ← ERRADO: comprehension gigante que ninguém entende
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row if n % 2 == 0]  # ← ok, 3+ vira pesadelo

# ← O erro real: comprehension com 3+ níveis de aninhamento quebra legibilidade
```

## Por que Python funciona assim?
Lambda existe porque Python precisa de funções de primeira classe (passar função como argumento), mas sem a sintaxe verbosa do `def` para usos descartáveis. Comprehensions vieram de Haskell — Python adotou a sintaxe `[expr for item in iterable if condition]` porque é mais rápida que `for`+`append` (executa em C por baixo dos panos). `isinstance()` suporta tupla de tipos como segundo argumento para evitar cadeias de `or`.

## Conexões
- Você já usou esse padrão quando: usou `map()` ou `filter()` — mas prefira comprehension, é mais pythonica
- Aparece também em: `sorted()`, `min()`, `max()` — todos aceitam `key` ou função como argumento
- Diferente de: Generator Expression `(x for x in ...)` — lazy, não aloca tudo na memória

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `lambda` e uma função definida com `def`?
2. Escreva uma list comprehension que retorna os números ímpares de 0 a 20 multiplicados por 3.
3. O que muda entre `[x for x in range(5)]`, `{x for x in range(5)}` e `{x: x for x in range(5)}`?

---

**Frase-âncora:** Lambda: função descartável. Comprehension: coleção construída na hora com filtro.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
