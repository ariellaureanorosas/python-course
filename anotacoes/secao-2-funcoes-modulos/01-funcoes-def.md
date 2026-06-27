# Funções (`def`)

## Quando você vai usar isso?
Quando você precisa executar o mesmo bloco de lógica várias vezes com dados diferentes. Tipo uma máquina de café: aperta o mesmo botão, mas coloca água e pó diferentes a cada xícara.

## Modelo mental
Funções são como receitas de bolo — você escreve os passos uma vez e executa com ingredientes variados quantas vezes quiser.

## Em uma linha
Bloco de código nomeado que recebe dados (parâmetros), processa e devolve um resultado.

## Na prática

### Caso simples
```python
def soma(a, b):
    # ← define a função com dois parâmetros; `a` e `b` são variáveis locais
    return a + b
    # ← `return` devolve o valor para quem chamou; sem ele a função retorna None

soma(3, 5)  # ← 8 — chama a função, executa o bloco, recebe o resultado
```

### Com variação
```python
def saudacao(nome, cumprimento="Olá"):
    # ← `nome` obrigatório; `cumprimento` opcional com valor padrão
    return f"{cumprimento}, {nome}!"

saudacao("João")              # ← usa "Olá" como padrão de cumprimento
saudacao("Ana", "Bom dia")    # ← substitui o padrão
saudacao(nome="Rui", cumprimento="Oi")  # ← argumentos nomeados: ordem não importa
```

### Em uso real
```python
def processa_pedido(itens, desconto=0):
    # ← função que centraliza uma regra de negócio real
    total = sum(item["preco"] * item["qtd"] for item in itens)
    total -= total * desconto / 100
    return round(total, 2)

carrinho = [{"preco": 10, "qtd": 2}, {"preco": 5, "qtd": 1}]
print(processa_pedido(carrinho, 10))  # ← imprime 22.5 (10% de desconto)
```

## O que NÃO fazer
```python
total = 0
def soma(a, b):
    total = a + b  # ← CUIDADO: cria `total` LOCAL, não altera a de fora
    return total
```
Sem `return` a função retorna `None`. Para modificar variável externa, use `global` (frágil) ou melhor: retorne o valor e atribua fora.

## Por que Python funciona assim?
Toda função em Python é um objeto de primeira classe — existe na memória como qualquer valor (`int`, `str`). Ao executar `def`, Python cria um objeto função, associa ao nome, e compila o bloco interno. Parâmetros viram variáveis locais que recebem os argumentos no momento da chamada. `return` encerra a execução e entrega o valor; sem ele, Python insere `return None` implicitamente ao final.

## Conexões
- Você já usou esse padrão quando: chamou `len()`, `print()`, `sum()` — todas são funções
- Aparece também em: métodos de classe, lambdas (funções anônimas de uma linha), decoradores (função que modifica outra)
- Diferente de: métodos (função dentro de classe que recebe `self` automático), `lambda` (expressão, não declaração, sem `return` explícito)

---

## Teste de recuperação — responda sem olhar para cima

1. O que uma função retorna se você não escrever `return`?
2. Escreva uma função `media` que recebe uma lista de números e retorna a média aritmética.
3. Qual a diferença entre argumento posicional e argumento nomeado na chamada?

---

**Frase-âncora:** Funções empacotam lógica para reuso com diferentes entradas.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
