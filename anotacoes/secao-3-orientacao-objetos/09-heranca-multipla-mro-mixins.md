# Herança múltipla, MRO e mixins

## Quando você vai usar isso?
Quando uma classe precisa somar comportamentos de fontes diferentes: um Smartphone É UM Eletronico E também precisa de logging (Mixin). O padrão saudável é usar um pai "principal" + vários mixins (classes pequenas que entregam UMA habilidade cada) — e sempre conferir o MRO (Method Resolution Order) para saber quem ganha quando dois pais definem a mesma coisa.

## Modelo mental
A classe é uma reunião de câmeras de segurança: o MRO é o gabarito de QUAL funcionário olha a fita primeiro quando acontece um evento. `Smartphone(Eletronico, LogFileMixin)` define a ordem: primeiro o próprio Smartphone, depois Eletronico, depois LogFileMixin, depois Log, depois object. O mixin é o "funcionário de habilidade única": um que só imprime, um que só grava arquivo — cada um faz UMA coisa bem feita.

## Em uma linha
Herança múltipla joga vários pais na classe; o MRO (`Classe.mro()`) decide a ordem de busca de métodos; mixins são classes pequenas de habilidade única, a forma segura de usar herança múltipla.

## Na prática

### Caso simples
```python
class Log:
    def _log(self, mensagem):
        raise NotImplementedError('Implemente o _log')   # ← contrato

    def log(self, mensagem):
        self._log(mensagem)          # ← padrão Template Method

class LogPrintMixin(Log):
    def _log(self, mensagem):
        print(mensagem)              # ← habilidade única: imprimir

class LogFileMixin(Log):
    def _log(self, mensagem):
        with open('log.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{mensagem}\n')   # ← habilidade única: arquivo

LogPrintMixin().log('Olá!')          # ← imprime
LogFileMixin().log('Salvar')         # ← grava em arquivo
```

### Com variação (pai principal + mixin)
```python
class Eletronico:
    def __init__(self, nome):
        self.nome = nome

class Smartphone(Eletronico, LogFileMixin):   # ← pai + mixin
    def __init__(self, nome, caminho_arquivo='log.txt'):
        super().__init__(nome)                # ← chama Eletronico
        LogFileMixin.__init__(self, caminho_arquivo)  # ← chama o mixin direto

    def ligar(self):
        mensagem = f'Smartphone {self.nome} ligado'
        self.log(mensagem)                    # ← habilidade herdada do mixin
        return mensagem

print(Smartphone('Galaxy').ligar())           # ← grava e retorna a mensagem
```

### Em uso real (consultando o MRO)
```python
class A:
    def falar(self):
        return 'A'

class B(A):
    def falar(self):
        return f'B-{super().falar()}'

class C(B):
    def falar(self):
        return f'C-{super().falar()}'

print(C().falar())                # ← 'C-B-A' — a corrente sobe o MRO
print(C.mro())                    # ← [C, B, A, object] — ordem canônica
print(C.__mro__)                  # ← a mesma ordem em atributo
# ← mro() é a ferramenta para prever qual pai vence em empate
```

## O que NÃO fazer
```python
# ← ERRADO: dois pais "principais" mexendo no mesmo atributo
class A:
    def __init__(self):
        self.x = 1

class B:
    def __init__(self):
        self.x = 2

class C(A, B):
    def __init__(self):
        A.__init__(self)      # ← seta x = 1
        B.__init__(self)      # ← SOBRESCREVE x = 2 — qual valeu??
# ← o certo: um pai principal + mixins que não têm estado conflitante

# ← ERRADO: presumir que super() sempre chama o "pai direto lexical"
class Filho(Eletronico, LogFileMixin): ...
# ← super() resolve pela ordem da instância (MRO de Filho),
# ← não pela classe onde a linha está escrita

# ← CUIDADO: mixin com `__init__` obrigatório surpreende no MRO
# ← o certo: mixins sem estado próprio, ou com __init__ opcional,
# ← chamado explicitamente (LogFileMixin.__init__(self, caminho))
```

## Por que Python funciona assim?
O MRO é calculado pelo algoritmo C3 linearization: a ordem respeita (1) a subclasse antes da superclasse, (2) a ordem dos pais na declaração e (3) é monotônica — se C herda A e B, e B herda D, a ordem é C, B?? não: C, A?? — na prática: linearização única que nunca inverte a ordem direta dos pais. Por isso `class Classe(Pai1, Pai2)` busca primeiro em Pai1 e depois em Pai2, e `super()` continua a busca de onde a própria classe parou no MRO — o que permite correntes como C → B → A funcionarem de forma consistente.

## Conexões
- Você já usou esse padrão quando: viu `LogPrintMixin`/`LogFileMixin` no projeto da aula 150, `str` herda de `Sequence`
- Aparece também em: bibliotecas Python (mixins em `django.contrib.auth.mixins`, `threading.Thread` sem mixins mas com protocolos), classes `collections.abc`
- Diferente de: herança simples (um pai — aula 148), ABC (contrato com método abstrato — aula 151), composição (reuso por "tem um" em vez de "é um")

---

## Teste de recuperação — responda sem olhar para cima

1. Como o MRO decide qual método de qual pai vence quando os dois definem a mesma coisa?
2. Escreva um `MixinGrega` que adiciona `saudar()` a qualquer classe da forma mais simples possível.
3. Por que mixins geralmente não devem ter `__init__` obrigatório?

---

**Frase-âncora:** MRO é a ordem da fila: o próprio, os pais na ordem da lista, o object por último; mixin é o parceiro de uma habilidade só.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14