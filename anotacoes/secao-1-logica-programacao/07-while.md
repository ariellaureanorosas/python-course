# Loop while

## Estrutura Básica
```python
while condicao:
    bloco
```

## break — interrompe
```python
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando == "sair":
        break
```

## continue — pula para próxima iteração
```python
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue  # pula o 5
    print(contador)
```

## while / else
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Loop terminou sem break!")
```

## Operadores de Atribuição
```python
contador += 1   # contador = contador + 1
contador -= 1   # contador = contador - 1
contador *= 2   # contador = contador * 2
contador /= 2   # contador = contador / 2
```
