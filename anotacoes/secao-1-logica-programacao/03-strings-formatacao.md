# Strings e Formatação

## f-strings (Python 3.6+, preferencial)

```python
nome = "João"
print(f"Olá, {nome}!")
print(f"Preço: R${preco:.2f}")
print(f"{numero:0=+10,.1f}")  # sinal, zeros, separador milhar
```

## `str.format()`

```python
"a={} b={}".format(1, 2)
"a={nome1} b={nome2}".format(nome1="João", nome2="Maria")
```

## Interpolação com `%` (estilo antigo)

```python
"%s tem %d anos e R$%.2f" % (nome, idade, preco)
"%08X" % (15123,)  # hexadecimal com 8 dígitos
```

## Alinhamento

```python
f"{nome:<10}"   # esquerda (10 espaços)
f"{nome:>10}"   # direita
f"{nome:^10}"   # centralizado
f"{nome!r}"     # representação (com aspas)
f"{nome!s}"     # string (padrão)
f"{nome!a}"     # ASCII (escapa unicode)
```
