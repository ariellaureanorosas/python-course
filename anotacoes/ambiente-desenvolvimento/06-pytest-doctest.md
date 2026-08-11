# Pytest e doctest — testes automáticos

## Quando você vai usar isso?
Quando o código deixa de ser "um script que eu rodo e vejo funcionar" e passa
a ser algo que você quer garantia de que continuará funcionando. O Pytest é o
framework de testes mais usado do Python. Neste repositório ele está configurado
no `pyproject.toml`, e os gabaritos das seções 2 e 3 já usam o primo dele: o
`doctest` (testes escritos dentro da docstring).

## Modelo mental
Teste automático é uma **rede de segurança**: você escreve "se eu chamar X com
entrada Y, a saída DEVE ser Z" e a máquina verifica isso milhões de vezes mais
rápido e sem esquecer. O doctest é o teste "embutido" — escreve o exemplo na
docstring com cara de conversa (`>>> validar_cpf("111.111.111-11")` + `False`),
e o Python executa esse exemplo e compara. O pytest é o teste "de verdade" —
funções `test_*` que rodam em paralelo (com o `pytest-xdist`) e produzem
relatórios coloridos.

## Em uma linha
Pytest roda os testes do projeto (e pode validar os doctests dos gabaritos);
é a garantia de que mudanças não quebraram o que já funcionava.

## Na prática

### A configuração DESTE projeto (pyproject.toml)

```toml
[tool.pytest.ini_options]
addopts = "-s --color=yes --tb=short"
```

| Flag | O que faz | Por quê |
|:----:|:----------|:--------|
| `-s` | não captura stdout | mostra os `print()` dos testes (os exercícios usam muito) |
| `--color=yes` | saída colorida | legibilidade |
| `--tb=short` | traceback curto | mostra só o essencial do erro |

### Rodando

```sh
uv run pytest                # roda tudo (procura test_*.py / *_test.py)
uv run pytest -v             # verbose: lista cada teste
uv run pytest arquivo.py     # roda os testes de um arquivo
uv run pytest -n auto        # paralelo (pytest-xdist)
```

### doctest — como os gabaritos do curso são validados

Os gabaritos (seções 2 e 3) já vêm com testes embutidos:

```python
def validar_cpf(cpf: str) -> bool:
    """Valida um CPF.

    >>> validar_cpf("529.982.247-25")
    True
    >>> validar_cpf("111.111.111-11")
    False
    """
    ...
```

Validar pelo terminal:

```sh
python -m doctest -v exercicios/secao-2-funcoes-modulos/gabaritos/gabarito-09-decorator-log.py
```

Ou rodar TODOS os doctests de uma vez com pytest:

```sh
uv run pytest --doctest-modules exercicios/
```

### pytest-xdist — o que ele agrega

```sh
uv run pytest -n auto    # roda os testes em N processos paralelos
```

- Acelera suítes grandes (seções futuras do curso terão MUITOS testes)
- `-n auto` usa todos os núcleos da sua máquina
- É o padrão do professor (`dev = ["pytest", "pytest-xdist"]`)

## O que NÃO fazer

```python
# ← ERRADO: teste que depende de input() do teclado
def test_menu():
    resposta = input("digite: ")   # ← trava o teste esperando alguém digitar
# ← o certo: refatorar para receber o valor por parâmetro e testar a função pura

# ← ERRADO: testar só o caminho feliz
def test_soma():
    assert soma(2, 3) == 5         # ← ok, mas...
# ← o certo: testar também o caso de erro (0, negativos, tipos errados)

# ← ERRADO: `assert` solto fora de testes como "validação de verdade"
# (assert é desligado com python -O em produção!)
# ← o certo: testes no pytest; validação real no código com if/raise

# ← ERRADO: print-debug no lugar de teste
# ← o certo: escrever o teste UMA vez e rodar quantas vezes precisar
```

## Por que Python funciona assim?
O doctest existe porque a documentação SEMPRE estava errada ("exemplo na
docstring desatualizado"). Executar os exemplos da docstring transforma a
documentação em teste que se auto-verifica. O pytest, por cima, usa a
convenção de descobrir arquivos `test_*.py`/`*_test.py` e funções `test_*` sem
configuração extra — e o `assert` nativo do Python vira a asserção do teste
(por isso o pytest não inventa sintaxe nova). O `-s` não capturar stdout é
crucial para os exercícios do curso, que ensinam com `print()`.

## Conexões
- Você já usou esse padrão quando: rodou `python -m doctest -v gabarito-XX.py`
  nos exercícios das seções 2 e 3 — o README do repositório documenta isso
- Aparece também em: nota 03-pyproject (`[tool.pytest.ini_options]`), nota
  08-vscode (`python.testing.pytestEnabled: true` — botão de testes na barra
  inferior do VS Code), nota 04-ruff (`per-file-ignores` de `tests/**`)
- Diferente de: doctest (teste na docstring), unittest (framework padrão mais
  verboso, desativado no settings.json), assert solto (não é teste automatizado)

---

## Teste de recuperação — responda sem olhar para cima

1. O que as flags `-s` e `--tb=short` fazem na config deste projeto?
2. Como validar um gabarito com doctest pelo terminal?
3. O que o pytest-xdist adiciona e como ativar?
4. Por que `assert` não substitui testes?

---

**Frase-âncora:** "Doctest prova a docstring; pytest prova o comportamento — e a rede pega antes de o bug virar produção."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
