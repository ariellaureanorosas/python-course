# Operação Ternária e Utilitários

## Quando você vai usar isso?
Quando uma decisão é simples o suficiente para caber em uma linha — status, categoria, valor padrão — sem escrever um bloco `if/else`. E sempre que lidar com dinheiro: `Decimal` elimina os erros de ponto flutuante que `float` introduz em contas financeiras.

## Modelo mental
O ternário é um pedágio: "se tiver dinheiro, passa; senão, volta". `Decimal` é uma calculadora financeira que nunca erra troco — diferente da calculadora de bolso (float) que faz `0.1 + 0.2 = 0.30000000000000004`. `round` é o caixa que segue a regra "arredonda para o par mais próximo".

## Em uma linha
Ternário escolhe entre dois valores com `X if condição else Y`; `Decimal` faz matemática exata com casas decimais configuráveis; `round` arredonda usando a regra "bancária" (par mais próximo em .5).

## Na prática

### Caso simples

```python
# ← ternário: valor_se_verdadeiro if condição else valor_se_falso
status = "Aprovado" if nota >= 7 else "Reprovado"
# ← Equivale a:
# if nota >= 7:
#     status = "Aprovado"
# else:
#     status = "Reprovado"
```

### Com variação

```python
# ← ternário aninhado — use parênteses para legibilidade
categoria = (
    "Alta" if valor > 100
    else "Média" if valor > 50
    else "Baixa"
)
# ← Avalia de cima para baixo: primeira condição True vence

from decimal import Decimal
# ← Sempre passe string para Decimal, nunca float
preco = Decimal("19.90")         # ← exato: 19.90
quantidade = Decimal("3")
total = preco * quantidade       # ← 59.70, sem 59.700000000000003
```

### Em uso real

```python
from decimal import Decimal, ROUND_HALF_EVEN

# ← Cálculo financeiro com precisão e arredondamento controlado
valor_bruto = Decimal("100.50")
imposto = valor_bruto * Decimal("0.15")        # ← 15.075
total = valor_bruto + imposto                   # ← 115.575
total_final = total.quantize(
    Decimal("0.01"), rounding=ROUND_HALF_EVEN
)                                                # ← 115.58

# ← Ternário decidindo formatação na mesma linha
exibir = f"R$ {total_final}" if total_final > 0 else "Grátis"
```

## O que NÃO fazer

```python
# ← ERRADO: usar float para dinheiro
preco = 0.1 + 0.2         # ← 0.30000000000000004
print(preco == 0.3)        # ← False! Erro silencioso em caixa registradora

# ← ERRADO: confiar em round() para decisões financeiras sem conhecer a regra
round(2.5)  # ← 2 (arredonda para o par mais próximo — "bankers' rounding")
round(3.5)  # ← 4 (arredonda para o par mais próximo)
# ← Se espera "sempre arredondar para cima", você terá bugs

# ← ERRADO: ternário aninhado sem parênteses — vira "if dentro de else dentro de if"
r = "A" if a else "B" if b else "C" if c else "D"  # ← confuso e frágil
```

## Por que Python funciona assim?
O ternário `X if cond else Y` é syntactic sugar: o compilador gera o mesmo bytecode de um `if/else`, mas como *expressão* (produz um valor que pode ser atribuído). `Decimal` sobrecarrega operadores aritméticos com math decimal de precisão arbitrária usando inteiros internos — não usa IEEE 754 como `float`. O `round()` implementa ROUND_HALF_EVEN para evitar viés estatístico: em .5, arredonda para o dígito par mais próximo (se 2.5 vai para 2, 3.5 vai para 4), o que estatisticamente tende a zero ao longo de muitas operações.

## Conexões
- Você já usou esse padrão quando: escreveu `if cond: x = a else: x = b` — ternário encurta exatamente isso
- Aparece também em: compreensão de listas (`[x if cond else y for ...]`), `numpy.where()`, pandas `apply()`
- Diferente de: `or` / `and` — eles retornam *um dos operandos* sem avaliar ambos; ternário sempre avalia as duas branches

---

## Teste de recuperação — responda sem olhar para cima

1. Explique por que `round(2.5)` retorna 2 e não 3 — qual o nome dessa regra?
2. Escreva uma linha que define `desconto = 0.10` se `cliente_vip` for True, senão `0.05`.
3. Qual a diferença entre `Decimal("0.1") + Decimal("0.2")` e `0.1 + 0.2`?

---

**Frase-âncora:** "Decisão em linha única e precisão financeira sem surpresas de floating point."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
