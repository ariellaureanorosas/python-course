"""
Gabarito 02 — Calculadora de Média Escolar
"""

nota_1: float = float(input('Nota 1: '))
nota_2: float = float(input('Nota 2: '))
nota_3: float = float(input('Nota 3: '))
nota_4: float = float(input('Nota 4: '))

media: float = (nota_1 + nota_2 + nota_3 + nota_4) / 4

status: str = 'Aprovado' if media >= 7 else 'Reprovado'

print(f'Média: {media:.2f} — {status}')
