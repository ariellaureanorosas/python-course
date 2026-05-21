"""
EXERCÍCIO 12 - Map com partial para Aumentar Preços

Tópicos: map(), functools.partial
Aula: 113

Crie as funções abaixo usando map() e functools.partial.

1. Função `aumentar(preco: float, percentual: float) -> float`
   - Recebe um preço e um percentual de aumento (ex: 10 para 10%)
   - Retorna preco * (1 + percentual / 100)

2. Função `aplicar_aumento(precos: list[float], percentual: float) -> list[float]`
   - Usa functools.partial para fixar o percentual em `aumentar`
   - Usa map() para aplicar a função parcial a todos os preços
   - Retorna a lista de preços aumentados

3. Função `aplicar_descontos(precos: list[float]) -> list[float]`
   - Usa map() com lambda para aplicar descontos progressivos:
     - Preço <= 50: 5% de desconto
     - Preço <= 100: 10% de desconto
     - Preço > 100: 15% de desconto
"""

from functools import partial


def aumentar(preco: float, percentual: float) -> float:
    ...


def aplicar_aumento(precos: list[float], percentual: float) -> list[float]:
    ...


def aplicar_descontos(precos: list[float]) -> list[float]:
    ...
