"""
EXERCÍCIO 18 - Combinar map/filter/reduce em Pipeline

Tópicos: filter(), map(), functools.reduce (integração)
Aulas: 113-115

Crie funções que combinam filter, map e reduce em um pipeline de processamento.

1. Função `processar_numeros(numeros: list[int]) -> int`
   - Pipeline completo:
     1. filter(): seleciona apenas números pares
     2. map(): eleva cada número ao quadrado
     3. reduce(): soma todos os resultados
   - Retorna o inteiro resultante

2. Função `processar_numeros_flexivel(
       numeros: list[int],
       *,
       pares: bool = True,
       expoente: int = 2,
   ) -> int`
   - Mesmo pipeline, mas com parâmetros keyword-only:
     - `pares`: se True, filtra apenas pares; se False, ímpares
     - `expoente`: expoente para elevar cada número
   - Usa reduce() para somar tudo

3. Função `processar_texto(palavras: list[str]) -> list[str]`
   - filter(): remove palavras com menos de 3 caracteres
   - map(): converte para maiúsculas
   - Retorna lista (NÃO usa reduce)
"""

from functools import reduce


def processar_numeros(numeros: list[int]) -> int:
    ...


def processar_numeros_flexivel(
    numeros: list[int],
    *,
    pares: bool = True,
    expoente: int = 2,
) -> int:
    ...


def processar_texto(palavras: list[str]) -> list[str]:
    ...
