# Print, Tipos Primitivos e Comentários

## Função print()
```python
print("Olá, mundo!")           # básico
print(12, 34, sep="-")         # separador: "12-34"
print("Linha 1", end="\n\n")   # final: duas quebras de linha
```

## Comentários
```python
# Comentário de uma linha

"""
Docstring / comentário
multilinha (várias linhas)
"""
```

## Tipos Primitivos
```python
type("Texto")   # <class 'str'>
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type(True)      # <class 'bool'>
```

## Type Conversion (coerção)
```python
int("42")       # 42
float("3.14")   # 3.14
str(42)         # "42"
bool("")        # False (string vazia = falsy)
bool(" ")       # True (string com espaço = truthy)
```

## Raw String
```python
print(r"Ariel \"Rosas\"")  # ignora escapes, mostra literal
```
