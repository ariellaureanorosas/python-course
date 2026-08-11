# @property, getter e setter

## Quando você vai usar isso?
Quando as pessoas que usam sua classe devem acessar dados como ATRIBUTO (`caneta.cor`) em vez de método (`caneta.cor()`), e principalmente quando você precisa CONTROLAR a entrada e a saída: validar cores permitidas, impedir idade negativa, recalcular um valor derivado sem chamar função. Também protege o código: se um dia o atributo interno mudar de nome, quem usa a classe nem percebe.

## Modelo mental
O atributo de verdade mora no quarto `_cor` (com underscore — é "interno"). O `@property` é a PORTEIRA: no getter ela anuncia quem sai (leitura); no setter ela CONFERE a identidade antes de deixar alguém entrar (escrita). Ninguém mais tem a chave do quarto — todo acesso passa pela porteira.

## Em uma linha
`@property` expõe um método como atributo de leitura (getter); `@setter` captura a escrita e permite validar antes de guardar; o atributo real fica em `_nome` (protected por convenção).

## Na prática

### Caso simples
```python
class Caneta:
    def __init__(self, cor, modelo):
        self._cor = cor          # ← interno, com underscore
        self._modelo = modelo

    @property
    def cor(self):               # ← getter: sem parênteses na chamada
        return self._cor

    @property
    def modelo(self):
        return self._modelo

caneta = Caneta('Azul', 'Bic')
print(caneta.cor)                # ← 'Azul' — parece atributo!
# caneta.cor = 'Vermelha'        # ← AttributeError: sem setter é leitura só
```

### Com variação
```python
CORES_VALIDAS = ('Azul', 'Vermelha', 'Preta')

class Caneta:
    def __init__(self, cor):
        self.cor = cor           # ← passa pelo setter (valida na criação!)

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, nova_cor):     # ← mesmo nome do getter, decorado com @cor
        if nova_cor not in CORES_VALIDAS:
            raise ValueError(f'Cor inválida: {nova_cor}')
        self._cor = nova_cor

caneta = Caneta('Azul')
caneta.cor = 'Vermelha'          # ← ok, validado
# caneta.cor = 'Roxa'            # ← ValueError: Cor inválida: Roxa
```

### Em uso real
```python
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade       # ← setter valida: idade' não aceita negativo

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError('Idade não pode ser negativa')
        self._idade = valor

    @property
    def maior_de_idade(self):    # ← valor DERIVADO sem método
        return self._idade >= 18

cliente = Cliente('Ana', 20)
print(cliente.maior_de_idade)    # ← True — calculado na hora, sempre atual
```

## O que NÃO fazer
```python
# ← ERRADO: getter e setter com o MESMO nome do atributo interno
@property
def cor(self):
    return self.cor              # ← RecursionError! self.cor chama o getter
# ← o certo: `return self._cor`

# ← ERRADO: setter que aceita qualquer coisa (aí nem precisa de setter)
@cor.setter
def cor(self, nova_cor):
    self._cor = nova_cor         # ← não valida nada — atributo público bastaria

# ← ERRADO: criar property sem necessidade real
@property
def nome(self):
    return self._nome            # ← atributo simples não precisa de porteira
# ← property é para CONTROLE: validação, cálculo, convenção interna
```

## Por que Python funciona assim?
`@property` é um descritor (decriptor protocol): por baixo, `cor = property(cor)` substitui o método por um objeto que intercepta leitura, escrita e deleção via `__get__`/`__set__`. Por isso as três são o MESMO atributo `cor` e o setter leva o nome do getter com `@cor.setter`. E a ordem em `@property @abstractmethod` importa (aula 152): o `@abstractmethod` precisa dizer que o DESCRITOR é abstrato, então ele fica por dentro.

## Conexões
- Você já usou esse padrão quando: acessou `str.upper` — na verdade um método embutido; o conceito de "atributo que calcula" também aparece em `len()` (protocolo)
- Aparece também em: dataclasses com `@property nome_completo`, Django `@property` em models, Pydantic (campos validados)
- Diferente de: `@classmethod` (fábrica), `@staticmethod` (função utilitária), atributo público simples (sem controle, direto no `__init__`)

---

## Teste de recuperação — responda sem olhar para cima

1. Por que o atributo interno ganha um underscore (`_cor`)?
2. Escreva uma classe `Conta` com `@property saldo` e um `@saldo.setter` que impede valor negativo.
3. O que acontece se o getter retorna `self.atributo` com o mesmo nome da property?

---

**Frase-âncora:** Property é a porteira do atributo: o quarto é `_cor`, o getter anuncia, o setter confere antes de deixar entrar.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14