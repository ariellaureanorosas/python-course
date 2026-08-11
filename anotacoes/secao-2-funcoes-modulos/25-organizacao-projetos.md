# Organização de projetos — arquivos, pastas e packages

## Quando você vai usar isso?
Assim que o programa passa de "um script" para "uma aplicação" — a partir daqui os arquivos se multiplicam (código, dados, menus, validações) e importar do jeito certo vira parte do problema. São as aulas 100, 103, 104 e 105: como estruturar pastas e módulos, hierarquia de caminhos e o grande aplicativo de estoque criado na aula 105.

## Modelo mental
Projeto é uma cidade: cada arquivo é um bairro com função (entrada da cidade = `main`; dados = depósitos; regras = fábricas). As pastas agrupam bairros afins e o `__init__.py` é o "cartório" que registra que uma pasta é um distrito importável (package). Importar é o endereço completo: caminho a partir da raiz do projeto — sem endereço, o guarda (`sys.path`) não acha a casa.

## Em uma linha
Separe responsabilidades em módulos e packages, use uma hierarquia de pastas clara e um ponto de entrada (`main`); `__init__.py` marca pastas como packages e `sys.path` decide o que você consegue importar.

## Na prática

### Caso simples — módulo auxiliar (aula 100)

```python
# aula100_modulo.py  ← módulo separado, importado pelo script principal
variavel = 1

# aula100.py  ← script principal (entrada)
import aula100_modulo
print(aula100_modulo.variavel)
```

### Com variação — package com __init__.py (aula 101)

```python
# aula101_package/__init__.py        ← marca a pasta como package
# aula101_package/modulo.py          ← conteúdo do package

# aula101_main.py                    ← ponto de entrada
import aula101_package.modulo        # ← endereço completo: package.modulo
from aula101_package import modulo   # ← caminho direto ao módulo
```

Estrutura de pastas do curso (aula 100/103/104):

```text
projeto/
├── main.py              ← entrada da aplicação
├── modulos/             ← packages com responsabilidades
│   └── __init__.py
├── dados/               ← separados do código (aula 105: produtos.json etc.)
└── utilidades/          ← funções de apoio
```

### Em uso real — aplicativo de estoque (aula 105)

A aula 105 organiza o aplicativo em partes:

```python
# main.py — importa e roda o fluxo principal
import produtos
import vendas

# dados dos produtos em arquivo separado (não no meio do código)
# ex.: dados_aula102/produtos → dict/listas lidos pelos módulos

# cada tela/menu vira função num módulo próprio
def menu_produtos():
    ...
```

O ganho aparece quando uma tela muda: você mexe SÓ no módulo dela, o resto da aplicação continua importando o mesmo nome de sempre.

## O que NÃO fazer

```python
# ← ERRADO: um único arquivo com 1000 linhas misturando tudo
# ← o certo: entrada + módulos por responsabilidade

# ← ERRADO: import que só funciona "por sorte" (rodando de outra pasta)
import dados_aula102         # ← ModuleNotFoundError se o caminho não estiver no sys.path
# ← o certo: rodar da raiz do projeto ou arrumar o sys.path

# ← ERRADO: pasta sem __init__.py esperando import direto
# (funciona como namespace package no Python 3, mas quebra a introspecção
# e confunde a IDE — declare o __init__.py mesmo que vazio)
```

## Por que Python funciona assim?
O `import` procura o módulo nos caminhos de `sys.path` (que inclui a pasta do script que está rodando). Por isso "import quebra" quando o script é executado de outra pasta: o ponto de partida muda e o endereço deixa de existir. Pastas com `__init__.py` viram *packages* — importáveis como `pacote.modulo`; no Python 3, pastas sem ele também importam (namespace packages), mas o `__init__.py` explícito documenta o package e evita surpresas. Separar dados de código (aula 105) também simplifica: o programa lê os arquivos, não precisa ser "reexecutado" quando o catálogo muda.

## Conexões
- Você já usou esse padrão quando: rodou os gabaritos com `python -m doctest arquivo.py` a partir da pasta certa — imports de módulos vizinhos só funcionam pelo caminho correto
- Aparece também em: nota 09-modulos-pacotes (`__name__`, `__all__`), nota 24-importlib-reload (recarregar módulos ao desenvolver), nota 20-dir-hasattr-getattr (inspecionar o que um módulo expõe)
- Diferente de: script único (`python arquivo.py`), biblioteca publicada (estrutura de `pyproject.toml`), projeto Django (apps com estrutura pré-definida)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual o papel do `__init__.py` dentro de uma pasta?
2. Por que um import pode quebrar ao rodar o script de outra pasta?
3. Como você estruturaria o aplicativo de estoque (aula 105) em módulos e packages?

---

**Frase-âncora:** "Projeto é cidade: main é a entrada, pastas são bairros, `__init__.py` é o cartório e o import é o endereço."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14