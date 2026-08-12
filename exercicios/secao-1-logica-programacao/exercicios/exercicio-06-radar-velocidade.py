"""
EXERCÍCIO 06 — Radar de Velocidade

Tópicos: constantes, input(), int, try/except, if/elif/else, porcentagem

Crie um programa que simule um radar de trânsito.

Regras:
  - Defina VELOCIDADE_MAXIMA como constante (ex.: 80 km/h).
  - Leia a velocidade do carro via input().
  - Calcule a diferença percentual:
        diff = (vel_carro - vel_max) / vel_max * 100
  - Se a velocidade estiver dentro do limite (<= máxima), exiba
    "Dentro do limite. Sem multa."
  - Se ultrapassar em até 10% (inclusive), exiba
    "Multa leve — até 10% acima do limite."
  - Se ultrapassar em mais de 10%, exiba
    "Multa grave — acima de 10% do limite."
  - Use operadores de comparação (>, <=) e lógicos (and, or) se
    necessário.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

VELOCIDADE_MAXIMA = 100
PERCENTUAL_MULTA_LEVE = 10.0

while True:
    try:
        velocidade_carro: float = float(input("Digite a velocidade do carro: "))
    except ValueError:
        print("ERRO: digite corretamente a velocidade")
    else:
        if velocidade_carro < 0:
            print("velocidade inválida")
        elif velocidade_carro < VELOCIDADE_MAXIMA:
            print("Dentro do limite. Sem multa.")
        else:
            diff: float = (
                (velocidade_carro - VELOCIDADE_MAXIMA) / VELOCIDADE_MAXIMA * 100
            )
            if diff <= PERCENTUAL_MULTA_LEVE:
                print("Multa leve — até 10% acima do limite.")
            else:
                print("Multa grave — acima de 10% do limite.")
        break
