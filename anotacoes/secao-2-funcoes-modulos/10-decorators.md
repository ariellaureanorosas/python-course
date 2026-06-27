# Decorators

## Quando você vai usar isso?
Tem 10 funções no seu código e precisa adicionar logging em todas, ou medir o tempo de cada uma, ou verificar permissão antes de executar. Em vez de copiar o mesmo código em 10 lugares, você cria um decorator e aplica com `@`.

## Modelo mental
Decorator é uma camada extra que envolve sua função como um presente: você coloca a função dentro, o decorator embrulha com comportamento extra, e quem chama nem percebe a diferença.

## Em uma linha
Decorator é uma função que recebe outra função, adiciona comportamento e retorna uma versão modificada — sem alterar o código original.

## Na prática

### Caso simples
```python
# ← Decorator que imprime antes e depois
from functools import wraps      # ← preserva metadados da função original

def meu_decorator(func):         # ← recebe a função decorada
    @wraps(func)                 # ← copia nome, docstring etc para wrapper
    def wrapper(*args, **kwargs):# ← *args, **kwargs repassa qualquer argumento
        print("Antes")           # ← código extra antes
        resultado = func(*args, **kwargs)  # ← chama a função original
        print("Depois")          # ← código extra depois
        return resultado         # ← retorna o que a função original retornou
    return wrapper               # ← retorna a função embrulhada

@meu_decorator                   # ← dizer_oi = meu_decorator(dizer_oi)
def dizer_oi():
    print("Oi!")

dizer_oi()  # ← "Antes" → "Oi!" → "Depois"
```

### Com variação
```python
# ← Decorator com parâmetros — tripla camada de funções
from functools import wraps

def repetir(vezes):              # ← 1ª camada: recebe o parâmetro
    def decorator(func):         # ← 2ª camada: recebe a função
        @wraps(func)
        def wrapper(*args, **kwargs):  # ← 3ª camada: executa a lógica
            for _ in range(vezes):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repetir(3)                      # ← repetir(3) retorna decorator que recebe a função
def dizer_oi():
    print("Oi!")

dizer_oi()  # ← "Oi!" "Oi!" "Oi!"

# ← Aplicação manual — sem syntax sugar, mesmo resultado
def dizer_ola():
    print("Olá!")

dizer_ola = repetir(3)(dizer_ola)  # ← exatamente o que @repetir(3) faz por baixo
```

### Em uso real
```python
# ← Medir tempo de execução de qualquer função
from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        duracao = time.time() - inicio
        print(f"{func.__name__} levou {duracao:.4f}s")
        return resultado
    return wrapper

@timer
def calcular():
    return sum(range(10**6))

calcular()  # ← "calcular levou 0.0456s" (valor varia)

# ← Cache simples (memorização) — evita recalcular mesma entrada
def memoizar(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoizar
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
# ← fib(100) sem memoizar travaria; com memoizar é instantâneo
```

## O que NÃO fazer
```python
# ← ERRADO: esquecer @wraps — perde metadados da função
def decorator_errado(func):
    def wrapper(*args, **kwargs):   # ← sem @wraps
        return func(*args, **kwargs)
    return wrapper

@decorator_errado
def ola():
    """Diz olá"""
    pass

print(ola.__name__)   # ← "wrapper" — deveria ser "ola"
print(ola.__doc__)    # ← None — deveria ser "Diz olá"

# ← ERRADO: decorator sem return na wrapper — engole o resultado
def decorator_sem_return(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)      # ← esqueceu o return
    return wrapper

@decorator_sem_return
def soma(a, b):
    return a + b

print(soma(2, 3))  # ← None — perdeu o resultado da função original

# ← O erro real: decorator que "consome" o retorno sem querer
```

## Por que Python funciona assim?
O `@` é syntactic sugar — `@decorator` equivale a `func = decorator(func)` executado na definição da função. Decorators funcionam porque Python tem funções de primeira classe: você passa função como argumento, retorna função de dentro de outra, e define funções dentro de funções (closures). O `@wraps` copia `__name__`, `__doc__`, `__module__` e `__dict__` da original para a wrapper — sem ele, a introspecção quebra. Decorator com parâmetro precisa da tripla camada porque `@repetir(3)` executa `repetir(3)` primeiro (retorna decorator), e o resultado é usado como decorator (recebe a função).

## Conexões
- Você já usou esse padrão quando: viu `@app.route()` no Flask, `@pytest.fixture` no pytest
- Aparece também em: `@property`, `@staticmethod`, `@classmethod` — decorators nativos do Python
- Diferente de: `contextlib.contextmanager` — transforma generator em context manager, não embrulha função

---

## Teste de recuperação — responda sem olhar para cima

1. O que acontece se você NÃO usar `@wraps` em um decorator?
2. Escreva um decorator `@log_chamadas` que imprime "Chamando <nome> com <args>" antes de executar.
3. Qual a diferença entre `@decorator` e `@decorator()`?

---

**Frase-âncora:** Decorator embrulha função com comportamento extra sem modificar o original.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
