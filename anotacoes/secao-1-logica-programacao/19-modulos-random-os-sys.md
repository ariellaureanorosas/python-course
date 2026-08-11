# Módulos random, os e sys

## Quando você vai usar isso?
Jogos e sorteios (random), limpar a tela ou interagir com o sistema operacional (os), interromper o programa com mensagem (sys). São os três imports que aparecem nos projetos de terminal da Seção 1 — e estarão em automações e ferramentas CLI depois.

## Modelo mental
`random` é a máquina de sorteio (dado de cassino). `os` é o controle remoto do sistema: limpa a tela, executa comandos, mexe em arquivos. `sys` é o painel do próprio programa: encerra a execução e dá acesso a argumentos e versão.

## Em uma linha
`import random` sorteia valores; `import os` conversa com o sistema operacional; `import sys` controla o fim (sys.exit) da execução.

## Na prática

### Caso simples — random

```python
import random

random.randint(1, 6)                    # ← inteiro entre 1 e 6 (inclusive) — um dado
random.choice(["pedra", "papel", "tesoura"])  # ← sorteia um item da lista
random.random()                         # ← float entre 0.0 e 1.0
lista = [1, 2, 3, 4]
random.shuffle(lista)                   # ← embaralha a lista NO LUGAR
```

### Com variação — os e sys

```python
import os
import sys

os.system("cls")    # ← limpa o terminal no Windows
# os.system("clear")  # ← Linux/macOS

print("antes")
sys.exit("Erro: dados inválidos")  # ← exibe a mensagem e ENCERRA o programa
print("depois")                    # ← nunca chega a executar
```

### Em uso real — sorteio sem repetição (estilo mega-sena)

```python
import random

sorteio = []
while len(sorteio) < 6:
    numero = random.randint(1, 60)
    if numero not in sorteio:        # ← evita repetidos
        sorteio.append(numero)

sorteio.sort()
print(sorteio)
```

## O que NÃO fazer

```python
# ← os.system com dados vindos de input(): o usuário poderia injetar
# comandos no shell. Use apenas com valores que você controla.
os.system(f"rm -rf {nome_do_usuario}")   # ← JAMAS

# ← random para sorteio de prêmios/senhas: é PSEUDOaleatório
# (previsível com semente). Para segurança real, use o módulo secrets.

# ← sys.exit no meio de fluxos que outros vão chamar: quem chama sua
# função não consegue capturar a saída. Prefira retornar ou levantar exceção.
```

## Por que Python funciona assim?
`random` usa um gerador pseudoaleatório determinístico: com `random.seed(42)` a mesma sequência se repete — ótimo para testes reproduzíveis. `os.system` delega o comando para o shell do sistema operacional (por isso o risco de injeção). `sys.exit` lança a exceção `SystemExit`, que o interpretador trata como "terminar limpo"; a mensagem opcional vai para o stderr.

## Conexões
- Você já usou esse padrão quando: jogo de adivinhação e mega-sena usam random; palavra secreta usa os.system (nota 14)
- Aparece também em: testes com seed fixa, roleta de escolhas, scripts de automação, CLIs profissionais
- Diferente de: `secrets` (criptograficamente seguro — para senhas e sorteios sérios) e de `return` (devolve valor e continua; `sys.exit` encerra tudo)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `random.randint(1, 6)` e `random.choice(lista)`?
2. Por que não se deve usar `os.system` com conteúdo digitado pelo usuário?
3. O que acontece com o código escrito depois de um `sys.exit()`?

---

**Frase-âncora:** "random sorteia, os comanda o sistema, sys encerra o programa."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14