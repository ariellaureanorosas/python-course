# Dicionários (dict)

## Criação
```python
d = {"nome": "João", "idade": 30}
d = dict(nome="João", idade=30)
vazio = {}
```

## Acesso e Manipulação
```python
d["nome"]               # "João" (KeyError se não existir)
d.get("nome")           # "João" (None se não existir)
d.get("nome", "padrão") # com valor padrão

d["email"] = "joao@email.com"  # criar/alterar
del d["idade"]                  # deletar
```

## Métodos Principais
```python
d.keys()        # dict_keys(['nome', 'idade'])
d.values()      # dict_values(['João', 30])
d.items()       # dict_items([('nome', 'João'), ('idade', 30)])

d.setdefault("cargo", "DEV")  # só define se não existir

d.copy()              # shallow copy
copy.deepcopy(d)      # deep copy (import copy)

d.pop("idade")        # remove e retorna
d.popitem()           # remove último
d.update({"a": 1})    # atualiza com outro dict
```

## Iteração
```python
for chave in d:
    print(chave, d[chave])

for chave, valor in d.items():
    print(chave, valor)
```
