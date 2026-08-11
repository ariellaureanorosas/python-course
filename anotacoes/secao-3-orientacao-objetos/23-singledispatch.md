# singledispatch (polimorfismo por tipo do primeiro argumento)

## Quando você vai usar isso?
Quando uma função cresceu cheia de `if isinstance(valor, ...)` dentro — "se for int, faz assim; se for str, faz assado" — e cada vez que aparece um tipo novo você mexe na função original. `singledispatch` deixa VOCÊ definir o comportamento por tipo FORA da função, como se fosse polimorfismo de classes horizontal: a função base continua intocada e os comportamentos entram como registros novos.

## Modelo mental
É o balcão de informações com filas separadas: a função `descrever()` é o painel "qual é a fila certa?"; cada `@descrever.register(tipo)` é uma fila específica — fila dos `int`, fila das `str`, fila das `list`. O Python OLHA o tipo do PRIMEIRO argumento e aponta para a fila certa. Não existe fila para o seu tipo? Cai na fila geral (a função default). Nada de rebolar `if tipo_especial:` na cara do cliente — a função base nem precisa saber que os outros tipos existem.

## Em uma linha
`@funcao.register(tipo)` anexa uma versão especializada da função para o tipo do 1º argumento; a chamada despacha automaticamente para a versão certa (ou para a default), eliminando o `isinstance` em cadeia.

## Na prática

### Caso simples (sem singledispatch — o problema)
```python
def descrever(valor):
    if isinstance(valor, int):
        return f'inteiro com {len(str(valor))} dígitos'
    elif isinstance(valor, str):
        return f'texto com {len(valor)} letras'
    elif isinstance(valor, list):
        return f'lista com {len(valor)} itens'
    return f'objeto {type(valor).__name__}'

# ← funciona, mas: cada novo tipo = mexer na função original (bug no bolso)
```

### Com variação (singledispatch — o remédio)
```python
from functools import singledispatch

@singledispatch
def descrever(valor):
    # ← fila geral: o "default" de quem não tem fila própria
    return f'objeto {type(valor).__name__}'

@descrever.register(int)
def _(valor):
    return f'inteiro com {len(str(valor))} dígitos'

@descrever.register(str)
def _(valor):
    return f'texto com {len(valor)} letras'

@descrever.register(list)
def _(valor):
    return f'lista com {len(valor)} itens'

print(descrever(1234))              # ← inteiro com 4 dígitos
print(descrever('oi'))              # ← texto com 2 letras
print(descrever([1, 2]))            # ← lista com 2 itens
print(descrever(1.5))               # ← objeto float (fila geral!)
# ← novidade amanhã? @descrever.register(dict) em outro arquivo,
# ← SEM tocar em descrever()
```

### Em uso real (registro de MRO: subclasse cai na fila da base)
```python
from functools import singledispatch

@singledispatch
def serializar(valor):
    raise TypeError(f'não sei serializar {type(valor).__name__}')

@serializar.register(int)
def _(valor):
    return f'num:{valor}'

@serializar.register(str)
def _(valor):
    return f'str:{valor}'

print(serializar(7))          # ← num:7
print(serializar('a'))        # ← str:a

class MeuInt(int):            # ← subclasse de int
    pass

print(serializar(MeuInt(3)))  # ← num:3 — despacho respeita a HERANÇA
# ← o dispatch procura o tipo exato e, na falta, sobe a MRO da classe
```

## O que NÃO fazer
```python
# ← ERRADO: confundir singledispatch com @overload (typing)
from typing import overload, Union

@overload
def somar(a: int, b: int) -> int: ...   # ← só DOCUMENTAÇÃO do tipo
@overload
def somar(a: str, b: str) -> str: ...   # ← NÃO despacha NADA
def somar(a, b):                        # ← só esta versão roda de verdade
    return a + b                        # ← (Python não tem overload de verdade)
# ← o certo: singledispatch se você quer COMPORTAMENTO diferente por tipo

# ← ERRADO: singledispatch para despachar pelo 2º argumento
@funcao.register(int)      # ← dispacho é SEMPRE sobre o PRIMEIRO argumento
def _(b, valor):           # ← int aqui não manda em nada
    ...
# ← o certo: só funciona com o 1º argumento; para outros, despacho manual
# ← ou classes polimórficas mesmo

# ← ERRADO: usar singledispatch para substituir polimorfismo de classes
# ← em métodos — para comportamento por tipo do SELF, herança resolve
# ← (o singledispatch existe para FUNÇÕES soltas que cresceram em isinstance)
```

## Por que Python funciona assim?
`singledispatch` aproveita duas características do Python: funções são objetos de primeira classe que aceitam atributos (a função decorada ganha um registro interno `_registry` mapeando tipo → função) e a MRO da classe fornece a ordem de fallback (se não acha o tipo exato, sobe a cadeia de herança — por isso `MeuInt` cai na fila de `int`). Na chamada, o wrapper inspeciona o tipo do primeiro argumento, busca no registro a versão mais específica e a executa; se não há nenhuma, roda a função original (a default). É o mesmo princípio do dispatch dinâmico do polimorfismo de classes — override herda da base e pode ser sobrescrito — só que aplicado a funções soltas, com os "overrides" registrados por decorator em vez de definidos em subclasses.

## Conexões
- Você já usou esse padrão quando: o polimorfismo de classes (aula 159) — lá o despacho é por `self` via herança; aqui o despacho é por `valor` via registro
- Aparece também em: `isinstance` em cadeia (o anti-padrão que ele substitui), `@overload` (aparência parecida, função totalmente diferente), bibliotecas que fazem "renderização por tipo" e serializadores
- Diferente de: `@overload` (só anota tipos p/ checagem estática — mypy respeita, o runtime ignora), `functools.cache`/`lru_cache` (caché de resultado, não dispatch), `classmethod` alternativos — funções fábrica em classes (analítico de um modelo mental de registro por subclasse)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual é o critério usado pelo `singledispatch` para escolher a função a executar?
2. Registre os tipos `int`, `str` e `list` para a função `descrever` e mostre a chamada para `1.5`.
3. Qual a diferença entre `singledispatch` e `@overload` do módulo `typing`?

---

**Frase-âncora:** Um balcão, várias filas: o Python lê o tipo do primeiro argumento e te entrega na fila certa — a função base nem precisa saber das outras.
**Nível:** Avançado
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14