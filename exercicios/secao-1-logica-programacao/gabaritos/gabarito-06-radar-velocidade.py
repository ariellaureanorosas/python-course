"""
Gabarito EXERCÍCIO 06 - Radar de Velocidade

Raciocínio sênior
-----------------
Primeiro se valida o dado (negativa é fisicamente impossível),
depois se compara a velocidade ao limite e só então se calcula a
porcentagem — quem está dentro do limite nunca paga custo de um
cálculo inútil.
O limiar da multa leve é <= 10% (inclusive): exatamente 10% acima
ainda é multa leve; mais que 10% é grave. Isso fecha todas as
faixas sem buraco lógico.
Alternativas descartadas: usar uma lista de mensagens indexada
(esconde o fluxo de decisão em índices mágicos 0, 1, 2).
"""

VELOCIDADE_MAXIMA: int = 80
PERCENTUAL_MULTA_LEVE: float = 10.0

try:
    velocidade_carro: float = float(input('Velocidade do carro (km/h): '))
except ValueError:
    print('Erro: digite um número válido para a velocidade.')
else:
    if velocidade_carro < 0:
        print('Erro: a velocidade não pode ser negativa.')
    elif velocidade_carro <= VELOCIDADE_MAXIMA:
        print('Dentro do limite. Sem multa.')
    else:
        porcentagem_excedida: float = (
            (velocidade_carro - VELOCIDADE_MAXIMA) / VELOCIDADE_MAXIMA * 100
        )
        if porcentagem_excedida <= PERCENTUAL_MULTA_LEVE:
            print('Multa leve — até 10% acima do limite.')
        else:
            print('Multa grave — acima de 10% do limite.')

# Onde você provavelmente divergiu:
# - testou diferenca == 10.0 (fraco: 5% de excesso virava multa grave;
#   e comparação de float com == é frágil — aqui usamos <= no percentual)
# - usou VELOCIDADE_MAXIMA = 100 em vez de 80 (o enunciado sugere 80)
# - não validou velocidade negativa (um radar recebe -5 km/h e
#   "multava" por estar dentro do limite)
# - usou uma lista de frases com índices 0/1/2 (a decisão vira
#   adivinhação de índice em vez de if/elif legível)
# - arredondou a porcentagem no meio do caminho (precisa ser exata
#   até a comparação; só a exibição formata)