# Closures

## Função que Retorna Função

```python
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

dizer_oi = criar_saudacao("Olá")
dizer_tchau = criar_saudacao("Tchau")

dizer_oi("João")    # "Olá, João!"
dizer_tchau("Ana")  # "Tchau, Ana!"
```

## Exemplo: Multiplicador

```python
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

dobro(10)   # 20
triplo(10)  # 30
```

## `nonlocal` — modificar escopo externo

```python
def contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

c = contador()
c()  # 1
c()  # 2
c()  # 3
```
