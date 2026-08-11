# Pyright / Pylance — tipagem estática em modo strict

## Quando você vai usar isso?
Sempre que quiser saber ANTES de rodar se o código está com tipos errados
(ex.: passar `str` onde se espera `int`). O Pyright é o "type checker"
(verificador de tipos) que roda por linha de comando; o Pylance é a extensão
do VS Code que usa o MESMO motor do Pyright para sublinhar erros enquanto
você digita. Este repositório configura os dois pelo `[tool.pyright]` do
`pyproject.toml`, no nível **strict** — o mais exigente que existe.

## Modelo mental
O Python é "dinâmico": variáveis podem mudar de tipo no meio do caminho, e o
erro só aparece na hora de rodar. O Pyright é um **espectador onisciente**: ele
lê o código inteiro e "simula" mentalmente a execução, rastreando que tipo
cada expressão TEM, e aponta quando você mistura tipos incompatíveis. O `strict`
é como aumentar o zoom do espectador: ele também reclama quando algo é "do tipo
errado mas não dá pra saber qual" (tipo desconhecido), obrigando o código a ser
explícito.

## Em uma linha
Pyright verifica os types hints do código SEM executá-lo; em modo strict ele
exige que cada parâmetro, retorno e variável tenha tipo conhecido — o Pylance
mostra isso ao vivo no VS Code.

## Na prática

### Rodando

```sh
uv run pyright                    # analisa o projeto todo (lê o pyproject)
uv run pyright arquivo.py         # analisa um arquivo
uv run pyright --stats            # estatísticas dos arquivos analisados
```

### O que o modo strict pega (exemplo real deste repositório)

O `gabarito-09-decorator-log.py` (anotação de decorators) dispara erros strict
porque o código do curso não tem os type hints "genéricos" de decorador:

```
error: Type annotation is missing for parameter "func" (reportMissingParameterType)
error: Return type, "_Wrapped[..., Unknown, ...]", is partially unknown (reportUnknownParameterType)
```

Isso é **intencional**: o ambiente do professor usa strict para que cada erro
deles vire uma lição de "o que um sênior escreveria aqui". Os gabaritos
antigos não passam — os novos exercícios devem passar (type hints, docstrings,
PEP 8). É o "modo difícil" ligado de propósito.

### Níveis de checagem

| Nível | O que permite |
|:------|:--------------|
| `off` | nada (só sintaxe) |
| `basic` | erros óbvios (ex.: `int` onde era `str`) |
| `standard` | erros médios + avisos de estilo de tipos |
| `strict` | tudo acima + reclama de tipo `Unknown` (nunca "chuta") |

### A config DESTE projeto

```toml
[tool.pyright]
typeCheckingMode = "strict"   # ← nível máximo
pythonVersion = "3.14"        # ← deve bater com o .python-version e o Ruff
include = ["."]               # analisa o projeto inteiro
exclude = [".git", ".venv", "**/venv", "**/env", "**/.env", "**/node_modules",
           "**/__pycache__", "**/.mypy_cache", "**/.ruff_cache", "**/.pytest_cache"]
venv = ".venv"                # resolve imports usando o venv do projeto
venvPath = "."                # o venv está na raiz do projeto
```

> `venv`/`venvPath`: o Pyright precisa saber ONDE estão os pacotes instalados
> (para não marcar `import requests` como erro). Apontando para o `.venv`, ele
> resolve imports de terceiros corretamente.

## O que NÃO fazer

```python
# ← ERRADO: ignorar o erro de tipo "porque funciona"
def soma(a, b):        # ← strict: ANN201 — falta type hint
    return a + b       # ← se a for str e b int, quebra em runtime

# ← ERRADO: usar `Any` como fuga de tudo
def f(x: Any) -> Any:  # ← desliga a checagem inteira nessa função
# ← o certo: tipar de verdade; Any só como último recurso documentado

# ← ERRADO: desligar o strict porque o curso não ensina type hints ainda
# (é justamente o contrário: ele te ensina na prática, erro por erro)

# ← ERRADO: dois "chefes" do tipo (pyright e mypy ativos ao mesmo tempo)
# (o settings.json deste repo tem config de mypy-type-checker, mas a extensão
#  não está nas recomendações — o padrão aqui é Pyright/Pylance para evitar
#  diagnóstico duplicado)
```

## Por que Python funciona assim?
Python é fortemente tipado em RUNTIME (não converte `str` + `int` silenciosamente)
mas dinâmico em COMPILE-TIME (o interpretador não verifica tipos antes de
executar). Os type hints (`def f(x: int) -> str`) são uma convenção (PEP 484)
que o interpretador IGNORA — servem para ferramentas e humanos. O Pyright usa
essas anotações para fazer **inferência de tipos**: rastreia o fluxo do código
e deriva o tipo de cada expressão, mesmo sem anotação explícita. No modo
strict, a regra de ouro é: **"se eu não consigo provar o tipo, isso é um erro"**
— porque código com tipo desconhecido é onde bugs de produção nascem.

## Conexões
- Você já usou esse padrão quando: viu o sublinhado vermelho no VS Code em
  tempo real — é o Pylance (mesmo motor do Pyright)
- Aparece também em: nota 03-pyproject (config `[tool.pyright]`), nota
  04-ruff (Ruff cuida de estilo/bugs; Pyright cuida de tipos — juntos cobrem
  o que um code review de sênior faria), nota 08-vscode
  (`python.analysis.typeCheckingMode: strict` no settings.json)
- Diferente de: Ruff (não analisa tipos), pytest (executa código e testa
  comportamento), Mypy (verificador de tipos alternativo, mais lento, config
  separada)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre Pyright e Pylance?
2. O que o modo `strict` exige além do modo `standard`?
3. Por que `venv` e `venvPath` estão configurados no `[tool.pyright]`?
4. Por que type hints não alteram o comportamento do código em runtime?

---

**Frase-âncora:** "Pyright é o espectador que sabe o tipo de tudo antes de rodar — e strict é ele se recusando a chutar."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
