# Operação Ternária e Utilitários

Usado para condicionais simples em uma linha e operações com precisão decimal.

## Operador Ternário

```python
# valor if condição else outro_valor
status = "Aprovado" if nota >= 7 else "Reprovado"

# Aninhado
categoria = (
    "Alta" if valor > 100
    else "Média" if valor > 50
    else "Baixa"
)
```

## `decimal.Decimal()` — precisão financeira

```python
from decimal import Decimal
valor = Decimal("10.50")
imposto = Decimal("0.15")
total = valor + (valor * imposto)
```

## `round()` — arredondamento

```python
round(3.14159, 2)  # 3.14
round(2.5)         # 2 (arredonda para par)
round(3.5)         # 4 (arredonda para par)
```
