# Glossário Git — Os Termos em Uma Linha Cada

O vocabulário do Git em fichas curtas. Se um termo não estiver claro, volte aqui antes de pesquisar em qualquer outro lugar.

## Conceitos centrais

- **Repositório:** todo o histórico de um projeto, com seus commits e branches. É a pasta `.git` oculta + o conteúdo rastreado.
- **Commit:** uma foto (snapshot) do estado do projeto num momento, com mensagem e autor. Imutável por padrão — é a unidade da história.
- **Hash (SHA):** a impressão digital de cada commit (ex.: `a1b2c3d`). Identifica o commit de forma única.
- **Branch (ramo):** uma linha independente de história, apontando para um commit. `main` é a linha principal.
- **HEAD:** o "ponteiro" que diz em que commit/branch você está agora. `git log --oneline --all` mostra tudo em relação ao HEAD.
- **Index / Staging / Área de preparação:** o rascunho do próximo commit — o que você `git add` antes de `git commit`.
- **Working tree:** seus arquivos no disco, fora do Git. É o que o `git status` compara com o índice.

## Operações

- **init:** cria um repositório novo numa pasta (o `.git` nasce ali).
- **add:** move mudanças do working tree para o staging (prepara o snapshot).
- **commit:** grava o staging como snapshot permanente.
- **status:** mostra a diferença entre working tree, staging e último commit.
- **log:** histórico de commits (use `--oneline` para a versão curta).
- **diff:** compara mudanças (entre working tree e staging, entre commits etc.).
- **restore:** devolve arquivos ao estado anterior (descarta mudanças).
- **checkout / switch:** move o HEAD para outro branch ou commit. `switch` é o comando moderno para trocar de branch.
- **reset:** move o HEAD para trás (desfaz commits). `--soft` mantém as mudanças, `--hard` descarta tudo.
- **revert:** cria um commit NOVO que desfaz outro commit — o jeito seguro de desfazer o que já foi enviado ao remoto.
- **rebase:** reaplica seus commits POR CIMA de outra base (reescreve o histórico — cuidado em time).
- **stash:** guarda mudanças não commitadas num bolso, limpa a tree e devolve depois (`stash pop`).
- **tag:** um nome fixo (ex.: `v1.0`) para um commit — "marco de versão".
- **cherry-pick:** copia UM commit específico de outro branch para o atual.

## Remoto e colaboração

- **Remote:** um repositório em outro lugar (GitHub, GitLab) ligado ao seu. O nome padrão é `origin`.
- **Clone:** copia um repositório remoto inteiro (histórico incluído) para a sua máquina.
- **Fetch:** baixa as mudanças do remoto SEM integrar — atualiza as referências remotas.
- **Pull:** `fetch` + `merge` na prática: baixa e integra.
- **Push:** envia seus commits ao remoto.
- **Upstream:** a relação "este branch local publica naquele branch remoto" (`push -u` a define).
- **Fork:** cópia de um repositório alheio para a SUA conta no GitHub (para contribuir sem acesso).
- **Pull Request (PR):** pedido para integrar sua branch num repositório — a unidade de review no GitHub.
- **Merge:** integra uma branch na outra, criando um commit de junção.
- **Merge conflict:** quando o Git não consegue juntar sozinho (as mesmas linhas mudaram dos dois lados).
- **Detached HEAD:** estado "flutuante" quando você aponta o HEAD para um commit direto, sem branch — commits aí ficam órfãos.
- **origin/main:** a referência que representa "o que o remoto origin tem na branch main" na sua máquina (sua visão do remoto).

## Termos que costumam confundir

- **fetch vs. pull:** fetch só baixa; pull baixa e já mistura na sua branch. Se quer decidir como integrar, `fetch` + ver + `git merge origin/main`.
- **merge vs. rebase:** merge preserva a história real (dois ramos viram um nó); rebase reescreve os commits como se a linha fosse reta. Sozinho, rebase deixa o histórico lindo; em time, mexe com commits alheios.
- **revert vs. reset:** revert cria um commit que desfaz (seguro, envie ao remoto sem culpa); reset move a história para trás (perigoso em remoto).
- **checkout vs. restore:** checkout movimenta HEAD/arquivos entre commits; restore é o verbo moderno para "voltar arquivos ao estado anterior".
- **.gitignore:** a lista de padrões que o Git NÃO rastreia (venv, .env, __pycache__). Sem ele, segredos e lixo entram no histórico.
- **HEAD~1:** o commit pai do HEAD (um antes). `~2` dois antes — atalho de navegação de história.

---

**Frase-âncora:** *HEAD diz onde você está, staging diz o que entra, commit congela, push publica.*
**Nível:** Iniciante
**Revisão sugerida:** 30 dias