# pyproject.toml — a "certidão de nascimento" do projeto

## Quando você vai usar isso?
Em todo projeto Python que é mais do que um script solto. O `pyproject.toml`
(leia-se "PEP 518 e PEP 621") é o lugar padrão onde o projeto se descreve:
nome, versão, dependências, e a configuração de TODAS as ferramentas de
desenvolvimento (Ruff, Pyright, Pytest, mypy, black, isort...). Ele substitui
a bagunça de arquivos soltos (`setup.py`, `requirements.txt`, `pytest.ini`,
`.ruff.toml`, `mypy.ini`...).

## Modelo mental
O `pyproject.toml` é a **escritura do imóvel**: identifica o dono (`[project]`),
lista quem mora dentro (`[dependency-groups]`) e contém o "manual do condomínio"
(`[tool.*]`) — as regras que cada ferramenta deve seguir. Todo mundo (o uv, o
Ruff, o Pyright, o Pytest, o VS Code) consulta a MESMA escritura; por isso a
configuração é consistente entre editor e terminal.

## Em uma linha
Um único arquivo TOML descreve o projeto e configura todas as ferramentas —
é o contrato que o uv, o Ruff, o Pyright e o Pytest obedecem.

## Na prática

### O arquivo DESTE repositório, seção por seção

```toml
# ============================
# Projeto
# ============================
[project]                      # ← identidade (PEP 621)
name = "curso-python"          # nome do projeto (usado pelo uv e pelo pip)
version = "0.0.1"              # versão (semântica: major.minor.patch)
description = "Estudos do curso Python 3 do Zero ao Avancado (Luiz Otavio Miranda)"
readme = "README.md"           # usado como "long description" em publicações
requires-python = ">=3.14"     # ← versão MÍNIMA exigida do interpretador
dependencies = ["python-dotenv>=1.2.0"]   # deps de produção (o código precisa delas)

[dependency-groups]            # ← grupos de dependências (uv)
dev = ["ruff", "pyright", "pytest", "pytest-xdist"]  # só ferramentas de dev
```

> `requires-python` é o que o uv usa para escolher/validar a versão do Python.
> A versão instalada nesta máquina (3.14.7) satisfaz `>=3.14`.
> **Consistência obrigatória:** o `[project].requires-python`, o
> `[tool.ruff].target-version` e o `[tool.pyright].pythonVersion` devem falar
> a mesma versão, senão ferramentas se contradizem.

### Configuração das ferramentas (`[tool.*]`)

```toml
# ============================
# Lint e formatação (Ruff)
# ============================
[tool.ruff]
line-length = 88                # ← limite de 88 colunas (padrão Black/PEP 8)
target-version = "py314"        # ← otimiza regras para Python 3.14
indent-width = 4                # ← 4 espaços de indentação
exclude = [".git", ".venv", "venv", "env", ".env", "node_modules", "__pycache__"]

[tool.ruff.lint]
select = [ "ASYNC", "A", "ANN", "B", "BLE", "C4", "C90", "COM", "E", ...]
ignore = ["T201", "COM812"]     # ← permite print() (curso) e ajusta vírgulas

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["ANN201", "S101"]   # testes não precisam de docstring/assert proibido

[tool.ruff.format]
quote-style = "double"          # ← aspas duplas no código formatado
indent-style = "space"          # ← indentação com espaços
line-ending = "lf"              # ← fim de linha Unix (LF)

# ============================
# Tipagem (Pyright)
# ============================
[tool.pyright]
typeCheckingMode = "strict"     # ← nível MÁXIMO de checagem de tipos
pythonVersion = "3.14"          # ← deve bater com requires-python
include = ["."]                 # analisa o projeto inteiro
exclude = [".git", ".venv", "**/venv", "**/env", "**/.env", "**/node_modules", ...]
venv = ".venv"                  # ← qual venv usar para resolver imports
venvPath = "."                  # ← onde está o venv

# ============================
# Testes (Pytest)
# ============================
[tool.pytest.ini_options]
addopts = "-s --color=yes --tb=short"   # mostra prints, cores, traceback curto
```

## O que NÃO fazer

```toml
# ← ERRADO: versões inconsistentes entre seções
requires-python = ">=3.12"
# [tool.ruff] target-version = "py314"   ← Ruff vai "exigir" sintaxe 3.14 num
#                                          projeto que roda 3.12 → erro confuso
# ← o certo: bater requires-python = ruff.target-version = pyright.pythonVersion

# ← ERRADO: dependência sem limite mínimo, sem intenção
dependencies = ["requests"]     # ← "qualquer versão" → comportamento imprevisível
# ← o certo: "requests>=2.31" (mínimo conhecido que funciona)

# ← ERRADO: espalhar config em arquivos soltos (pytest.ini + .ruff.toml + mypy.ini)
# ← o certo: tudo no pyproject.toml (um lugar só)

# ← ERRADO: colocar senha/token no pyproject.toml (é versionado!)
# ← o certo: variáveis de ambiente com python-dotenv (nota 07)
```

## Por que Python funciona assim?
Historicamente a configuração de projeto vivia em vários lugares:
`setup.py` (código executável, difícil de ler/validar), `setup.cfg`,
`requirements.txt` (sem estrutura), `pytest.ini`, `.flake8`... A PEP 518
(2016) padronizou que a config de build deve estar num arquivo TOML chamado
`pyproject.toml`, e a PEP 621 (2020) padronizou o formato do `[project]`.
TOML é declarativo (não roda código), legível e validável por máquina — o que
permite ao uv, ao Ruff e ao Pylance lerem o MESMO arquivo e se comportarem
coerentemente. `[dependency-groups]` é o formato do uv (2024) para separar
deps de dev sem precisar de pacote instalável — o professor usa o equivalente
`[project.optional-dependencies]` no ambiente dele.

## Conexões
- Você já usou esse padrão quando: o `pip install -r requirements.txt` dos
  READMEs antigos do curso — agora `uv sync` lê o pyproject e o lock
- Aparece também em: nota 02-uv (quem lê o pyproject e gera o uv.lock), nota
  04-ruff (as regras `[tool.ruff]`), nota 05-pyright (`[tool.pyright]`), nota
  06-pytest (`[tool.pytest]`), nota 07-dotenv (deps em `dependencies`)
- Diferente de: `setup.py` (imperativo, legado), `requirements.txt` (só lista,
  sem estrutura), `.env` (segredos, NUNCA no pyproject)

---

## Teste de recuperação — responda sem olhar para cima

1. Quais PEPs definem o `pyproject.toml` e o que cada uma padronizou?
2. Liste as seções do pyproject deste repositório e o papel de cada uma.
3. O que acontece se `requires-python`, `target-version` e `pythonVersion` forem diferentes?
4. Onde ficam as dependências de DEV e por que isso é melhor que requirements-dev.txt?

---

**Frase-âncora:** "Um arquivo, todas as regras: pyproject.toml é a escritura que uv, Ruff, Pyright e Pytest consultam."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
