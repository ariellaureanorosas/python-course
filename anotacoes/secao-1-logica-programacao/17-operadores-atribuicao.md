# Operadores de Atribuição

## Quando você vai usar isso?
Sempre que precisar acumular: contador de tentativas (`+= 1`), total de compras (`+= preco`), dobrar a cada volta (`*= 2`), dividir um valor ao meio (`//= 2`). É o atalho "pegue o valor atual, aplique a operação, guarde de volta" — onipresente em loops e acumuladores.

## Modelo mental
É a fita métrica: `+=` mede o comprimento atual, aplica a operação e anota o novo valor de volta nela. A variável participa dos dois lados da conta.

## Em uma linha
`a op= b` equivale a `a = a op b`: aplica `op` com `b` ao valor atual e grava o resultado em `a`.

## Na prática

### Caso simples — aritmética

```python
total = 0
total += 10     # ← 0 + 10 = 10
total += 5      # ← 10 + 5 = 15
total -= 3      # ← 12
total *= 2      # ← 24
total /= 2      # ← 12.0   (divisão SEMPRE vira float)
total //= 2     # ← 6.0    (divisão inteira mantém float)
total **= 2     # ← 36.0
total %= 7      # ← 1.0    (resto da divisão)
```

### Com variação — strings e listas

```python
mensagem = "olá"
mensagem += ", mundo!"   # ← "olá, mundo!" (concatenação)

numeros = [1, 2]
numeros += [3]           # ← [1, 2, 3] — estende a lista (como .extend)
```

### Em uso real — acumulador clássico

```python
precos = [19.90, 5.50, 8.75]
total_pedido = 0
for preco in precos:
    total_pedido += preco         # ← acumula a cada volta

dobro = 2
for _ in range(3):
    dobro *= 2                    # ← 4, 8, 16 — dobra em sequência
```

## O que NÃO fazer

```python
x = 10
x += 1        # ← correto: x = 11
x =+ 1        # ← ERRADO: isso é x = (+1) — reatribui 1!
x == 1        # ← isso é COMPARAÇÃO, devolve True/False — não altera nada
```

## Por que Python funciona assim?
O interpretador "expande" o operador composto em duas etapas: lê o valor atual de `a`, aplica a operação com `b` e reatribui em `a`. Como `+` também funciona para strings e listas, os compostos seguem o mesmo caminho. Atenção: `lista += [x]` estende a lista com os ITENS do lado direito (como .extend), não anexa a lista inteira.

## Conexões
- Você já usou esse padrão quando: `contador += 1` nos loops while da nota 07
- Aparece também em: pontuação de jogos, caixa de supermercado, estatísticas acumuladas
- Diferente de: `==` (compara, não atribui) e de `x = x + 1` (equivalente, só que mais verboso)

---

## Teste de recuperação — responda sem olhar para cima

1. O que `total *= 2` faz com o valor atual de total?
2. Por que `x /= 2` transforma x em float mesmo quando x era int?
3. Reescreva `saldo = saldo - saque` usando o operador composto.

---

**Frase-âncora:** "Operador composto: leia, calcule, guarde de volta."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14