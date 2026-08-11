# Escopo de Variáveis e a Palavra global

## Quando você vai usar isso?
Quando uma função precisa CONTAR algo compartilhado (total de chamadas, saldo acumulado) ou quando você quer entender por que uma variável "não muda" dentro da função. Escopo é a resposta para a pergunta clássica do iniciante: "por que meu for/if não altera a variável?".

## Modelo mental
Escopo é o andar do prédio onde o nome existe. O térreo (global) todo mundo vê. Um andar (função) pode VER o térreo, mas não pode REESCREVER o térreo — a menos que a palavra `global` dê a chave. Andares mais altos (funções dentro de funções) não são vistos de fora.

## Em uma linha
Ler global é livre; ESCREVER global exige `global`; sem ela, `x = 10` dentro de função cria um x LOCAL novo.

## Na prática

### Caso simples — ler vs. escrever (aula 69)

```python
x = 1                       # ← global

def escopo():
    x = 10                  # ← SEM global: cria um x LOCAL, o de fora fica 1
    print(x)                # ← 10 (local)

escopo()
print(x)                    # ← 1 — o escopo não "vazou" para fora
```

### Com variação — global explícita

```python
contador = 0

def incrementar():
    global contador         # ← "use a variável global, não crie outra"
    contador += 1

incrementar()
incrementar()
print(contador)             # ← 2 — mudou de verdade o escopo global
```

### Em uso real — funções aninhadas e o escopo em camadas

```python
x = 1

def escopo():
    x = 10                  # ← local do escopo()

    def outra():
        global x            # ← aponta para o x GLOBAL (o = 1)
        x = 11
        y = 2               # ← local só da outra() — ninguém de fora vê

    outra()
    print(x)                # ← 10 — o x local do escopo() não foi tocado

escopo()
print(x)                    # ← 11 — o GLOBAL foi alterado pela global x
```

## O que NÃO fazer

```python
# ← ERRADO: esperar que a atribuição "suba" sozinha
total = 0
def somar(valor):
    total += valor          # ← UnboundLocalError: 'total' usado antes de ser local
# a += só "lê" total e reescreve — sem global, ela tenta criar local

# ← ERRADO: global para TUDO — vira dependência escondida e testável
# com dificuldade; prefira retornar o novo valor e reatribuir fora:
def somar(total, valor):
    return total + valor

total = somar(total, 5)     # ← sem global, visível, declarativo
```

## Por que Python funciona assim?
Python decide o escopo de um nome PELA ATRIBUIÇÃO: se a função atribui `x`, x é local dela — mesmo que exista um x global (isso evita sobrescrever globais por acidente). Sem atribuição, o nome é resolvido de dentro para fora: local → envolvente (closures, nota 03) → global → builtins (LEGB). `global` diz "trate o nome como o do módulo". O `global` é raro na prática: funções que devolvem valores (retorno puro) são mais testáveis — o global só ganha quando o estado compartilhado é o objetivo (contadores, config).

## Conexões
- Você já usou esse padrão quando: closures (nota 03) têm o escopo ENVOLVENTE — o primo do global que não exige a palavra mágica
- Aparece também em: flags de configuração em módulos, contadores de debug, memoização manual
- Diferente de: `nonlocal` (aula 103-104, nota 03) — que altera a variável do escopo ENVOLVENTE, não a global; e de atribuição local pura (cria um novo nome)

---

## Teste de recuperação — responda sem olhar para cima

1. Por que `total += 1` dentro de função levanta UnboundLocalError se existe total global?
2. Qual a diferença entre `global` (aula 69) e `nonlocal` (closures)?
3. Escreva um contador de chamadas com global e uma versão equivalente devolvendo o valor.

---

**Frase-âncora:** "Ler global é livre; escrever exige global — senão, é local novo."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14