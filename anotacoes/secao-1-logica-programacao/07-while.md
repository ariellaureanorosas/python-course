# Loop `while`

## Quando você vai usar isso?
Você está lendo linhas de um arquivo até o fim, ou pedindo senha até o usuário acertar, ou processando uma fila de tarefas sem saber quantas são. A condição decide quando parar.

## Modelo mental
É uma porta giratória: enquanto o segurança (condição) deixar, você continua passando. Quando ele barra, o loop morre.

## Em uma linha
Repita um bloco enquanto a condição for True.

## Na prática

### Caso simples — contador
```python
contador = 0

# ← executa enquanto contador < 5 for True
while contador < 5:
    print(contador)       # ← 0, 1, 2, 3, 4
    contador += 1         # ← soma 1 a cada volta
# ← quando contador = 5, condição vira False, loop acaba
```

### Com variação — break e continue
```python
# ← break: sai do loop NA HORA, independente da condição
while True:                     # ← loop "infinito" (intencional)
    entrada = input("Digite 'sair': ")
    if entrada == "sair":
        break                   # ← interrompe o loop aqui
    print("Ainda no loop")      # ← não executa se entrou no break

# ← continue: pula o resto da volta, volta pro começo
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue                # ← volta pro while sem printar 5
    print(contador)             # ← 1,2,3,4,6,7,8,9,10
```

### Em uso real — menu com validação
```python
# ← combina while + break + flag de controle
executando = True

while executando:
    opcao = input("(1) Novo (2) Sair: ")

    if opcao == "1":
        print("Criando...")
    elif opcao == "2":
        print("Até logo!")
        executando = False      # ← condição vira False, loop termina
        # ← poderia ser `break` no lugar da flag
    else:
        print("Opção inválida, tente de novo")
        # ← volta ao while sem sair

# ← while/else: else executa QUANDO a condição fica False (NÃO com break)
contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print("Loop terminou naturalmente")  # ← printa porque NÃO deu break
```

## O que NÃO fazer
```python
while True:           # ← loop infinito ACIDENTAL
    print("travado")  # ← nunca sai — falta break ou condição de saída

x = 10
while x > 0:          # ← NUNCA vai executar (x > 0 é False)
    print(x)          # ← condição já é falsa antes de entrar

contador = 0
while contador < 5:
    print(contador)
    # ← ESQUECEU o contador += 1 — loop infinito!
```

## Por que Python funciona assim?
O while avalia a condição ANTES de cada iteração. Se for True, executa o bloco; se False, pula pro próximo comando. `break` desvia o fluxo pra fora do while imediatamente. `continue` desvia pro topo, reavaliando a condição. O `else` de while executa APENAS se a condição ficou False naturalmente — se deu break, o else NÃO roda. É um else meio contraintuitivo, mas útil pra confirmar que o loop completou sem interrupção.

## Conexões
- Você já usou esse padrão quando: usou `if` pra verificar uma condição
- Aparece também em: loops de evento em jogos, servidores web, listeners de socket
- Diferente de: `for` (sabe quantas iterações tem); `while` só sabe a condição

---

## Teste de recuperação — responda sem olhar para cima

1. O que faz o `else` depois de um `while` ser diferente do `else` normal?
2. Escreva um loop que só sai quando o usuário digitar "sair", sem usar `break`.
3. Qual a diferença entre `break` e `continue`?

---

**Frase-âncora:** "Enquanto for True, executa. False ou break, encerra."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
