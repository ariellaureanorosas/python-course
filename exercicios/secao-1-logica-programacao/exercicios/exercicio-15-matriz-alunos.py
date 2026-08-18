"""
EXERCÍCIO 15 — Matriz de Alunos (Lista de Listas)

Tópicos: listas de listas, for aninhado, append()

Crie uma matriz 3x3 de notas de alunos.
Cada linha representa um aluno.
Cada coluna representa uma nota (3 notas por aluno).

O programa deve:
    1. Solicitar as 9 notas (3 alunos - 3 notas).
    2. Armazenar em uma lista de listas (matriz).
    3. Usar for aninhado para calcular a média de cada aluno.
    4. Exibir em formato de tabela.

Exemplo de saída:

    Aluno 1:  8.5   7.0   9.2  |  Média: 8.23
    Aluno 2:  6.0   5.5   7.8  |  Média: 6.43
    Aluno 3:  9.0   8.5   9.5  |  Média: 9.00

Dica: use append() para montar as linhas da matriz.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

lista_alunos: list[str] = []
matriz_notas: list[list[float]] = []

for _alunos in range(3):
    lista_notas: list[float] = []
    aluno: str = input("Digite o nome do aluno: ")
    lista_alunos.append(aluno)
    for numero_nota, _ in enumerate(range(3), start=1):
        while True:
            try:
                notas: float = float(input(f"Digite a nota {numero_nota}: "))
            except ValueError:
                print("Digite corretamente a nota")
            else:
                if not notas:
                    print("Digite um valor válido")
                elif notas < 0 or notas > 10:
                    print("A nota tem que ser maior >= 0 e <= que 10")
                else:
                    lista_notas.append(notas)
                    break
    matriz_notas.append(lista_notas)


for indice, pessoa in enumerate(lista_alunos):
    soma_notas: float = 0
    notas_do_aluno: list[float] = matriz_notas[indice]
    for nota in notas_do_aluno:
        soma_notas += nota
    media: float = soma_notas / len(notas_do_aluno)
    notas_formatadas: str = " ".join(f"{n:.2f}" for n in notas_do_aluno)
    print(f"Aluno: {pessoa} - Notas: {notas_formatadas} | Média: {media:.2f}")
