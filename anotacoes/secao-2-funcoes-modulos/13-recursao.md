# Funções Recursivas

## Quando você vai usar isso?
Você precisa calcular o fatorial de 5, ou navegar por uma estrutura de pastas com profundidade desconhecida, ou percorrer uma árvore binária. A solução natural é a função chamar a si mesma com um problema menor — até atingir um caso tão simples que a resposta é óbvia.

## Modelo mental
Boneca russa (matrioska): para abrir a boneca maior, você abre a menor dentro dela, que abre outra menor, até a última que não abre mais. O caso base é a boneca final. Cada chamada resolve uma camada e volta com a resposta.

## Em uma linha
Função que chama a si mesma com um problema menor até atingir um caso base que interrompe a recursão.

## Na prática

### Caso simples

```python
def fatorial(n):
    if n <= 1:                                     # ← caso base: para aqui
        return 1
    return n * fatorial(n - 1)                      # ← caso recursivo: reduz o problema

fatorial(5)                                         # ← 5 * 4 * 3 * 2 * 1 = 120
```

### Com variação

```python
def contar(start, end):
    if start > end:                                # ← caso base: já passou do fim
        return
    print(start)                                   # ← ação: imprime o atual
    contar(start + 1, end)                         # ← recursão: próximo número

contar(1, 5)                                       # ← 1, 2, 3, 4, 5 (um por linha)
```

### Em uso real

```python
import os

def listar_arquivos(caminho):
    for item in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, item)
        if os.path.isdir(caminho_completo):
            listar_arquivos(caminho_completo)       # ← pasta: chama de novo
        else:
            print(caminho_completo)                 # ← arquivo: exibe caminho

listar_arquivos(".")

import sys
sys.getrecursionlimit()                             # ← 1000 (padrão)
sys.setrecursionlimit(2000)                         # ← aumenta se necessário
```

## O que NÃO fazer

```python
def fatorial(n):
    return n * fatorial(n - 1)                      # ← ERRO: sem caso base!

# RecursionError: maximum recursion depth exceeded
# ← Sem caso base, a função chama a si mesma para sempre até estourar a pilha.

def infinito():
    return infinito()                               # ← caso recursivo sem progressão
# ← Mesmo erro: nunca converge, nunca reduz o problema.
```

## Por que Python funciona assim?
Python tem um **limite de recursão** (padrão 1000) porque cada chamada de função empilha um frame na memória. Diferente de linguagens funcionais (Haskell, Elixir), Python **não otimiza tail call recursion** — mesmo que a recursão esteja no final, a pilha cresce. Por isso, para loops profundos (>1000), prefira iteração (`for`, `while`). Recursão é ideal para problemas inerentemente recursivos (árvores, grafos, divisão-e-conquista) com profundidade controlada.

## Conexões
- Você já usou esse padrão quando: chamou uma função dentro dela mesma sem saber
- Aparece também em: algoritmos de busca (DFS em árvores), JSON aninhado, processamento de expressões matemáticas
- Diferente de: iteração (`for`/`while`) não empilha frames — prefira para loops profundos

---

## Teste de recuperação — responda sem olhar para cima

1. Quais são os dois componentes obrigatórios de toda função recursiva?
2. Escreva uma função recursiva `soma(n)` que retorna a soma de 1 até n.
3. Por que Python lança `RecursionError` e não otimiza recursão em cauda (tail call)?

---

**Frase-âncora:** "Função que se resolve chamando a si mesma até o caso base."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
