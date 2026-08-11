# python-dotenv — variáveis de ambiente e segredos fora do Git

## Quando você vai usar isso?
Sempre que o projeto precisar de dados que não devem (e não podem) ir para o
Git: senha de banco, chave de API, token, URL de ambiente. Nos próximos
módulos do curso (Django, MySQL, Selenium), isso vira regra. O `python-dotenv`
carrega um arquivo `.env` local (invisível ao Git) para as variáveis de
ambiente do processo, e o `.env-example` (versionado) mostra QUAIS variáveis
existem sem revelar valores.

## Modelo mental
O `.env` é o **cofre da casa**: fica guardado só na sua máquina, nunca vai para
o repositório. O `.env-example` é o **letreiro da porta**: diz "aqui dentro
existe uma chave chamada GREETINGS" sem mostrar o conteúdo. O código lê
`somente os nomes` via `os.getenv()`. Assim, o mesmo código funciona em sua
máquina, no GitHub e num servidor — cada lugar fornece seus próprios segredos.

## Em uma linha
`.env` guarda segredos locais (ignorado pelo Git); `python-dotenv` os carrega
para o código; `.env-example` documenta os nomes sem os valores.

## Na prática

### O `.env-example` deste repositório

```text
# Copie este arquivo para '.env' e ajuste os valores.
GREETINGS='dotenv is working fine'
```

> Para ativar: copie para `.env` (o `.gitignore` já ignora `.env`):
> ```powershell
> Copy-Item .env-example .env
> ```

### Usando no código

```python
import os
from dotenv import load_dotenv

load_dotenv()                    # lê o arquivo .env da pasta atual
print(os.getenv("GREETINGS"))    # "dotenv is working fine"

# Convenções:
# - variável não existente → os.getenv retorna None
# - valor padrão: os.getenv("CHAVE", "fallback")
```

### Verificação rápida (testamos no terminal)

```sh
uv run python -c "from dotenv import load_dotenv; import os; load_dotenv('.env-example'); print(os.getenv('GREETINGS'))"
# → dotenv is working fine
```

### Como fica no Git

```text
# Versionado (compartilhado):
.env-example          # ← só os NOMES das variáveis
.gitignore            # ← .env ignorado

# Nunca versionado (local):
.env                  # ← valores reais (segredos)
```

## O que NÃO fazer

```sh
# ← ERRADO: commitar o .env com segredos reais
git add .env          # ← senha de banco vai para o histórico do GitHub (irreversível!)
# ← o certo: .env no .gitignore, .env-example no repositório

# ← ERRADO: hardcodar segredo no código
senha = "minhasenha123"          # ← vaza no Git e no diff de qualquer commit
# ← o certo: os.getenv("SENHA")

# ← ERRADO: `load_dotenv()` em produção em servidor sem .env
# (falha silenciosa: variável vira None e o erro aparece longe)
# ← o certo: validar no startup (raise se faltar) ou deixar o servidor
#   injetar variáveis de ambiente reais (Docker, CI, etc.)

# ← ERRADO: colocar segredo no pyproject.toml ou README
# (tudo que está versionado é público para quem tem acesso ao repo)
```

## Por que Python funciona assim?
Processos têm um ambiente de variáveis (o `os.environ`): nomes → valores que
o sistema operacional repassa. O `python-dotenv` apenas lê o arquivo `.env`
(linhas `CHAVE=valor`, ignorando comentários e aspas) e injeta no `os.environ`
antes do código rodar. O segredo NUNCA fica no código-fonte nem no repositório
— cada ambiente (sua máquina, dev, staging, produção) fornece o seu `.env`.
É o mesmo padrão dos `.env` do Node.js/Next.js, do Docker Compose e dos CI
(GitHub Actions, GitLab CI) — ferramenta independente de linguagem.

## Conexões
- Você já usou esse padrão quando: o ambiente do professor tinha
  `python-dotenv` como dependência e o `.env-example` com a mensagem de teste
- Aparece também em: nota 01-venv (dependência instalada no `.venv`), nota
  03-pyproject (`dependencies = ["python-dotenv>=1.2.0"]`), nota 08-vscode
  (`envFile` no launch.json — o debugger carrega o .env automaticamente)
- Diferente de: variáveis do Windows (`setx` — global, persiste), Docker env
  (`-e`), config em arquivo Python (fica versionado), `.env` do Node (mesma
  ideia, sintaxe própria)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `.env` e `.env-example` e por que um é versionado?
2. O que `load_dotenv()` faz e o que `os.getenv("X")` retorna se X não existir?
3. Por que não devemos commitar o `.env`?
4. Como o debugger do VS Code carrega o `.env` (veja a nota 08)?

---

**Frase-âncora:** "O código pergunta, o ambiente responde: nomes no exemplo, valores no cofre — e o Git só vê o letreiro."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
