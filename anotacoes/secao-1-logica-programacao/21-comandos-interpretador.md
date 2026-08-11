# Comandos do Interpretador (python -u, -m, -c, -i)

## Quando você vai usar isso?
Quando você precisa do Python fora do botão do editor: testar uma expressão sem criar arquivo, rodar módulos instalados (venv, pip, doctest), manter o terminal vivo depois do script, ou acompanhar logs em tempo real.

## Modelo mental
`python` é o motor; as flags são os modos de direção: sem flag roda arquivo (a marcha normal), `-c` é o atalho (código na lata), `-m` é o cruzeiro do módulo, `-i` é o estacionar (termina e continua no terminal).

## Em uma linha
`python [flag] [alvo]`: sem flag executa arquivos; `-c` executa código da linha de comando; `-m` executa um módulo como programa; `-i` entra no modo interativo depois do script; `-u` desativa o buffer de saída.

## Na prática

### Caso simples — rodar arquivo

```bash
python meu_script.py        # ← executa o arquivo e encerra
```

### Com variação — as principais flags

```bash
python -c "print(2 ** 10)"             # ← 1024  (código sem arquivo)
python -m venv .venv                   # ← roda o MÓDULO venv
python -m pip install requests         # ← roda o pip como módulo
python -m doctest -v arquivo.py        # ← executa testes dentro de docstrings
python -i meu_script.py                # ← roda e abre o REPL com as variáveis vivas
python -u meu_script.py                # ← saída sem buffer (prints aparecem na hora)
```

### Em uso real — explorar depois de executar

```bash
python -i gabarito-30-gerador-cpf.py
# ...executa o script...
>>> cpf_gerado                       # ← variáveis do script continuam disponíveis
'529.982.247-25'
```

## O que NÃO fazer

```bash
python -m meu_script.py      # ← ERRO: -m espera um MÓDULO, não um caminho .py
python meu_script.py         # ← arquivos rodam sem -m

python -c 'print("oi")'      # ← cuidado com aspas: no Windows prefira
                             #   aspas duplas por fora e simples por dentro
python -c "print(\"oi\")"    # ← ou use aspas duplas com escape
```

## Por que Python funciona assim?
Sem argumento, o interpretador abre o REPL (leia-avalie-imprima). Com caminho de arquivo, executa e sai. `-c` compila a string como código-fonte. `-m` procura o módulo no sys.path e o executa como `__main__` — é assim que pacotes instalam "comandos". `-i` executa o arquivo e cai no REPL com o namespace preservado. `-u` faz o stdout escrever imediatamente (sem buffer), essencial para logs em pipelines.

## Conexões
- Você já usou esse padrão quando: `python -m pip install` para instalar dependências; o VS Code, por baixo, chama o python do .venv
- Aparece também em: CI/CD, build de projetos, scripts de deploy, Jupyter (que interpreta células como -c)
- Diferente de: o botão "Run" do editor (embute o interpretador do venv e o caminho do arquivo para você)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `python script.py` e `python -m script`?
2. O que a flag `-i` faz de diferente das outras?
3. Como executar um `print(2 ** 10)` sem criar nenhum arquivo?

---

**Frase-âncora:** "Arquivo direto, -m é módulo, -c é código solto, -i deixa vivo."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14