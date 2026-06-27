# `*args`, `**kwargs` e Higher Order Functions

## Quando você vai usar isso?
Quando não sabe quantos argumentos vão chegar — como um `console.log` que aceita qualquer quantidade de valores. Ou quando precisa construir uma chamada dinâmica, tipo um executor genérico de tarefas.

## Modelo mental
`*args` é uma sacola que coleta todos os argumentos posicionais extras que sobrarem; `**kwargs` é um fichário que coleta os nomeados.

## Em uma linha
Parâmetros especiais que capturam argumentos excedentes como tupla (`*args`) ou dicionário (`**kwargs`).

## Na prática

### Caso simples
```python
def log(*args):
    # ← `*args` empacota todos os argumentos posicionais numa tupla
    for msg in args:
        print(f"[LOG] {msg}")

log("iniciou", "processou", "finalizou")  # ← imprime 3 linhas
```

### Com variação
```python
def config(**kwargs):
    # ← `**kwargs` empacota argumentos nomeados num dicionário
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")

config(host="localhost", porta=8080, ssl=True)  # ← 3 pares chave-valor
```

### Em uso real
```python
def envia_email(destino, assunto, *anexos, **opcoes):
    # ← args fixos + args variáveis posicionais + args variáveis nomeados
    print(f"Para: {destino}, Assunto: {assunto}")
    for anexo in anexos:
        print(f"Anexo: {anexo}")
    if opcoes.get("cc"):
        print(f"CC: {opcoes['cc']}")
    if opcoes.get("prioridade"):
        print(f"Prioridade: {opcoes['prioridade']}")

envia_email("joao@email.com", "Relatório", "foto.jpg", "planilha.xlsx",
            cc="adm@empresa.com", prioridade="alta")
# ← função flexível: aceita 2, 3, ou 100 anexos + configs extras
```

## O que NÃO fazer
```python
def soma(*args):
    return sum(args)

numeros = [1, 2, 3]
print(soma(numeros))  # ← ERRO: `args` será ([1, 2, 3],) — tupla com um elemento
print(soma(*numeros)) # ← certo: `*` desempaca a lista em 3 argumentos
```
Na chamada, `*` desempaca (inverso da definição). Esquecer o `*` passa a lista inteira como um único argumento.

## Por que Python funciona assim?
O `*` antes do parâmetro na definição diz: "tudo que sobrar dos argumentos posicionais, coloca numa tupla". O `**` faz o mesmo para nomeados, mas num dict. Na chamada da função, `*sequencia` faz o inverso: itera a sequência e passa cada item como argumento separado. É açúcar sintático que evita ter que escrever `sum([1, 2, 3])` em vez de `sum(*[1, 2, 3])`.

## Conexões
- Você já usou esse padrão quando: chamou `print("a", "b", "c")` — `print` aceita `*args` internamente
- Aparece também em: `zip(*matriz)` para transpor linhas/colunas, `dict(**d1, **d2)` para mesclar, `functools.partial`
- Diferente de: parâmetros com valor padrão (são fixos e nomeados na definição), `*` sozinho (força keyword-only args)

---

## Teste de recuperação — responda sem olhar para cima

1. Que estrutura de dados é `args` dentro da função? E `kwargs`?
2. Escreva uma função `soma_tudo` que aceita qualquer quantidade de números e retorna a soma.
3. Qual a diferença entre `*args` na definição da função vs `*lista` na chamada da função?

---

**Frase-âncora:** Coleta argumentos excedentes como tupla (`*args`) ou dict (`**kwargs`).
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
