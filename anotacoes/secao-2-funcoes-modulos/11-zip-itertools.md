# zip e itertools

## Quando você vai usar isso?
Você tem duas listas — nomes e idades — e precisa percorrê-las lado a lado. Ou quer gerar todas as combinações possíveis de times de 2 jogadores a partir de um elenco. Essas ferramentas unem, combinam e agrupam iteráveis sem escrever loops aninhados.

## Modelo mental
Imagine um zíper: os dentes de um lado se encaixam nos dentes do outro na mesma posição. `itertools` é como uma caixa de ferramentas de encaixes (combinações, permutações, produtos cartesianos) que você monta sem pensar em índice.

## Em uma linha
Combine dois ou mais iteráveis em pares (ou tuplas) elemento por elemento, e gere combinações/permutações lazy.

## Na prática

### Caso simples

```python
nomes = ["Ana", "João", "Maria"]
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):           # ← percorre ambos ao mesmo tempo
    print(f"{nome} tem {idade} anos")             # ← "Ana tem 25 anos", "João tem 30 anos"

list(zip(nomes, idades))                          # ← [("Ana", 25), ("João", 30), ("Maria", 22)]
```

### Com variação

```python
from itertools import zip_longest, count

a = [1, 2, 3]
b = [1, 2]

list(zip_longest(a, b, fillvalue=0))             # ← preenche o que falta com 0
# [(1, 1), (2, 2), (3, 0)]

for i in count(start=0, step=2):                 # ← contagem infinita: 0, 2, 4, 6...
    if i > 10:
        break
    print(i)                                     # ← 0, 2, 4, 6, 8, 10
```

### Em uso real

```python
from itertools import groupby

alunos = [("A", 8), ("B", 7), ("A", 9), ("B", 6)]
alunos.sort(key=lambda a: a[0])                  # ← groupby exige dados ordenados

for turma, grupo in groupby(alunos, key=lambda a: a[0]):  # ← agrupa pela turma
    print(turma, list(grupo))                    # ← A [(A,8),(A,9)]  B [(B,7),(B,6)]

from itertools import combinations, permutations, product

list(combinations([1, 2, 3], 2))                 # ← ordem não importa: (1,2)(1,3)(2,3)
list(permutations([1, 2, 3], 2))                 # ← ordem importa: 6 pares
list(product([1, 2], [3, 4]))                    # ← produto cartesiano: 4 pares
```

## O que NÃO fazer

```python
alunos = [("A", 8), ("B", 7), ("A", 9), ("B", 6)]
for turma, grupo in groupby(alunos, key=lambda a: a[0]):  # ← ERRO: não ordenou antes
    print(turma, list(grupo))
# Resultado: A [(A,8)], B [(B,7)], A [(A,9)], B [(B,6)]
# ← groupby só agrupa elementos CONSECUTIVOS com mesma chave. Sem sort, dados intercalados viram grupos separados.
```

## Por que Python funciona assim?
`zip` e `itertools` retornam **iteradores** (não listas). Cada elemento é produzido sob demanda — você não carrega tudo na memória. `zip` para no menor iterável (como um zíper que acaba quando o lado mais curto termina). `zip_longest` preenche com `fillvalue` para não perder dados. `groupby` é preguiçoso: só olha o elemento atual e o próximo, por isso exige ordenação prévia.

## Conexões
- Você já usou esse padrão quando: percorreu duas listas com `for i in range(len(...))` — `zip` elimina a necessidade de índices
- Aparece também em: `enumerate` é um primo próximo (índice + valor), `map` também itera em paralelo
- Diferente de: `zip` é diferente de `zip_longest` — o primeiro trunca, o segundo preenche

---

## Teste de recuperação — responda sem olhar para cima

1. Por que `groupby` exige que os dados estejam ordenados antes de usar?
2. Escreva um código que dado `[1,2,3]` e `["a","b","c"]` produza `[(1,"a"),(2,"b"),(3,"c")]`.
3. Qual a diferença prática entre `zip` e `zip_longest`?

---

**Frase-âncora:** "Junta iteráveis lado a lado sem loops manuais."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
