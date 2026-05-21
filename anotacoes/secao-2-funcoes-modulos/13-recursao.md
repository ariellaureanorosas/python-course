# Funções Recursivas

## Conceito
Função que chama a si mesma:
1. Caso base (condição de parada)
2. Caso recursivo (chama a si mesma)

## Fatorial
```python
def fatorial(n):
    if n <= 1:   # caso base
        return 1
    return n * fatorial(n - 1)  # caso recursivo

fatorial(5)  # 120
```

## Limite de Recursão
```python
import sys
sys.getrecursionlimit()   # 1000 (padrão)
sys.setrecursionlimit(2000)  # aumenta limite
```

## Exemplo: contagem
```python
def contar(start, end):
    if start > end:
        return
    print(start)
    contar(start + 1, end)
```

## Cuidados
- Sempre ter um caso base
- Certificar que converge para o caso base
- Python não otimiza recursão (tail call)
- Prefira iteração para loops profundos
