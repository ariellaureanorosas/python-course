# Métodos de String e Imutabilidade

## Quando você vai usar isso?
Formulários chegam em caixa alta misturada, com espaços sobrando ("  MARIA "). Antes de comparar ou salvar, você normaliza. Ou precisa: descobrir a posição de uma palavra (.find), contar quantas vezes algo aparece (.count), saber se um campo é numérico (.isdigit), padronizar um ID com zeros (.zfill). Entrada de usuário é quase sempre string — esses métodos são o canivete suíço do texto.

## Modelo mental
String é um livro em capa dura: você não risca a página — cola um post-it por cima. Cada método devolve uma CÓPIA nova, modificada; a string original permanece intocada a menos que você atribua o retorno.

## Em uma linha
Métodos de string transformam (devolvem string nova) ou inspecionam (devolvem int/bool) o texto — nunca alteram a original.

## Na prática

### Caso simples — transformação (devolvem cópia)

```python
nome = "  maria silva  "

nome.upper()          # ← "  MARIA SILVA  " — tudo maiúsculo
nome.lower()          # ← "  maria silva  " — tudo minúsculo
nome.strip()          # ← "maria silva" — remove espaços das pontas
nome.strip().title()  # ← "Maria Silva" — 1ª letra de cada palavra
"python é legal".capitalize()  # ← "Python é legal" — só a 1ª letra
```

### Com variação — inspeção (devolvem outro tipo)

```python
frase = "o python é home, python é legal"

frase.find("python")   # ← 2 — posição da 1ª ocorrência; -1 se não existir
frase.rfind("python")  # ← 17 — posição da ÚLTIMA ocorrência
frase.count("python")  # ← 2 — quantas vezes aparece
"123".isdigit()        # ← True — todos os caracteres são dígitos
"abc".isalpha()        # ← True — todos são letras
"AB".isupper()         # ← True — tudo maiúsculo
"ab".islower()         # ← True — tudo minúsculo
str(7).zfill(2)        # ← "07" — preenche com zeros até 2 posições
```

### Em uso real — projeto da aula 42: letra que mais aparece

```python
frase = "Banana amarela"

frase_normalizada = frase.lower()          # ← evita contar 'A' e 'a' separado
letra_mais_frequente = ""
maior_quantidade = 0

for letra in frase_normalizada:
    if letra == " ":                       # ← espaço não é letra
        continue
    quantidade = frase_normalizada.count(letra)   # ← conta ocorrências
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        letra_mais_frequente = letra

print(f"{letra_mais_frequente!r} aparece {maior_quantidade}x")  # ← 'a' aparece 5x
```

## O que NÃO fazer

```python
nome = "maria"
nome.upper()          # ← ERRO CLÁSSICO: resultado DESCARTADO
print(nome)           # ← "maria" — nada mudou
nome = nome.upper()   # ← correto: atribua a cópia de volta

frase = "abc"
frase.count("A")      # ← 0 — count diferencia maiúsculas de minúsculas
# Normalize com .lower() antes de contar sem distinção.

"12a".isalpha()       # ← False — isalpha exige TODOS os caracteres como letra
```

## Por que Python funciona assim?
Strings são IMUTÁVEIS: nenhum método altera a string existente; tudo devolve uma string nova. É uma proteção: se duas variáveis apontam para a mesma string e você "muda" uma, a outra não é corrompida (diferente de listas mutáveis, nota 09). .find/.rfind devolvem -1 em vez de erro — você precisa checar esse caso. .count conta ocorrências não sobrepostas e é sensível a maiúsculas/minúsculas.

## Conexões
- Você já usou esse padrão quando: `len()` na nota 06 também inspeciona e devolve um int
- Aparece também em: sanitização de formulários (.strip() + .lower() antes de comparar), busca em texto, máscaras (.isdigit() para validar dígitos de CPF, nota 13)
- Diferente de: fatiamento `[i:f:p]` (nota 06) — slicing recorta posições; métodos transformam o conteúdo inteiro

---

## Teste de recuperação — responda sem olhar para cima

1. Por que `nome.upper()` sozinho não muda o valor da variável nome?
2. O que .find() devolve quando a substring não existe? Como você trata isso?
3. Escreva o código que conta quantas 'a' existem em "Banana", ignorando maiúsculas.

---

**Frase-âncora:** "Imutável: métodos devolvem cópia — atribua o retorno."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14