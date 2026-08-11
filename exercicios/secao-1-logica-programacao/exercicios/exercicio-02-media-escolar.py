"""
EXERCÍCIO 02 — Calculadora de Média Escolar

Tópicos: input(), float, f-string, if/else

Escreva um programa que receba 4 notas de um aluno via input(),
calcule a média aritmética e exiba o resultado.

Requisitos:
  - Cada nota deve ser convertida para float.
  - A média deve ser exibida com EXATAMENTE 2 casas decimais.
  - Use f-string para formatar a saída.
  - Se a média for >= 7, exiba "Aprovado"; caso contrário, "Reprovado".

Exemplo:
  Nota 1: 8.5
  Nota 2: 7.0
  Nota 3: 9.2
  Nota 4: 6.8
  Média: 7.88 — Aprovado

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
MEDIA_APROVAÇÃO: float = 7.0

lista_notas: list[float] = []
for i in range(1, 5):
    while True:
        try:
            nota = float(input(f"Digite a nota {i}: "))
            if 0 <= nota <= 10:
                lista_notas.append(nota)
                break
            else:
                print("Erro: A nota deve ser entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Erro: Digite um número válido.")
for chave, valor in enumerate(lista_notas):
    print(f"Nota {chave + 1}: {valor}")
media: float = sum(lista_notas) / len(lista_notas)
print(
    f"Média: {media} - APROVADO"
    if media == MEDIA_APROVAÇÃO
    else f"Media: {media} - REPROVADO"
)
