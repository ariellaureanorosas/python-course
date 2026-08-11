# cached_property (cache na instância, não na classe)

## Quando você vai usar isso?
Quando a propriedade é cara de calcular E os dados não mudam depois que a instância existe — um relatório que soma milhares de registros, uma consulta que monta JSON, um total que seria recalculado a cada acesso. Você usa `@cached_property` para calcular UMA vez e guardar o resultado no próprio objeto, em vez de recalcular em toda leitura de atributo como a `@property` comum faz.

## Modelo mental
`@property` comum é o porteiro que refaz a pergunta toda vez que você bate na porta: "qual é o total?" → recalcula. `cached_property` é o recibo da portaria: na primeira pergunta ele anota a resposta no quadro de avisos do prédio (o `__dict__` da instância) e, nas próximas, só aponta para o quadro. Cada prédio (instância) tem o SEU quadro — Ana não vê o recibo de Bia.

## Em uma linha
`@cached_property` roda o cálculo uma vez e guarda o resultado em `objeto.__dict__`; nas leituras seguintes devolve direto do dicionário — e `del objeto.atributo` limpa o recibo para recalcular.

## Na prática

### Caso simples (cálculo caro rodando uma vez)
```python
from functools import cached_property

class Relatorio:
    def __init__(self, vendas):
        self.vendas = vendas          # ← lista de valores

    @cached_property
    def total(self):
        # ← conta as chamadas para VER o cache funcionar
        print('calculando total...')
        return sum(self.vendas)

    @cached_property
    def media(self):
        return self.total / len(self.vendas)

r = Relatorio([10, 20, 30])
print(r.total)       # ← 'calculando total...'  → 60
print(r.total)       # ← 60 (SEM 'calculando total...' de novo!)
print(r.media)       # ← 20.0 (linha usa total ALREADY calculado)
```

### Com variação (invalidação manual com del)
```python
from functools import cached_property

class Relatorio:
    def __init__(self, vendas):
        self.vendas = vendas

    @cached_property
    def total(self):
        print('calculando total...')
        return sum(self.vendas)

r = Relatorio([10, 20, 30])
print(r.total)                    # ← 'calculando total...' → 60
r.vendas.append(40)               # ← dados mudaram...
print(r.total)                    # ← 60 — STALE! recibo antigo no quadro
del r.total                       # ← apaga o recibo do __dict__
print(r.total)                    # ← 'calculando total...' → 100 (novo!)
```

### Em uso real (contraponto: quando é cache ERRADO)
```python
from functools import cached_property

class Pedido:
    def __init__(self, itens):
        self.itens = itens

    @cached_property
    def total(self):
        return sum(self.itens)

    def adicionar(self, valor):
        self.itens.append(valor)   # ← muta o estado DEPOIS do cache...
        # del self.total            # ← ...então o chamador é o culpado:
        #                           # ← cache precisa de invalidação explícita

p = Pedido([50])
print(p.total)      # ← 50
p.adicionar(20)     # ← estado muda, cache continua 50 (STALE)
# ← regra prática: cached_property para dados IMUTÁVEIS após a criação
# ← (ou vel o contador em tabuleiro; senão está calculando 'na hora errada')
```

## O que NÃO fazer
```python
# ← ERRADO: usar cached_property calculado a partir de atributos mutáveis
class Portal:
    def __init__(self):
        self.usuarios = []

    @cached_property
    def contagem(self):
        return len(self.usuarios)

portal = Portal()
print(portal.contagem)    # ← 0 — e nunca mais atualiza se ganhar usuários!
# ← o certo: @property COMUM — recalculada a cada acesso (barata demais p/ cache)
# ← o certo: ou invalidar com del portal.contagem a cada mudança

# ← CUIDADO: decorator empilhado — cached_property DEVE ser o de CIMA
class Exemplo:
    @property                # ← ERRO na definição da classe!
    @cached_property         # ← (cached_property vira objeto, não descriptor)
    def valor(self):
        return 42
# ← TypeError: Cannot use cached_property instance without calling __set_name__
# ← o certo: @cached_property por cima de tudo; na dúvida, não empilhe
```

## Por que Python funciona assim?
`cached_property` é um descritor não-dados (implementa `__get__`, mas não `__set__`). Na primeira leitura, a resolução de atributos do Python encontra o descritor na CLASSE, executa a função e guarda o resultado em `self.__dict__['total']`. Nas leituras seguintes, o lookup checa PRIMEIRO o `__dict__` da instância — encontra o valor guardado e nem consulta a classe, então o descritor nunca roda de novo. Isso é a mesma mecânica que faz `atributo = x` no `__init__` sombrear métodos de classe. A invalidação com `del instancia.total` simplesmente remove a entrada do `__dict__`, devolvendo a vez ao descritor. E por isso, ao contrário de `lru_cache` (que é um cache GLOBAL por função, chaveado pelos argumentos), o `cached_property` é por instância: cada objeto guarda o seu próprio recibo.

## Conexões
- Você já usou esse padrão quando: `lru_cache` na Seção 2 — mesmo princípio de memoizar, só que lá o cache fica na FUNÇÃO (chave: argumentos) e aqui na INSTÂNCIA (chave: objeto)
- Aparece também em: Django (models com campos computados), frameworks web que calculam URLs/totais caros, `dataclass` do Python 3.13+ (parâmetro `slots=True` com cached_property requer cuidado especial)
- Diferente de: `@property` comum (recalcula SEMPRE), `lru_cache` (global e por argumentos, não por objeto), `@property` com variável `self._cache` manual (funciona, mas é 4 linhas onde cached_property é 1)

---

## Teste de recuperação — responda sem olhar para cima

1. Onde exatamente `cached_property` guarda o valor calculado e por que as leituras seguintes não rodam a função?
2. Escreva `Relatorio` com `@cached_property` `total` e mostre como forçar o recálculo.
3. Qual a diferença prática entre `cached_property` e `lru_cache` quanto a onde o cache vive?

---

**Frase-âncora:** A primeira pergunta é cara, as outras são grátis — o recibo fica no quadro de cada prédio; invalide o quadro quando os dados mudarem.
**Nível:** Avançado
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14