# Criar um Repositório no GitHub e Ligar ao Local

Passo a passo com os dois caminhos: projeto NOVO no GitHub e projeto que JÁ existe local.

## Caminho A — Projeto novo (GitHub primeiro)

1. No GitHub, botão **New repository**.
2. Nome curto e descritivo (ex.: `curso-python-estudos`).
3. **NÃO marque** "Add a README" nem ".gitignore" nesta tela — deixe o repositório vazio. Os dois históricos precisam nascer do MESMO lado para não ter "unrelated histories".
4. GitHub mostra 3 opções. Use a primeira:

```bash
git init
git add .
git commit -m "primeiro commit"
git branch -M main
git remote add origin https://github.com/seu-usuario/seu-repo.git
git push -u origin main
```

Pronto: o local e o remoto estão ligados pelo `origin`.

## Caminho B — Projeto que já existe local

1. Crie o repositório vazio no GitHub (sem README/.gitignore — você já tem os seus).
2. Na pasta do projeto:

```bash
git remote add origin https://github.com/seu-usuario/seu-repo.git
git branch -M main
git push -u origin main
```

Se você já tinha commits, eles vão todos; se ainda não tinha nenhum (`git init` dado agora), faça o primeiro commit antes do push.

## Caminho C — Já existe um README no GitHub (não recomendo, mas funciona)

```bash
git pull --allow-unrelated-histories origin main
# resolva conflitos se houver, depois:
git push
```

Em geral é mais simples apagar o repositório do GitHub e criar do zero seguindo o caminho A.

## Autenticação via HTTPS vs. SSH

**HTTPS:** `https://github.com/usuario/repo.git` — pede token/credencial. No GitHub, senha de terminal não vale mais; gere um *Personal Access Token* (Settings → Developer settings → Tokens) e use-o como senha.

**SSH:** `git@github.com:usuario/repo.git` — sem senha depois de configurar a chave:

```bash
ssh-keygen -t ed25519 -C "seu@email.com"
# cole o conteúdo de ~/.ssh/id_ed25519.pub em
# GitHub → Settings → SSH and GPG keys → New SSH key
```

Depois: `git remote set-url origin git@github.com:usuario/repo.git`.

## Checklist antes do primeiro push

- [ ] `.gitignore` existe e cobre `venv/`, `__pycache__/`, `.env`, `*.pyc`
- [ ] `git status` limpo de coisas que não devem ir ao GitHub
- [ ] `git log --oneline` com mensagens que contam história
- [ ] `git branch` mostra `main` (ou renomeie com `git branch -M main`)
- [ ] `git push -u origin main` publicou sem erro
- [ ] No GitHub: abra o repositório e confira os arquivos

## Depois do primeiro push

O fluxo vira o do guia de fluxo de trabalho: `status → add → commit → push`. E antes de trabalhar depois de um tempo: `git pull`.

---

**Frase-âncora:** *Repositório vazio no GitHub, histórico nasce local, push -u define o origin.*
**Nível:** Iniciante
**Revisão sugerida:** 30 dias