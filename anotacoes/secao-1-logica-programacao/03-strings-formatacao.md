# Strings e Formatação

## Quando você vai usar isso?
Você precisa exibir um relatório com nome, preço e total formatado — números com duas casas decimais, alinhamento bonito, zeros à esquerda. Formatação de string é o que separa output amador de output profissional.

## Modelo mental
f-string é uma plantilla de documento: você deixa buracos `{ }` e o Python preenche com os valores na hora. Cada método de formatação (f, .format(), %) é uma geração diferente da mesma ferramenta.

## Em uma linha
f-strings interpolam variáveis dentro de texto com suporte a formatação de números, alinhamento e representação.

## Na prática

### Caso simples
```python
# f-strings (Python 3.6+) — a forma mais direta e preferida de formatar
nome = "João"
print(f"Olá, {nome}!")              # ← {nome} é substituído pelo valor da variável na hora
print(f"Preço: R${preco:.2f}")      # ← :.2f formata o float com 2 casas decimais
print(f"{numero:0=+10,.1f}")        # ← 0=+10,.1f: zero à esquerda, sinal, 10 dígitos, vírgula milhar, 1 decimal
```

### Com variação
```python
# str.format() — método mais verboso, útil quando o template vem de uma string externa
print("a={} b={}".format(1, 2))               # ← {} vazios preenchem na ordem dos argumentos
print("a={nome1} b={nome2}".format(nome1="João", nome2="Maria"))  # ← argumentos nomeados são mais claros

# Interpolação com % — estilo antigo herdado da linguagem C, ainda aparece em código legado
print("%s tem %d anos e R$%.2f" % (nome, idade, preco))  # ← %s=string, %d=int, %.2f=float 2 casas
print("%08X" % (15123,))      # ← 08X: 8 dígitos com zero à esquerda, hexadecimal maiúsculo → 003B13
```

### Em uso real
```python
# Alinhamento e representação — controle fino de como o texto aparece na tela
f"{nome:<10}"   # ← alinhamento à esquerda em campo de 10 caracteres (completa com espaços)
f"{nome:>10}"   # ← alinhamento à direita em campo de 10 caracteres
f"{nome:^10}"   # ← centralizado em campo de 10 caracteres
f"{nome!r}"     # ← representação: retorna a versão "crua" com aspas (útil pra debug)
f"{nome!s}"     # ← string: o padrão, retorna str() do valor
f"{nome!a}"     # ← ASCII: escapa caracteres não-ASCII pra \x, \u, \U
```

## O que NÃO fazer
```python
# Misturar métodos de formatação no mesmo código — confunde e dificulta manutenção
nome = "João"
print("Olá, %s!" % nome + f" {idade}")  # ← funciona, mas é feio e inconsistente
# Prefira f-strings sempre (Python 3.6+) — é o padrão moderno, mais legível e rápido
```

## Por que Python funciona assim?
Python herdou o `%` do C (por isso a sintaxe estranha). O `.format()` veio no Python 2.6 pra resolver limitações do `%`. As f-strings (3.6+) são a evolução final: mais rápidas, mais legíveis, e resolvem tudo que os anteriores faziam. A `!r`/`!s`/`!a` usam os métodos `__repr__`, `__str__` e `__ascii__` dos objetos — cada classe pode definir como quer ser representada.

## Conexões
- Você já usou esse padrão quando: escreveu `print(f"Resultado: {valor}")` na seção anterior — f-string é o padrão moderno
- Aparece também em: logging — `logging.info(f"User {user} logged in")`; templates web (Jinja2 usa sintaxe similar)
- Diferente de: concatenação com `+` — `"a" + str(1) + "b"` funciona mas é menos legível que `f"a{1}b"`

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `f"{nome}"`, `"{}".format(nome)` e `"%s" % nome`?
2. Formate o número 1234.5678 como moeda brasileira: R$ 1.234,57 usando f-string.
3. Por que f-strings são preferíveis a `.format()` e `%` em código moderno?

---

**Frase-âncora:** "f-string interpola, .format() organiza, % é relíquia — use o mais novo que puder."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
