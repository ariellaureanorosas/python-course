"""
Exercício 02 — Calculadora de Média Escolar

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
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

MEDIA = 7.0
QNTD_NOTAS = 4

try:
    LISTA_NOTAS: list[float] = [
        float(input(f"Digite a nota {i}: "))
        for i, _ in enumerate(range(0, QNTD_NOTAS, 1), 1)
    ]
except ValueError:
    print("A nota deve ser um número válido")
else:
    media_somada = sum(LISTA_NOTAS) / QNTD_NOTAS
    print(f"Sua média final foi de: {media_somada:.2f}")
    print(f"Seu status é: {'APROVADO' if media_somada >= MEDIA else 'REPROVADO'}")
finally:
    print("Deus seja Louvado")
