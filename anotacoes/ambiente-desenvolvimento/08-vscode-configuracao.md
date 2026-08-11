# VS Code — configuração do editor para Python sênior

## Quando você vai usar isso?
Sempre que abrir este projeto no VS Code. A pasta `.vscode/` do repositório
contém a configuração que faz o editor "saber" tudo sobre o projeto: qual
Python usar, como formatar, quais extensões instalar, como depurar, como rodar
testes. Como é versionada no Git, qualquer pessoa (ou você, em outra máquina)
abre o projeto e o editor já está pronto — as preferências viajam com o código.

## Modelo mental
O `.vscode/` é o **painel de controle do avião**: o piloto (você) vê o mesmo
painel em qualquer aeroporto (máquina), porque o avião (projeto) carrega as
configurações junto. Três arquivos, três funções: `settings.json` (o que o
editor faz), `extensions.json` (quais ferramentas instalar), `launch.json`
(como depurar).

## Em uma linha
A pasta `.vscode/` versionada configura editor, extensões e debugger para o
projeto — preferências pessoais de tema/fonte, configurações profissionais de
ferramentas.

## Na prática

### 1. `settings.json` — preferências do projeto

```jsonc
{
  // ===== APARÊNCIA ===== (suas preferências pessoais — preservadas!)
  "workbench.colorTheme": "Bearded Theme Vivid Black",  // tema
  "editor.fontFamily": "'JetBrains Mono', monospace",   // fonte
  "editor.fontSize": 17,

  // ===== PYTHON ===== (o que faz o ambiente funcionar)
  "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",  // ← QUAL python
  "python.venvPath": ".venv",                                     // ← ONDE está o venv
  "python.analysis.typeCheckingMode": "strict",   // Pylance = strict (igual Pyright)

  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",  // formatador = Ruff
    "editor.formatOnSave": true,                      // formata ao salvar
    "editor.codeActionsOnSave": {                     // ao salvar:
      "source.fixAll.ruff": "explicit",               // 1. corrige lint
      "source.organizeImports.ruff": "explicit"       // 2. ordena imports
    },
    "editor.rulers": [88]                             // régua no limite do Ruff
  },

  "python.testing.pytestEnabled": true,   // botão de testes (Pytest)
  "python.testing.unittestEnabled": false // unittest desativado (usamos pytest)
}
```

> **`python.defaultInterpreterPath`** é o que resolveu o problema do `.venv`
> "quebrado": com ele, o VS Code usa exatamente o Python do projeto, sem
> adivinhar. **`python.venvPath`** diz onde procurar ambientes virtuais.

### 2. `extensions.json` — extensões recomendadas

O VS Code pergunta "instalar as extensões recomendadas?" ao abrir o projeto:

```jsonc
{
  "recommendations": [
    "ms-python.python",            // base do Python (inclui Pylance)
    "ms-python.vscode-pylance",    // type checker em tempo real
    "charliermarsh.ruff",          // lint + format
    "formulahendry.code-runner",   // botão "play" para rodar scripts
    "tamasfe.even-better-toml",    // edição de pyproject.toml
    "kevinrose.vsc-python-indent", // indentação correta do Python
    "streetsidesoftware.code-spell-checker", // ortografia (cSpell)
    "omthemes.omthemes",           // temas (o Bearded Theme vem daqui)
    ...
  ]
}
```

> O professor recomenda ainda: `bradlc.vscode-tailwindcss` (front-end),
> `chadalen.vscode-jetbrains-icon-theme` (ícones JetBrains), `esbenp.prettier`
> (JS/HTML), `batisteo.vscode-django` (para as seções de Django do curso).

### 3. `launch.json` — depuração pronta

```jsonc
{
  "configurations": [
    {
      "name": "Python: Arquivo Atual",     // F5 roda o arquivo aberto
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",                // o arquivo em foco
      "console": "integratedTerminal",     // terminal integrado (input() funciona)
      "envFile": "${workspaceFolder}/.env",// ← carrega o .env (nota 07!)
      "python": "${command:python.interpreterPath}" // usa o .venv configurado
    },
    {
      "name": "Pytest: Arquivo Atual",     // debug de testes do arquivo aberto
      "module": "pytest",
      "args": ["${file}", "-v", "--tb=short"]
    }
  ]
}
```

## O que NÃO fazer

```jsonc
// ← ERRADO: desligar o formatador do Python ou usar outro (black)
"[python]": { "editor.defaultFormatter": "ms-python.black-formatter" }
// ← o certo: Ruff (é o configurado no pyproject — consistência!)

// ← ERRADO: `python.analysis.typeCheckingMode: "off"` "para não incomodar"
// ← o certo: strict — é o padrão sênior que o curso ensina (nota 05)

// ← ERRADO: apontar interpreter para o Python GLOBAL
"python.defaultInterpreterPath": "C:\\Python\\python.exe"  // perde o venv!
// ← o certo: .venv do projeto

// ← ERRADO: editar o settings.json do projeto para preferência estritamente pessoal
// (tema/fonte sua: fica no settings do USUÁRIO — o do projeto é compartilhado)
```

## Por que Python funciona assim?
O VS Code tem três níveis de configuração, do maior para o menor escopo:
`settings do usuário` (todas as suas máquinas/projetos) → `workspace`
(`.vscode/settings.json` do projeto) → `pasta específica`. O do projeto
sobrescreve o do usuário para aquela pasta — então é o lugar certo para
configurações TÉCNICAS (formatter, interpreter, lint), e o settings do usuário
para preferências estéticas (tema, fonte). As extensões usam o `extensions.json`
para sugerir instalação automática, e o `launch.json` define como o debugger
(debugpy) chama o interpretador — por isso o `envFile` e o `interpreterPath`
precisam bater com o restante do ambiente (venv + dotenv).

## Conexões
- Você já usou esse padrão quando: o professor configurou Code Runner,
  extensões e tema no `ambiente_python_2025` (mesmo padrão aqui)
- Aparece também em: nota 01-venv (interpreter aponta para o .venv), nota
  04-ruff (formatter + codeActionsOnSave), nota 05-pyright (strict do Pylance),
  nota 06-pytest (botão de testes), nota 07-dotenv (envFile no debug)
- Diferente de: settings do usuário (preferências globais suas), pyproject.toml
  (configura as FERRAMENTAS; o settings.json configura o EDITOR)

---

## Teste de recuperação — responda sem olhar para cima

1. Quais os 3 arquivos de `.vscode/` e o papel de cada um?
2. O que `python.defaultInterpreterPath` e `python.venvPath` fazem e por que importam?
3. O que acontece ao salvar um .py com as configurações atuais?
4. Onde o debugger procura o `.env` ao rodar o F5?

---

**Frase-âncora:** "O avião carrega o painel: .vscode versionado deixa qualquer máquina pronta para voar igual."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
