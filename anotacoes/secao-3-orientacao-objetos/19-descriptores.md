# Descritores (o protocolo por trás de @property)

## Quando você vai usar isso?
Quando uma regra de atributo se repete em MUITOS campos da classe (validar que é inteiro positivo, que é texto não vazio, logar toda leitura/escrita, converter valor ao guardar) e você não quer copiar um getter/setter para cada campo. O descritor é a máquina de comportamento REUTILIZÁVEL: você define UMA vez como um atributo se comporta (`__get__`, `__set__`, `__delete__`, `__set_name__`) e aplica em dezenas de campos só declarando o descritor na classe. Você já usa descritores todo dia sem saber: `@property`, `@classmethod` e `@staticmethod` SÃO descritores prontos do Python.

## Modelo mental
Pense no atributo como um corredor de portas. Atributo comum: porta sempre aberta — qualquer um entra e sai (o `__dict__` da instância). Property: uma ÚNICA porta com vigia fixo. Descritor: uma AGÊNCIA de vigias — você contrata um modelo de vigia (a classe do descritor) e coloca o MESMO vigia em várias portas diferentes (vários atributos da classe). Cada porta continua normal para o resto do sistema, mas toda passagem (ler, escrever, apagar) passa pelo vigia e é conferida.

## Em uma linha
Um descritor é uma classe com `__get__`/`__set__`/`__delete__` que, declarada como atributo de outra classe, passa a interceptar o acesso a esse atributo — é o mecanismo que faz `@property`, `classmethod` e `staticmethod` funcionarem.

## Na prática

### Caso simples (descritor Campo que valida tipo)
```python
class Campo:
    """Vigia reutilizável: exige o tipo certo em qualquer atributo."""

    def __init__(self, tipo):
        self.tipo = tipo
        self.nome = ''                  # ← preenchido pelo __set_name__

    def __set_name__(self, dono, nome):
        self.nome = nome                # ← Python avisa: atributo='idade'

    def __set__(self, instancia, valor):
        if not isinstance(valor, self.tipo):
            raise TypeError(
                f'{self.nome} espera {self.tipo.__name__}, '
                f'recebeu {type(valor).__name__}'
            )
        instancia._dados[self.nome] = valor   # ← guarda na instância

    def __get__(self, instancia, dono=None):
        if instancia is None:
            return self                 # ← acesso pela CLASSE: devolve o vigia
        return instancia._dados[self.nome]

class Pessoa:
    nome = Campo(str)      # ← mesmo modelo de vigia, portas diferentes
    idade = Campo(int)

    def __init__(self, nome, idade):
        self._dados = {}   # ← dicionário privado DESTA instância
        self.nome = nome   # ← passa pelo vigia Campo.__set__
        self.idade = idade

p = Pessoa('Ana', 30)
print(p.nome, p.idade)     # ← Ana 30
# p.idade = 'trinta'       # ← TypeError: idade espera int, recebeu str
```

### Com variação (data vs non-data descriptor)
```python
class SomenteLeitura:
    """NON-data descriptor: intercepta só a LEITURA (sem __set__)."""

    def __get__(self, instancia, dono=None):
        return 'valor fixo'

class A:
    x = SomenteLeitura()

a = A()
print(a.x)                 # ← 'valor fixo'
a.x = 'outro'              # ← FUNCIONA: sem __set__, o __dict__ vence
print(a.x)                 # ← 'outro' — instância sobrepõe non-data descriptor

# Compare com Campo (DATA descriptor, tem __set__): p.idade = 5 NUNCA
# escreve direto no dict — SEMPRE passa pelo __set__.
# Enumeração: DATA se tiver __set__ (ou __delete__); NON-DATA só __get__.
```

