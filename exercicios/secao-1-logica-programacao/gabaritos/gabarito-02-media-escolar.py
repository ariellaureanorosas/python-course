"""
Calcula a média aritmética de quatro notas e informa se o aluno foi
aprovado ou reprovado.
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
