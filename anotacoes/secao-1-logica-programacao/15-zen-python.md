# Zen of Python e Boas Práticas

## Quando você vai usar isso?
Antes de escrever qualquer linha — o Zen é o guardrail que guia decisões de design. Na prática, você aplica ao nomear variáveis, decidir entre duas soluções, revisar código alheio, ou configurar linters. PEP 8 é o que você usa todo dia sem pensar — igual cinto de segurança.

## Modelo mental
O Zen of Python é a constituição da linguagem: 19 artigos que definem o que é "pythônico". PEP 8 é o manual de padronização visual — como o uniforme de uma empresa: mesmas regras, mesma aparência, qualquer um entende.

## Em uma linha
19 princípios filosóficos (PEP 20) + guia de estilo (PEP 8) que priorizam legibilidade, simplicidade, e explicitude sobre esperteza ou brevidade.

## Na prática

### Caso simples

```python
# ← Explícito > Implícito: não esconda efeitos colaterais
def processar(dados):
    return sum(dados) / len(dados)   # ← função pura: só processa, não altera estado

# ← Simples > Complexo: linha reta vence desvio elegante
# Em vez de:
status = {True: "ativo", False: "inativo"}[ativo]   # ← engenhoso, mas ilegível
# ← Prefira:
status = "ativo" if ativo else "inativo"            # ← simples e direto

# ← Legibilidade conta: nomes descritivos > comentários
a = 10                              # ← o que é a?
taxa_desconto = 10 / 100           # ← claro: 10% de desconto
```

### Com variação

```python
# ← PEP 8: indentação, espaçamento, e nomes consistentes
def calcular_media(
    notas: list[float],
    peso: float = 1.0,
) -> float:                          # ← parênteses quebram se > 79 chars
    """Calcula média ponderada."""
    total = sum(notas) * peso
    return total / len(notas)


# ← 2 linhas em branco entre funções
TAXA_JUROS = 0.05                    # ← constantes em MAIUSCULAS

def nova_funcao():
    pass
```

### Em uso real

```python
from typing import Optional

# ← Type hints (use a partir de agora) + docstring + f-string
def buscar_usuario(user_id: int) -> Optional[dict]:
    """Retorna dados do usuário ou None se não encontrado."""
    try:
        dados = banco.query(f"SELECT * FROM usuarios WHERE id = {user_id}")
    except DatabaseConnectionError:    # ← exceção específica, nunca except:
        logger.error("Banco indisponível")
        return None
    except QueryError:
        logger.error(f"Usuário {user_id} não encontrado")
        return None

    return {
        "nome": dados["nome"],
        "email": f"{dados['nome'].lower()}@empresa.com",
    }
```

## O que NÃO fazer

```python
# ← ERRADO: except: sem tipo — captura TUDO, inclusive erros inesperados
try:
    resultado = 10 / 0
except:                               # ← também captura Ctrl+C, MemoryError...
    pass                               # ← "erros nunca devem passar silenciosamente"

# ← ERRADO: nomes de uma letra (exceto i, j em loops)
def calc(a, b, c):                    # ← o que significa a? b? c?
    return a * b - c

# ← ERRADO: linha ultrapassando 79 caracteres
x = funcao_muito_longa(arg1, arg2, arg3, arg4, arg5, arg6, arg7)  # ← ilegível

# ← ERRADO: comentário explicando o óbvio
x = x + 1   # ← incrementa x em 1
# ← Comente o "por que", não o "o que" — o código já mostra o que faz
```

## Por que Python funciona assim?
`import this` exibe o PEP 20 gravado como Easter egg no bytecode do Python — são princípios, não regras, mas moldaram cada decisão de design da linguagem. PEP 8 é opcional (diferente de Go com `gofmt`), mas a comunidade segue por convenção — código que viola PEP 8 é tecnicamente válido, mas vai gerar estranhamento em revisões. Type hints (`: int`, `-> dict`) são ignorados pelo interpretador em runtime — servem apenas para tools (mypy, pyright) e IDEs, como documentação executável. "Erros nunca devem passar silenciosamente" se reflete na obrigatoriedade de tratar exceções — não existe `checked exception` como em Java, mas a cultura de `try/except` específico é forte.

## Conexões
- Você já usou esse padrão quando: escreveu `if usuario is not None:` em vez de `if usuario:` (explícito beats implícito)
- Aparece também em: linters (ruff, flake8, pylint), formatadores (black, autopep8), revisão de código, CI/CD
- Diferente de: PEP 8 vs. Zen — PEP 8 diz *como* (4 espaços, 79 chars), Zen diz *por que* (legibilidade conta, simples é melhor que complexo)

---

## Teste de recuperação — responda sem olhar para cima

1. Cite três princípios do Zen of Python e dê um exemplo concreto de cada.
2. Escreva uma função com type hints, docstring, f-string, e que trata uma exceção específica (não `except:`).
3. Qual a diferença de propósito entre PEP 8 e o Zen of Python?

---

**Frase-âncora:** "Código legível é código de qualidade — Python foi projetado para isso."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
