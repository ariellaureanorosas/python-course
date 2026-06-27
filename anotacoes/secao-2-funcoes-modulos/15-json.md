# JSON

## Quando você vai usar isso?
Sua aplicação precisa salvar uma lista de tarefas e carregá-la na próxima execução. Ou você está consumindo uma API que devolve dados do usuário. JSON é o formato universal de troca — leve, legível e suportado por toda linguagem. Em Python, você converte dict/lista nativa em JSON e vice-versa.

## Modelo mental
Uma máquina de moldar plástico: você tem um boneco de ação (dict/lista Python) e aperta um botão — ele vira um molde de texto (JSON). Outra máquina faz o caminho inverso: pega o molde de texto e produz o boneco idêntico.

## Em uma linha
Converta dicionários/ listas Python para string JSON e salve em arquivo, ou carregue de volta para objetos Python.

## Na prática

### Caso simples

```python
import json

dados = {
    "nome": "João",
    "idade": 30,
    "email": "joao@email.com"
}

with open("dados.json", "w", encoding="utf-8") as f:        # ← abre pra escrita
    json.dump(dados, f, indent=2, ensure_ascii=False)       # ← dict → arquivo JSON

with open("dados.json", "r", encoding="utf-8") as f:        # ← abre pra leitura
    dados_carregados = json.load(f)                          # ← arquivo JSON → dict
```

### Com variação

```python
import json

# dict → string (sem arquivo)
string_json = json.dumps(dados, indent=2, ensure_ascii=False)  # ← .dumps com 's' = string
print(string_json)                                               # ← '{"nome": "João", ...}'

# string → dict (sem arquivo)
dados = json.loads(string_json)                                  # ← .loads com 's' = string

# Parâmetros úteis
json.dump(dados, f, indent=2, ensure_ascii=False, sort_keys=True)  # ← chaves ordenadas A→Z
```

### Em uso real

```python
import json

def ler_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            return json.load(f)                              # ← carrega do disco
    except FileNotFoundError:
        return []                                            # ← se não existe, lista vazia

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)  # ← persiste no disco

tarefas = ler_tarefas()
tarefas.append({"id": 3, "desc": "Estudar JSON", "feito": False})
salvar_tarefas(tarefas)
```

## O que NÃO fazer

```python
dados = {"nome": "João", "idade": 30}
json.dumps(dados)                                            # ← sem ensure_ascii=False

# Resultado: '{"nome": "Jo\\u00e3o", "idade": 30}'
# ← Acentos viram escape \\u. Sempre use ensure_ascii=False.

json.dumps({"chave": "valor"}, indent=2)                     # ← certo
json.loads('{"chave": "valor",}')                            # ← ERRO: vírgula final!
# ← JSON não permite trailing comma, Python permite.
```

## Por que Python funciona assim?
`json.dump` / `json.load` trabalham com arquivos (recebem `file`); `json.dumps` / `json.loads` trabalham com strings (recebem `str`). O `s` no nome = **s**tring. `ensure_ascii=False` impede que caracteres Unicode (acentos, emojis) sejam escapados como `\\uXXXX` — ele mantém os caracteres reais no arquivo. `indent=2` insere quebras de linha e espaços para legibilidade. JSON nativo do Python mapeia: `dict` → objeto, `list` → array, `str` → string, `int/float` → número, `None` → null, `bool` → boolean.

## Conexões
- Você já usou esse padrão quando: salvou configurações do seu programa em `.json` em vez de `.txt`
- Aparece também em: APIs REST (`requests.get().json()`), arquivos de configuração (`package.json`, `tsconfig.json`)
- Diferente de: `pickle` serializa objetos Python arbitrários (mas não é seguro nem legível); CSV é tabela plana sem aninhamento

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `json.dump` e `json.dumps`?
2. Escreva uma função que recebe um dicionário e salva em `config.json` com indentação e acentos preservados.
3. O que acontece se você esquecer `ensure_ascii=False` ao salvar texto com acentos?

---

**Frase-âncora:** "Dict vira JSON, JSON vira dict — ponte entre Python e o mundo."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
