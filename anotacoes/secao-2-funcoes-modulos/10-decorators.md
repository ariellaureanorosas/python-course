# Decorators

Usado para adicionar funcionalidades a funções existentes sem modificar seu código.

## Estrutura Básica

```python
from functools import wraps

def meu_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Depois")
        return resultado
    return wrapper

@meu_decorator
def dizer_oi():
    print("Oi!")
```

## Decorator com Parâmetros

```python
def repetir(vezes):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repetir(3)
def dizer_oi():
    print("Oi!")
```

## Aplicação Manual

```python
dizer_oi = meu_decorator(dizer_oi)
```

## Usos Comuns

- Logging
- Validação de argumentos
- Cache
- Controle de acesso
- Medição de tempo
