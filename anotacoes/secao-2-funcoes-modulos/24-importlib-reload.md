# importlib: import_module e reload

## Quando você vai usar isso?
Quando você está em um REPL ou Jupyter e editou um módulo — importá-lo de novo NÃO o atualiza (o Python cacheia). `importlib.reload` força a recarga. E `importlib.import_module` importa por NOME DINÂMICO (uma string), útil para plugins e código carregado em tempo de execução.

## Modelo mental
O `import` é um "já tenho?" no estoque: se o módulo já está no sys.modules (o armazém), ele entrega o MESMO objeto — não reexecuta o arquivo. reload é o "atualiza o estoque": reexecuta o código do módulo e troca o conteúdo no lugar. import_module é a nota de compra que aceita o nome escrito à mão.

## Em uma linha
`import` cacheia no sys.modules; `importlib.reload(modulo)` reexecuta; `importlib.import_module("nome")` importa com nome string.

## Na prática

### Caso simples — recarregar após editar (aula 100)

```python
import importlib
import aula100_modulo

print(aula100_modulo.variavel)      # ← versão atual

for _ in range(10):
    importlib.reload(aula100_modulo)  # ← reexecuta o módulo 10x
# útil em desenvolvimento: editei o arquivo, reload busca as mudanças
```

### Com variação — import por nome dinâmico

```python
import importlib

modulo = importlib.import_module("os")     # ← mesmo que `import os`
modulo.getcwd()                            # ← usa como módulo normal

pacote = importlib.import_module("dados_aula102")
produtos = getattr(pacote, "produtos")     # ← combina com getattr (nota 20)
```

### Em uso real — carregar o módulo pelo nome armazenado em config

```python
import importlib

# ← nome do módulo vem de um arquivo de configuração ou input
nome_modulo = "aula101_package"
modulo = importlib.import_module(nome_modulo)
modulo.modulo()          # ← chama a função exposta pelo pacote
```

## O que NÃO fazer

```python
# ← ERRADO: reimportar não recarrega
import aula100_modulo
# ... editei o arquivo ...
import aula100_modulo    # ← NADA acontece: já está em sys.modules
importlib.reload(aula100_modulo)  # ← o caminho certo

# ← ERRADO: import_module com nome de ARQUIVO com extensão
importlib.import_module("aula100_modulo.py")   # ← ModuleNotFoundError

# ← CUIDADO: reload devolve o módulo — reatribua se preciso
modulo = importlib.reload(modulo)
```

## Por que Python funciona assim?
O dicionário `sys.modules` mapeia nome → objeto-módulo. O `import` verifica esse mapa antes de ler o disco — segunda importação é instantânea e NÃO reexecuta o arquivo (é isso que mantém estado de módulo como variáveis globais persistentes). `reload` remove o módulo do cache, importa de novo e REATRIBUI o conteúdo no objeto existente — mas cuidado: variáveis já importadas com `from modulo import x` não são atualizadas pelo reload (ficam apontando para o objeto antigo).

## Conexões
- Você já usou esse padrão quando: deu import em módulos repetidamente e ficou confuso com mudanças que não apareciam
- Aparece também em: Jupyter (autoreload), plugins com hot-reload, testes que resetam módulos
- Diferente de: `import` (uma vez, cacheado), `from ... import *` (depende de `__all__`, nota 09) e `exec(open(...).read())` (hack arriscado, evite)

---

## Teste de recuperação — responda sem olhar para cima

1. Por que o segundo `import aula100_modulo` não reexecuta o arquivo?
2. Qual a diferença entre `import_module("os")` e `import os`?
3. O que o reload NÃO atualiza quando você usou `from modulo import x`?

---

**Frase-âncora:** "Import cacheia; reload recarrega; import_module importa por string."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14