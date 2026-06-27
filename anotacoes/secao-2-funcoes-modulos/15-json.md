# JSON

Usado para salvar e carregar dados estruturados no formato JSON (trocas entre sistemas).

## Escrever JSON

```python
import json

dados = {
    "nome": "João",
    "idade": 30,
    "email": "joao@email.com"
}

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)
```

## Ler JSON

```python
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
```

## Operações em Memória

```python
# dict → string JSON
string_json = json.dumps(dados, indent=2, ensure_ascii=False)

# string JSON → dict
dados = json.loads(string_json)
```

## Parâmetros Importantes

```python
indent=2              # formata com indentação
ensure_ascii=False    # preserva acentos
sort_keys=True        # ordena chaves
```

## Exemplo: Lista de Tarefas

```python
def ler_tarefas():
    try:
        with open("tarefas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as f:
        json.dump(tarefas, f, indent=2)
```
