# Ambiente de Desenvolvimento — Índice

Notas sobre as adições feitas ao ambiente deste repositório (padrão do curso
"Python 3 do Zero ao Avançado", Luiz Otávio Miranda) — o "ambiente de sênior".

| # | Nota | Assunto principal |
|:-:|:-----|:------------------|
| 01 | [01-venv-ambiente-virtual.md](01-venv-ambiente-virtual.md) | `venv`, `.venv`, por que isolar, o problema do venv "quebrado" |
| 02 | [02-uv-gerenciador-dependencias.md](02-uv-gerenciador-dependencias.md) | O que é o `uv`, como instalar, comandos do dia a dia, `uv.lock` |
| 03 | [03-pyproject-toml.md](03-pyproject-toml.md) | Anatomia do `pyproject.toml`: `[project]`, `[dependency-groups]`, `[tool.*]` |
| 04 | [04-ruff-lint-formatacao.md](04-ruff-lint-formatacao.md) | Ruff: lint + formatação, regras selecionadas, comandos, integração VS Code |
| 05 | [05-pyright-tipagem-estatica.md](05-pyright-tipagem-estatica.md) | Pyright/Pylance: type hints, modo strict, config no projeto |
| 06 | [06-pytest-doctest.md](06-pytest-doctest.md) | Pytest, pytest-xdist e `doctest` (validação dos gabaritos) |
| 07 | [07-dotenv-variaveis-ambiente.md](07-dotenv-variaveis-ambiente.md) | `python-dotenv`, `.env` vs `.env-example`, segredos fora do Git |
| 08 | [08-vscode-configuracao.md](08-vscode-configuracao.md) | `.vscode/`: settings.json, extensions.json, launch.json |

> **Guia de Git:** o `git-guia/` (pasta irmã desta) reúne os guias de Git:
> `guia-rapido.md`, `guia-fluxo-trabalho.md`, `guia-mensagens-commit.md`,
> `guia-criar-repositorio-github.md`, `erros-comuns-e-solucoes.md` e
> `glossario-git.md`.

---

## Como este ambiente foi montado

```
CURSO PYTHON/
├── .vscode/            ← preferências do editor (tema, fonte, debug, Ruff, Pylance)
├── .env-example        ← modelo das variáveis de ambiente (copie para .env)
├── .gitignore          ← o que NÃO vai para o Git (.env, .venv, caches)
├── .python-version     ← versão exata do Python usada no projeto (3.14.7)
├── pyproject.toml      ← "contrato" do projeto: deps + config de Ruff/Pyright/Pytest
├── uv.lock             ← versões exatas congeladas de todas as dependências
└── .venv/              ← ambiente virtual (NÃO versionado — recriado com `uv sync`)
```

**Fluxo de uso resumido:**

```sh
uv sync                 # cria/atualiza o .venv e instala tudo (deps + dev)
uv run python app.py    # roda qualquer script usando o .venv
uv run ruff check .     # lint
uv run ruff format .    # formatação automática
uv run pyright          # checagem de tipos
uv run pytest           # testes
```

> **Dica de estudo:** ao ler cada nota, faça o teste de recuperação no final
> SEM olhar o conteúdo (o padrão deste repositório).

---

**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
