# Herança e super()

## Quando você vai usar isso?
Quando você tem classes que são variações de outra — Carro É UM Veiculo, Cachorro É UM Animal, ContaPoupanca É UMA Conta — e quer compartilhar o que é comum (atributos e métodos) sem duplicar código. A subclasse herda, adiciona e pode SOBREPOR (override) comportamentos.

## Modelo mental
Herança é família: o filho Carro nasce com as características do pai Veiculo (marca, modelo, mover()) e ganha as suas (portas, cavalos). `super()` é o "chame o papai": quando o filho precisa do comportamento inicial do pai antes de fazer a parte dele — `super().__init__(...)` chama o construtor do pai para não repetir `self.marca = marca`. O override é o filho que diz "eu faço diferente": `mover()` do carro se apoia no do pai com `super().mover()` e acrescenta "sobre 4 rodas".

## Em uma linha
`class Filho(Pai)` herda tudo do pai; `super()` acessa o pai dentro da subclasse (para `__init__` e para base do override); override redefine um método com o MESMO nome e assinatura.

## Na prática

### Caso simples
```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        return 'O veículo está se movendo'

class Carro(Veiculo):                    # ← entre parênteses: o pai
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)  # ← NÃO repita a linha do pai
        self.portas = portas

carro = Carro('Fiat', 'Uno', 4)
print(carro.marca)      # ← 'Fiat'  (herdado)
print(carro.portas)     # ← 4      (próprio)
```

### Com variação (override com super())
```python
class Veiculo:
    def mover(self):
        return 'O veículo está se movendo'

class Carro(Veiculo):
    def mover(self):                     # ← override: mesmo nome
        return f'{super().mover()} sobre 4 rodas'   # ← base + detalhe

class Moto(Veiculo):
    def mover(self):
        return f'{super().mover()} sobre 2 rodas'

print(Carro('A', 'B').mover())   # ← 'O veículo está se movendo sobre 4 rodas'
print(Moto('A', 'B').mover())    # ← 'O veículo está se movendo sobre 2 rodas'
```

### Em uso real
```python
class Conta:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0.0

    def depositar(self, valor):
        self._saldo += valor
        return self._saldo

class ContaPoupanca(Conta):
    def __init__(self, titular, rendimento):
        super().__init__(titular)        # ← herda o básico
        self.rendimento = rendimento

    def render(self):
        self._saldo *= (1 + self.rendimento)
        return self._saldo

conta = ContaPoupanca('Ana', 0.01)
conta.depositar(100.0)
print(conta.render())   # ← 101.0 — reutilizou depositar e _saldo do pai
```

## O que NÃO fazer
```python
# ← ERRADO: esquecer super().__init__ — os atributos do pai nem existem
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        self.portas = portas            # ← self.marca NUNCA foi criado!
# ← AttributeError: 'Carro' object has no attribute 'marca'

# ← ERRADO: copiar o __init__ do pai no filho
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        self.marca = marca              # ← duplicação: se o pai mudar,
        self.modelo = modelo            # ← o filho fica desatualizado
        self.portas = portas

# ← CUIDADO: herdar por "preguiça" — se é só para reusar um método,
# ← composição ou mixin costumam ser mais limpos que herança
```

## Por que Python funciona assim?
`super()` não é "a classe pai" — é um proxy que resolve a ordem de resolução (MRO, aula 149) a partir do `self` real. Numa herança simples ele sobe direto ao pai, mas em herança múltipla ele decide pela ordem `__mro__`. E o override funciona porque Python busca métodos na hora da CHAMADA: `carro.mover()` procura na classe de `carro` primeiro (Carro) e só depois no pai — é isso que permite ao filho interceptar a chamada e ao `super().mover()` seguir a busca de onde parou.

## Conexões
- Você já usou esse padrão quando: `class MeuError(Exception)` (aula 154), `class Cliente(Pessoa)` no sistema bancário (aula 171)
- Aparece também em: ABC (classes abstratas que herdam de ABC — aula 151), Django `models.Model`, `unittest.TestCase` (o TestCase é a base do seu teste)
- Diferente de: composição ("tem um" em vez de "é um"), herança múltipla (vários pais — próxima nota), interface/ABC (contrato sem implementação)

---

## Teste de recuperação — responda sem olhar para cima

1. O que acontece se a subclasse não chama `super().__init__()` e usa atributos do pai?
2. Escreva `Animal` com `fazer_som()` e `Cachorro(Animal)` com override usando `super()` no retorno.
3. Como o `override` funciona por baixo quando você chama `objeto.metodo()`?

---

**Frase-âncora:** Filho herda do pai o que serve, `super()` chama o pai na hora certa, e o override deixa o filho ser diferente.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14