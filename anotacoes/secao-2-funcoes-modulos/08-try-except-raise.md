# Tratamento de Erros (try / except / raise)

## Quando você vai usar isso?
Seu programa vai abrir um arquivo que pode não existir, dividir por zero ou receber entrada inválida do usuário. Em vez de quebrar com traceback feio, você captura o erro e decide o que fazer — tentar de novo, usar valor padrão ou avisar o usuário.

## Modelo mental
É um paraquedas: você espera que o avião funcione (try), mas se algo der errado o paraquedas abre (except). O else abre se o pouso foi perfeito. O finally é o seguro de vida — pague sempre, aconteça o que acontecer.

## Em uma linha
Try tenta executar, except captura erro específico, else roda se deu certo, finally roda sempre — controle de fluxo para falhas.

## Na prática

### Caso simples
```python
# ← Proteger divisão que pode falhar
try:
    resultado = 10 / 0           # ← ZeroDivisionError acontece aqui
except ZeroDivisionError:        # ← captura só esse erro específico
    print("Divisão por zero")    # ← executa se o erro ocorreu
```

### Com variação
```python
# ← Múltiplos excepts + else + finally
try:
    valor = int(input("Digite um número: "))  # ← pode lançar ValueError
    resultado = 10 / valor                     # ← pode lançar ZeroDivisionError
except ValueError:                             # ← captura entrada não numérica
    print("Isso não é um número")
except ZeroDivisionError:                      # ← captura divisão por zero
    print("Não pode dividir por zero")
else:                                          # ← só roda se NENHUM except entrou
    print(f"Resultado: {resultado}")
finally:                                       # ← roda SEMPRE, erro ou não
    print("Fim da tentativa")
```

### Em uso real
```python
# ← Validar argumentos com raise + tratar quem chama
def dividir(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a deve ser int ou float")
    if b == 0:
        raise ZeroDivisionError("Divisão por zero")
    return a / b

try:
    print(dividir(10, "abc"))
except TypeError as e:                          # ← as e: captura mensagem
    print(f"Erro de tipo: {e}")
except ZeroDivisionError as e:
    print(f"Erro matemático: {e}")
```

## O que NÃO fazer
```python
# ← ERRADO: except sem tipo — captura TUDO, inclusive Ctrl+C
try:
    resultado = 10 / 0
except:                      # ← equivalente a except BaseException:
    pass                     # ← silencia até erro de digitação interno

# ← ERRADO: silenciar erro sem tratar
try:
    arquivo = open("dados.txt")
except FileNotFoundError:
    pass                     # ← programa continua como se nada tivesse acontecido

# ← ERRADO: except genérico que esconde bugs
try:
    import modulo_inexistente
except Exception:            # ← captura tudo, esconde ImportError
    pass                     # ← você nunca vai saber que o módulo não existe

# ← O erro real: except: pass é a forma mais segura de criar bugs impossíveis de debugar
```

## Por que Python funciona assim?
Python usa exceções como objetos — tudo herda de `BaseException`. Quando `raise` é executado, a pilha de chamadas (call stack) é percorrida até achar um `except` compatível (match por tipo com `isinstance`). Se não acha, o interpretador imprime o traceback e morre. O `finally` é garantido porque o interpretador usa um bloco `try/finally` interno de baixo nível (C) que executa mesmo com `return`, `break` ou exceção no meio. `else` existe para separar o código que pode falhar do código que só deve executar se tudo deu certo — evita colocar código no `try` que não deveria ser protegido.

## Conexões
- Você já usou esse padrão quando: viu `with open(...)` — context managers usam try/finally por baixo
- Aparece também em: `assert` lança `AssertionError`, bibliotecas como `requests` lançam exceções HTTP
- Diferente de: `if/else` para validação — try é para situações excepcionais, não para controle de fluxo previsível

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a ordem de execução de try/except/else/finally quando NÃO ocorre erro?
2. Escreva uma função que recebe uma lista e um índice, retorna o elemento ou `None` se o índice não existir.
3. Qual a diferença entre `except:`, `except Exception:` e `except ZeroDivisionError:`?

---

**Frase-âncora:** Try protege, except captura, else confirma, finally garante — sempre.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
