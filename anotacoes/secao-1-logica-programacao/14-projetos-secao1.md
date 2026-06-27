# Projetos da Seção 1

## Quando você vai usar isso?
Sempre que precisar de um programa que conversa com o usuário em loop — menus interativos, jogos de adivinhação, CRUDs no terminal. Esses três padrões (calculadora + jogo + lista) cobrem 80% da lógica de sistemas CLI.

## Modelo mental
Um programa interativo é uma recepção de hotel: pergunta, processa, responde, e repete até o hóspede pedir a conta. `while True` mantém o balcão aberto; `break` é a chave que fecha; `continue` manda o próximo hóspede para frente sem terminar o atendimento atual.

## Em uma linha
Loop infinito com `input`, decisão com `if/elif`, proteção com `try/except`, e saída controlada por `break`.

## Na prática

### Caso simples

```python
# ← Calculadora com menu — operadores dentro de string são validados com "in"
while True:
    n1 = input("Número 1: ")         # ← input sempre retorna string
    n2 = input("Número 2: ")
    operador = input("Operador (+-*/): ")

    if operador not in "+-*/":        # ← validação: operador existe?
        print("Operador inválido")
        continue                       # ← volta ao início, não executa o resto

    try:
        n1_float, n2_float = float(n1), float(n2)
    except ValueError:
        print("Digite números válidos")
        continue

    if operador == "+":  print(n1_float + n2_float)
    elif operador == "-": print(n1_float - n2_float)
    elif operador == "*": print(n1_float * n2_float)
    else:                print(n1_float / n2_float)

    sair = input("Sair? (S/N): ").lower()
    if sair == "s":
        break                            # ← único ponto de saída do loop
```

### Com variação

```python
# ← Lista de compras com operações I/A/L/S e tratamento de erro
lista = []
while True:
    opcao = input("[I]nserir [A]pagar [L]istar [S]air: ").lower()

    if opcao == "i":
        item = input("Item: ")
        lista.append(item)                # ← adiciona ao final

    elif opcao == "a":
        try:
            indice = int(input("Índice: "))
            lista.pop(indice)             # ← remove pelo índice
        except (ValueError, IndexError):  # ← captura letra OU índice inexistente
            print("Índice inválido")

    elif opcao == "l":
        for i, item in enumerate(lista):  # ← enumerate: índice automático
            print(i, item)

    elif opcao == "s":
        break
```

### Em uso real

```python
# ← Jogo da Palavra Secreta — lógica de estado acumulativo
palavra_secreta = "python"
letras_acertadas = ""          # ← string que acumula acertos (não lista)
tentativas = 0

while True:
    letra = input("Digite uma letra: ").lower()
    tentativas += 1

    if len(letra) != 1:        # ← validação: exatamente 1 caractere
        print("Digite exatamente uma letra")
        continue

    if letra in palavra_secreta and letra not in letras_acertadas:
        letras_acertadas += letra   # ← concatena à string de acertos

    # ← Constrói palavra mascarada: p***on → pyth*n → python
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if "*" not in palavra_formada:   # ← todas as letras foram descobertas
        print(f"Você acertou! Tentativas: {tentativas}")
        break
```

## O que NÃO fazer

```python
# ← ERRADO: except sem tipo — engole TUDO, inclusive erros inesperados
try:
    lista.pop(int(input("Índice: ")))
except:                               # ← captura até KeyboardInterrupt (Ctrl+C)
    print("Deu erro")                  # ← "erros nunca devem passar silenciosamente"

# ← ERRADO: condição de saída no while sem break
while sair != "s":                    # ← se sair nunca for definido, NameError!
    # ...
    sair = input("Sair? ")            # ← funciona, mas se o usuário digitar "S" em vez de "s"?

# ← ERRADO: não converter input de string para número
n1 = input("Número: ")
n2 = input("Número: ")
print(n1 + n2)                        # ← concatena strings, não soma!

# ← ERRADO: continue sem atualizar variável de controle
tentativas = 0
while tentativas < 3:
    if condicao:
        continue                      # ← volta sem incrementar — loop INFINITO!
    tentativas += 1
```

## Por que Python funciona assim?
`while True:` cria um loop que só termina com `break` — não há condição de parada no cabeçalho. `continue` interrompe a iteração atual e volta ao início do loop — útil para pular entradas inválidas sem aninhar o resto em um `else`. `input()` sempre retorna string por design — a conversão explícita (`int()`, `float()`) segue o princípio "explícito é melhor que implícito". `try/except` com tipos específicos segue "erros nunca devem passar silenciosamente" — capturar só o que você sabe tratar.

## Conexões
- Você já usou esse padrão quando: fez `while resposta != "sair":` em exercícios de repetição
- Aparece também em: chatbots, formulários interativos, sistemas de CLI (como `git`), jogos baseados em turno
- Diferente de: `for` — `for` é para iterações sobre coleções (número definido); `while` é para "repita até que algo mude"

---

## Teste de recuperação — responda sem olhar para cima

1. O que acontece se você esquecer o `break` no loop da calculadora e o usuário digitar "S" para sair?
2. Escreva um loop que lê números até o usuário digitar "fim" e exibe a soma acumulada.
3. Qual a diferença de comportamento entre `continue` e `break` dentro de um `while True`?

---

**Frase-âncora:** "Loop infinito com input, decisão, proteção, e saída controlada por break."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
