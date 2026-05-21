# Closures

## Função que Retorna Função
```python
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

dizer_oi = criar_saudacao("Olá")
dizer_tchau = criar_saudacao("Tchau")

print(dizer_oi("João"))   # "Olá, João!"
print(dizer_tchau("Ana")) # "Tchau, Ana!"
```

## Exercício: Multiplicador
```python
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(10))   # 20
print(triplo(10))  # 30
```

## nonlocal — modificar variável do escopo externo
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
