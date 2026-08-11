# Classes abstratas (ABC) e @abstractmethod

## Quando você vai usar isso?
Quando várias classes têm O MESMO método, mas cada uma implementa do seu jeito — Notificacao envia e-mail ou SMS, Pagamento processa cartão ou Pix — você cria a classe base que diz O QUE fazer (o contrato) e deixa cada filha dizer COMO. O ABC garante pela linguagem que ninguém esqueça de implementar: tentar instanciar uma classe com método abstrato pendente dá TypeError.

## Modelo mental
ABC é o contrato de trabalho: o formulário diz "todo funcionário entrega relatório semanal" sem dizer como escrever. Se você contratar (instanciar) alguém que não aceitou o formulário, o RH (Python) barra na porta — TypeError. O `@abstractmethod` é a cláusula do contrato que todo mundo é obrigado a assinar antes de ser contratado.

## Em uma linha
Classe que herda de `ABC` e marca métodos com `@abstractmethod` vira um contrato: não pode ser instanciada, e cada subclasse precisa implementar todos os métodos abstratos — senão ela também fica abstrata e não instancia.

## Na prática

### Caso simples
```python
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self):      # ← contrato: todo pagamento processa
        ...                   # ← Ellipsis = "a subclasse decide"

class PagamentoCartao(Pagamento):
    def processar(self):
        return 'Pagamento com cartão processado'

class PagamentoPix(Pagamento):
    def processar(self):
        return 'Pagamento via Pix processado'

print(PagamentoCartao().processar())   # ← 'Pagamento com cartão processado'
print(PagamentoPix().processar())      # ← 'Pagamento via Pix processado'
```

### Com variação (esquecer implementação)
```python
class PagamentoBoleto(Pagamento):
    pass                    # ← não implementou processar()

# pagamento = PagamentoBoleto()
# ← TypeError: Can't instantiate abstract class PagamentoBoleto
# ← with abstract method processar
```

### Em uso real (property abstrata)
```python
from abc import ABC, abstractmethod

class Produto(ABC):
    @property                 # ← PROPERTY preciso... POR FORA
    @abstractmethod           # ← ...e ABSTRACT por DENTRO (ordem!)
    def preco(self):
        """Preço do produto (propriedade abstrata)."""

class Frutas(Produto):
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):          # ← implementa a property concreta
        return self._preco

print(Frutas(4.5).preco)      # ← 4.5
# ← sem a implementação: TypeError na criação, mesma regra
```

## O que NÃO fazer
```python
# ← ERRADO: instanciar uma classe abstrata
pagamento = Pagamento()   # ← TypeError — contrato sem assinatura
# ← o certo: sempre instanciar uma SUBCLASSE que implementou tudo

# ← ERRADO: ABC só para "fazer bonito", sem método abstrato
class Base(ABC):
    def util(self):        # ← nenhum @abstractmethod: é classe normal
        pass

# ← o certo: ABC tem utilidade quando há CONTRATO a exigir

# ← ERRADO: subclasse que esquece UM método abstrato
class Pix(Pagamento):
    pass                   # ← vira abstrata sem querer! TypeError na criação
# ← o erro só aparece na INSTANCIAÇÃO (TypeError) — e não na definição
```

## Por que Python funciona assim?
`ABC` configura `__abstractmethods__` via metaclasse: qualquer método marcado com `@abstractmethod` entra nessa tupla. No momento de instanciar, `type.__call__` verifica `__abstractmethods__` — se não estiver vazio, levanta TypeError. Subclasses que implementam os métodos removem os nomes da tupla (a própria herança mergeia isso). Como a verificação é na criação, o erro é cedo, na hora do `Classe()`, e não no meio da execução de um método que não existe.

## Conexões
- Você já usou esse padrão quando: viu `class MinhaException(Exception)` — Exception é "abstração" de erro sem implementação exigida
- Aparece também em: `collections.abc` (Mapping, Iterable), `typing.Protocol`, Django/SQLAlchemy abstract models
- Diferente de: herança comum (sem obrigação), mixin (habilidade, não contrato — aula 149), Protocol (duck typing: contrato por ESTRUTURA, sem exigir herança)

---

## Teste de recuperação — responda sem olhar para cima

1. O que acontece ao instanciar uma classe com `@abstractmethod` não implementado?
2. Escreva `Animal(ABC)` com `fazer_som()` abstrato e `Gato(Animal)` implementando.
3. Qual a ordem correta dos decorators em uma property abstrata e por quê?

---

**Frase-âncora:** Só se me ama quem assina o contrato: `@abstractmethod` assina, quem não assina não entra (TypeError na porta).
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14