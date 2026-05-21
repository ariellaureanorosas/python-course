# JSON

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

## Operações Diretas
```python
# dict → string JSON
string_json = json.dumps(dados, indent=2, ensure_ascii=False)

# string JSON → dict
dados = json.loads(string_json)
```

## Parâmetros Importantes
```python
indent=2              # formata com indentação
ensure_ascii=False    # preserva acentos (ñ vira \u00f1)
sort_keys=True        # ordena chaves alfabeticamente
```

## Projeto: Lista de Tarefas com JSON
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
