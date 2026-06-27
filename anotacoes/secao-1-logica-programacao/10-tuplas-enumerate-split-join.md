# Tuplas, Enumerate, Split/Join

## Quando você vai usar isso?
Você tem coordenadas (x, y) que não devem mudar, quer percorrer uma lista sabendo o índice de cada item, ou precisa quebrar um CSV em campos e depois juntar palavras numa frase.

## Modelo mental
Tupla é uma caixa de ovos lacrada (não tira nem põe). Enumerate é um funcionário que entrega cada item com uma etiqueta numérica. Split/Join é um Lego: separa peças ou junta.

## Em uma linha
Tuplas fixam dados, enumerate dá índice automático, split quebra string em lista, join monta string da lista.

## Na prática

### Caso simples — tupla e desempacotamento
```python
# ← Tupla = igual lista, mas IMUTÁVEL (não muda depois de criada)
tupla = (1, 2, 3)

# ← Parênteses são opcionais na criação
tupla = 1, 2, 3            # ← "tuple packing" — Python entende

# ← Desempacotamento: joga cada valor numa variável
a, b, c = tupla            # ← a=1, b=2, c=3

# ← MESMO número de variáveis e elementos (senão dá erro)
# ← Muito usado pra retornar múltiplos valores de função

# ← tupla[0] = 0           # ← ERRO! TypeError: 'tuple' object does not support item assignment
```

### Com variação — enumerate()
```python
# ← enumerate() emparelha cada item com seu índice
nomes = ["Ana", "João", "Maria"]

# ← enumerate(iterável, start=0) — start diz onde começar a contar
for indice, nome in enumerate(nomes, start=1):
    print(indice, nome)    # ← 1 Ana, 2 João, 3 Maria

# ← Equivalente sem enumerate:
for i in range(len(nomes)):
    print(i + 1, nomes[i])
# ← enumerate poupa digitação e evita erros de índice
```

### Em uso real — split, join, strip
```python
# ← split(separador): string → lista (corta onde achar o separador)
frase = "banana,maçã,uva"
lista = frase.split(",")     # ← ["banana", "maçã", "uva"]

# ← split sem argumento separa por ESPAÇOS (remove vazios)
"a  b  c".split()            # ← ["a", "b", "c"]

# ← join(iterável): lista → string (COLOCA o separador ENTRE itens)
palavras = ["Python", "é", "legal"]

" ".join(palavras)           # ← "Python é legal"
"-".join(palavras)           # ← "Python-é-legal"

# ← strip() remove espaços (e tabs, newlines) das bordas
"   texto com espaço   ".strip()    # ← "texto com espaço"
"   texto".lstrip()                 # ← "texto" (só esquerda)
"texto   ".rstrip()                 # ← "texto" (só direita)

# ← Uso real combinado: limpar e quebrar uma linha de CSV
linha = "  nome, idade, cidade  \n"
campos = linha.strip().split(",")   # ← ["nome", " idade", "cidade"]
```

## O que NÃO fazer
```python
tupla = (1, 2)
tupla[0] = 10              # ← TypeError: não altera tupla

# ← Desempacotar com número errado de variáveis
a, b = (1, 2, 3)           # ← ValueError: too many values to unpack

# ← join funciona SÓ com lista de STRINGS
", ".join([1, 2, 3])       # ← TypeError: sequência item 0: str expected, int found

# ← split com separador errado
"01/01/2024".split("-")    # ← ["01/01/2024"] — não quebrou (é "/", não "-")
```

## Por que Python funciona assim?
Tuplas são **imutáveis por design** — depois de criadas, o objeto não pode ser alterado. Isso permite que tuplas sejam **hashable** (podem virar chave de dicionário), enquanto listas não. O desempacotamento usa a sintaxe de tupla implícita: `a, b = b, a` funciona porque Python empacota e desempacota na mesma linha. Enumerate é um **gerador** — produz os pares (índice, item) um por vez, sem criar uma lista intermediária. Split e join são inversos um do outro: split devora o separador, join coloca ele de volta. Split sem argumento trata qualquer quantidade de whitespace como um separador (diferente de `split(" ")`).

## Conexões
- Você já usou esse padrão quando: retornou dois valores numa função com `return x, y`
- Aparece também em: `dict.items()` devolve tuplas (chave, valor); `split()` em processamento de CSV, logs; `join()` em montagem de SQL, caminhos, URLs
- Diferente de: listas (mutáveis); `range()` (gera números, não índices); `replace()` (troca texto, não quebra em lista)

---

## Teste de recuperação — responda sem olhar para cima

1. Por que tuplas podem ser chave de dicionário e listas não?
2. Escreva um loop que imprime "0: maçã", "1: banana" usando enumerate().
3. O que `"x-x".split("-")` retorna e por que `"-".join(["a", "b"])` é diferente?

---

**Frase-âncora:** "Tupla trava, enumerate conta, split quebra, join cola."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
