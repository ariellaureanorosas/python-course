"""
EXERCÍCIO 22 — Calculadora com while

Tópicos: while, if/elif, operadores aritméticos, flag de saída

Crie uma calculadora de terminal com menu:

  - Digite 1 para SOMAR, 2 para SUBTRAIR, 3 para MULTIPLICAR,
    4 para DIVIDIR ou 5 para SAIR.
  - Para as operações, leia dois números (float).
  - Divisão por zero deve exibir "Erro: divisão por zero." sem
    travar o programa (use try/except ZeroDivisionError).
  - O menu repete até o usuário escolher 5.
  - Opção inválida exibe "Opção inválida." e volta ao menu.

Exemplo de saída esperada:
=== CALCULADORA ===
1) Somar  2) Subtrair  3) Multiplicar  4) Dividir  5) Sair
Opção: 4
Primeiro número: 10
Segundo número: 0
Erro: divisão por zero.

Dica: leia a opção como string para comparar com "5" sem conversão.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

while True:
    try:
        opcao = int(
            input(
                "Digite 1 para SOMAR, 2 para SUBTRAIR, 3 para MULTIPLICAR, 4 para DIVIDIR ou 5 para SAIR: "
            )
        )
        if opcao not in [1, 2, 3, 4, 5]:
            print("Digite apenas as opções acima")
        if opcao == 5:
            print("você decidiu sair")
            break
        try:
            numero_1 = float(input("Digite o primeiro número: "))
            numero_2 = float(input("Digite o segundo número: "))
            match opcao:
                case 1:
                    print(numero_1 + numero_2)
                case 2:
                    print(numero_1 - numero_2)
                case 3:
                    print(numero_1 * numero_2)
                case 4:
                    try:
                        resultado_divisão: float = numero_1 / numero_2
                    except ZeroDivisionError:
                        print("erro ao dividir por zero")
        except ValueError:
            print("Digite apenas números")
    except ValueError:
        print("Digite apenas números")
