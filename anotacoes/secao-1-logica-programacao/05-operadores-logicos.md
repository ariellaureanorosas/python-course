# Operadores Lógicos

## and (e) — todas precisam ser True
```python
if usuario == "admin" and senha == "123":
    print("Login autorizado")
```

## or (ou) — qualquer True já basta
```python
if idade < 18 or altura < 1.50:
    print("Não pode entrar")
```

## not (não) — inverte
```python
if not senha:
    print("Senha vazia!")
```

## in / not in — verifica pertencimento
```python
if "a" in nome:
    print("Tem letra 'a'")
if "z" not in nome:
    print("Não tem letra 'z'")
```

## Valores Falsy
```python
0, 0.0, "", '', False, None, [], {}, set(), range(0)
# Qualquer outro valor é Truthy
```

## Curto-Circuito
```python
# and para na primeira condição falsa
# or para na primeira condição verdadeira
nome = input("Nome: ") or "Sem nome"  # se vazio, usa padrão
```
