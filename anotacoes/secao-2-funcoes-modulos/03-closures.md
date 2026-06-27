# Closures

## Quando você vai usar isso?
Quando precisa que uma função "lembre" de um valor sem usar variável global. Tipo um contador de visitas que começa em zero para cada nova sala — cada sala (função) tem seu próprio contador isolado.

## Modelo mental
Uma função que carrega uma mochila invisível com variáveis do escopo onde nasceu, mesmo depois da função externa ter terminado.

## Em uma linha
Função interna que captura e mantém acesso persistente a variáveis do escopo da função externa.

## Na prática

### Caso simples
```python
def criar_saudacao(saudacao):
    # ← função externa: recebe e guarda `saudacao` no stack
    def saudar(nome):
        # ← função interna: "lembra" de `saudacao` mesmo depois
        return f"{saudacao}, {nome}!"
        # ← `saudacao` veio do escopo externo (closure)
    return saudar
    # ← retorna a função sem executar (sem parênteses)

dizer_oi = criar_saudacao("Olá")  # ← `dizer_oi` guarda a closure com "Olá"
dizer_oi("João")                  # ← "Olá, João!"
```

### Com variação
```python
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador  # ← `multiplicador` está no closure
    return multiplicar

dobro = criar_multiplicador(2)   # ← closure com multiplicador=2 congelado
triplo = criar_multiplicador(3)  # ← closure com multiplicador=3 congelado
dobro(10)                        # ← 20
triplo(10)                       # ← 30
```

### Em uso real
```python
def contador():
    count = 0
    # ← variável "privada" — só a closure pode ler/modificar
    def incrementar():
        nonlocal count
        # ← `nonlocal` permite modificar variável do escopo externo
        count += 1
        return count
    return incrementar

acessos = contador()
acessos()  # ← 1
acessos()  # ← 2
acessos()  # ← 3
```
Útil para rate limiter, cache com estado interno, lazy initialization.

## O que NÃO fazer
```python
def criar_funcoes():
    funcoes = []
    for i in range(3):
        def func():
            return i  # ← `i` é a mesma variável, não o valor no momento
        funcoes.append(func)
    return funcoes

criar_funcoes()[0]()  # ← 2, não 0! `i` vale 2 quando as closures executam
```
Solução: `lambda i=i: i` — o valor é congelado como argumento padrão no momento da criação.

## Por que Python funciona assim?
Toda função em Python carrega um atributo `__closure__` com referências (células) às variáveis do escopo onde foi definida. Quando a função externa termina, suas variáveis locais normalmente seriam destruídas. Mas o garbage collector as mantém vivas porque a closure ainda as referencia. Cada chamada da externa cria um novo conjunto de variáveis no closure — por isso `dobro` e `triplo` têm multiplicadores diferentes.

## Conexões
- Você já usou esse padrão quando: usou callback de evento que acessa `self` — método de classe é uma closure de `self`
- Aparece também em: decorators, `functools.partial`, `threading.Timer` com lambda, memoization
- Diferente de: função aninhada sem retorno (morre junto da externa), classe com estado (mais verbosa mas mais legível para estado complexo)

---

## Teste de recuperação — responda sem olhar para cima

1. O que acontece com as variáveis da função externa depois que ela termina, se uma closure ainda as referencia?
2. Escreva uma closure `criar_saudacao_personalizada` que recebe `prefixo` e retorna uma função que recebe `nome` e imprime `{prefixo} {nome}!`.
3. Por que o exemplo com `for i in range(3)` retorna 2 em vez de 0? Como corrigir?

---

**Frase-âncora:** Função que carrega consigo variáveis do escopo onde nasceu.
**Nível:** Avançado
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
