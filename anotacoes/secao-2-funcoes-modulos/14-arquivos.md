# Manipulação de Arquivos

## Modos de Abertura

```python
r   # leitura
w   # escrita (cria/substitui)
x   # criação exclusiva (erro se existir)
a   # anexar ao final
b   # modo binário
t   # modo texto (padrão)
+   # leitura e escrita
```

Combinações comuns: `"w"`, `"r"`, `"w+"`, `"rb"`

## Escrever

```python
with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("Linha 1\n")
    f.write("Linha 2\n")
    f.writelines(["Linha 3\n", "Linha 4\n"])
```

## Ler

```python
with open("arquivo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()       # tudo
    linha = f.readline()      # uma linha
    linhas = f.readlines()    # lista de linhas

f.seek(0, 0)  # volta ao início
```

## Remover e Renomear

```python
import os
os.remove("arquivo.txt")     # deleta
os.unlink("arquivo.txt")     # deleta (alternativa)
os.rename("old.txt", "new.txt")  # renomeia
```

## `strip()` ao ler

```python
with open("arquivo.txt") as f:
    for linha in f:
        print(linha.strip())  # remove \n
```
