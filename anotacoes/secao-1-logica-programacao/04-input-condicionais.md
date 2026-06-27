# Input e Estruturas Condicionais

## Quando você vai usar isso?
Seu programa precisa perguntar algo ao usuário — nome, idade, escolha — e reagir de forma diferente dependendo da resposta. Input captura, condicionais decidem. Juntos são o esqueleto de qualquer programa interativo.

## Modelo mental
input() é um porteiro que pergunta "quem é?" e anota a resposta num papel. if/elif/else é um semáforo inteligente: se a condição for verde, avança; senão, testa a próxima; senão, para.

## Em uma linha
input() captura texto do teclado (sempre string), if/elif/else desvia o fluxo baseado em condições, operadores de comparação produzem True/False.

## Na prática

### Caso simples
```python
# input() — captura o que o usuário digitar e devolve como string (sempre!)
nome = input("Digite seu nome: ")          # ← o argumento é o prompt exibido pro usuário
idade = int(input("Digite sua idade: "))   # ← input retorna str, então converta se precisar de número

# if/elif/else — estrutura de decisão com três caminhos
if condicao:             # ← a condição é uma expressão que retorna True ou False
    bloco                 # ← executado se a condição for True (obrigatório 4 espaços de indentação)
elif outra_condicao:     # ← elif = else + if; testa nova condição se a primeira foi False
    bloco
else:                    # ← else: executado se nenhuma condição anterior foi True
    bloco
```

### Com variação
```python
# Operadores de comparação — comparam dois valores e retornam bool (True/False)
10 > 5     # ← True — maior que
10 >= 10   # ← True — maior ou igual a
5 < 10     # ← True — menor que
5 <= 5     # ← True — menor ou igual a
10 == 10   # ← True — igual a (NÃO confundir com = que é atribuição)
10 != 5    # ← True — diferente de
```

### Em uso real
```python
# Programa que compara dois números e diz qual é maior — exemplo clássico de decisão
a = int(input("Valor 1: "))   # ← converte pra int já na leitura, evita erro depois
b = int(input("Valor 2: "))
if a > b:                     # ← se a for maior que b
    print(f"{a} é maior")
elif a < b:                   # ← se não (a não é maior que b), testa se a é menor
    print(f"{b} é maior")
else:                         # ← se nenhuma das anteriores, só resta serem iguais
    print("Iguais")
```

## O que NÃO fazer
```python
# Comparar número com string sem converter — o erro é silencioso e sutil
idade = input("Idade: ")     # ← retorna "25" (string)
if idade > 18:                # ← TypeError! > não funciona entre str e int
# Solução: idade = int(input("Idade: "))
# Outro erro: usar = no lugar de ==
if idade = 18:                # ← SyntaxError: = é atribuição, não comparação
```

## Por que Python funciona assim?
`input()` sempre retorna string porque o teclado só produz texto — segurança primeiro (evita injeção de código). `elif` é uma abreviação de `else if` e existe pra evitar aninhamento excessivo. Python não tem `switch/case` propositadamente — a filosofia é "uma maneira óbvia de fazer" e o `if/elif/else` é essa maneira. Operadores de comparação podem ser encadeados: `10 < idade < 60` funciona.

## Conexões
- Você já usou esse padrão quando: validou campos em formulários — mesma lógica de if para cada campo
- Aparece também em: validação de dados de API — `if response.status_code == 200:` é a mesma estrutura
- Diferente de: operador walrus `:=` — `if (idade := int(input())) > 18:` atribui e compara numa linha só

---

## Teste de recuperação — responda sem olhar para cima

1. O que `input()` sempre retorna e por quê?
2. Escreva um código que pergunta a idade e diz se a pessoa é maior de idade (>= 18), menor (< 18) ou idosa (>= 65).
3. Qual a diferença entre `=` e `==` em Python?

---

**Frase-âncora:** "input captura teclado, if decide rota — o diálogo do seu programa com o mundo."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
