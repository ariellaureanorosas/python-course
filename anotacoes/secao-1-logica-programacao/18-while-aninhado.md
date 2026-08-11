# While Aninhado

## Quando você vai usar isso?
Quando a repetição tem duas dimensões: uma grade (linhas × colunas), uma tabuada (número × multiplicador), um tabuleiro, um mapa. O loop externo percorre a 1ª dimensão; para CADA passo dele, o interno percorre a 2ª inteira.

## Modelo mental
É um prédio com varredura andar a andar: o externo sobe de andar; dentro de cada andar, o interno visita todos os quartos; só então o externo sobe.

## Em uma linha
Loop dentro de loop: o bloco interno roda por completo a cada volta do externo.

## Na prática

### Caso simples — grade 3×3

```python
linha = 1
while linha <= 3:                # ← loop EXTERNO (dimensão 1)
    coluna = 1
    while coluna <= 3:           # ← loop INTERNO (dimensão 2)
        print(f"({linha},{coluna})", end=" ")
        coluna += 1              # ← interno avança
    print()                      # ← quebra a linha ao fim do interno
    linha += 1                   # ← externo avança
```

### Em uso real — tabuada

```python
numero = 1
while numero <= 3:
    multiplicador = 1
    while multiplicador <= 10:
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
        multiplicador += 1
    numero += 1
```

### Com variação — sair dos dois loops com flag

```python
# ← break só encerra o loop MAIS INTERNO; a flag controla o externo
encontrado = False
linha = 1
while linha <= 3 and not encontrado:   # ← condição dupla no externo
    coluna = 1
    while coluna <= 3:
        if linha == 2 and coluna == 2:
            print("Achou!")
            encontrado = True          # ← derruba a condição do externo
            break                      # ← sai só do interno (obrigatório)
        coluna += 1
    linha += 1
```

## O que NÃO fazer

```python
linha = 1
while linha <= 3:
    coluna = 1
    while coluna <= 3:
        print(coluna)
        # ← ESQUECEU coluna += 1: loop interno infinito, nunca sai do prédio

# ← Esperar que um único break saia dos dois loops: break só derruba o
# aninhado mais próximo — para o externo, use flag ou condição composta
```

## Por que Python funciona assim?
Cada `while` tem condição, `break` e `continue` próprios: eles só afetam o loop onde foram escritos. É por isso que o padrão "sair de tudo" usa uma FLAG (variável booleana) combinada à condição do externo — quando a flag vira True, a condição cai na próxima checagem. O custo é multiplicativo: um loop 3×3 executa o bloco interno 9 vezes.

## Conexões
- Você já usou esse padrão quando: loops while simples da nota 07 — o aninhado é a composição deles
- Aparece também em: matrizes e listas de listas (nota 11), jogos de tabuleiro, animações de eixo X/Y
- Diferente de: `for` aninhado (nota 08) — mesma lógica, sintaxe mais limpa quando o número de repetições é conhecido

---

## Teste de recuperação — responda sem olhar para cima

1. Um `break` dentro do loop interno sai dos dois loops? Como sair dos dois?
2. Escreva um while aninhado que imprima uma pirâmide de 3 linhas de "*" (1, 2, 3 asteriscos).
3. O que acontece se você esquecer `coluna += 1` no loop interno?

---

**Frase-âncora:** "Externo = andares; interno = quartos; break só derruba o mais próximo."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14