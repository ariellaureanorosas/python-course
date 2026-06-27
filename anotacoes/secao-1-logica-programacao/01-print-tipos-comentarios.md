# Print, Tipos e Comentários

## Quando você vai usar isso?
Você termina de escrever uma função e precisa saber se ela retorna o que deveria — print é seu debugger improvisado. Mais tarde, alguém (pode ser você) vai ler aquele código e um comentário bem colocado salva horas. Os tipos primitivos são o alfabeto do Python: sem eles nada se constrói.

## Modelo mental
Print é o alto-falante do código — manda uma mensagem e ela ecoa no terminal. Tipo é a carteira de identidade do valor: str é texto, int é número redondo, float é número quebrado, bool é interruptor.

## Em uma linha
Print exibe no terminal, comentários documentam o código, tipos primitivos classificam todo valor que você manipula.

## Na prática

### Caso simples
```python
print("Olá, mundo!")         # ← exibe a string no terminal — seu primeiro contato com output
print(12, 34, sep="-")       # ← sep troca o espaço entre argumentos por "-" → "12-34"
print("Linha 1", end="\n\n") # ← end substitui a quebra de linha padrão por duas linhas vazias

# ← Comentário de linha única: o interpretador ignora tudo depois do #
"""
Docstring / comentário multilinha:
delimitada por três aspas (simples ou duplas).
Usada para documentar funções, classes e módulos.
"""
```

### Com variação
```python
# Os quatro tipos primitivos — reconheça cada um pelo formato do valor
type("Texto")   # ← <class 'str'>   — string: qualquer texto entre aspas
type(42)        # ← <class 'int'>   — integer: número inteiro, sem casa decimal
type(3.14)      # ← <class 'float'> — ponto flutuante: número decimal com ponto
type(True)      # ← <class 'bool'>  — booleano: True ou False, sempre maiúsculo

# Raw string: ignora caracteres de escape, exibe o texto literal
print(r"Ariel \"Rosas\"")  # ← saída: Ariel \"Rosas\" — as barras aparecem, não escapam
```

### Em uso real
```python
# Conversão de tipos (coerção/type casting) — transforma um tipo em outro
int("42")       # ← "42" (str) → 42 (int); a string precisa ter formato numérico válido
float("3.14")   # ← "3.14" (str) → 3.14 (float); mesma regra, aceita ponto decimal
str(42)         # ← 42 (int) → "42" (str); útil para concatenar número com texto
bool("")        # ← False — string vazia é o único valor string considerado Falsy
bool(" ")       # ← True — string com pelo menos um caractere (espaço incluso) é Truthy
```

## O que NÃO fazer
```python
# Tentar converter string não numérica para int — erro fatal
int("quarenta e dois")  # ← ValueError: invalid literal for int() with base 10: 'quarenta e dois'
# Sempre valide a entrada ou use try/except antes de converter
```

## Por que Python funciona assim?
Python usa tipagem dinâmica (tipo é inferido na atribuição) e forte (não converte automaticamente tipos incompatíveis). Isso significa que `"5" + 3` levanta erro de propósito — o Python prefere te avisar do que fazer algo silenciosamente errado. A raw string (`r"..."`) existe porque em caminhos de arquivo no Windows as barras invertidas seriam interpretadas como escape.

## Conexões
- Você já usou esse padrão quando: chamou `len("texto")` e recebeu um int de volta — você usou o resultado de um tipo sem declarar nada
- Aparece também em: funções como `sorted()` que devolvem listas, ou `str.join()` que exige strings — sempre lidando com tipos
- Diferente de: JavaScript (tipagem fraca) — `"5" + 3` retorna `"53"` sem erro, enquanto Python te protege com TypeError

---

## Teste de recuperação — responda sem olhar para cima

1. Quais são os 4 tipos primitivos do Python e em que situações você usa cada um?
2. Escreva um código que lê dois números do teclado (como strings) e exibe a soma deles convertendo para inteiro.
3. Por que `bool(" ")` retorna True mas `bool("")` retorna False?

---

**Frase-âncora:** "Print exibe, comentário documenta, tipo classifica — o mínimo que você precisa saber."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
