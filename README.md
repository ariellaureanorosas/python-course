<div align="center">

# Python 3 — Do Zero ao Avançado

![Python](https://img.shields.io/badge/Python-3.13|3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-web-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20andamento-F59E0B?style=for-the-badge)
![Progresso](https://img.shields.io/badge/Progresso-5%2F23%20seções%20(~22%25)-3B82F6?style=for-the-badge)
![License](https://img.shields.io/badge/Uso-Estudo%20pessoal%20%2F%20não%20redistribuir-6B7280?style=for-the-badge)

**Repositório de estudo estruturado** com anotações, exercícios e projetos do curso
[**Python 3 do Zero ao Avançado**](https://www.udemy.com/course/python-3-do-zero-ao-avancado/) — Luiz Otávio Miranda (Udemy, 745+ aulas).

Não é só um repositório de "código do curso": é um **sistema de revisão** — cada exercício está
rastreado até as notas que o explicam e ao gabarito que documenta o raciocínio, não só a resposta.

</div>

---

## Sumário

- [Filosofia deste repositório](#filosofia-deste-repositório)
- [Setup rápido](#setup-rápido)
- [Estrutura](#estrutura-do-repositório)
- [Exemplo de gabarito](#exemplo-de-gabarito)
- [Bônus — Exercícios Extras](#-bônus--exercícios-extras)
- [Índice do Curso](#️-índice-do-curso--aula-nota-e-exercício)
- [Como estudar com este repo](#como-estudar-com-este-repo)
- [Roadmap](#roadmap)
- [Stack](#stack)
- [Licença e uso](#licença-e-uso)

---

## Filosofia deste repositório

> Estudar programação copiando código funciona até a primeira entrevista técnica ou até o
> primeiro bug em produção. Este repositório é organizado para **recuperação ativa** e
> **raciocínio sênior**, não decoreba.

Três princípios guiam a organização:

1. **Rastreabilidade** — todo exercício aponta para a(s) nota(s) que o fundamentam. Se você
   travou, o caminho de volta ao conceito é direto.
2. **Gabarito como último recurso** — os gabaritos existem para comparar *depois* de tentar,
   não para copiar antes. Eles explicam o *porquê*, não só o *como*.
3. **Revisão espaçada** — ao fechar uma seção, três exercícios sorteados da anterior são
   refeitos de memória, sem consultar nada.

---

## Setup rápido

```bash
# 1. Clonar o repositório
git clone https://github.com/<seu-usuario>/python-course.git
cd python-course

# 2. Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows

# 3. Instalar dependências (quando aplicável — seções com Django, Selenium, PySide6 etc.)
pip install -r requirements.txt

# 4. Rodar os exercícios da Seção 1 (input no terminal)
python exercicios/secao-1-logica-programacao/exercicios/exercicio-01-cartao-visita.py

# 5. Validar um gabarito das Seções 2 e 3 (doctest)
python -m doctest -v exercicios/secao-2-funcoes-modulos/gabaritos/gabarito-09-decorator-log.py
```

> Requer **Python 3.13+**. Cada seção com dependências extras (Django, Selenium, PySide6, MySQL)
> terá seu próprio `requirements.txt` dentro da respectiva pasta quando aplicável.

---

## Estrutura do Repositório

```
PYTHON-COURSE/
├── .vscode/
├── anotacoes/                       ← resumo e revisão do conteúdo
│   ├── secao-1-logica-programacao/
│   ├── secao-2-funcoes-modulos/
│   ├── secao-3-orientacao-objetos/
│   ├── ambiente-desenvolvimento/    ← notas do ambiente (venv, uv, Ruff, Pyright, etc.)
│   └── git-guia/                    ← guias de Git (comandos, erros, fluxo)
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
├── Type Hints - Youtube/
├── ... (mais seções em andamento)
├── .gitignore
├── README.md
└── .venv/
```

---

## Exemplo de gabarito

Amostra do padrão usado em todos os gabaritos: type hints, docstring, `doctest` embutido e
uma seção final explicando o raciocínio — não apenas a resposta.

```python
def validar_cpf(cpf: str) -> bool:
    """Valida um CPF verificando os dígitos verificadores.

    >>> validar_cpf("529.982.247-25")
    True
    >>> validar_cpf("111.111.111-11")
    False

    Args:
        cpf: string do CPF, com ou sem formatação (pontos e traço).

    Returns:
        True se os dois dígitos verificadores baterem, False caso contrário.
    """
    digitos = [int(c) for c in cpf if c.isdigit()]
    if len(digitos) != 11 or len(set(digitos)) == 1:
        return False

    for posicao in (9, 10):
        soma = sum(d * peso for d, peso in zip(digitos[:posicao], range(posicao + 1, 1, -1)))
        digito_calculado = (soma * 10 % 11) % 10
        if digito_calculado != digitos[posicao]:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

**Raciocínio sênior:** a validação de dígito repetido (`len(set(digitos)) == 1`) evita falsos
positivos com CPFs inválidos como `"111.111.111-11"`, que passariam no cálculo de dígito
verificador mas nunca são documentos reais — um erro comum em implementações ingênuas.

**Onde você provavelmente divergiu:** usar `cpf.replace(".", "").replace("-", "")` em vez de
`isdigit()` funciona, mas quebra se o CPF vier com espaços ou outro separador. Preferir
filtro por `isdigit()` é mais robusto a formatos de entrada variados.

---

## 💪 Bônus — Exercícios Extras

Além do material original do curso, este repositório contém exercícios complementares
para fixação, organizados por seção e com gabaritos em **estilo dev sênior** (type hints,
docstrings e conformidade com PEP 8).

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
      <td>31 exercícios de lógica (print a gerador de CPF)</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-1-logica-programacao/gabaritos/</code></td>
      <td>31 gabaritos profissionais (seção 1)</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-2-funcoes-modulos/exercicios/</code></td>
      <td>31 exercícios de funções/dicts/módulos</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-2-funcoes-modulos/gabaritos/</code></td>
      <td>31 gabaritos profissionais (seção 2)</td>
    </tr>
    <tr>
      <td><code>anotacoes/secao-1-logica-programacao/</code></td>
      <td>22 resumos em markdown para revisão rápida</td>
    </tr>
    <tr>
      <td><code>anotacoes/secao-2-funcoes-modulos/</code></td>
      <td>25 resumos em markdown para revisão rápida</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-3-orientacao-objetos/exercicios/</code></td>
      <td>33 exercícios de POO e classes</td>
    </tr>
    <tr>
      <td><code>exercicios/secao-3-orientacao-objetos/gabaritos/</code></td>
      <td>33 gabaritos profissionais (seção 3)</td>
    </tr>
    <tr>
      <td><code>anotacoes/secao-3-orientacao-objetos/</code></td>
      <td>25 resumos de POO em markdown para revisão rápida</td>
    </tr>
    <tr>
      <td><code>anotacoes/git-guia/</code></td>
      <td>Guias de Git: comandos, erros, fluxo, mensagens de commit e glossário</td>
    </tr>
    <tr>
      <td><code>anotacoes/ambiente-desenvolvimento/</code></td>
      <td>Notas do ambiente: venv, uv, pyproject.toml, Ruff, Pyright, Pytest, dotenv e VS Code</td>
    </tr>
  </tbody>
</table>

---

## 🗺️ Índice do Curso — Aula, Nota e Exercício

Mapa de navegação: cada exercício aponta para as notas (aulas) que o explicam e para o
gabarito comentado.

### Seção 1 — Lógica de Programação

Base: `anotacoes/secao-1-logica-programacao/` · Exercícios: `exercicios/secao-1-logica-programacao/exercicios/` · Gabaritos: `exercicios/secao-1-logica-programacao/gabaritos/`

| # | Exercício | Notas relacionadas | Tema |
|:-:|---|---|---|
| 01 | cartao-visita | 01-print-tipos-comentarios, 03-strings-formatacao | print, f-strings |
| 02 | media-escolar | 02-variaveis-operadores, 04-input-condicionais | input, float |
| 03 | par-impar | 04-input-condicionais, 05-operadores-logicos | if/else, módulo |
| 04 | classificador-triangulos | 04-input-condicionais | if aninhado |
| 05 | login-simples | 05-operadores-logicos | comparadores |
| 06 | radar-velocidade | 05-operadores-logicos | if/elif/else |
| 07 | analisador-nome | 06-slicing-none-constantes, 10-tuplas-enumerate-split-join | len, métodos de string |
| 08 | tabuada-while | 07-while | while, contador |
| 09 | validador-senha | 07-while | loop com flag |
| 10 | jogo-adivinhacao | 07-while, 12-ternario-decimal-round | loop + condicional |
| 11 | contagem-regressiva | 08-for-range | range reverso |
| 12 | tabuada-lista | 08-for-range, 09-listas | for + listas |
| 13 | analisador-frase | 10-tuplas-enumerate-split-join, 06-slicing-none-constantes | split, contagem |
| 14 | lista-compras | 09-listas, 11-listas-aninhadas-desempacotamento | CRUD em lista, menu |
| 15 | matriz-alunos | 11-listas-aninhadas-desempacotamento, 09-listas | listas aninhadas |
| 16 | desempacotamento-ternario | 11-listas-aninhadas-desempacotamento, 12-ternario-decimal-round | ternário, `*` unpack |
| 17 | sorteio-megasena | 09-listas, 08-for-range | random, set |
| 18 | primeiro-digito-cpf | 13-logica-cpf | funções, cálculo |
| 19 | validador-cpf | 13-logica-cpf | funções, modularização |
| 20 | jogo-palavra-secreta | 09-listas, 07-while | loops + listas |
| 21 | tuplas-escalacao | 10-tuplas-enumerate-split-join | tuplas, imutabilidade |
| 22 | calculadora-while | 07-while, 17-operadores-atribuicao | menu, laço |
| 23 | caixa-decimal | 12-ternario-decimal-round | `Decimal`, `round()` |
| 24 | else-loops | 07-while, 08-for-range | while/else, for/else |
| 25 | iterador-manual | 08-for-range | `iter()`, `next()`, `StopIteration` |
| 26 | copias-listas | 09-listas | mutabilidade, `.copy()`, `id()` |
| 27 | contato-none | 06-slicing-none-constantes | `None`, `is`/`is not` |
| 28 | formatacao-classica | 03-strings-formatacao | `%`, `.format()` |
| 29 | curto-circuito-input | 05-operadores-logicos | curto-circuito, fallback `or` |
| 30 | gerador-cpf | 19-modulos-random-os-sys, 13-logica-cpf | `random`, módulo 11 |
| 31 | analisador-metodos-string | 16-metodos-string | find, count, zfill |

> Extra útil: `14-projetos-secao1`, `15-zen-python`, `16-metodos-string`, `19-modulos-random-os-sys`, `21-comandos-interpretador`, `22-debugger-breakpoint`.

### Seção 2 — Funções e Módulos

Base: `anotacoes/secao-2-funcoes-modulos/` · Exercícios: `exercicios/secao-2-funcoes-modulos/exercicios/` · Gabaritos: `exercicios/secao-2-funcoes-modulos/gabaritos/`

| # | Exercício | Notas relacionadas | Tema |
|:-:|---|---|---|
| 01 | multiplicacao-args | 02-args-kwargs | `*args` |
| 02 | par-ou-impar | 01-funcoes-def | funções básicas |
| 03 | closure-saudacao | 03-closures | closure |
| 04 | closure-multiplicador | 03-closures | closure com estado |
| 05 | sistema-cadastro-dict | 04-dicionarios, 16-positional-keyword | dict + CRUD |
| 06 | sistema-perguntas-dict | 04-dicionarios | dict armazenando funções |
| 07 | filtrar-transformar-list-comp | 06-lambda-comprehension | list comprehension |
| 08 | groupby-categoria | 11-zip-itertools | `itertools.groupby` |
| 09 | decorator-log | 10-decorators | decoradores |
| 10 | decorator-com-parametro | 10-decorators | decorador parametrizado |
| 11 | zip-combinar-dados | 11-zip-itertools | zip |
| 12 | map-partial-aumentar-precos | 12-map-filter-reduce, 18-collections-functools | map, partial |
| 13 | filter-selecionar-produtos | 12-map-filter-reduce | filter |
| 14 | reduce-calcular-total | 12-map-filter-reduce | reduce |
| 15 | funcao-recursiva-fatorial | 13-recursao | recursão |
| 16 | criar-ler-arquivo-txt | 14-arquivos, 17-datetime | arquivos TXT |
| 17 | gerenciador-tarefas-json | 15-json, 04-dicionarios | JSON persistente |
| 18 | pipeline-map-filter-reduce | 12-map-filter-reduce | pipeline funcional |
| 19 | combinations-permutations-senhas | 11-zip-itertools | combinations/permutations |
| 20 | positional-only-keyword-only | 16-positional-keyword | `/` e `*` |
| 21 | primeiro-duplicado-set | 05-sets | set, primeiro duplicado |
| 22 | funcoes-geradoras | 07-generators | yield, yield from |
| 23 | modulos-pacotes | 09-modulos-pacotes | __name__, __main__, __all__ |
| 24 | try-except-else-finally | 08-try-except-raise | try/except/else/finally |
| 25 | itertools-count-product | 11-zip-itertools | count, islice, product |
| 26 | collections-counter-deque | 18-collections-functools | Counter, defaultdict, deque |
| 27 | agenda-datetime | 17-datetime | datetime, timedelta |
| 28 | escopo-global | 23-escopo-global | global, escopo |
| 29 | copy-rasa-profunda | 22-copy-rasa-profunda | shallow/deep copy |
| 30 | gerenciador-desfazer-refazer | 03-closures, 18-collections-functools | closures, pilhas |
| 31 | cache-functools | 18-collections-functools | lru_cache |

> Extra útil: `19-truthy-falsy`, `20-dir-hasattr-getattr`, `21-parametro-padrao-mutavel`, `22-copy-rasa-profunda`, `23-escopo-global`, `24-importlib-reload`, `25-organizacao-projetos`.

### Seção 3 — Orientação a Objetos

Base: `anotacoes/secao-3-orientacao-objetos/` · Exercícios: `exercicios/secao-3-orientacao-objetos/exercicios/` · Gabaritos: `exercicios/secao-3-orientacao-objetos/gabaritos/`

| # | Exercício | Notas relacionadas | Tema |
|:-:|---|---|---|
| 01 | classes-init-self | 01-classes-init-self | `__init__`, `self` |
| 02 | metodos-estado | 02-metodos-estado | estado em métodos |
| 03 | atributos-classe | 03-atributos-classe-instancia | atributo de classe, `vars()` |
| 04 | serializacao-json | 03-atributos-classe-instancia + `json` da stdlib | `vars()` + json |
| 05 | classmethod-factory | 04-classmethod-staticmethod | classmethod factory |
| 06 | staticmethod | 04-classmethod-staticmethod | staticmethod |
| 07 | property-getter | 05-property-getter-setter | propriedade de leitura |
| 08 | property-setter | 05-property-getter-setter | setter com validação |
| 09 | encapsulamento | 06-encapsulamento-name-mangling | name mangling |
| 10 | associacao | 07-associacao-agregacao-composicao | associação |
| 11 | agregacao | 07-associacao-agregacao-composicao | agregação |
| 12 | composicao | 07-associacao-agregacao-composicao | composição |
| 13 | heranca-super | 08-heranca-super | herança, `super()` |
| 14 | heranca-multipla-mixins | 09-heranca-multipla-mro-mixins | mixins, MRO |
| 15 | classes-abstratas | 10-classes-abstratas-abc | ABC |
| 16 | polimorfismo-excecoes | 11-polimorfismo-liskov, 12-excecoes-customizadas | polimorfismo, exceções |
| 17 | metodos-magicos | 13-metodos-magicos-dunder | dunders (`__add__`, `__gt__`) |
| 18 | context-manager | 14-context-managers | `with`, `__exit__` |
| 19 | dataclasses | 15-dataclasses | `dataclass`, `field` |
| 20 | sistema-biblioteca | 16-enum-metaclasses + todas as anteriores | capstone (composição) |
| 21 | slots-funcionario | 17-slots | `__slots__`, memória |
| 22 | new-singleton | 18-new-singleton | `__new__`, singleton |
| 23 | descritores-campo | 19-descriptores | descritores (`__get__`/`__set__`) |
| 24 | callable-contador | 20-callable-objeto | `__call__` |
| 25 | ordenacao-jogadores | 21-comparacao-rica | `__lt__`, `total_ordering` |
| 26 | cached-property-relatorio | 22-cached-property | `cached_property` |
| 27 | singledispatch-descrever | 23-singledispatch | `singledispatch` |
| 28 | iteraveis-tabuada | 24-iteraveis-poo | `__iter__`, `__next__` |
| 29 | hotel-reservas | 05-property-getter-setter, 06-encapsulamento-name-mangling, 07-associacao-agregacao-composicao | associação + validação |
| 30 | loja-estoque | 04-classmethod-staticmethod, 10-classes-abstratas-abc, 11-polimorfismo-liskov | ABC + composição |
| 31 | jogo-cartas | 17-slots até 24-iteraveis-poo (avançados) | capstone (slots + dunders) |
| 32 | documentando-codigo | 25-docstrings-documentacao, 13-metodos-magicos-dunder | docstrings, doctest |
| 33 | enum-status | 16-enum-metaclasses | Enum, `auto()`, máquina de estados |

---

## Como estudar com este repo

1. **Leia a nota** da aula relacionada antes de tentar o exercício.
2. **Tente resolver sozinho**, sem abrir o gabarito.
3. **Compare com o gabarito** e leia as seções *"Raciocínio sênior"* e *"Onde você provavelmente divergiu"*.
4. **Refaça de memória após 48h** (recuperação ativa — é o que fixa o conteúdo a longo prazo).
5. Ao concluir uma seção, **sorteie 3 exercícios da seção anterior** e refaça sem consulta.

**Convenções técnicas:**

| Regra | Detalhe |
|---|---|
| Validação | Exercícios da **Seção 1** rodam via `input()` no terminal; **Seções 2 e 3** validam por `doctest` |
| Testes | Todo gabarito executa com `python -m doctest -v arquivo.py` ou `doctest.testmod()` embutido |
| Estilo | Gabaritos seguem **PEP 8**, com type hints e docstrings no padrão Google/NumPy |
| Ambiente | `.venv/` local — não versionado; recriar com `python -m venv .venv` |

---

## Roadmap

**Progresso geral: 5 de 23 seções concluídas**

```
[██████░░░░░░░░░░░░░░░░░░░░░] ~22%
```

### ✅ Concluído

| # | Seção |
|:-:|:------|
| 01 | Informações, avisos e boas-vindas |
| 02 | Python + VS Code — Ambiente de desenvolvimento |
| 03 | Lógica de programação básica com Python |
| 04 | Python Intermediário — Funções, Dicionários, Módulos e Programação Funcional |
| 05 | Introdução à POO em Python — Classes |

### ⏳ Em andamento / Pendente

**Orientação a Objetos e Módulos**

| # | Seção |
|:-:|:------|
| BÔNUS | Type Hints — Type Checkers, Tipagem para Variáveis, Constantes, Funções, Classes, Decoradores, Coleções, Generics, protocols, TypeVar e ParamSpec |
| 06 | Módulos Python — `os`, `datetime`, `sys`, `json`, `csv`, Selenium, Pillow e mais |

**Interfaces e Banco de Dados**

| # | Seção |
|:-:|:------|
| 07 | PySide6 — Interface gráfica com Qt 6 (GUI para Desktop) |
| 08 | Bases de dados — SQLite (`sqlite3`) e MySQL (`pymysql`) |

**Django**

| # | Seção |
|:-:|:------|
| 09 | Django — Básico |
| 10 | Django — Projeto Agenda |
| 11 | Django — Primeiro Deploy (Linux) |
| 12 | Django — Projeto Blog |
| 13 | Django — Projeto E-commerce |

**Qualidade e Padrões**

| # | Seção |
|:-:|:------|
| 14 | Testes e TDD no Python — `unittest` |
| 15 | Type Annotations (Hints) no Python 3.10+ |
| 16 | Structural Pattern Matching — Padrões estruturais (3.10) |
| 17 | Design Patterns (GoF) — POO Avançado |

**Conteúdo Extra**

| # | Seção |
|:-:|:------|
| 18 | Expressões Regulares (Regex) — módulo `re` |
| 19 | SQL com MySQL — Bases de dados relacionais |
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
| SQLite | Banco de dados local (`sqlite3`) |
| MySQL | Banco de dados relacional (`pymysql`) |
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
