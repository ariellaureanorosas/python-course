# Guia Rápido — Comandos do Dia a Dia

Referência direta: copie e cole. Os comandos essenciais do Git num único arquivo.

## Configuração (uma vez por máquina)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
git config --global core.editor "code --wait"     # VS Code como editor
```

## Começando

```bash
git init                        # transforma a pasta atual em repositório
git clone <url>                 # copia um repositório remoto
```

## Ciclo de trabalho

```bash
git status                      # o que mudou? (sempre olhe antes de agir)
git add <arquivo>               # adiciona a área de staging (índice)
git add .                       # adiciona tudo do diretório atual
git commit -m "mensagem"        # registra o snapshot do que está no índice
git log --oneline               # histórico resumido
git diff                        # mudanças ainda não preparadas
git diff --staged               # mudanças já no índice
git restore <arquivo>           # descarta mudanças não preparadas
git restore --staged <arquivo>  # tira do índice sem apagar mudanças
```

## Branches (ramificações)

```bash
git branch                          # lista branches (o * marca o atual)
git branch nome-da-branch           # cria uma nova
git switch nome-da-branch           # troca para a branch
git switch -c nome-da-branch        # cria E troca
git merge nome-da-branch            # integra a branch no branch atual
git branch -d nome-da-branch        # apaga a branch (já integrada)
```

## Remoto (GitHub, GitLab, etc.)

```bash
git remote add origin <url>         # liga o repositório local ao remoto
git remote -v                       # lista remotos
git push -u origin main             # publica e define o upstream (primeira vez)
git push                            # publica (depois de ter upstream)
git pull                            # baixa E integra (fetch + merge)
git fetch                           # só baixa, não integra
```

## Utilitários

```bash
git stash                   # guarda mudanças não commitadas para depois
git stash pop               # devolve o que foi guardado
git tag v1.0                # marca um ponto importante do histórico
git show <hash>             # detalha um commit
git log -p                  # histórico com as diffs
```

## Quando errar

```bash
git commit --amend          # corrige a mensagem do ÚLTIMO commit local
git reset --soft HEAD~1     # desfaz o último commit, mantém as mudanças
git reset --hard HEAD       # descarta tudo até o último commit (PERIGO)
git switch -                # volta para o branch anterior
```

## Ordem mental em 4 passos

1. `git status` — o que mudou?
2. `git add` — o que entra no snapshot?
3. `git commit` — snapshot com mensagem.
4. `git push` — publica no remoto (se houver).

---

**Frase-âncora:** *Status antes de agir, commit pequeno e frequente, push só com a mensagem certa.*
**Nível:** Iniciante
**Revisão sugerida:** 15 dias