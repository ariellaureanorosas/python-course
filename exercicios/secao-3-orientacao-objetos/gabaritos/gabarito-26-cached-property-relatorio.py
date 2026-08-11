"""
Gabarito EXERCÍCIO 26 - Relatorio com Cache (functools.cached_property)

Raciocínio sênior
-----------------
O ponto é deixar o CACHE ser infraestrutura, não lógica: o
cached_property calcula na primeira leitura e guarda no __dict__
da instância — as leituras seguintes nunca re-executam a função.
A cópia defensiva `list(vendas)` no __init__ impõe o principal
contrato do encapsulamento (o caller não controla o estado
interno). media chama self.total (e não sum de novo) para
REAPROVEITAR o cache do total — somar duas vezes seria o
anti-padrão que o exercício quer evitar. `del r.total` remove a
chave do __dict__ e o recálculo volta a acontecer: a demo mostra
invalidação de cache sem criar um setter manual.
"""

from __future__ import annotations

from functools import cached_property


class Relatorio:
    """Relatorio de vendas com totais cacheados na instancia."""

    def __init__(self, vendas: list[float]) -> None:
        self.__vendas = list(vendas)

    @cached_property
    def total(self) -> float:
        """Soma de todas as vendas; calculada uma unica vez por instancia.

        Exemplos:
        >>> r = Relatorio([10.0, 20.0, 30.0])
        >>> r.total
        60.0
        >>> r.total
        60.0
        """
        return sum(self.__vendas)

    @cached_property
    def media(self) -> float:
        """Media das vendas; reaproveita o total ja cacheado.

        Exemplos:
        >>> r = Relatorio([10.0, 20.0, 30.0])
        >>> r.media
        20.0
        >>> 'total' in r.__dict__
        True
        """
        return self.total / len(self.__vendas)

    def __repr__(self) -> str:
        """Representacao textual para depuracao.

        Exemplos:
        >>> Relatorio([10.0, 20.0, 30.0])
        Relatorio(vendas=[10.0, 20.0, 30.0])
        >>> r = Relatorio([10.0, 20.0, 30.0])
        >>> r.total
        60.0
        >>> del r.total
        >>> r.total
        60.0
        """
        return f'Relatorio(vendas={self.__vendas!r})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - guardou self.vendas = vendas SEM cópia (o caller podia alterar
#   o relatório por fora; list(vendas) corta a referência)
# - calculou a média com sum() de novo em vez de self.total (perde
#   o reaproveitamento do cache — a ideia central do exercício)
# - tentou emular o cache com if hasattr(self, '_total') na mão
#   (cached_property já faz isso, sem código de cache espalhado)
# - esqueceu que cached_property NÃO funciona com __slots__: ele
#   grava o valor no __dict__ da instância (é o que `'total' in
#   r.__dict__` mostra)