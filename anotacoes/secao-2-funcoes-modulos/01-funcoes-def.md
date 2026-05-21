# Funções (def)

## Estrutura Básica
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

## Escopo (global/local)
```python
x = "global"

def func():
    x = "local"   # variável local (não modifica global)
    
def func2():
    global x       # modifica a global
    x = "alterada"
```

## return
```python
def soma(a, b):
    return a + b    # retorna valor

def sem_return():
    pass            # retorna None implicitamente
```
