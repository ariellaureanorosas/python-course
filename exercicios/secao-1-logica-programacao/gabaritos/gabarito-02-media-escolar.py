"""
Gabarito EXERCÍCIO 02 - Calculadora de Média Escolar

Raciocínio sênior
-----------------
A média é um cálculo puro; a leitura das notas e o tratamento de
erro ficam isolados no try/except para o fluxo principal não se
misturar com a validação. A regra de aprovação usa uma constante
(MEDIA_MINIMA_APROVACAO) em vez de um "número mágico" pelo código.
Alternativas descartadas: list comprehension com sum() — legível
para quem está além deste ponto, mas aqui o objetivo é dominar
variáveis e if/else passo a passo.
"""

MEDIA_MINIMA_APROVACAO: float = 7.0
QUANTIDADE_NOTAS: int = 4

try:
    nota_1: float = float(input('Nota 1: '))
    nota_2: float = float(input('Nota 2: '))
    nota_3: float = float(input('Nota 3: '))
    nota_4: float = float(input('Nota 4: '))
except ValueError:
    print('Erro: todas as notas devem ser números válidos.')
else:
    media: float = (nota_1 + nota_2 + nota_3 + nota_4) / QUANTIDADE_NOTAS
    status: str = 'Aprovado' if media >= MEDIA_MINIMA_APROVACAO else 'Reprovado'
    print(f'Média: {media:.2f} — {status}')

# Onde você provavelmente divergiu:
# - separou a leitura em try/except e a média no else (o except captura
#   só a conversão; o cálculo não roda se a leitura falhar)
# - usou "APROVADO"/"REPROVADO" em maiúsculas (o enunciado pede
#   "Aprovado"/"Reprovado")
# - somou as notas sem QUANTIDADE_NOTAS como constante (4 espalhado)
# - usou .2f na média, não no status — a formatação é só do número