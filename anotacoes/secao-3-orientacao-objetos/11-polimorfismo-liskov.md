# Polimorfismo e o princípio de Liskov

## Quando você vai usar isso?
Quando o seu código aceita UMA classe base (Notificacao, Pagamento, FormaDeEnvio) e precisa funcionar com TODAS as subclasses sem saber qual é — hoje é e-mail, amanhã SMS, depois WhatsApp. Essa é a essência de sistemas que crescem: a função não muda, as implementações é que aparecem.

## Modelo mental
Polimorfismo é o controle remoto universal: você aponta para a TV e digita o número do canal — não importa se é Samsung ou LG, o botão chamado "canal" funciona em todas, cada uma responde do seu jeito por baixo. Liskov é a garantia da troca: se um Samsung cabe no suporte da parede, QUALQUER TV com o mesmo encaixe também cabe — você pode trocar a marca sem remover o suporte. Se uma TV vier com o encaixe diferente (violou o contrato), a parede quebra.

## Em uma linha
Polimorfismo: mesma assinatura de método, comportamentos diferentes por subclasse; Liskov: qualquer subclasse pode SUBSTITUIR a base sem quebrar quem a usa.

## Na prática

### Caso simples
```python
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self):          # ← a mesma ASSINATURA para todas
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f'Enviando e-mail: {self.mensagem}')
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print(f'Enviando SMS: {self.mensagem}')
        return True
```

### Com variação (a função que não muda)
```python
def notificar(notificacao):
    """Funciona com QUALQUER subclasse de Notificacao (Liskov)."""
    return notificacao.enviar()   # ← só usa o contrato

notificar(NotificacaoEmail('Olá!'))   # ← 'Enviando e-mail: Olá!'
notificar(NotificacaoSMS('Promoção')) # ← 'Enviando SMS: Promoção'
# ← amanhã cria NotificacaoPush: notificar() continua igual!
```

### Em uso real (LOOP sem condicionais)
```python
notificacoes = [
    NotificacaoEmail('Bem-vindo'),
    NotificacaoSMS('Código: 1234'),
    NotificacaoEmail('Promoção'),
]

for notificacao in notificacoes:
    notificacao.enviar()
# ← NENHUM if type(...) — o polimorfismo substitui os condicionais
```

## O que NÃO fazer
```python
# ← ERRADO: "descobrir o tipo" para decidir — quebra o polimorfismo
def notificar(notificacao):
    if type(notificacao) is NotificacaoEmail:
        return notificacao.enviar_email()      # ← acoplado ao tipo!
    elif type(notificacao) is NotificacaoSMS:
        return notificacao.enviar_sms()
# ← o certo: contrato único enviar() e deixar cada um se virar

# ← ERRADO: subclasse que muda a ASSINATURA (viola Liskov)
class NotificacaoWhatsApp(Notificacao):
    def enviar(self, numero):      # ← parâmetro extra = contrato quebrado
        ...
# ← quem chamava enviar() agora dá TypeError; a base prometia enviar()

# ← ERRADO: subclasse que retorna coisa totalmente diferente do prometido
def enviar(self):
    return 'erro qualquer'         # ← o contrato diz bool; devolve str
# ← Liskov: subclasses devem manter o CONTRATO (assinatura + sentido)
```

## Por que Python funciona assim?
Python é duck typing: não checa herança na chamada — o que importa é que o objeto TEM o método `enviar()` com a assinatura esperada. Por isso o `ABC` aqui é importante: ele DOCUMENTA o contrato e adianta o erro (TypeError na criação), compensando a falta de checagem estática. Liskov entra porque funções como `notificar()` confiam no contrato: se uma subclasse muda a assinatura ou o significado, o bug aparece longe, no chamador — exatamente onde é mais difícil de achar.

## Conexões
- Você já usou esse padrão quando: chamou `len(x)` — funciona com str, list, dict, set (todos implementam `__len__`)
- Aparece também em: `collections.abc`, context managers (qualquer objeto com `__enter__`/`__exit__` — aula 158), `__add__`/`__gt__` (cada tipo soma do seu jeito — aula 156)
- Diferente de: solução feita de condicionais (if por tipo), sobrecarga de métodos (Python não tem overload — mesma classe não repete nome com assinaturas diferentes), composição ("tem um" que também entrega contratos)

---

## Teste de recuperação — responda sem olhar para cima

1. O que é assinatura de método e por que o polimorfismo depende dela?
2. Escreva `Figura(ABC)` com `area()` e duas figuras; use num loop que soma as áreas sem `if`.
3. O que uma subclasse pode quebrar se retornar um tipo diferente do prometido pela base?

---

**Frase-âncora:** O contrato é único, a assinatura é a mesma, o comportamento é de cada um — e quem usa nem sabe com quem está falando.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14