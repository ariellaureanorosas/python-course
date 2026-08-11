# Enum e metaclasses (o avançado da seção)

## Quando você vai usar isso?
Duas ferramentas distintas, mas que respondem à mesma pergunta — "e se o CÓDIGO valer por um valor?": Enum para quando você quer um CONJUNTO FECHADO de opções com nome (dias da semana, status do pedido, cores) em vez de strings soltas; metaclasses para quando você quer controlar a CRIACÃO de classes — casos raros e poderosos, como o próprio Enum usa por baixo (uma metaclasse valida e organiza o que você define).

## Modelo mental
Enum é o cardápio fixo: você não escolhe qualquer coisa — escolhe entre PENDENTE, PAGO, CANCELADO. Metaclasse é a "fábrica de classes": toda classe nasce de uma fábrica (o `type`); escrever uma metaclasse é MODIFICAR a fábrica para que TODAS as classes que ela cria venham com algo pronto ou validado — como a pré-fábrica do Enum que transforma `STATUS = 1` em `STATUS.pendente.value == 1`.

## Em uma linha
`Enum` cria um conjunto fixo de constantes nomeadas com `.name`/`.value` e `auto()`; metaclasse é a classe das classes — `type` cria classes, e você pode criar a sua versão de `type` para controlar/validar como cada classe é definida.

## Na prática

### Caso simples (Enum)
```python
from enum import Enum, auto

class StatusPedido(Enum):
    PENDENTE = auto()      # ← auto(): valor automático sequencial
    PAGO = auto()
    CANCELADO = auto()

print(StatusPedido.PAGO)                 # ← StatusPedido.PAGO
print(StatusPedido.PAGO.name)            # ← 'PAGO'
print(StatusPedido.PAGO.value)           # ← 2
for status in StatusPedido:              # ← iterável
    print(status.name)                   # ← PENDENTE, PAGO, CANCELADO
print(StatusPedido.PAGO == StatusPedido.PAGO)  # ← True (mesmo membro)
```

### Com variação (Enum com valores próprios)
```python
from enum import Enum

class DiaDaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2

def eh_dia_de_trabalho(dia):
    return dia in (DiaDaSemana.SEGUNDA, DiaDaSemana.TERCA)

print(eh_dia_de_trabalho(DiaDaSemana.SEGUNDA))   # ← True
# ← sem Enum: 'sexta' vs 'Sexta' vs 'SEXTA' — comparava corda por corda
```

### Em uso real (metaclasse)
```python
class MetaValidadora(type):
    """Fábrica de classes que exige o método `falar` em toda classe."""

    def __call__(cls, *args, **kwargs):
        # ← todo cls() passa por aqui ANTES de instanciar
        if not hasattr(cls, 'falar'):
            raise TypeError('Classe precisa do método falar')
        return super().__call__(*args, **kwargs)

class Pessoa(metaclass=MetaValidadora):   # ← "criada pela fábrica"
    def falar(self):
        return 'Olá'

p = Pessoa()      # ← ok: tem falar
print(p.falar())
# class SemFalar(metaclass=MetaValidadora):
#     pass
# SemFalar()      # ← TypeError: Classe precisa do método falar
```

## O que NÃO fazer
```python
# ← ERRADO: strings mágicas espalhadas no lugar de Enum
if status == 'pago':        # ← 'pago' vs 'Pago' vs 'pago ' — bug esperando
    ...
# ← o certo: StatusPedido.PAGO

# ← ERRADO: criar metaclasse para VALIDAR coisa simples
# ← (a maioria dos casos resolve com __init_subclass__ ou decorator)
class Meta(type):           # ← 20 linhas para uma checagem...
    ...
# ← o certo: só criar metaclasse quando o controle precisa do tempo
# ← de criação da classe (Enum, ORMs) — senão, ferramenta mais simples

# ← CUIDADO: Enum com dois valores iguais vira ALIAS (mesmo membro!)
class StatusPedido(Enum):
    PAGO = 1
    CONCLUIDO = 1           # ← alias! StatusPedido.CONCLUIDO is PAGO
# ← o certo: valores únicos ou usar auto()
```

## Por que Python funciona assim?
"Tudo é objeto" tem um nível a mais: classes TAMBÉM são objetos — instâncias de `type` (ou de uma metaclasse). `type` é a fábrica padrão: `type('Classe', (Base,), {'nome': 'x'})` equivale a `class Classe(Base):`. Uma metaclasse herda de `type` e intercepa `__new__` (criação da classe: você pode injetar métodos) ou `__call__` (instanciação: pode validar ANTES de criar instância). O `Enum` faz exatamente isso: sua metaclasse `EnumMeta` transforma os atributos do corpo (SEGUNDA = 1) em membros `.name`/`.value` no momento da definição. Por isso "Enum + metaclasses" andam juntos: o segundo é o mecanismo interno do primeiro.

## Conexões
- Você já usou esse padrão quando: usou `type(nome_da_classe)` para descobrir a classe de um objeto — a metaclasse é a classe dessa classe
- Aparece também em: Django Models (toda `class Produto(models.Model)` é reescrita pela metaclasse do ORM), SQLAlchemy, singletons — e Enum internamente
- Diferente de: `@decorator` (modifica função/instância no tempo de execução, não a definição da classe), `__init_subclass__` (gancho MAIS SIMPLES que metaclasse), `dataclass` (gera métodos, não valida a estrutura)

---

## Teste de recuperação — responda sem olhar para cima

1. Como criar um Enum com valores automáticos e como ler `.name` e `.value`?
2. Escreva um Enum `Prioridade(Enum)` com BAIXA/MEDIA/ALTA via `auto()`.
3. O que é a metaclasse de uma classe e qual é ela "padrão" para toda classe criada com `class`?

---

**Frase-âncora:** Enum é o cardápio fechado do seu domínio; metaclasse é a fábrica que fabrica as próprias fábricas — poder dosado, usado com propósito.
**Nível:** Avançado
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14