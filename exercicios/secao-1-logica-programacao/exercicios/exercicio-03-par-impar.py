"""
Exercício 03 — Par ou Ímpar com Validação

Receba um número inteiro do usuário e informe se ele é par ou ímpar.

Requisitos:
  - Use try/except para garantir que o valor digitado é um número
    inteiro válido. Caso não seja, exiba "Erro: digite um número
    inteiro válido." e encerre o programa.
  - Use o operador % para determinar paridade.
  - O programa deve funcionar tanto para números positivos quanto
    para negativos (0 é par).

Exemplos:
  Digite um número: 7
  7 é ímpar.

  Digite um número: -4
  -4 é par.

  Digite um número: abc
  Erro: digite um número inteiro válido.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

try:
    numero: int = int(input("Digite um valor: "))
except TypeError:
    print("Digite um Número")
else:
    paridade: str = "par" if numero % 2 == 0 else "impar"
    print(f"{numero} é {paridade}")
finally:
    print("-" * 15)
    print("Deus seja Louvado")
