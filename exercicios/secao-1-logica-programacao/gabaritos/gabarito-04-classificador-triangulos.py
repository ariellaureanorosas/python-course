"""
Gabarito EXERCÍCIO 04 - Classificador de Triângulos

Raciocínio sênior
-----------------
A ordem dos elif é o segredo: validar a existência do triângulo
ANTES de classificar evita classificar lados impossíveis. A
validação (>= soma dos outros dois) é feita por combinação — são
as 3 condições do enunciado, sem compará-las par a par.
Alternativas descartadas: classificar equilátero/isósceles antes de
validar (classificaria "2, 1, 1" como isósceles, embora não exista;
e "0, 0, 0" como equilátero).
"""

try:
    lado_1: float = float(input("Primeiro lado: "))
    lado_2: float = float(input("Segundo lado: "))
    lado_3: float = float(input("Terceiro lado: "))
except ValueError:
    print("Erro: todos os lados devem ser números válidos.")
else:
    if lado_1 <= 0 or lado_2 <= 0 or lado_3 <= 0:
        print("Erro: os lados devem ser maiores que zero.")
    elif (
        lado_1 >= lado_2 + lado_3
        or lado_2 >= lado_1 + lado_3
        or lado_3 >= lado_1 + lado_2
    ):
        print("Erro: estas medidas não formam um triângulo.")
    elif lado_1 == lado_2 == lado_3:
        print("Triângulo equilátero.")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")

# Onde você provavelmente divergiu:
# - comparou par a par (lado1 == lado2, lado1 == lado3, ...) em vez de
#   usar a cadeia lado_1 == lado_2 == lado_3
# - usou > em vez de >= na validação ("2, 2, 4" com >= é inválido;
#   com > passaria como isósceles e a geometria quebra)
# - validou depois de classificar (classificações falsas como "0,0,0"
#   equilátero)
# - não tratou ValueError na entrada dos lados
