"""
GABARITO 12 - Map com partial para Aumentar Preços
"""

from functools import partial


def aumentar(preco: float, percentual: float) -> float:
    """Aplica um percentual de aumento sobre o preço.

    Args:
        preco: Valor original.
        percentual: Percentual de aumento (ex: 10 para 10%).

    Returns:
        Preço com aumento aplicado.
    """
    return preco * (1 + percentual / 100)


def aplicar_aumento(precos: list[float], percentual: float) -> list[float]:
    """Aplica um mesmo percentual de aumento a todos os preços.

    Usa partial para fixar o percentual e map para aplicar a lista.

    Args:
        precos: Lista de preços originais.
        percentual: Percentual de aumento.

    Returns:
        Lista de preços com aumento.
    """
    aumentar_com_percentual = partial(aumentar, percentual=percentual)
    return list(map(aumentar_com_percentual, precos))


def aplicar_descontos(precos: list[float]) -> list[float]:
    """Aplica descontos progressivos conforme a faixa de preço.

    Usa map com lambda para aplicar regras de desconto:
    - Preço <= 50: 5%
    - Preço <= 100: 10%
    - Preço > 100: 15%

    Args:
        precos: Lista de preços originais.

    Returns:
        Lista de preços com desconto aplicado.
    """
    return list(map(
        lambda p: p * 0.95 if p <= 50 else (
            p * 0.90 if p <= 100 else p * 0.85
        ),
        precos,
    ))
