# Módulos e Pacotes

## Importação
```python
import modulo               # namespace preservado
from modulo import funcao   # sem namespace
import modulo as apelido    # apelido
from modulo import *        # (evitar)
```

## if __name__ == "__main__"
```python
# Só executa quando rodado diretamente
if __name__ == "__main__":
    main()
```

## Pacotes (pastas com __init__.py)
```python
# meu_pacote/
#   __init__.py
#   modulo.py

from meu_pacote import modulo
```

## __all__ — controla o que `from modulo import *` exporta
```python
__all__ = ["funcao_publica", "VariavelPublica"]
```

## importlib.reload()
```python
import importlib
importlib.reload(modulo)  # recarrega sem reiniciar
```

## Boas Práticas
1. imports padrão (stdlib) primeiro
2. imports de terceiros depois
3. imports locais por último
4. separar grupos com linha em branco
5. evitar imports circulares
