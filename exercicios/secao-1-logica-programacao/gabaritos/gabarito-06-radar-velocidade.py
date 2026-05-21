"""
Verifica se a velocidade de um carro está dentro do limite e classifica
a multa em leve ou grave quando houver excesso.
"""

VELOCIDADE_MAXIMA: int = 80
PERCENTUAL_MULTA_LEVE: float = 10.0

try:
    velocidade_carro: float = float(input('Velocidade do carro (km/h): '))
except ValueError:
    print('Erro: digite um número válido para a velocidade.')
else:
    if velocidade_carro <= VELOCIDADE_MAXIMA:
        print('Dentro do limite. Sem multa.')
    else:
        porcentagem_excedida: float = (
            (velocidade_carro - VELOCIDADE_MAXIMA) / VELOCIDADE_MAXIMA * 100
        )
        if porcentagem_excedida <= PERCENTUAL_MULTA_LEVE:
            print(f'Multa leve — {porcentagem_excedida:.1f}% acima do limite.')
        else:
            print(f'Multa grave — {porcentagem_excedida:.1f}% acima do limite.')
