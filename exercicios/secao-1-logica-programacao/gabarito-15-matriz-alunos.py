"""
GABARITO — EXERCÍCIO 15 — Matriz de Alunos (Lista de Listas)

Cria uma matriz 3x3 de notas, calcula médias com for aninhado e exibe
em formato de tabela.
"""

matriz: list = []
QUANTIDADE_ALUNOS: int = 3
QUANTIDADE_NOTAS: int = 3

for aluno in range(1, QUANTIDADE_ALUNOS + 1):
    linha: list = []
    for nota in range(1, QUANTIDADE_NOTAS + 1):
        valor: float = float(input(f"Nota {nota} do Aluno {aluno}: "))
        linha.append(valor)
    matriz.append(linha)

print("\n" + "=" * 50)
print("BOLETIM".center(50))
print("=" * 50)

for i, linha in enumerate(matriz, start=1):
    soma: float = 0
    for nota in linha:
        soma += nota

    media: float = soma / QUANTIDADE_NOTAS
    med_arredondada: float = round(media, 2)

    notas_str: str = "  ".join(f"{n:5.1f}" for n in linha)
    print(f"Aluno {i}:  {notas_str}  |  Média: {med_arredondada:.2f}")
