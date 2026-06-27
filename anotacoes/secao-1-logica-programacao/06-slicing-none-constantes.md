# Slicing, None, Constantes, Try/Except

Usado para extrair partes de strings, representar ausência de valor e tratar erros básicos.

## Fatiamento de Strings `[i:f:p]`

```python
texto = "Python"

texto[0]        # 'P'
texto[-1]       # 'n' (último)
texto[0:3]      # 'Pyt'
texto[::2]      # 'Pto' (pulando de 2)
texto[::-1]     # 'nohtyP' (invertido)
len(texto)      # 6
```

## Constantes (convenção)

```python
VELOCIDADE_MAXIMA = 80
TAXA_JUROS = 0.05
# Python não impede alteração — é convenção
```

## `None`, `is`, `is not`, `id()`

```python
variavel = None
if variavel is None:
    print("Não definido")
if variavel is not None:
    print("Definido")

id(variavel)  # endereço de memória do objeto
```

## `try`/`except` Básico

```python
try:
    numero = float(input("Digite um número: "))
except ValueError:
    print("Isso não é um número válido")
```
