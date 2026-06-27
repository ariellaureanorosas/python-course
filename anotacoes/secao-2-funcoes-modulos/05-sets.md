# Sets (Conjuntos)

## Quando você vai usar isso?
Quando precisa garantir que não tem duplicatas ou fazer operações de conjunto — tipo saber quem está na festa A e na festa B sem contar ninguém duas vezes, ou achar quem está em ambas.

## Modelo mental
Uma sacola que joga fora itens repetidos automaticamente. Você não sabe em que posição cada item está, só sabe se ele está ou não dentro.

## Em uma linha
Coleção mutável, não ordenada, sem índices e sem elementos duplicados, com suporte a operações matemáticas de conjunto.

## Na prática

### Caso simples
```python
numeros = [1, 2, 2, 3, 3, 3]
unicos = set(numeros)
# ← filtra duplicatas automaticamente: {1, 2, 3}
vazio = set()
# ← {} criaria dict vazio, não set!
```

### Com variação
```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b  # ← união: tudo em a OU em b → {1, 2, 3, 4}
a & b  # ← interseção: só o que está em AMBOS → {2, 3}
a - b  # ← diferença: só em a e NÃO em b → {1}
a ^ b  # ← diferença simétrica: em um ou outro, não ambos → {1, 4}
```

### Em uso real
```python
def primeiro_duplicado(lista):
    vistos = set()
    # ← conjunto vazio que cresce conforme iteramos
    for item in lista:
        # ← `item in set` é O(1) — muito mais rápido que lista O(n)
        if item in vistos:
            return item
            # ← primeiro item que já apareceu antes
        vistos.add(item)
        # ← insere no conjunto (ignora se já existir)
    return None  # ← nenhum duplicado

primeiro_duplicado([3, 5, 1, 3, 7])  # ← 3
```

## O que NÃO fazer
```python
s = {1, 2, [3, 4]}
# ← ERRO: listas são mutáveis → não hashable → não podem estar num set
s = {1, 2, (3, 4)}
# ← OK: tupla imutável → hashable
```
Elementos de set precisam ser hashable (imutáveis) pelo mesmo motivo das chaves de dict — o hash precisa ser fixo.

## Por que Python funciona assim?
Sets usam a mesma tabela hash dos dicionários, mas armazenam apenas as chaves (sem valores). A unicidade é consequência do hash: objetos iguais produzem o mesmo hash, então o set simplesmente não insere o segundo. Operações como `| & - ^` percorrem os hashes e são otimizadas para O(min(n, m)) no caso médio.

## Conexões
- Você já usou esse padrão quando: fez `list(set(minha_lista))` para limpar duplicatas
- Aparece também em: testes de permissão (`{"admin"} & user.permissoes`), consultas SQL (tabelas são conjuntos), `collections.Counter` internamente
- Diferente de: listas (ordenadas, indexadas, permitem duplicatas), tuplas (imutáveis, ordenadas, permitem duplicatas), `frozenset` (versão imutável do set)

---

## Teste de recuperação — responda sem olhar para cima

1. Por que `{}` não cria um set vazio? Como criar um set vazio corretamente?
2. Escreva uma função que recebe duas listas e retorna os elementos em comum sem duplicatas.
3. Qual operador de set retorna elementos que estão em um conjunto mas não no outro?

---

**Frase-âncora:** Coleção sem duplicatas com operações de união, interseção e diferença.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
