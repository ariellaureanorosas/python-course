# Ruff — lint e formatação em uma ferramenta só

## Quando você vai usar isso?
Sempre que for escrever código Python. O Ruff roda em dois modos: **lint**
(analisa e aponta erros de estilo, bugs prováveis e más práticas) e **format**
(reformata o código automaticamente no padrão Black/PEP 8). Ele substitui as
ferramentas antigas (flake8 + black + isort + pyupgrade + bandit...) em um
binário único, escrito em Rust, ~10 a 100x mais rápido. É o que o professor
usa e o que este repositório configura no `pyproject.toml`.

## Modelo mental
O Ruff é o **revisor de código que nunca cansa**: você escreve, ele aponta
"aqui falta type hint", "aqui tem import não usado", "aqui o `except` está
largo demais". O `ruff format` é o **diagramador**: reorganiza espaçamento,
quebras de linha e aspas sem mudar UMA vírgula de lógica. Lint = o que está
errado; format = como ficará bonito. Ele não executa o código — analisa a
sintaxe e a estrutura (análise estática), por isso é instantâneo.

## Em uma linha
Ruff é o linter + formatador do projeto: aponta problemas (lint) e padroniza
o estilo (format) em milissegundos, com regras configuráveis no pyproject.

## Na prática

### Comandos

```sh
uv run ruff check .            # analisa todo o projeto (só reporta)
uv run ruff check arquivo.py   # analisa um arquivo
uv run ruff check --fix .      # CORRIGE automaticamente o que for seguro
uv run ruff check --statistics # resumo dos erros por código
uv run ruff format .           # formata todo o projeto
uv run ruff format --check .   # só mostra o que mudaria (CI)
```

### O que ele aponta (principais códigos deste projeto)

| Código | Regra | Exemplo do que pega |
|:------:|:------|:--------------------|
| `F` | pyflakes | import não usado, variável não definida |
| `E` / `W` | PEP 8 | linha longa demais, espaços em excesso |
| `I` | isort | imports fora de ordem |
| `ANN` | type hints | função sem anotação de parâmetro/retorno |
| `B` | bugs prováveis | lista mutável como parâmetro default |
| `UP` | pyupgrade | sintaxe antiga → moderna (ex.: `str.format` → f-string) |
| `SIM` | simplificações | `if x: return True else: return False` → `return x` |
| `S` | segurança (bandit) | `eval()`, senha hardcoded, `subprocess` com shell |
| `C4` | comprehensions | `[i for i in ...]` quando `list(...)` basta |
| `N` | nomes | variável em snake_case, classe em PascalCase |
| `RUF` | regras próprias do Ruff | códigos ambíguos (unicode), etc. |
| `TD` / `FIX` | TODOs | TODO sem autor, FIXME esquecido |
| `ERA` | código comentado | bloco de código desligado com `#` |
| `EM` | exceções | `raise ValueError("msg")` sem contexto |
| `TRY` | try/except | `except Exception` largo demais |

### A configuração DESTE projeto (resumo)

- `line-length = 88` — quebra de linha em 88 caracteres (padrão Black)
- `target-version = "py314"` — considera sintaxe/regras do Python 3.14
- `ignore = ["T201", "COM812"]` — **T201**: permite `print()` (os exercícios do
  curso usam muito); **COM812**: regra de vírgula que conflita com o formatter
- `per-file-ignores` — em `tests/**/*.py`, dispensa anotação de retorno
  (`ANN201`) e libera `assert` (`S101`), comum em testes
- No VS Code (settings.json): Ruff é o formatador padrão do Python e roda
  `fixAll` + `organizeImports` ao salvar

## O que NÃO fazer

```python
# ← ERRADO: "lint é frescura, o código funciona"
# (o lint pega bugs de verdade: F405 usa variável que não existe em escopo...)

# ← ERRADO: rodar `ruff check --fix` e commitar sem revisar o diff
# (fix é seguro por definição, mas SEMPRE revise o que mudou)

# ← ERRADO: ignorar o Ruff "porque ele reclama de tudo no curso"
# (as regras do professor são propositais: ANN te força a tipar como um sênior;
#  T201 já foi ignorado de propósito para não brigar com o curso)

# ← ERRADO: desligar formatação automática no VS Code
# (o padrão do professor é formatar no salvar — código sempre padronizado)
```

> **Nota importante:** este repositório herdou a config do professor SEM o
> `fix = true` automático. Um `ruff check` aqui só reporta; o `--fix` é
> explícito. O VS Code ainda aplica correções seguras no salvar (configurado
> no settings.json). Nunca rode `uv run ruff check --fix .` sem antes
> `git diff` para ver o que será alterado.

## Por que Python funciona assim?
Python não tem compilador que valide o código em tempo de compilação — ele
aceita muita coisa que só quebra em runtime. O lint preenche esse vazio:
analisa a AST (árvore sintática) sem executar, aplicando centenas de regras
de "bom senso coletivo" da comunidade. Cada código de regra é rastreável (a
documentação oficial explica o porquê). O formatter, por sua vez, elimina a
guerra de estilo: a máquina decide a formatação, o humano decide a lógica —
o que encurta code reviews e diffs.

## Conexões
- Você já usou esse padrão quando: viu o VS Code sublinhando código
  amarelo/laranja — é o Pylance + Ruff trabalhando juntos
- Aparece também em: nota 03-pyproject (config `[tool.ruff]`), nota
  08-vscode (extensão Ruff + codeActionsOnSave), nota 05-pyright (o Pyright
  cuida de TIPOS; o Ruff cuida de ESTILO e bugs — se complementam)
- Diferente de: pyright/mypy (analisam TIPOS), pytest (EXECUTA testes),
  black/isort/flake8 (ferramentas antigas que o Ruff unifica)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `ruff check` e `ruff format`?
2. Cite 3 códigos de regra e o que cada um pega.
3. Por que `T201` está em `ignore` neste projeto?
4. O que o `--fix` faz e por que revisar o diff antes de commitar?

---

**Frase-âncora:** "Lint aponta o erro, format apaga a discussão — e nenhum dos dois executa seu código."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
