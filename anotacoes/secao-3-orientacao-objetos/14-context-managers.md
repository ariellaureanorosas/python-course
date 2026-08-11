# Context managers — with, __enter__, __exit__

## Quando você vai usar isso?
Quando um recurso precisa entrar e SAIR com garantia — fechar arquivo, liberar conexão, finalizar medição — mesmo que o código no meio exploda com um erro. O `with` é a forma de dizer "abre, usa, e FECHA NA HORA QUE SAIR — aconteça o que acontecer". Você já usou com `open()`; agora você implementa o seu próprio contexto com `__enter__`/`__exit__` ou com `@contextmanager`.

## Modelo mental
É o contrato da piscina: ao entrar, entregam a toalha (`__enter__`); aconteça o que acontecer lá dentro (nadou, escorregou, chorou — até exceção), ao sair você devolve a toalha (`__exit__`) — o salva-vidas (Python) garante que o `__exit__` roda SEMPRE, com erro ou sem. Duck typing manda: se um objeto tem `__enter__` e `__exit__`, ele é um context manager — não importa a classe.

## Em uma linha
`with X() as recurso:` chama `X.__enter__()` na entrada e `X.__exit__()` na saída (mesmo com exceção); `@contextmanager` faz a mesma coisa com uma função geradora usando `yield` e `try/finally`.

## Na prática

### Caso simples
```python
class MeuArquivo:
    def __init__(self, caminho, modo='r'):
        self.caminho = caminho
        self.modo = modo
        self.arquivo = None

    def __enter__(self):                  # ← roda na entrada do with
        self.arquivo = open(self.caminho, self.modo, encoding='utf-8')
        return self                       # ← o `as` recebe este retorno

    def __exit__(self, exc_type, exc_val, exc_tb):
        # ← roda SEMPRE na saída — com erro ou sem
        if self.arquivo is not None:
            self.arquivo.close()
        return False                      # ← False = não engolir exceções

    def ler(self):
        return self.arquivo.read()

with MeuArquivo('nota.txt') as arquivo:
    print(arquivo.ler())                  # ← arquivo aberto, e fechado depois
```

### Com variação (os parâmetros do __exit__)
```python
class ContextoControlado:
    def __enter__(self):
        print('entrando')                 # ← 'entrando'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'saindo; erro? {exc_type.__name__ if exc_type else "nenhum"}')
        return False                      # ← não suprime o erro

with ContextoControlado() as ctx:
    print('dentro')                       # ← 'dentro'
# ← 'saindo; erro? nenhum'

# ← com erro no meio do bloco:
# with ContextoControlado() as ctx:
#     raise ValueError('ops')
# ← 'saindo; erro? ValueError' e o erro continua subindo
```

### Em uso real (função geradora — aula 160)
```python
from contextlib import contextmanager

@contextmanager
def abrir_arquivo(caminho, modo='r'):
    arquivo = open(caminho, modo, encoding='utf-8')
    try:
        yield arquivo                      # ← o with recebe o arquivo
    finally:
        arquivo.close()                    # ← SEMPRE fecha

with abrir_arquivo('nota.txt') as arquivo:
    print(arquivo.read())
```

## O que NÃO fazer
```python
# ← ERRADO: abrir arquivo sem with (ou esquecer o close no erro)
arquivo = open('dados.txt', encoding='utf-8')
dados = arquivo.read()
# ← se der erro entre o open e o close, o arquivo vaza (resource leak)
# ← o certo: with open(...) as arquivo: (ou o seu context manager)

# ← ERRADO: __exit__ que retorna True "de brincadeira" — engole erros
def __exit__(self, exc_type, exc_val, exc_tb):
    print('finalizando')
    return True          # ← falso! exceção do bloco some silenciosamente
# ← o certo: return False salvo decisão EXPLÍCITA de suprimir

# ← ERRADO: esquecer o try/finally no @contextmanager
@contextmanager
def abrir(caminho):
    arquivo = open(caminho, 'r')
    yield arquivo          # ← sem try/finally: erro no bloco pula o close!
```

## Por que Python funciona assim?
O `with` desenrola para um `try/finally` invisível: `entrada = obj.__enter__()`, o bloco roda, e no `finally` o `__exit__(exc_type, exc_val, exc_tb)` é chamado — com os três dados da exceção se houver (None, None, None se não). Se `__exit__` retorna True, Python engole a exceção; se False, ela continua subindo. O `as` recebe exatamente o retorno do `__enter__` — por isso `with open(...) as f` entrega o arquivo. Duck typing garante a mágica: não há interface obrigatória herdada, basta ter os dois métodos.

## Conexões
- Você já usou esse padrão quando: `with open(...) as arquivo`, `with sqlite3.connect(...) as conexao`, testes com `with pytest.raises(...)`
- Aparece também em: fechamento automático em libs (semáforos, locks), `contextlib.suppress`, `ExitStack` para múltiplos recursos
- Diferente de: `try/finally` puro (mais verboso e fácil de esquecer), `@decorator` (envolve chamadas de função, não blocos), GC do Python (não garante timing — o with garante)

---

## Teste de recuperação — responda sem olhar para cima

1. Quais métodos um objeto precisa para funcionar com `with`?
2. Escreva um `@contextmanager` que mede e imprime o tempo de um bloco.
3. O que significa o `return True` no `__exit__` — e quando é razoável?

---

**Frase-âncora:** Entrega a toalha ao entrar, devolve SEMPRE ao sair — com erro ou sem: isso é o `with`.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14