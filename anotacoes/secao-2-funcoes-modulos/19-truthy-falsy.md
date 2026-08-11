# Valores Truthy e Falsy

## Quando você vai usar isso?
Quando você escreve `if lista:` em vez de `if len(lista) > 0:`, ou `if usuario:` depois de um input que pode vir vazio. Entender o que é Truthy/Falsy é pré-requisito para ler metade dos códigos Python do mundo — condicionais, loops, `or`/`and` com fallback e funções que validam entrada.

## Modelo mental
Todo valor tem uma "personalidade booleana" nativa: ou é Falsy (finge ser False) ou é Truthy (finge ser True). Lista vazia, string vazia, 0 — todos são Falsy. "Qualquer coisa com conteúdo" é Truthy.

## Em uma linha
`bool(valor)` revela a personalidade: os valores Falsy do Python são escassos e memoráveis — os vazios, os zeros e o None.

## Na prática

### Caso simples — a lista oficial dos Falsy

```python
valores_falsy = [
    [],        # ← lista vazia
    {},        # ← dict vazio
    set(),     # ← set vazio
    (),        # ← tupla vazia
    "",        # ← string vazia
    0,         # ← zero (int)
    0.0,       # ← zero (float)
    0j,        # ← zero (complex)
    None,      # ← ausência de valor
    False,     # ← o próprio booleano
    range(0),  # ← range vazio
]

bool([])   # ← False
bool(" ")  # ← True! String com ESPAÇO tem conteúdo → é Truthy
bool("a")  # ← True
bool(42)   # ← True
```

### Com variação — o padrão `if not lista`

```python
tarefas = []

if not tarefas:                    # ← lê: "se não há tarefas"
    print("Nada a fazer")          # ← lista vazia é Falsy → entra aqui
# Equivalente ao verbose: if len(tarefas) == 0: (pior de ler)

entrada = input("Nome (opcional): ").strip()
if entrada:                        # ← Truthy = tem conteúdo
    print(f"Olá, {entrada}!")
```

### Em uso real — função que classifica

```python
def falsy(valor) -> str:
    return "falsy" if not valor else "truthy"

falsy([])      # ← 'falsy'
falsy("TESTE") # ← 'truthy'
falsy(None)    # ← 'falsy'
falsy([0])     # ← 'truthy' — lista COM um elemento, mesmo zero dentro
```

## O que NÃO fazer

```python
# ← ERRADO: comparar explicitamente o que o if já faz
if len(lista) == 0:          # ← verboso; o idioma é `if not lista:`
if x != "" and x is not None:  # ← idem; `if x:` cobre os dois

# ← CUIDADO: 0 e "" são Falsy, mas isso não é culpa deles — é regra
# Se 0 (nota) é um valor VÁLIDO da sua lógica, `if nota:` quebra;
# nesse caso explicite: `if nota is not None:` (nota 27 da Seção 1)
```

## Por que Python funciona assim?
A aula 90 mostra que os Falsy são exatamente os "vazios e zeros": coleções vazias, strings vazias, números zero e None/False. É uma escolha de design por consistência: `if not lista` e `if not texto` funcionam sempre, sem precisar lembrar de chamar `len()`. Em C, por exemplo, só o 0 (e NULL) é falso — em Python, todos os vazios também. A exceção clássica: `range(0)` é Falsy, mas `range(1)` é Truthy mesmo sendo um objeto — "vazio" aqui significa sem elementos.

## Conexões
- Você já usou esse padrão quando: `input() or "padrão"` no exercício 29 da Seção 1 — o `or` avalia o Falsy da string vazia e cai no padrão
- Aparece também em: `filter(None, lista)` (remove vazios), checagem de dicts/sets vazios, validação de formulários
- Diferente de: `is None` (identidade — só True quando é literalmente None) e de `== False` (comparação de valor, que 0 e "" também "ganham")

---

## Teste de recuperação — responda sem olhar para cima

1. Liste todos os valores Falsy básicos do Python.
2. Por que `bool(" ")` é True mas `bool("")` é False?
3. Escreva o idiomático para "se a lista não estiver vazia, mostre o primeiro item".

---

**Frase-âncora:** "Vazio, zero ou None: Falsy. Qualquer conteúdo: Truthy."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14