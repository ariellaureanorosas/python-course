"""
Matriz de Alunos — Boletim Escolar (Lista de Listas)

Cria uma matriz 3x3 de notas de alunos, calcula a média de cada
um utilizando loops aninhados e exibe os resultados formatados
em forma de tabela (boletim).
"""

QUANTIDADE_ALUNOS: int = 3
QUANTIDADE_NOTAS: int = 3
LARGURA_LINHA: int = 50

matriz_notas: list = []

for aluno_atual in range(1, QUANTIDADE_ALUNOS + 1):
    notas_aluno: list = []
    for nota_atual in range(1, QUANTIDADE_NOTAS + 1):
        while True:
            try:
                valor_nota: float = float(
                    input(f"Nota {nota_atual} do Aluno {aluno_atual}: ")
                )
                break
            except ValueError:
                print("Erro: digite um número válido (use ponto para decimais).")
        notas_aluno.append(valor_nota)
    matriz_notas.append(notas_aluno)

print(f"\n{'=' * LARGURA_LINHA}")
print("BOLETIM".center(LARGURA_LINHA))
print(f"{'=' * LARGURA_LINHA}")

for indice_aluno, notas in enumerate(matriz_notas, start=1):
    soma_notas: float = 0
    for nota in notas:
        soma_notas += nota

    media_aluno: float = soma_notas / QUANTIDADE_NOTAS

    notas_formatadas: list = []
    for nota in notas:
        notas_formatadas.append(f"{nota:5.1f}")
    notas_linha: str = "  ".join(notas_formatadas)

    print(f"Aluno {indice_aluno}:  {notas_linha}  |  Média: {media_aluno:.2f}")
