# venv e ambiente virtual — por que isolar tudo

## Quando você vai usar isso?
Sempre que você instalar QUALQUER pacote de terceiros (`pip install`, `uv add`)
ou abrir um projeto que não seja "só a biblioteca padrão". A partir do momento
em que o projeto tem dependências (Django, Selenium, PySide6, PyMySQL — as
seções 6 a 13 do curso), o ambiente virtual deixa de ser opcional e vira a
coisa mais importante para o seu código rodar igual em qualquer máquina.

## Modelo mental
O Python do sistema é uma "fábrica global": tudo o que você instala vai para o
mesmo depósito (`site-packages` global). O venv é um **container** (como uma
caixa fechada) que copia apenas o interpretador e cria um depósito PRÓPRIO de
pacotes dentro da pasta do projeto (`.venv`). O que está dentro da caixa não
afeta o resto da máquina, e o resto da máquina não afeta a caixa. Quando você
"ativa" o venv, o terminal passa a usar o Python E os pacotes da caixa.

## Em uma linha
O venv isola as dependências de cada projeto num `.venv` local, para projetos
diferentes poderem usar versões diferentes do mesmo pacote sem conflito.

## Na prática

### Como o `.venv` é criado (neste repositório)

```sh
# Python tradicional (o jeito "clássico"):
python -m venv .venv

# Com o uv (o jeito moderno — foi assim que fizemos aqui):
uv sync
```

O `uv sync` lê o `pyproject.toml` + `uv.lock`, cria o `.venv` se não existir e
instala tudo de uma vez. Ele reutilizou o `.venv` que já existia (não criou
outro), porque detectou que já estava configurado.

### O que existe DENTRO do `.venv` (estrutura no Windows)

```text
.venv/
├── pyvenv.cfg          ← "certidão de nascimento": aponta pro Python pai e a versão
├── Scripts/            ← executáveis (python.exe, pip.exe, Activate.ps1, ruff.exe...)
├── Lib/site-packages/  ← TODOS os pacotes instalados do projeto ficam AQUI
├── Include/            ← headers C (pouco usado em Windows puro)
└── Lib/                ← biblioteca padrão copiada
```

O `pyvenv.cfg` é o arquivo mais importante para entender "venv quebrado":

```ini
home = C:\Users\Administrador\AppData\Local\Programs\Python\Python314
include-system-site-packages = false
version = 3.14.7
executable = C:\Users\Administrador\AppData\Local\Programs\Python\Python314\python.exe
command = ... -m venv D:\...\CURSO PYTHON\.venv
```

- `home` / `executable` → caminho do Python ORIGINAL usado na criação
- `include-system-site-packages = false` → o venv NÃO enxerga pacotes globais
  (por isso "pip install sem ativar o venv" instala em outro lugar e "não acha")
- `version` → versão exata usada

### Ativar e desativar (Windows PowerShell)

```powershell
# Ativar:
.venv\Scripts\Activate.ps1
# Se der erro de permissão, rode antes (uma vez por máquina):
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Desativar:
deactivate
```

> Com `uv`, ativar é opcional: `uv run python app.py` já usa o `.venv` na hora.
> O VS Code também ativa automaticamente quando você abre o projeto.

## O que NÃO fazer

```sh
# ← ERRADO: instalar pacotes "no ar", sem venv ativo
pip install requests          # vai para o Python GLOBAL da máquina
# ← o certo: ativar o .venv antes (ou usar uv add / uv sync)

# ← ERRADO: copiar a pasta .venv de outro computador
# (o pyvenv.cfg grava caminhos ABSOLUTOS — na outra máquina eles não existem)
# ← foi exatamente o problema deste repositório: o .venv apontava para
#   C:\Users\Ariel Rosas\... que não existe nesta máquina → nada funcionava
# ← o certo: apagar o .venv e recriar na máquina nova (`uv sync` faz tudo)

# ← ERRADO: commitar o .venv no Git
# ← o certo: deixá-lo no .gitignore (já está) e documentar a recriação no README

# ← ERRADO: usar a mesma instalação global para vários projetos com requisitos conflitantes
# (projeto A quer Django 4, projeto B quer Django 5 — um quebra o outro)
# ← o certo: um .venv por projeto
```

## Por que Python funciona assim?
O Python resolve imports procurando pacotes em `sys.path` (uma lista de pastas
que inclui a pasta do script e o `site-packages`). O venv **injetou** o
`Lib/site-packages` DO PRÓPRIO `.venv` no começo dessa lista quando ativado —
por isso, com o venv ativo, `import requests` acha o pacote do projeto; sem
ativo, procura no site-packages global (e pode achar NADA, ou achar uma versão
errada). `include-system-site-packages = false` garante que o venv não "vaze"
pacotes do sistema para dentro do projeto, mantendo a caixa isolada de verdade.

## Conexões
- Você já usou esse padrão quando: rodou os gabaritos com `python -m doctest` —
  se o venv não estiver ativo e o código importar algo, dá ModuleNotFoundError
- Aparece também em: nota 02-uv (o uv gerencia o .venv por você), nota 03-pyproject
  (`[dependency-groups]` define o que entra no venv), nota 08-vscode
  (`python.defaultInterpreterPath` aponta para o .venv)
- Diferente de: instalação global (`pip install` no sistema), Docker (isola até
  o sistema operacional), virtualenv (ferramenta antiga equivalente ao venv)

---

## Teste de recuperação — responda sem olhar para cima

1. O que o `pyvenv.cfg` armazena e por que copiar a pasta `.venv` de outra máquina quebra?
2. O que `include-system-site-packages = false` significa na prática?
3. Qual a diferença entre `pip install` com o venv ativo e sem o venv ativo?

---

**Frase-âncora:** "O venv é a caixa do projeto: o Python de fora não entra, o de dentro não sai — e a caixa não se copia entre máquinas."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
