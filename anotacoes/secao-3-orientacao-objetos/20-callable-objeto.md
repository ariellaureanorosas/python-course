# Objetos chamáveis (funções com estado)

## Quando você vai usar isso?
Quando uma FUNÇÃO precisa de ESTADO entre uma chamada e outra — um contador que lembra quantas vezes rodou, um callback configurável que guarda um prefixo/peso/limite fixo — e você prefere deixar esse estado visível e nomeado em vez de escondido numa closure. Também é o caminho para "objetos que se comportam como função": `minha_instancia()` direto, sem método `.executar()`. É o que decorators usam quando precisam devolver algo com memória e configuração (a função decorada + o contador de chamadas ficam como atributos do objeto chamável).

## Modelo mental
`__call__` é o "DNA de função" aplicado a um objeto: qualquer objeto com `__call__` pode ser invocado com parênteses — `objeto()`. Se uma função é uma máquina que recebe entrada e devolve saída, um objeto chamável é essa mesma máquina com um ARQUIVO EMBUTIDO: além de processar, ela LEMBRA coisas entre chamadas (o contador acumula, o callback guarda a config). A closure faz a mesma coisa com o estado escondido; o objeto chamável deixa o estado à vista — `contador.vezes` é um atributo de verdade.

## Em uma linha
`def __call__(self, ...)` torna a instância executável como função — `callable(objeto)` fica `True` — permitindo contadores com estado, callbacks configuráveis e decorators com memória.

## Na prática

### Caso simples (Contador com estado visível)
```python
class Contador:
    def __init__(self):
        self.vezes = 0

    def __call__(self):
        self.vezes += 1
        return self.vezes

contador = Contador()
print(callable(contador))     # ← True — tem __call__, é chamável
print(contador())             # ← 1
print(contador())             # ← 2
print(contador.vezes)         # ← 2 — estado visível, pode ser lido de fora
```

### Com variação (callback configurável)
```python
class Saudacao:
    """Uma "função" por configuração: mesma classe, usos diferentes."""

    def __init__(self, prefixo):
        self.prefixo = prefixo      # ← configuração guardada como estado

    def __call__(self, nome):
        return f'{self.prefixo}, {nome}!'

ola = Saudacao('Olá')
bom_dia = Saudacao('Bom dia')       # ← dois callbacks, uma classe
print(ola('Ana'))                   # ← Olá, Ana!
print(bom_dia('Bruno'))             # ← Bom dia, Bruno!
```

### Em uso real (decorator que devolve objeto chamável)
```python
def contar_chamadas(funcao):
    """Decorator: devolve um OBJETO chamável com contador interno."""

    class Envoltorio:
        def __init__(self, fn):
            self.fn = fn
            self.quantidade = 0

        def __call__(self, *args, **kwargs):
            self.quantidade += 1
            return self.fn(*args, **kwargs)

    return Envoltorio(funcao)

@contar_chamadas
def soma(a, b):
    return a + b

print(soma(1, 2))             # ← 3
print(soma(3, 4))             # ← 7
print(soma.quantidade)        # ← 2 — o próprio soma virou objeto com memória
```

### Comparação: closure × partial × __call__
```python
from functools import partial

# closure: estado escondido (não dá para ler de fora)
def criar_contador():
    vezes = 0
    def contar():
        nonlocal vezes
        vezes += 1
        return vezes
    return contar

c = criar_contador()
print(c(), c())               # ← 1 2 — funciona, mas `vezes` é inacessível

# partial: pré-configurar função SEM classe e SEM __call__
def saudar(prefixo, nome):
    return f'{prefixo}, {nome}!'

ola = partial(saudar, 'Olá')  # ← função nova com 'Olá' já fixado
print(ola('Ana'))             # ← Olá, Ana! — mesmo resultado de Saudacao('Olá')
# ← regra: estado que só CONFIGURA → partial; estado que ACUMULA → __call__
```

## O que NÃO fazer
```python
# ← ERRADO: chamar a instância sem __call__ definido
pessoa = Pessoa('Ana')        # ← tem só __init__
pessoa()                      # ← TypeError: 'Pessoa' object is not callable
print(callable(pessoa))       # ← False
# ← o certo: implementar __call__ (ou usar uma função comum)

# ← ERRADO: esquecer o `self` na assinatura do __call__
def __call__(nome):           # ← TypeError: missing 1 required argument
    ...
# ← o certo: def __call__(self, nome):

# ← ERRADO: forçar classe chamável onde partial resolve em UMA linha
class Adicionar:              # ← 7 linhas para um default fixo...
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return x + self.n
# ← o certo: from functools import partial
#            add5 = partial(lambda a, b: a + b, 5)
# ← use __call__ quando o estado CRESCE entre chamadas (contador, acumulador)

# ← CUIDADO: __call__ com efeito colateral silencioso — documente
def __call__(self, url):
    self.total += 1           # ← mutação a cada chamada pode surpreender
    return self.total
# ← o certo: deixar explícito (nome do atributo claro, docstring curta)
```

## Por que Python funciona assim?
Tudo em Python é objeto, inclusive funções — e o que faz algo ser chamável é UM atributo: a presença de `__call__` na classe. `callable(x)` olha `type(x).__call__`. O operador `x(...)` compila para o mesmo mecanismo: o interpretador procura `__call__` na classe de `x` e executa. Por isso são todas as coisas chamáveis: funções (têm `__call__` na própria `type` delas), classes (`Cliente()` chama `type.__call__`, que orquestra `__new__`/`__init__`) e instâncias com `__call__` definido. E como `__call__` é um método NORMAL, ele pode mutar `self` — é isso que dá estado entre chamadas à "função". Funções também podem ter atributos, mas `__call__` deixa isso explícito e organizado.

## Conexões
- Você já usou esse padrão quando: chamou uma classe (`Cliente()` chama `type.__call__` por baixo — classe É um objeto chamável) e usou conversores como `int('10')`/`str(5)` (callbacks de conversão)
- Aparece também em: decorators com estado (o exemplo acima é como o `functools.wraps` trabalha preservando atributos), `functools.partial` (pré-configura argumentos), views baseadas em classe do Django (`.as_view()` devolve um objeto chamável), `unittest.mock.Mock` (chamável e registra chamadas), callbacks de interfaces gráficas (tkinter `command=...`)
- Diferente de: closure com `nonlocal` (estado escondido e imutável de fora), `functools.partial` (configura argumentos, não acumula estado), geradores (`yield`/`next()`, não `()`), `@decorator` simples que devolve função (sem memória própria)

---

## Teste de recuperação — responda sem olhar para cima

1. O que `callable(x)` verifica de verdade? (Que atributo ele procura e em que LUGAR?)
2. Escreva uma classe `Contador` chamável que conta quantas vezes foi chamada e expõe o total como atributo.
3. Closure com `nonlocal` e classe com `__call__` guardam estado de formas diferentes — qual é a diferença prática na visibilidade?

---

**Frase-âncora:** `__call__` dá à instância o DNA de função — `objeto()` — para criar máquinas que processam E lembram: o estado fica à vista, o comportamento pode ser chamado.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14