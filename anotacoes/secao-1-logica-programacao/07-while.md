# Loop `while`

Usado para repetir blocos de código enquanto uma condição for verdadeira.

## Estrutura

```python
while condicao:
    bloco
```

## `break` — interrompe

```python
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando == "sair":
        break
```

## `continue` — pula para próxima iteração

```python
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print(contador)  # 1,2,3,4,6,7,8,9,10
```

## `while` / `else`

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Loop terminou sem break")
```

## Operadores de Atribuição

```python
contador += 1    # contador = contador + 1
contador -= 1    # contador = contador - 1
contador *= 2    # contador = contador * 2
contador /= 2    # contador = contador / 2
```
