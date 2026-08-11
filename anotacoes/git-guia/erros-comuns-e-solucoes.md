# Erros Comuns e Soluções

Cada erro abaixo é acompanhado da causa e do remédio. Se a mensagem que você viu não está aqui, copie o texto exato e pesquise — o Git é um dos softwares mais documentados do mundo.

## 1. `warning: LF will be replaced by CRLF`

**Causa:** Windows usa `\r\n` (CRLF), o Git/Linux usa `\n` (LF). O Git avisa que vai normalizar as quebras de linha ao commitar.

**Solução (recomendada):** deixe o Git fazer a normalização por você. Crie um arquivo `.gitattributes` na raiz:

```
* text=auto
```

Depois de adicionar, rode uma normalização única:

```bash
git add --renormalize .
git commit -m "normaliza quebras de linha"
```

## 2. `fatal: Not a git repository (or any of the parent directories)`

**Causa:** você rodou um comando git fora de um repositório (ou numa subpasta que não pertence a ele).

**Solução:** confirme que existe uma pasta `.git` na raiz (`ls -a`) e rode os comandos a partir dela. Se você quer a pasta da raiz como repositório, rode `git init` no lugar certo, não numa pasta interna.

## 3. `You are in 'detached HEAD' state`

**Causa:** você fez `git checkout <hash>` (ou `<tag>`) — o HEAD ficou "solto", fora de qualquer branch.

**Solução:** se só queria olhar, volte com `git switch -` (ou `git checkout main`). Se queria trabalhar ali, crie uma branch: `git switch -c minha-branch`. NUNCA faça commits novos em detached HEAD — eles ficariam órfãos e seriam descartados depois.

## 4. Merge conflict (conflito de merge)

**Causa:** duas pessoas (ou você em dois momentos) alteraram as mesmas linhas; o Git não sabe qual versão vale.

**Solução:**
1. `git status` mostra a lista de arquivos em conflito (marcados `UU`).
2. Abra o arquivo: procure `<<<<<<< HEAD`, `=======` e `>>>>>>> branch`.
3. Escolha o conteúdo certo, apague os marcadores.
4. `git add <arquivo>` e `git commit` (o Git já abre uma mensagem pronta de merge).

## 5. `! [rejected] ... (non-fast-forward) / Updates were rejected`

**Causa:** seu remoto tem commits que você não tem — suas histórias divergiram.

**Solução:** integre primeiro, publique depois:

```bash
git pull --rebase    # ou: git pull  (se preferir merge)
git push
```

## 6. `fatal: remote origin already exists`

**Causa:** o repositório já tem um remoto chamado `origin` (não existe remoto "padrão" automático — alguém já ligou).

**Solução:** veja com `git remote -v`; se a URL estiver errada, troque-a em vez de criar outra:

```bash
git remote set-url origin <url-nova>
```

## 7. `fatal: refusing to merge unrelated histories`

**Causa:** dois históricos sem ancestral comum (ex.: você criou o README no GitHub e `git init` local em separado).

**Solução:** se os dois lados têm arquivos, escolha UM como fonte da verdade (`git pull --allow-unrelated-histories` só quando você sabe o que está fazendo). O jeito limpo é: não crie README/.gitignore na tela do GitHub quando o repositório já existe localmente — adicione esses arquivos você mesmo.

## 8. `git push` pedindo senha toda hora

**Causa:** você está autenticando por HTTPS com usuário/senha toda vez, ou o GitHub descontinuou senha de terminal.

**Solução:** no GitHub, use um *Personal Access Token* (pela URL) ou, de preferência, a CLI do GitHub hoje em dia é via SSH:

```bash
git remote set-url origin git@github.com:seu-usuario/seu-repo.git
```

## 9. Commit com mensagem errada ou faltou um arquivo

```bash
git commit --amend                # edita a mensagem do último commit
git add <arquivo-esquecido>
git commit --amend --no-edit      # incorpora sem mudar a mensagem
```

Cuidado: `--amend` reescreve histórico. Depois de um `push`, não reescreva commits que já estão no remoto (a menos que ninguém mais os use — em time, evite).

## 10. Arquivo que não deveria estar no repositório (senha, .env, venv)

**Causa:** foi commitado por engano, ou o `.gitignore` não existia.

**Solução:**
1. Adicione ao `.gitignore` (ex.: `venv/`, `.env`, `*.pyc`).
2. Tire do rastreamento sem apagar do disco:

```bash
git rm --cached .env
git commit -m "remove .env do versionamento"
```

## Regra de bolso

A mensagem do erro não é o problema: é o diagnóstico. Leia a frase inteira antes de procurar a solução — 90% dos erros do Git dizem exatamente o que fazer.

---

**Frase-âncora:** *A mensagem do erro é o diagnóstico — leia antes de pesquisar.*
**Nível:** Iniciante
**Revisão sugerida:** 15 dias