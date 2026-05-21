# Módulos e Pacotes

## Importação

```python
import modulo               # namespace preservado
from modulo import funcao   # sem namespace
import modulo as apelido    # apelido
from modulo import *        # evitar
```

## `if __name__ == "__main__"`

```python
if __name__ == "__main__":
    main()
```

## Pacotes (pastas com `__init__.py`)

```
meu_pacote/
  __init__.py
  modulo.py
```

```python
from meu_pacote import modulo
```

## `__all__` — controla `from modulo import *`

```python
__all__ = ["funcao_publica", "VariavelPublica"]
```

## `importlib.reload()`

```python
import importlib
importlib.reload(modulo)
```

## Ordem de Imports

1. Biblioteca padrão (stdlib)
2. Terceiros
3. Locais
