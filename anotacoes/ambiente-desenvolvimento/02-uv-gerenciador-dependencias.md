# uv — o gerenciador de projetos Python (Astral)

## Quando você vai usar isso?
No dia a dia de TODO projeto Python moderno: criar o venv, instalar pacotes,
rodar scripts, atualizar versões, congelar dependências. O uv substitui (em
uma ferramenta só, escrita em Rust) o conjunto pip + venv + virtualenv +
pip-tools + pipx + poetry + pyenv. É o padrão que o professor Luiz Otávio
Miranda usa no ambiente `ambiente_python_2025` e a recomendação da indústria
em 2025+.

## Modelo mental
O pip é um "entregador" que traz pacotes um a um na ordem que pedem. O uv é um
"gerente de logística": baixa em paralelo, resolve conflitos de versão de forma
inteligente (como resolveria um quebra-cabeça completo, não peça por peça) e
guarda a "foto final" do quebrado no `uv.lock`. Por isso é 10 a 100x mais
rápido: ele não reinstala o que já está certo e usa cache global em vez de
baixar tudo de novo.

## Em uma linha
O uv gerencia o Python, o venv e as dependências do projeto em um comando só —
com resolução de verdade, lockfile e velocidade de Rust.

## Na prática

### Como foi instalado nesta máquina (Windows)

```powershell
# Comando oficial de instalação (sem admin):
iwr https://astral.sh/uv/install.ps1 -useb | iex

# Instalou em: C:\Users\Administrador\.local\bin\uv.exe
# (se "uv" não for reconhecido: reabra o terminal — o PATH é atualizado no login)
```

### Comandos essenciais

```sh
uv sync                    # cria .venv + instala tudo (deps e dev) + gera uv.lock
uv add requests            # instala E registra no pyproject.toml
uv add --dev ruff          # instala como dependência de DEV
uv remove requests         # desinstala e remove do pyproject
uv run python app.py       # roda usando o .venv (sem precisar ativar)
uv run ruff check .        # roda qualquer ferramenta instalada no venv
uv run pytest              # testes
uv lock                    # atualiza o uv.lock sem instalar
uv lock --check            # verifica se o lock está atualizado
uv pip list                # lista pacotes instalados no .venv (como o pip)
uv python install 3.12     # instala outra versão do Python (substitui o pyenv)
uv python list             # lista versões disponíveis
uv tool install ruff       # instala ferramenta GLOBAL (como pipx)
uv tree                    # árvore de dependências
```

### O que aconteceu neste repositório

1. O `pyproject.toml` ganhou `[project]` (nome, versão, `requires-python`) e
   `[dependency-groups] dev` (ruff, pyright, pytest, pytest-xdist)
2. `uv sync` detectou o `.venv` existente, verificou os 13 pacotes já
   instalados (todos compatíveis) e **não reinstalou nada** — só gerou o `uv.lock`
3. `uv lock --check` confirmou: `Resolved 14 packages` sem erros
4. `requirements.txt` e `requirements-dev.txt` foram REMOVIDOS — o
   `pyproject.toml` + `uv.lock` agora são a fonte única de verdade

### `uv.lock` — por que ele existe

```sh
# O uv.lock congela as versões EXATAS (incluindo transitivas)
# ex.: "ruff==0.16.2", "pytest==9.1.1", "colorama==0.4.6" ...
```

- **`pyproject.toml`** diz as regras: "quero `ruff`, `pytest>=8`"
- **`uv.lock`** diz a verdade: "vou usar exatamente `ruff==0.16.2`, `pytest==9.1.1`"
- Em outra máquina (ou daqui a 2 anos), `uv sync` reproduz o ambiente IDÊNTICO
- Por isso o `uv.lock` é **versionado no Git** (igual ao professor faz)

### `[dependency-groups]` vs `requirements-*.txt`

| | `requirements.txt` (antigo) | `[dependency-groups]` (uv) |
|---|---|---|
| Onde fica | arquivo solto | dentro do `pyproject.toml` |
| Tipos | um arquivo por conjunto | `dev`, `test`, `docs`... no mesmo lugar |
| Lockfile | não tem | `uv.lock` cobre tudo |
| Instalação | `pip install -r ...` | `uv sync` (tudo de uma vez) |
| `uv add` | não sabe dele | atualiza o grupo automaticamente |

## O que NÃO fazer

```sh
# ← ERRADO: misturar pip e uv no mesmo projeto
pip install requests          # o uv não sabe disso → uv.lock fica desatualizado
# ← o certo: sempre uv add / uv sync

# ← ERRADO: editar o uv.lock na mão
# ← o certo: deixar o uv gerar (uv add / uv lock)

# ← ERRADO: dar `uv sync --no-dev` em produção se o código precisa de pytest
# (comum: rodar testes no CI sem grupo dev — decidir conscientemente)

# ← ERRADO: commitar o .venv "do jeito que está" achando que o lock basta
# (o lock garante reprodutibilidade; o .venv continua ignorado pelo Git)
```

## Por que Python funciona assim?
Historicamente o Python tinha `pip` (instala) e `venv` (isola) como peças
separadas, sem lockfile nativo (o `requirements.txt` não congela transitivas a
menos que você gere na mão). O uv unificou isso e trouxe resolução determinística:
ele resolve o GRAFO completo de dependências (o que cada pacote exige, incluindo
conflitos), calcula as versões compatíveis e grava no lock. É o mesmo modelo do
Rust (Cargo), do Node (npm/pnpm) e do Go — a indústria convergiu para
"arquivo de regras + arquivo de versões exatas".

## Conexões
- Você já usou esse padrão quando: rodou `python -m venv .venv` no curso —
  o uv faz o mesmo internamente, só que mais rápido e com resolução de conflitos
- Aparece também em: nota 01-venv (o uv cria e gerencia o .venv), nota
  03-pyproject (`[project]` e `[dependency-groups]` são lidos por ele), nota
  08-vscode (o VS Code usa o venv que o uv gerencia)
- Diferente de: pip (só instala, sem lock), poetry (faz o mesmo papel, mais
  lento e com conceito de lock diferente), pyenv (só gerencia VERSÕES do
  Python — o uv também faz isso via `uv python install`)

---

## Teste de recuperação — responda sem olhar para cima

1. Quais ferramentas o uv substitui e qual o papel do `uv.lock`?
2. Por que o `uv.lock` deve ser versionado no Git?
3. Como você adiciona uma dependência nova com o uv, e o que isso muda no pyproject?
4. `uv run python app.py` vs ativar o venv manualmente — qual a diferença prática?

---

**Frase-âncora:** "pip traz pacotes; uv gerencia o projeto — e o lockfile é a foto exata de como o ambiente deve ser."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
