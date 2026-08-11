# Cópia Rasa (shallow) e Cópia Profunda (deep)

## Quando você vai usar isso?
Quando você precisa duplicar uma estrutura para transformar SEM estragar a original — a aula 102 faz exatamente isso: aumentar preços e ordenar produtos com `copy.deepcopy(produtos)` para que o catálogo original fique intocado. É o dia a dia de quem trabalha com listas/dicts aninhados: configs, catálogos, carrinhos de compra.

## Modelo mental
Cópia rasa é copiar o mapa da cidade: os endereços são iguais — se alguém reformar uma casa, os dois mapas mudam. Cópia profunda é copiar a cidade inteira em outra: reformar uma não afeta a outra.

## Em uma linha
`copy.copy` copia o topo (itens aninhados continuam compartilhados); `copy.deepcopy` recria TUDO em cascata (nada é compartilhado).

## Na prática

### Caso simples — onde as cópias se separam

```python
import copy

original = [[1, 2], [3, 4]]

rasa = copy.copy(original)      # ← topo novo, listas de dentro SHARED
profunda = copy.deepcopy(original)

rasa[0].append(99)              # ← mexe na lista interna compartilhada
profunda[0].append(88)          # ← mexe na lista interna nova

original          # ← [[1, 2, 99], [3, 4]]  ← a rasa MUDOU a original!
# (o 88 da profunda não aparece: listas internas eram cópias novas)
```

### Com variação — lista.copy() é rasa; dict() também

```python
lista = [[1], [2]]
copia = lista.copy()            # ← shalow: o topo é novo...
copia[0].append(9)
lista                            # ← [[1, 9], [2]] — o 9 vazou!

dados = {"cat": {"nome": "miau"}}
d = dict(dados)                 # ← shalow também
d["cat"]["nome"] = "rex"
dados                            # ← {'cat': {'nome': 'rex'}} — vazou!
```

### Em uso real — a aula 102: transformar sem tocar na original

```python
import copy

produtos = [{"nome": "caneca", "preco": 10.00}]

novos = [
    {**produto, "preco": round(produto["preco"] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
]

print(produtos)   # ← preco continua 10.00 — catálogo original intocado
print(novos)      # ← [{nome: caneca, preco: 11.0}] — cópia aumentada
```

## O que NÃO fazer

```python
novos = produtos                     # ← NÃO é cópia: é ALIAS (nota 26, Seção 1)
novos = produtos.copy()              # ← rasa: resolve só se não houver aninhados
novos = [p.copy() for p in produtos] # ← "rasa manual": falha se o dict aninhar dict

# → quando a estrutura tem ANINHAMENTO, deepcopy é a resposta direta:
novos = copy.deepcopy(produtos)
```

## Por que Python funciona assim?
`copy.copy` percorre a estrutura UM nível: cria um container novo e copia as REFERÊNCIAS dos itens — itens mutáveis continuam apontando para os mesmos objetos. `copy.deepcopy` mantém um memo (mapa de objetos já copiados) e recria cada objeto em profundidade, inclusive os aninhados; ele também trata referências CÍCLICAS (lista contendo ela mesma). O custo é tempo e memória — copiar 1 milhão de itens aninhados é caro, e por isso a cópia rasa é o padrão na maioria das situações; recorra à profunda quando houver aninhamento.

## Conexões
- Você já usou esse padrão quando: `lista.copy()` e `dict()` nas seções anteriores eram cópias rasas "por acidente" — seguras porque os itens eram imutáveis (strings/números)
- Aparece também em: clonagem de estados em jogos, snapshots de configuração, testes (isolar a estrutura do mocks)
- Diferente de: `.copy()`/`list[:]` (rasas), `copy.copy` (rasa explícita), `copy.deepcopy` (profunda), e do alias `=` (que não copia nada)

---

## Teste de recuperação — responda sem olhar para cima

1. Diferença entre `copy.copy` e `copy.deepcopy`?
2. Por que `.copy()` em `[[1], [2]]` não protege as listas internas?
3. Na aula 102, por que deepcopy era necessário para os produtos?

---

**Frase-âncora:** "Rasa copia o mapa; profunda copia a cidade."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14