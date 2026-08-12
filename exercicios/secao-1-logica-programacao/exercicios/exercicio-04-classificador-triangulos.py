"""
EXERCÍCIO 04 — Classificador de Triângulos

Tópicos: input(), float, try/except, if/elif/else, operadores lógicos

Receba 3 valores (lados de um triângulo) e determine se eles formam
um triângulo válido. Caso positivo, classifique-o em equilátero,
isósceles ou escaleno.

Regras para existência de um triângulo:
  - Cada lado deve ser menor que a soma dos outros dois (válido para
    todas as 3 combinações).
  - Nenhum lado pode ser zero ou negativo.

Classificação:
  - Equilátero: 3 lados iguais.
  - Isósceles: 2 lados iguais e 1 diferente.
  - Escaleno: 3 lados diferentes.

Dica: use if/elif/else encadeados.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
lados_triangulo: list[int] = []
try:
    for lado in range(1, 4):
        while True:
            lado = int(input(f"Digite o lado {lado} do triangulo: "))
            if lado > 0:
                lados_triangulo.append(lado)
                break
except ValueError:
    print("ERRO: Digite o valor correto")
else:
    lado_1, lado_2, lado_3 = lados_triangulo
    if (
        (lado_1 + lado_2 > lado_3)
        and (lado_1 + lado_3 > lado_2)
        and (lado_2 + lado_3 > lado_1)
    ):
        if lado_1 == lado_2 == lado_3:
            print("Equilátero")
        elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
            print("Escaleno")
        else:
            print("Isósceles")
    else:
        print("Triângulo Inválido")
