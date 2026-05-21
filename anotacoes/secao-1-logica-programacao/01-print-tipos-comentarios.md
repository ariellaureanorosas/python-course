# Print, Tipos Primitivos e Comentários

## `print()`

```python
print("Olá, mundo!")
print(12, 34, sep="-")         # "12-34"
print("Linha 1", end="\n\n")   # duas quebras no final
```

## Comentários

```python
# Comentário de uma linha

"""
Docstring / comentário
multilinha
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
bool("")        # False — string vazia é falsy
bool(" ")       # True — string com espaço é truthy
```

## Raw String

```python
print(r"Ariel \"Rosas\"")  # ignora escapes, exibe literal
```