### Em uso real (property/classmethod/staticmethod são descritores)
```python
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property                              # ← property() é UM DESCRITOR
    def fahrenheit(self):                  # ← gerencia _celsius na leitura
        return self._celsius * 9 / 5 + 32

    @classmethod                           # ← classmethod() é descritor
    def da_kelvin(cls, kelvin):            # ← __get__ devolve método preso a cls
        return cls(kelvin - 273.15)

print(Temperatura(0).fahrenheit)               # ← 32.0
print(Temperatura.da_kelvin(300).fahrenheit)   # ← 80.6
print(hasattr(Temperatura.fahrenheit, '__get__'))  # ← True — é descritor!
# del t.fahrenheit   # ← se property não define __delete__, vira AttributeError

# # Se Campo tivesse __delete__, `del p.nome` passaria pelo vigia também:
# def __delete__(self, instancia):
#     del instancia._dados[self.nome]
```

## O que NÃO fazer
```python
# ← ERRADO: descritor NON-DATA para VALIDAÇÃO — o __set__ não existe,
#            então a escrita NUNCA passa pelo vigia
class Campo:
    def __get__(self, instancia, dono=None):
        return instancia._dados[self.nome]
# p.idade = 'x'        # ← vai direto para o __dict__, validação ignorada
# ← o certo: para controlar ESCRITA precisa de __set__ (data descriptor)

# ← ERRADO: guardar o valor no próprio descritor — é COMPARTILHADO
class Campo:
    def __set__(self, instancia, valor):
        self.valor = valor    # ← UMA variável para TODAS as instâncias!
# ← o certo: guardar na instância (instancia.__dict__[nome] ou _dados)

# ← ERRADO: "fixar" o nome na mão — quebra ao renomear o atributo
self.nome = 'idade'           # ← se virar 'anos', o descritor segue errado
# ← o certo: deixar o hook __set_name__ preencher pelo nome real da classe

# ← CUIDADO: com DATA descriptor, `self.idade = ...` DENTRO do __init__
# também passa pelo __set__ — inclusive se for antes de _dados existir:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome          # ← corre por __set__ ANTES de _dados = {}
# ← o certo: inicializar _dados ANTES de qualquer atributo com descritor
```

## Por que Python funciona assim?
Quando uma classe é definida, o `__build_class__` percorre o corpo e, para cada atributo que implementa o protocolo de descritor (`__get__`, `__set__`, `__delete__`), chama `__set_name__(classe, nome)`. Depois, todo acesso a atributo segue a ORDEM da busca do CPython: (1) data descriptors na classe ancestral; (2) `__dict__` da instância; (3) non-data descriptors/atributos da classe. Por isso `Campo` (com `__set__`) vence o dicionário da instância e `SomenteLeitura` (sem `__set__`) perde para ele. `@property` é um descritor escrito em C: guarda `fget`/`fset`/`fdel` e dispara o método certo em `__get__`/`__set__`/`__delete__`. `@classmethod` também é um descritor — seu `__get__` devolve uma função que injeta `cls` em vez de `self`.

## Conexões
- Você já usou esse padrão quando: usou `@property` (é exatamente um descritor), `@classmethod`/`@staticmethod` (descritores que desviam a função), e configurou `models.CharField(max_length=50)` no Django (configuração guardada em descritores internos)
- Aparece também em: Django ORM e SQLAlchemy (cada atributo de model vira um "atributo instrumentado" que rastreia leitura/escrita e conversão), Pydantic (campo validado é descritor), `functools.cached_property`, e os próprios `__slots__` (cada slot é um `member_descriptor`)
- Diferente de: `__getattr__`/`__setattr__` (interceptam TODA a classe indiscriminadamente — descritor é por atributo), metaclasse (age na CRIAÇÃO da classe, não no acesso a atributos), `@property` (um único vigia fixo; o descritor é o mesmo serviço, mas reutilizável em N campos)

---

## Teste de recuperação — responda sem olhar para cima

1. Quais são os métodos do protocolo de descritor e o que cada um intercepta?
2. O que muda entre um data descriptor e um non-data descriptor? (Quem ganha a disputa com o `__dict__` da instância?)
3. Quando o Python chama `__set_name__` e qual problema ele resolve?

---

**Frase-âncora:** Descritor é a agência de vigias: o comportamento de atributo é contratado uma vez, na classe do descritor, e vendido em portas diferentes — `@property` é o vigia de fábrica.
**Nível:** Avançado
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14