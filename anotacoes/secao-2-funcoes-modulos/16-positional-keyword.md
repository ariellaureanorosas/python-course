# Positional-Only e Keyword-Only Arguments

## Quando você vai usar isso?
Você está escrevendo uma função pública de uma biblioteca e quer forçar quem chama a usar `nome=` para evitar confusão com a ordem dos parâmetros. Ou está criando uma API interna e quer proibir argumentos nomeados para manter performance. Os marcadores `/` e `*` controlam exatamente como os argumentos podem ser passados.

## Modelo mental
Catracas de controle. `/` é uma catraca na entrada: antes dela, só passa na ordem da fila (posição). `*` é uma catraca na saída: depois dela, só passa se chamar pelo nome. Entre elas, livre arbítrio.

## Em uma linha
Use `/` para forçar argumentos posicionais e `*` para forçar argumentos nomeados na assinatura da função.

## Na prática

### Caso simples

```python
def somar(a, b, /):                                    # ← / diz: tudo ANTES é posicional
    return a + b

somar(1, 2)                                            # ← OK: posicional
somar(a=1, b=2)                                        # ← TypeError! nomeado proibido

def saudacao(*, nome, saudacao="Olá"):                 # ← * diz: tudo DEPOIS é nomeado
    return f"{saudacao}, {nome}!"

saudacao(nome="João")                                  # ← OK: nomeado
saudacao("João")                                       # ← TypeError! posicional proibido
```

### Com variação

```python
def calcular(valor, /, taxa, *, desconto=0):            # ← três zonas:
    """                                                  #   antes de / = positional-only
    valor: positional-only                               #   entre / e * = ambos
    taxa: positional ou keyword                          #   depois de * = keyword-only
    desconto: keyword-only
    """
    return valor * taxa - desconto

calcular(100, 0.1)               # ← OK: valor posicional, taxa posicional
calcular(100, taxa=0.1)          # ← OK: valor posicional, taxa nomeada
calcular(100, 0.1, desconto=5)   # ← OK: valor posicional, taxa posicional, desconto nomeado
calcular(valor=100, taxa=0.1)    # ← TypeError! valor é positional-only
```

### Em uso real

```python
# Biblioteca pública: força nome nos parâmetros para evitar erro de ordem
def conectar(*, host, porta, timeout=30):
    print(f"Conectando a {host}:{porta} (timeout={timeout}s)")

conectar(host="localhost", porta=8080)                  # ← claro e seguro
conectar("localhost", 8080)                             # ← TypeError! obriga nomear

# API interna: performance máxima com argumentos posicionais
def processar_lote(dados, /):                            # ← sem overhead de nomeação
    return [dado * 2 for dado in dados]

processar_lote([1, 2, 3])                                # ← rápido, sem lookup de keyword
```

## O que NÃO fazer

```python
def misturar(a, /, b, /, c):                             # ← ERRO de sintaxe!
# SyntaxError: / vai SOMENTE uma vez, no fim dos posicionais.

def errado(*, a, b):                                     # ← OK: tudo keyword-only
def errado(a, b, /):                                     # ← OK: tudo positional-only
def errado(a, /, b, *, c):                               # ← OK: mistura correta
def errado(a, /, b, *, c, /):                            # ← ERRO: / depois de *

# O marcador / separa parâmetros em posicionais (antes) do resto (depois).
# O marcador * separa parâmetros em posicionais/normais (antes) de keyword-only (depois).
# Ordem obrigatória na assinatura: positional-only (/), ambos, keyword-only (*).
```

## Por que Python funciona assim?
`/` e `*` são marcadores de assinatura introduzidos no PEP 457 e PEP 3102. Eles existem porque:
- Funções built-in como `len(x)` sempre foram posicionais — `/` formaliza isso.
- `*` resolve ambiguidade quando uma função tem muitos parâmetros opcionais com nomes descritivos.
- Internamente, Python faz distinção entre `METH_VARARGS` (posicional) e `METH_KEYWORDS` (nomeado) no C — esses marcadores expõem essa diferença para o Python puro.
- Ordem no parser: Python primeiro separa os parâmetros antes de `/` (só posição), depois os entre `/` e `*` (qualquer), depois os depois de `*` (só nome).

## Conexões
- Você já usou esse padrão quando: passou argumentos para `print()` sem nomear (`print("oi")`) — `print` aceita positional-only
- Aparece também em: `range(10)` é positional-only; `dict()` tem keyword-only (`dict.fromkeys`)
- Diferente de: `*args` captura posicionais extras como tupla; `**kwargs` captura nomeados extras como dict — são diferentes dos marcadores que *restringem* como passar

---

## Teste de recuperação — responda sem olhar para cima

1. O que o marcador `/` faz na assinatura de uma função?
2. Escreva uma função `configurar` que force `host` e `porta` como keyword-only.
3. Qual a diferença de usar `*` sozinho na assinatura versus usar `*args`?

---

**Frase-âncora:** "`/` obriga posição, `*` obriga nome — controle total da assinatura."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
