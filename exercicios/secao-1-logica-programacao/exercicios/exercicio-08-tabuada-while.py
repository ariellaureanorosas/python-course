"""
EXERCÍCIO 08 — Calculadora de Tabuada com while

Tópicos: input(), int, try/except, while, f-string, alinhamento

Receba um número inteiro e exiba a tabuada dele de 1 a 10.

Requisitos:
  - Use um laço while (NÃO use for).
  - Formate a saída com f-string usando alinhamento (> direita,
    ^ centralizado) para que os resultados fiquem organizados.
  - O formato deve ser parecido com:
         1 x  5 =   5
         2 x  5 =  10
         ...
        10 x  5 =  50
  - Caso o usuário digite algo que não seja número, exiba uma
    mensagem de erro com try/except.

Exemplo:
  Digite um número: 5
   1 x  5 =   5
   2 x  5 =  10
   3 x  5 =  15
   4 x  5 =  20
   5 x  5 =  25
   6 x  5 =  30
   7 x  5 =  35
   8 x  5 =  40
   9 x  5 =  45
  10 x  5 =  50

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
TABUADA = 10
while True:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("ERRO: Digite o valor correto no input")
    else:
        contador = 1
        while contador <= TABUADA:
            print(f"{contador} X {numero} = {contador * numero}")
            contador += 1
        break
