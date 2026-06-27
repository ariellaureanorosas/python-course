# Listas

## Quando você vai usar isso?
Você precisa guardar nomes de alunos, notas de provas, ou qualquer coleção ordenada que vai crescer, encolher ou ter itens trocados. Lista é o container versátil do Python — serve pra tudo.

## Modelo mental
É um armário com gavetas numeradas: você pode colocar coisa nova, tirar, trocar de lugar, ou passar tudo a limpo. Cada gaveta é um índice numérico.

## Em uma linha
Coleção ordenada e mutável de itens — o curinga do Python.

## Na prática

### Caso simples — CRUD básico
```python
# ← Criação: colchetes, itens separados por vírgula
lista = [1, 2, 3]

# ← Create: adiciona no final
lista.append(4)          # ← lista vira [1, 2, 3, 4]

# ← Read: acessa pelo índice (começa em 0)
print(lista[0])          # ← 1

# ← Update: reatribui no índice
lista[0] = "novo"        # ← lista vira ["novo", 2, 3, 4]

# ← Delete: pop() remove e RETORNA o último
ultimo = lista.pop()     # ← ultimo = 4, lista = ["novo", 2, 3]

# ← pop(índice) remove e retorna específico
primeiro = lista.pop(0)  # ← primeiro = "novo", lista = [2, 3]
```

### Com variação — métodos complementares
```python
# ← insert: adiciona em posição específica (empurra os outros)
lista = [1, 3]
lista.insert(1, 2)       # ← insere 2 no índice 1: [1, 2, 3]

# ← extend: adiciona VÁRIOS itens no final
lista.extend([4, 5])     # ← [1, 2, 3, 4, 5] — append() só um item

# ← del: deleta por índice (sem retornar)
del lista[0]             # ← [2, 3, 4, 5]

# ← clear: limpa TUDO
lista.clear()            # ← []

# ← Concatenação com + cria NOVA lista (não modifica original)
a = [1, 2]
b = [3, 4]
c = a + b                # ← c = [1, 2, 3, 4], a e b intactos
```

### Em uso real — iteração + mutabilidade (CUIDADO!)
```python
# ← Duas formas de iterar uma lista:
lista = [10, 20, 30]

# ← Forma 1: direta — pega o VALOR
for item in lista:
    print(item)           # ← 10, 20, 30

# ← Forma 2: por índice — pega POSIÇÃO (precisa quando vai modificar)
for i in range(len(lista)):
    lista[i] = lista[i] * 2   # ← dobra cada valor no lugar

# ← CUIDADO com atribuição! Listas são mutáveis:
a = [1, 2, 3]
b = a                  # ← b NÃO é cópia — é o MESMO objeto
b.append(4)            # ← modifica a E b (mesma lista)
print(a)               # ← [1, 2, 3, 4] — a foi afetado!

# ← Cópia verdadeira:
c = a.copy()           # ← shallow copy: nova lista, itens independentes
c.append(5)            # ← só modifica c, a intacto
```

## O que NÃO fazer
```python
# ← Modificar lista enquanto itera (índices bagunçam)
lista = [1, 2, 3, 4]
for item in lista:
    if item % 2 == 0:
        lista.remove(item)   # ← pula itens, resultado errado!

# ← Assumir que cópia com = é independente
a = [1, 2]
b = a
b[0] = 99
print(a[0])            # ← 99! a foi alterado junto

# ← Índice inexistente
print(lista[10])       # ← IndexError: lista só tem 4 itens
```

## Por que Python funciona assim?
Listas são **arrays dinâmicos**: Python aloca um bloco de memória contíguo para os ponteiros dos objetos. Quando a lista enche, realoca um bloco maior (sobra de ~12,5% pra amortizar o custo). A atribuição `b = a` copia o ponteiro da lista — ambas variáveis apontam pro mesmo endereço. `copy()` cria um novo array com os mesmos ponteiros (shallow = rasa). Métodos como `append` e `pop` no final são O(1) — rápidos. `insert(0, x)` e `pop(0)` são O(n) — lentos porque precisam deslocar todos os outros itens.

## Conexões
- Você já usou esse padrão quando: criou uma variável pra guardar um valor
- Aparece também em: `json.load()` retorna listas/dicts, `csv.reader()` retorna listas de linhas
- Diferente de: tuplas (imutáveis → não podem ser alteradas depois de criadas); arrays do módulo `array` (só um tipo); `set` (não ordenado, sem duplicatas)

---

## Teste de recuperação — responda sem olhar para cima

1. Por que `b = a` não cria uma cópia da lista?
2. Escreva um trecho que dobra cada número de uma lista [1, 2, 3] no lugar.
3. Qual a diferença entre `append()`, `extend()` e concatenação com `+`?

---

**Frase-âncora:** "Coleção mutável e ordenada. = não copia, .copy() sim."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
