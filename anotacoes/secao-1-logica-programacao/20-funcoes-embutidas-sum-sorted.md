# Funções Embutidas sum() e sorted()

## Quando você vai usar isso?
Somou as notas de uma sala, os itens de um carrinho, os minutos de um trajeto — sum. Precisa exibir dados em ordem (alfabética, por tamanho, decrescente) SEM estragar a ordem original — sorted. São duas das funções embutidas mais usadas do Python, e aparecem nos gabaritos 15, 16 e 17.

## Modelo mental
`sum` é a calculadora de um iterável: soma todos os números e devolve um único valor. `sorted` é a arrumadeira cuidadosa: devolve uma cópia ordenada e devolve a lista original exatamente como estava.

## Em uma linha
`sum(iteravel)` soma os números; `sorted(iteravel)` devolve uma LISTA NOVA em ordem — sem modificar a original.

## Na prática

### Caso simples — sum

```python
notas = [7.5, 8.0, 6.5, 9.0]
sum(notas)                # ← 31.0
sum(notas) / len(notas)   # ← 7.75 — média clássica
sum(range(1, 11))         # ← 55 — soma inteiros de 1 a 10
```

### Com variação — sorted

```python
nomes = ["Zeca", "ana", "Caio"]

sorted(nomes)                 # ← ['Caio', 'Zeca', 'ana'] — ordem ASCII (maiúsculas primeiro)
sorted(nomes, reverse=True)   # ← ['ana', 'Zeca', 'Caio'] — decrescente
sorted(nomes, key=len)        # ← ['ana', 'Zeca', 'Caio'] — ordena pelo tamanho
print(nomes)                  # ← ['Zeca', 'ana', 'Caio'] — ORIGINAL intacta
```

### Em uso real — ranking sem destruir a lista

```python
pontuacoes = [340, 120, 890, 450]

melhores = sorted(pontuacoes, reverse=True)
print(melhores[:3])           # ← top 3: [890, 450, 340]
print(pontuacoes)             # ← original preservada para o histórico
```

## O que NÃO fazer

```python
numeros = [3, 1, 2]
numeros.sort()        # ← funciona, mas MODIFICA a lista no lugar
# Use sorted() quando precisar manter a ordem original.

sum([1, "2"])         # ← TypeError: soma exige números

sum([1, 2], 10)       # ← 13 — o 2º argumento é o valor inicial (start=); raramente necessário
```

## Por que Python funciona assim?
`sum` reduz um iterável somando elemento a elemento a partir de um acumulador inicial (padrão 0, configurável com `start=`). `sorted` usa o algoritmo TimSort (estável — mantém a ordem relativa de empates) e aceita `key=` para extrair o critério de ordenação e `reverse=True`. A alternativa `lista.sort()` ordena no lugar e devolve None — útil para economizar memória, mas destrói a ordem original. As comparações padrão são lexicográficas por código ASCII: "A" (65) < "a" (97) — por isso "Zeca" aparece antes de "ana".

## Conexões
- Você já usou esse padrão quando: os gabaritos 15/16/17 somam matrizes com sum e ordenam sorteados com sorted
- Aparece também em: relatórios ordenados, rankings de jogo, top N, estatísticas
- Diferente de: `.sort()` (mutável, só de lista), `reduce` (nota da Seção 2) e `sorted` com `key=lambda` (Seção 2)

---

## Teste de recuperação — responda sem olhar para cima

1. O que `sorted(nomes, reverse=True)` devolve? E como fica a lista original?
2. Como calcular a média de uma lista de notas usando sum e len?
3. Qual a diferença entre `sorted(lista)` e `lista.sort()`?

---

**Frase-âncora:** "sum soma tudo; sorted devolve cópia em ordem."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14