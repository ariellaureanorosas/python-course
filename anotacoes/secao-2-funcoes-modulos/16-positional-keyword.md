# Positional-Only e Keyword-Only Arguments

## Positional-Only Parameters (/)
```python
# Parâmetros ANTES de / são APENAS posicionais
def somar(a, b, /):
    return a + b

somar(1, 2)      # OK
somar(a=1, b=2)  # ERRO!
```

## Keyword-Only Arguments (*)
```python
# Parâmetros DEPOIS de * são APENAS nomeados
def saudacao(*, nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

saudacao(nome="João")  # OK
saudacao("João")       # ERRO!
```

## Combinando Ambos
```python
def calcular(valor, /, taxa, *, desconto=0):
    """
    valor: positional-only (/)
    taxa: positional ou keyword
    desconto: keyword-only (*)
    """
    return valor * taxa - desconto

calcular(100, 0.1)               # OK
calcular(100, taxa=0.1)          # OK
calcular(100, 0.1, desconto=5)   # OK
calcular(valor=100, taxa=0.1)    # ERRO (valor é positional-only)
```
