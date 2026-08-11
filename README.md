<div align="center">

# Python 3 — Do Zero ao Avançado

![Python](https://img.shields.io/badge/Python-3.13|3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-web-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20andamento-F59E0B?style=for-the-badge)

Anotações, exercícios e projetos do curso **Python 3 do Zero ao Avançado**
ministrado por [Luiz Otávio Miranda](https://www.udemy.com/course/python-3-do-zero-ao-avancado/) na Udemy — **745+ aulas**.

</div>

---

## Estrutura do Repositório

```
PYTHON-COURSE/
├── .vscode/
├── anotacoes/                        ← resumo e revisão do conteúdo
│   ├── secao-1-logica-programacao/
│   ├── secao-2-funcoes-modulos/
│   └── secao-3-orientacao-objetos/
├── exercicios/                       ← exercícios práticos + gabaritos
│   ├── secao-1-logica-programacao/
│   │   ├── exercicios/
│   │   └── gabaritos/
│   ├── secao-2-funcoes-modulos/
│   │   ├── exercicios/
│   │   └── gabaritos/
│   └── secao-3-orientacao-objetos/
│       ├── exercicios/
│       └── gabaritos/
├── Seção 1 - Iniciando na programação com Python (Lógica de programação básica)/
├── Seção 2 - Python Intermediário - Funções - Dicionários - Módulos - Programação Funcional/
├── Seção 3 - Introdução à Programação Orientada a Objetos em Python - POO (Classes)/
├── ... (mais seções em andamento)
├── git-guia/                        ← guias de Git (comandos, erros, fluxo)
├── .gitignore
├── README.md
└── venv/
```

---

## 💪 Bônus — Exercícios Extras

Além do material do curso, este repositório contém exercícios complementares para fixação:

<table align="center">
  <thead>
    <tr>
      <th>Pasta</th>
      <th>Conteúdo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>exercicios/secao-1-logica-programacao/exercicios/</code></td>
      <td>20 exercícios de lógica (print a CPF)</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-1-logica-programacao/gabaritos/</code></td>
      <td>20 gabaritos profissionais (seção 1)</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-2-funcoes-modulos/exercicios/</code></td>
      <td>20 exercícios de funções/dicts/módulos</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-2-funcoes-modulos/gabaritos/</code></td>
      <td>20 gabaritos profissionais (seção 2)</td>
    </tr>
    <tr>
      <td><code>anotacoes/secao-1-logica-programacao/</code></td>
      <td>15 resumos em markdown para revisão rápida</td>
    </tr>
    <tr>
      <td><code>anotacoes/secao-2-funcoes-modulos/</code></td>
      <td>18 resumos em markdown para revisão rápida</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-3-orientacao-objetos/exercicios/</code></td>
      <td>20 exercícios de POO e classes</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-3-orientacao-objetos/gabaritos/</code></td>
      <td>20 gabaritos profissionais (seção 3)</td>
    </tr>
    <tr>
      <td><code>anotacoes/secao-3-orientacao-objetos/</code></td>
      <td>16 resumos de POO em markdown para revisão rápida</td>
    </tr>
    <tr>
      <td><code>git-guia/</code></td>
      <td>Guias de Git: comandos, erros, fluxo, mensagens de commit e glossário</td>
    </tr>
  </tbody>
</table>

Os gabaritos seguem estilo **dev sênior** com type hints, docstrings e PEP 8.

---

## 🗺️ Índice do Curso — Aula, Nota e Exercício

Mapa de navegação: cada exercício aponta para as notas (aulas) que o explicam e para o gabarito comentado. Estude a nota, tente o exercício sozinho e só então abra o gabarito — ele explica o RACIOCÍNIO, não só a resposta.

### Como usar

1. Leia a nota da aula antes de tentar o exercício.
2. Tente resolver sozinho (sem gabarito).
3. Compare com o gabarito e leia as seções "Raciocínio sênior" e "Onde você provavelmente divergiu".
4. Refaça o exercício de memória depois de 48h (recuperação ativa).

### Seção 1 — Lógica de Programação

Base: `anotacoes/secao-1-logica-programacao/` · Exercícios: `exercicios/secao-1-logica-programacao/exercicios/` · Gabaritos: `exercicios/secao-1-logica-programacao/gabaritos/`

| Exercício | Notas relacionadas | Tema |
|---|---|---|
| 01-cartao-visita | 01-print-tipos-comentarios, 03-strings-formatacao | print, f-strings |
| 02-media-escolar | 02-variaveis-operadores, 04-input-condicionais | input, float |
| 03-par-impar | 04-input-condicionais, 05-operadores-logicos | if/else, módulo |
| 04-classificador-triangulos | 04-input-condicionais | if aninhado |
| 05-login-simples | 05-operadores-logicos | comparadores |
| 06-radar-velocidade | 05-operadores-logicos | if/elif/else |
| 07-analisador-nome | 06-slicing-none-constantes, 10-tuplas-enumerate-split-join | len, metodos de string |
| 08-tabuada-while | 07-while | while, contador |
| 09-validador-senha | 07-while | loop com flag |
| 10-jogo-adivinhacao | 07-while, 12-ternario-decimal-round | loop + condicional |
| 11-contagem-regressiva | 08-for-range | range reverso |
| 12-tabuada-lista | 08-for-range, 09-listas | for + listas |
| 13-analisador-frase | 10-tuplas-enumerate-split-join, 06-slicing-none-constantes | split, contagem |
| 14-lista-compras | 09-listas, 11-listas-aninhadas-desempacotamento | CRUD em lista, menu |
| 15-matriz-alunos | 11-listas-aninhadas-desempacotamento, 09-listas | listas aninhadas |
| 16-desempacotamento-ternario | 11-listas-aninhadas-desempacotamento, 12-ternario-decimal-round | ternário, * unpack |
| 17-sorteio-megasena | 09-listas, 08-for-range | random, set |
| 18-primeiro-digito-cpf | 13-logica-cpf | funções, cálculo |
| 19-validador-cpf | 13-logica-cpf | funções, modularização |
| 20-jogo-palavra-secreta | 09-listas, 07-while | loops + listas |

Extra útil: `14-projetos-secao1`, `15-zen-python`.

### Seção 2 — Funções e Módulos

Base: `anotacoes/secao-2-funcoes-modulos/` · Exercícios: `exercicios/secao-2-funcoes-modulos/exercicios/` · Gabaritos: `exercicios/secao-2-funcoes-modulos/gabaritos/`

| Exercício | Notas relacionadas | Tema |
|---|---|---|
| 01-multiplicacao-args | 02-args-kwargs | *args |
| 02-par-ou-impar | 01-funcoes-def | funções básicas |
| 03-closure-saudacao | 03-closures | closure |
| 04-closure-multiplicador | 03-closures | closure com estado |
| 05-sistema-cadastro-dict | 04-dicionarios, 16-positional-keyword | dict + CRUD |
| 06-sistema-perguntas-dict | 04-dicionarios | dict armazenando funções |
| 07-filtrar-transformar-list-comp | 06-lambda-comprehension | list comprehension |
| 08-groupby-categoria | 11-zip-itertools | itertools.groupby |
| 09-decorator-log | 10-decorators | decoradores |
| 10-decorator-com-parametro | 10-decorators | decorador parametrizado |
| 11-zip-combinar-dados | 11-zip-itertools | zip |
| 12-map-partial-aumentar-precos | 12-map-filter-reduce, 18-collections-functools | map, partial |
| 13-filter-selecionar-produtos | 12-map-filter-reduce | filter |
| 14-reduce-calcular-total | 12-map-filter-reduce | reduce |
| 15-funcao-recursiva-fatorial | 13-recursao | recursão |
| 16-criar-ler-arquivo-txt | 14-arquivos, 17-datetime (relógio/log) | arquivos TXT |
| 17-gerenciador-tarefas-json | 15-json, 04-dicionarios | JSON persistente |
| 18-pipeline-map-filter-reduce | 12-map-filter-reduce | pipeline funcional |
| 19-combinations-permutations-senhas | 11-zip-itertools | combinations/permutations |
| 20-positional-only-keyword-only | 16-positional-keyword | / e * |

### Seção 3 — Orientação a Objetos

Base: `anotacoes/secao-3-orientacao-objetos/` · Exercícios: `exercicios/secao-3-orientacao-objetos/exercicios/` · Gabaritos: `exercicios/secao-3-orientacao-objetos/gabaritos/`

| Exercício | Notas relacionadas | Tema |
|---|---|---|
| 01-classes-init-self | 01-classes-init-self | __init__, self |
| 02-metodos-estado | 02-metodos-estado | estado em métodos |
| 03-atributos-classe | 03-atributos-classe-instancia | atributo de classe, vars() |
| 04-serializacao-json | 03-atributos-classe-instancia (vars), `json` da stdlib | vars() + json |
| 05-classmethod-factory | 04-classmethod-staticmethod | classmethod factory |
| 06-staticmethod | 04-classmethod-staticmethod | staticmethod |
| 07-property-getter | 05-property-getter-setter | propriedade leitura |
| 08-property-setter | 05-property-getter-setter | setter validando |
| 09-encapsulamento | 06-encapsulamento-name-mangling | name mangling |
| 10-associacao | 07-associacao-agregacao-composicao | associação |
| 11-agregacao | 07-associacao-agregacao-composicao | agregação |
| 12-composicao | 07-associacao-agregacao-composicao | composição |
| 13-heranca-super | 08-heranca-super | herança, super() |
| 14-heranca-multipla-mixins | 09-heranca-multipla-mro-mixins | mixins, MRO |
| 15-classes-abstratas | 10-classes-abstratas-abc | ABC |
| 16-polimorfismo-excecoes | 11-polimorfismo-liskov, 12-excecoes-customizadas | polimorfismo, exceções |
| 17-metodos-magicos | 13-metodos-magicos-dunder | dunders (+ >) |
| 18-context-manager | 14-context-managers | with, __exit__ |
| 19-dataclasses | 15-dataclasses | dataclass, field |
| 20-sistema-biblioteca | 16-enum-metaclasses + todas as anteriores | capstone (composição) |

### Regras de ouro

- Gabarito é o último recurso: ele existe para VOCÊ comparar depois de tentar.
- Todo gabarito roda `doctest.testmod()` — alterou, rode o arquivo.
- Os exercícios da seção 1 rodam com `input()` no terminal; os das seções 2 e 3 validam por doctest.
- Ao terminar uma seção, refaça 3 exercícios sorteados da seção anterior (revisão espaçada).

---

## Roadmap

### ✅ Concluído

| # | Seção |
|:-:|:------|
| 01 | Informações, avisos e boas-vindas |
| 02 | Python + VS Code — Ambiente de desenvolvimento |
| 03 | Lógica de programação básica com Python |
| 04 | Python Intermediário — Funções, Dicionários, Módulos e Programação Funcional |
| 05 | Introdução à POO em Python — Classes |

---

### ⏳ Em andamento / Pendente

**— Orientação a Objetos e Módulos —**

| # | Seção |
|:-:|:------|
| 06 | Módulos Python — os, datetime, sys, json, csv, selenium, pillow e mais |

**— Interfaces e Banco de Dados —**

| # | Seção |
|:-:|:------|
| 07 | PySide6 — Interface gráfica com Qt 6 (GUI para Desktop) |
| 08 | Bases de dados — SQLite (sqlite3) e MySQL (pymysql) |

**— Django —**

| # | Seção |
|:-:|:------|
| 09 | Django — Básico |
| 10 | Django — Projeto Agenda |
| 11 | Django — Primeiro Deploy (Linux) |
| 12 | Django — Projeto Blog |
| 13 | Django — Projeto E-commerce |

**— Qualidade e Padrões —**

| # | Seção |
|:-:|:------|
| 14 | Testes e TDD no Python — unittest |
| 15 | Type Annotations (Hints) no Python 3.10 |
| 16 | Structural Pattern Matching — Padrões estruturais (3.10) |
| 17 | Design Patterns (GOF) — POO Avançado |

**— Conteúdo Extra —**

| # | Seção |
|:-:|:------|
| 18 | Expressões Regulares (Regex) — Módulo `re` |
| 19 | SQL com MySQL — Bases de dados Relacionais |
| 20 | HTML5 e CSS3 para iniciantes |
| 21 | Landing Page com HTML5 e CSS3 |
| 22 | Comandos Linux/Unix — Terminal |
| 23 | Notas finais |

---

## Stack

<div align="center">

[![skillicons](https://skillicons.dev/icons?i=py,django,sqlite,mysql,qt,selenium,html,css,linux,vscode&theme=dark)](https://skillicons.dev)

| Tecnologia | Uso no curso |
|:----------:|:-------------|
| Python | Linguagem principal |
| Django | Desenvolvimento web — projetos Agenda, Blog e E-commerce |
| SQLite | Banco de dados local (sqlite3) |
| MySQL | Banco de dados relacional (pymysql) |
| Qt / PySide6 | Interface gráfica para Desktop |
| Selenium | Automação web |
| HTML5 + CSS3 | Front-end básico e Landing Page |
| Linux | Deploy e comandos de terminal |
| VS Code | Editor principal |

</div>

---

<div align="center">
<sub>Estudos em andamento · Curso por <a href="https://www.udemy.com/course/python-3-do-zero-ao-avancado/">Luiz Otávio Miranda</a></sub>
</div>
