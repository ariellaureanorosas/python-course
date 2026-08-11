# Fluxo de Trabalho — Do Novo Arquivo ao Push

O fluxo mínimo de quem trabalha sozinho OU em time, na ordem em que as coisas acontecem.

## 1. Prepare o terreno (uma vez)

```bash
git init
# crie o .gitignore ANTES do primeiro commit
# .gitignore mínimo para Python:
#   venv/
#   __pycache__/
#   *.pyc
#   .env
```

Primeiro commit de verdade:

```bash
git add .
git commit -m "inicia projeto: estrutura base"
```

## 2. Sempre antes de mexer

```bash
git status      # sei o que mudou?
git pull        # estou alinhado com o remoto? (se houver)
```

## 3. Mudança pequena, commit pequeno

A regra de ouro dos commits:

1. Um commit resolve UM problema.
2. A mensagem diz O QUE e POR QUE, não COMO.
3. Se o commit tem duas ideias, divida-o.

```bash
git add exercicios/secao-2/  # só o que interessa
git commit -m "corrige contrato de ler_arquivo: retorna lista vazia se arquivo nao existe"
```

Mensagens ruins: "atualiza", "changes", "final", "v2", "merge".
Mensagens boas: "adiciona validacao de CPF ao validador", "corrige off-by-one na tabuada", "extrai funcao de soma para modulo util".

Exemplo completo do formato sênior (assunto + corpo + rodapé), todos os tipos com casos de uso e o checklist do assunto perfeito: [guia-mensagens-commit.md](guia-mensagens-commit.md).

## 4. Branch (só em time, e para recursos maiores)

```bash
git switch -c feature/validador-cpf
# ... trabalha, commita normalmente ...
git push -u origin feature/validador-cpf
```

Depois de revisado e integrado (merge/PR), apague a branch:

```bash
git switch main
git merge feature/validador-cpf
git branch -d feature/validador-cpf
```

## 5. Publicar

```bash
git push -u origin main    # primeira vez cria o upstream
git push                   # nas seguintes
```

## 6. Receber mudanças de quem trabalhou junto

```bash
git pull                    # alinhou com o remoto
```

Se houver conflito, resolva (veja o guia de erros), `git add` os arquivos resolvidos e `git commit`.

## Regras que evitam 90% dos problemas

1. `git status` antes de qualquer commit — nunca commite no automático sem olhar.
2. Arquivos gerados (venv, binários, segredos) nunca entram: `.gitignore` ganha deles.
3. Commit local pequeno e frequente; push quando a ideia está concluída.
4. Nunca reescreva (`--amend`, `reset --hard`) commits já enviados ao remoto em trabalho compartilhado.
5. O `git log --oneline` deve contar uma história legível do projeto.

---

**Frase-âncora:** *Status antes de agir, commit pequeno por ideia, push só com história legível.*
**Nível:** Iniciante
**Revisão sugerida:** 30 dias