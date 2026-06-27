# Manipulação de Arquivos

## Quando você vai usar isso?
O programa terminou e você precisa que os dados — configurações, logs, resultados — sobrevivam ao desligamento. Você quer gravar um relatório em `.txt`, carregar um CSV ou mover arquivos entre pastas. Arquivos são a memória persistente mais básica do sistema.

## Modelo mental
Um bloco de notas com trava: você abre (abre a tampa), escreve ou lê (vira as páginas) e fecha (fecha o bloco). Se esquecer de fechar, a caneta pode ficar presa e corromper a escrita. O `with` é a mão que abre e fecha automaticamente.

## Em uma linha
Escreva e leia dados do disco usando `with open()` que garante fechamento automático do arquivo.

## Na prática

### Caso simples

```python
with open("arquivo.txt", "w", encoding="utf-8") as f:  # ← abre pra escrita
    f.write("Linha 1\n")                                # ← escreve string
    f.write("Linha 2\n")                                # ← \n quebra a linha

with open("arquivo.txt", "r", encoding="utf-8") as f:  # ← abre pra leitura
    conteudo = f.read()                                  # ← lê TUDO como string
```

### Com variação

```python
# Escrita em lote
with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.writelines(["Linha 3\n", "Linha 4\n"])             # ← lista de strings

# Leitura linha a linha
with open("arquivo.txt", "r", encoding="utf-8") as f:
    for linha in f:                                      # ← iterador nativo
        print(linha.strip())                             # ← strip() remove \n

# Voltar ao início
with open("arquivo.txt", "r") as f:
    print(f.readline())                                  # ← primeira linha
    f.seek(0, 0)                                         # ← volta posição 0 (início)
    print(f.read())                                      # ← lê tudo de novo
```

### Em uso real

```python
import os

# Relatório que persiste entre execuções
with open("relatorio.txt", "w", encoding="utf-8") as f:
    vendas = [("Camisa", 50), ("Calça", 100)]
    for produto, valor in vendas:
        f.write(f"{produto}: R$ {valor:.2f}\n")          # ← formata valores

# Remover e renomear
os.remove("relatorio_antigo.txt")                        # ← deleta arquivo
os.unlink("relatorio_antigo.txt")                        # ← alternativa idêntica

if os.path.exists("relatorio.txt"):                     # ← verifica antes
    os.rename("relatorio.txt", "relatorio_final.txt")    # ← renomeia
```

## O que NÃO fazer

```python
f = open("arquivo.txt", "w")                             # ← abre sem with
f.write("dados")
# ← Se ocorrer um erro antes de f.close(), o arquivo fica aberto
# e pode corromper ou travar o sistema de arquivos.

f = open("arquivo_inexistente.txt", "r")                 # ← FileNotFoundError!
# ← Sem try/except, o programa quebra se o arquivo não existe.
```

## Por que Python funciona assim?
O `with` (context manager) chama `__enter__` na abertura e `__exit__` no final do bloco — mesmo com exceção, o arquivo é fechado. `encoding="utf-8"` é obrigatório em texto moderno: sem ele, Python usa o encoding do sistema (pode ser ASCII no Linux ou latin-1 no Windows), causando erros com acentos. `seek(0, 0)` move o cursor para o byte 0 (início) — o ponteiro interno do arquivo é como a agulha de um toca-discos.

## Conexões
- Você já usou esse padrão quando: escreveu `print(..., file=f)` para redirecionar saída para arquivo
- Aparece também em: `json.dump`, `csv.writer`, `pickle.dump` — todos usam `open()` internamente
- Diferente de: `"w"` sobrescreve, `"a"` anexa ao final, `"x"` cria (erro se existir)

---

## Teste de recuperação — responda sem olhar para cima

1. O que acontece se você esquecer `f.close()` ao usar `open()` sem `with`?
2. Escreva código que abre `dados.txt`, lê todas as linhas, remove quebras de linha e imprime.
3. Qual a diferença entre os modos `"w"` e `"a"`?

---

**Frase-âncora:** "Abra, leia/escreva, feche — com with, nunca esqueça o último."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
