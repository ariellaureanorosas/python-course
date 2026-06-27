# Tratamento de Erros (`try`/`except`/`raise`)

Usado para lidar com erros de forma controlada sem interromper o programa.

## `try` / `except` / `else` / `finally`

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero")
except TypeError:
    print("Tipo inválido")
else:
    print("Executado se NÃO houve erro")
finally:
    print("Sempre executado")
```

## Exceções Comuns

```python
ValueError           # valor inválido
TypeError            # tipo inválido
KeyError             # chave de dict não existe
IndexError           # índice de lista inválido
ZeroDivisionError
FileNotFoundError
```

## `raise` — lançar exceções

```python
def dividir(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a deve ser int ou float")
    if b == 0:
        raise ZeroDivisionError("Divisão por zero")
    return a / b
```

## Boas Práticas

- Sempre especificar o tipo de exceção
- Nunca usar `except:` sem tipo
- Não silenciar erros com `except: pass`
- Usar `raise` para repassar se não puder tratar
