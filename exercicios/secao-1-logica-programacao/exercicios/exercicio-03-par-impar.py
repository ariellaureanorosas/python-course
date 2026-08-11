"""
EXERCÍCIO 03 — Par ou Ímpar com Validação

Tópicos: input(), int, try/except, operador %

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

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

while True:
    try:
        numero = int(input("Digite o número: "))
    except ValueError:
        print("ERRO: Digite o valor correto")
    else:
        print(f"{numero} é par" if numero % 2 == 0 else f"{numero} é impar")
        pergunta = input("Deseja continuar: [S]-[N] ").lower()
        if pergunta.__contains__("n"):
            break
