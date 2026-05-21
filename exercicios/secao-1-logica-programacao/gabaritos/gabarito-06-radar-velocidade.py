"""
Gabarito 06 — Radar de Velocidade
"""

VELOCIDADE_MAXIMA: int = 80

vel_carro: float = float(input('Velocidade do carro (km/h): '))

if vel_carro <= VELOCIDADE_MAXIMA:
    print('Dentro do limite. Sem multa.')
else:
    diff: float = (vel_carro - VELOCIDADE_MAXIMA) / VELOCIDADE_MAXIMA * 100
    if diff <= 10:
        print('Multa leve — até 10% acima do limite.')
    else:
        print('Multa grave — acima de 10% do limite.')
