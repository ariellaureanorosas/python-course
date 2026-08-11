# Exceções customizadas (herdando de Exception)

## Quando você vai usar isso?
Quando `ValueError` ou `TypeError` não dizem o suficiente — "Saldo insuficiente", "Cliente não encontrado", "Título duplicado" são ERROS DO SEU DOMÍNIO. Criar a própria exceção permite capturar por NOME (`except ClienteNaoEncontradoError`) e transportar dados extras (quanto faltou, qual id). Também é hora de praticar `raise ... from erro` para não perder o histórico.

## Modelo mental
O Python é o mensageiro de erros com uma bolsa: ao `raise`, ele prende o erro na bolsa e atira para cima até alguém pegar. Exceção customizada é uma bolsa ETIQUETADA do seu domínio — `except ClienteNaoEncontradoError` é o posto de coleta que só aceita bolsas com essa etiqueta. O `from` (encadeamento) é o recibo colado: mostra que essa bolsa veio de outra — `raise X from erro` anexa o erro ORIGINAL como "causa" (Exception.__cause__).

## Em uma linha
`class MinhaError(Exception)` cria exceção do seu domínio; `raise` dispara; `raise ... from erro` relança PRESERVANDO a origem; `except MinhaError` captura só o que você marcou.

## Na prática

### Caso simples
```python
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        super().__init__(f'Saldo insuficiente: R$ {saldo:.2f} (tentativa de R$ {valor:.2f})')
        # ← super().__init__ recebe a MENSAGEM; os dados ficam nos atributos

class Conta:
    def __init__(self, saldo=0.0):
        self._saldo = saldo

    def sacar(self, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)
        self._saldo -= valor
        return valor

conta = Conta(10.0)
try:
    conta.sacar(20.0)
except SaldoInsuficienteError as erro:
    print(erro)          # ← 'Saldo insuficiente: R$ 10.00 (tentativa de R$ 20.00)'
    print(erro.saldo)    # ← 10.0 — os dados viajaram junto!
```

### Com variação (relançar com contexto)
```python
def tentar_sacar(conta, valor):
    try:
        return conta.sacar(valor)
    except SaldoInsuficienteError as erro:
        raise RuntimeError('Falha no saque') from erro
        # ← o RuntimeError é a bolsa NOVA para a camada de cima,
        # ← o `from erro` cola a causa original na bagagem

# tentar_sacar(Conta(10.0), 20.0)
# ← RuntimeError: Falha no saque
# ← The above exception was the direct cause of the following exception:
# ←   SaldoInsuficienteError: Saldo insuficiente: ...
```

### Em uso real (hierarquia de erros)
```python
class CadastroError(Exception):           # ← base do domínio

class EmailDuplicadoError(CadastroError):
    def __init__(self, email):
        self.email = email
        super().__init__(f'E-mail já cadastrado: {email}')

class EmailInvalidoError(CadastroError):
    pass

usuarios = {'ana@email.com'}

def cadastrar(email):
    if '@' not in email:
        raise EmailInvalidoError(f'E-mail inválido: {email}')
    if email in usuarios:
        raise EmailDuplicadoError(email)
    usuarios.add(email)

try:
    cadastrar('ana@email.com')
except CadastroError as erro:     # ← captura QUALQUER erro do cadastro
    print(erro)                   # ← 'E-mail já cadastrado: ana@email.com'
```

## O que NÃO fazer
```python
# ← ERRADO: herdar de BaseException (ou de classes erradas)
class MeuErro(BaseException):     # ← BaseException pega KeyboardInterrupt, etc.
# ← o certo: herdar de Exception (ou de uma exceção do seu domínio)

# ← ERRADO: `except: pass` — engole o erro e o programa segue cego
try:
    conta.sacar(100.0)
except:                            # ← captura TUDO, sem informação
    pass
# ← o certo: except com o TIPO específico e ação (ou raise de novo)

# ← ERRADO: relançar sem `from` — perde a trilha de investigação
except SaldoInsuficienteError as erro:
    raise RuntimeError('Falha')   # ← sem from: a causa vira só __context__
# ← o certo: `raise RuntimeError('Falha') from erro`
```

## Por que Python funciona assim?
Exceções são objetos: `raise X` cria a instância, preenche `__traceback__` no caminho, e a cadeia de `except` compara por tipo (`except` com herança: captura a subclasse também — por isso capturar `CadastroError` pega `EmailDuplicadoError`). O encadeamento tem dois campos: `__cause__` (definida com `from`) e `__context__` (preenchida automaticamente quando o raise acontece DENTRO de um except). Ferramentas e logs — e o próprio interactive traceback — usam esses campos para mostrar a causa raiz com `raise ... from` explícito.

## Conexões
- Você já usou esse padrão quando: pegou `FileNotFoundError`/`json.JSONDecodeError` no gerenciador de tarefas — eram dos mesmos "mecanismos", agora você cria os seus
- Aparece também em: bibliotecas (pydantic `ValidationError`, SQLAlchemy `IntegrityError`), `add_note()` (Python 3.11) para anexar contexto extra
- Diferente de: `assert` (facilmente desligável com -O), `logging` (registrar sem interromper), retorno `None`/código de erro (silencioso e fácil de esquecer)

---

## Teste de recuperação — responda sem olhar para cima

1. Por que herdar de `Exception` e não de `BaseException`?
2. Escreva `ItemNaoEncontradoError` com campos extras e uma classe que a lança no `remover()`.
3. Qual a diferença entre `raise X` e `raise X from erro`?

---

**Frase-âncora:** Exceção customizada é a bolsa etiquetada do seu domínio: quem captura pelo nome, quem relança, cola o recibo com `from`.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14