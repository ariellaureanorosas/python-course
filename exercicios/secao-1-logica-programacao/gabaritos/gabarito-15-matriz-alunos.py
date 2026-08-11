"""
Gabarito EXERCÍCIO 15 - Matriz de Alunos (Lista de Listas)

Raciocínio sênior
-----------------
Dois problemas separados em duas fases: montar a matriz (for
aninhado + validação de cada nota) e exibir (for aninhado para
média + formatação). O laço interno de entrada usa while True com
break no sucesso — o padrão clássico "peça de novo enquanto for
inválido" que você reencontrará em CLIs profissionais.
LARGURA_LINHA é uma constante que controla o cabeçalho do boletim
e a linha de "=" — consistência visual sem números mágicos.

Alternativas descartadas: exibir no mesmo loop que lê (misturar
entrada com saída); list comprehension para a média (avançado
demais aqui — o exercício pede o for aninhado).
"""

QUANTIDADE_ALUNOS: int = 3
QUANTIDADE_NOTAS: int = 3
LARGURA_LINHA: int = 50

matriz_notas: list[list[float]] = []

for aluno_atual in range(1, QUANTIDADE_ALUNOS + 1):
    notas_aluno: list[float] = []
    for nota_atual in range(1, QUANTIDADE_NOTAS + 1):
        while True:
            try:
                valor_nota: float = float(
                    input(f'Nota {nota_atual} do Aluno {aluno_atual}: ')
                )
                break
            except ValueError:
                print('Erro: digite um número válido (use ponto para decimais).')
        notas_aluno.append(valor_nota)
    matriz_notas.append(notas_aluno)

print(f'\n{"=" * LARGURA_LINHA}')
print('BOLETIM'.center(LARGURA_LINHA))
print(f'{"=" * LARGURA_LINHA}')

for indice_aluno, notas in enumerate(matriz_notas, start=1):
    soma_notas: float = 0
    for nota in notas:
        soma_notas += nota

    media_aluno: float = soma_notas / QUANTIDADE_NOTAS

    notas_formatadas: list[str] = []
    for nota in notas:
        notas_formatadas.append(f'{nota:5.1f}')
    notas_linha: str = '  '.join(notas_formatadas)

    print(f'Aluno {indice_aluno}:  {notas_linha}  |  Média: {media_aluno:.2f}')

# Onde você provavelmente divergiu:
# - digitou `list` sem tipos (aqui list[list[float]] e list[float])
# - misturou leitura e exibição no mesmo loop (aqui: monta a matriz
#   primeiro, exibe depois)
# - leu as 9 notas "na mão" em 9 variáveis em vez de usar a matriz
#   (o exercício é sobre listas de listas)
# - não validou a nota com while True/break (entrada inválida derruba
#   o programa), e
# - esqueceu de fechar o "=" * LARGURA_LINHA com f-string (format
#   com {expr} dentro do f-string é a forma correta)