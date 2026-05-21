"""
EXERCÍCIO 14 - Reduce para Calcular Total

Tópicos: functools.reduce, sum(), generator expressions
Aula: 115

Considere a estrutura de produto:
    produto = {"nome": "Camiseta", "preco": 59.90, "quantidade": 10}

Crie as funções abaixo.

1. Função `calcular_total_estoque(produtos: list[dict]) -> float`
   - Usa functools.reduce() para somar preco * quantidade de cada produto
   - Retorna o valor total do estoque

2. Função `calcular_total_sum(produtos: list[dict]) -> float`
   - Usa sum() com generator expression para obter o mesmo resultado
   - Retorna o valor total do estoque

3. Função `calcular_total_com_desconto(produtos: list[dict], desconto: float) -> float`
   - Usa reduce() para somar preco * quantidade, mas aplica `desconto` percentual
     no preço de cada produto antes de somar
   - Retorna o valor total com desconto

Dica: Para o reduce, importe functools.reduce
"""

from functools import reduce


def calcular_total_estoque(produtos: list[dict]) -> float:
    ...


def calcular_total_sum(produtos: list[dict]) -> float:
    ...


def calcular_total_com_desconto(produtos: list[dict], desconto: float) -> float:
    ...
