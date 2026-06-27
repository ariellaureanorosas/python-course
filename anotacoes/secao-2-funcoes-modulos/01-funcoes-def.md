# Funções (`def`)

Usado para organizar e reutilizar blocos de código com parâmetros e retorno.

## Estrutura

```python
def nome_funcao(param1, param2=valor_padrao):
    """Docstring explicativa."""
    return resultado
```

## Argumentos Nomeados vs Posicionais

```python
def soma(a, b):
    return a + b

soma(1, 2)      # posicionais
soma(a=1, b=2)  # nomeados
soma(1, b=2)    # misto (posicionais primeiro)
```

## Escopo (local/global)

```python
x = "global"

def func():
    x = "local"    # não modifica a global

def func2():
    global x       # modifica a global
    x = "alterada"
```

## `return`

```python
def soma(a, b):
    return a + b    # retorna valor

def sem_return():
    pass            # retorna None implicitamente
```
