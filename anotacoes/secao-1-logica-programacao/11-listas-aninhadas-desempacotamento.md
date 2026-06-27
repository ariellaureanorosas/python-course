# Listas Aninhadas e Desempacotamento

## Quando você vai usar isso?
Processar planilhas, tabuleiros, ou qualquer dado tabular onde cada linha tem sub-elementos. Também quando recebe uma lista e quer distribuir os valores em variáveis específicas sem acessar cada índice manualmente.

## Modelo mental
Uma estante com prateleiras — você abre a prateleira certa, depois pega o livro dentro dela. Desempacotar com `*` é como abrir uma caixa mista: "os dois primeiros vão para essas gavetas, o resto fica junto na gaveta de sobras".

## Em uma linha
Listas dentro de listas representam grids ou hierarquias; `*` coleta o excedente de um desempacotamento em uma única variável.

## Na prática

### Caso simples

```python
salas = [
    ["Ana", "Bruno"],          # ← sala 0: 2 alunos
    ["Carlos", "Diana", "Eva"],# ← sala 1: 3 alunos
    ["Fabio"],                  # ← sala 2: 1 aluno
]
print(salas[0][1])   # ← "Bruno" — acessa lista 0, elemento 1
print(salas[1][2])   # ← "Eva" — acessa lista 1, elemento 2

for sala in salas:          # ← percorre cada lista interna
    for aluno in sala:      # ← percorre alunos da lista atual
        print(aluno)        # ← Ana, Bruno, Carlos, Diana, Eva, Fabio
```

### Com variação

```python
# ← * captura o "resto" em uma nova lista
primeiro, segundo, *resto = [1, 2, 3, 4, 5]
# ← primeiro = 1, segundo = 2, resto = [3, 4, 5]

# ← _ ignora posições que você não quer nomear
_, nome, *_ = ["Sr.", "João", "Silva", "Jr."]
# ← nome = "João"; _ descarta "Sr."; *_ descarta ["Silva", "Jr."]

# ← * também espalha iteráveis em chamadas de função
print(*[1, 2, 3])   # ← 1 2 3 (equivale a print(1, 2, 3))
print(*"ABC")       # ← A B C (desempacota cada caractere)
```

### Em uso real

```python
# ← Processar planilha: primeira coluna = nome, restante = notas
alunos = [
    ["Ana", 8, 7, 9],
    ["Bruno", 6, 5, 7],
    ["Carlos", 10, 9, 8],
]
for linha in alunos:
    nome, *notas = linha     # ← desempacota nome + lista de notas
    media = sum(notas) / len(notas)
    print(f"{nome}: {media:.1f}")  # ← Ana: 8.0 | Bruno: 6.0 | Carlos: 9.0

# ← Transpor matriz com zip + desempacotamento
matriz = [[1, 2], [3, 4], [5, 6]]
transposta = list(zip(*matriz))  # ← [(1, 3, 5), (2, 4, 6)]
```

## O que NÃO fazer

```python
# ← ERRADO: esquecer que índice começa em 0
salas = [["Ana", "João"], ["Maria", "Pedro"]]
print(salas[1][0])  # ← "Maria", e não "João" (seria salas[0][1])

# ← ERRADO: número errado de valores no desempacotamento
a, b, c = [1, 2]    # ← ValueError: not enough values to unpack
a, b = [1, 2, 3]    # ← ValueError: too many values to unpack
# ← Corrija com *:  a, b, *resto = [1, 2, 3]

# ← ERRADO: confundir * (desempacotar) com * (multiplicar)
# Na atribuição:  *valores = [1, 2, 3]   ← SyntaxError!
# ← * só funciona do lado esquerdo COM outras variáveis
```

## Por que Python funciona assim?
`lista[i][j]` executa dois `__getitem__` em cadeia: primeiro `lista.__getitem__(i)` retorna a sublista, depois `.__getitem__(j)` no resultado. O `*` no desempacotamento usa o protocolo de iteração (`__iter__`): as variáveis simples consomem itens um a um pela esquerda, e a variável com `*` engole todo o restante em uma nova lista (não é uma referência, é cópia dos elementos).

## Conexões
- Você já usou esse padrão quando: percorreu caracteres de uma string com `for letra in palavra`
- Aparece também em: `*args` em funções, `zip(*matriz)` para transpor, `csv.reader` que retorna listas por linha
- Diferente de: fatiamento `[start:stop]` — fatias têm tamanho fixo, `*` se adapta ao que sobra

---

## Teste de recuperação — responda sem olhar para cima

1. Por que `listas[1][0]` acessa o primeiro elemento da segunda lista — qual a ordem de avaliação?
2. Dada `dados = [10, 20, 30, 40, 50]`, escreva o código que coloca 10 em `a`, 50 em `b`, e o restante em `c`.
3. Qual a diferença prática entre `*resto` no desempacotamento e `resto = lista[1:-1]`?

---

**Frase-âncora:** "Matriz de dados e distribuição elástica de valores entre variáveis."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
