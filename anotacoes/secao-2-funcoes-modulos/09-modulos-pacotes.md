# Módulos e Pacotes

## Quando você vai usar isso?
Seu projeto tem mais de 200 linhas e está tudo num arquivo só. Ou você quer usar `requests` mas não sabe como importar. Hora de organizar em módulos (arquivos .py) e pacotes (pastas com `__init__.py`).

## Modelo mental
Módulo é um fichário: cada arquivo .py é uma gaveta com funções e variáveis. Pacote é o armário: uma pasta que agrupa fichários. `__init__.py` é a etiqueta na porta dizendo "isso aqui é um pacote".

## Em uma linha
Módulo é qualquer arquivo .py importável; pacote é uma pasta com `__init__.py` que agrupa módulos sob um namespace.

## Na prática

### Caso simples
```python
# ← Três formas de importar com efeitos diferentes
import math                # ← namespace preservado: math.sqrt(9)
from math import sqrt      # ← sem namespace: sqrt(9) direto
import math as m           # ← apelido: m.sqrt(9)

# modulo.py
def saudacao(nome):
    return f"Olá, {nome}"

# main.py
import modulo
print(modulo.saudacao("Ana"))  # ← "Olá, Ana"
```

### Com variação
```python
# ← if __name__ == "__main__" — protege código na importação
# util.py
def dobra(x):
    return x * 2

if __name__ == "__main__":    # ← só executa se rodar util.py direto
    print(dobra(5))           # ← não roda quando outro importa util

# ← Pacote com __init__.py
# meu_pacote/
#   __init__.py  (pode ser vazio)
#   modulo.py
from meu_pacote import modulo

# ← __all__ — controla "from modulo import *"
# modulo.py
__all__ = ["funcao_publica", "VariavelPublica"]

def funcao_publica(): pass
def _privada(): pass           # ← _ no início é convenção de "privado"
```

### Em uso real
```python
# ← Estrutura padrão de projeto
# projeto/
#   main.py
#   utils/
#     __init__.py
#     arquivo.py
#     banco.py

# utils/__init__.py
from .arquivo import ler_csv    # ← import relativo: . = pacote atual
from .banco import conectar

# utils/banco.py — ordem padrão de imports
import sqlite3                  # ← 1. stdlib primeiro
import requests                 # ← 2. terceiro depois
from .arquivo import config     # ← 3. local por último
```

## O que NÃO fazer
```python
# ← ERRADO: from modulo import * — polui namespace e causa colisão
from math import *    # ← traz dezenas de nomes que você não sabe que existem
sqrt = 42            # ← sobrescreveu a função sqrt sem aviso

# ← ERRADO: import circular — A importa B, B importa A
# a.py: from b import funcao_b
# b.py: from a import funcao_a  # ← ImportError ou NoneType

# ← ERRADO: módulo com nome de biblioteca padrão
# Cria random.py e depois tenta import random de verdade
import random  # ← importa SEU arquivo, não o módulo padrão

# ← O erro real: import circular só funciona se um dos imports for dentro de função
```

## Por que Python funciona assim?
Python trata cada .py como módulo — ao importar, executa o arquivo inteiro e guarda em `sys.modules`. Na segunda importação, pega do cache, não executa de novo. `if __name__ == "__main__"` funciona porque Python define `__name__` como `"__main__"` no arquivo executado diretamente e como o nome do módulo quando importado. Pacotes são módulos com `__path__` — `__init__.py` vira o código do pacote (obrigatório no 3.2-, opcional no 3.3+). `__all__` é uma lista de strings que `from modulo import *` usa como filtro de exportação.

## Conexões
- Você já usou esse padrão quando: usou `import os`, `import sys` — ambos são módulos padrão
- Aparece também em: pacotes pip como `requests`, `flask` — são pacotes com módulos internos
- Diferente de: `exec()` ou `importlib.import_module()` — import dinâmico em runtime

---

## Teste de recuperação — responda sem olhar para cima

1. O que `if __name__ == "__main__"` impede de acontecer?
2. Crie a estrutura de um pacote `validadores` com `email` e `cpf`, e mostre como importar `validadores.email`.
3. Qual a diferença entre `import pacote` e `from pacote import modulo`?

---

**Frase-âncora:** Módulo = .py. Pacote = pasta + __init__.py. Namespace organiza tudo.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
