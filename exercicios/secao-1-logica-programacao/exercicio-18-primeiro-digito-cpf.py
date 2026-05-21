"""
EXERCÍCIO 18 — Primeiro Dígito Verificador do CPF

Receba 9 dígitos (o CPF sem os dois dígitos verificadores).
Calcule o primeiro dígito verificador usando a lógica das aulas 63-65:

    1. Multiplique cada um dos 9 dígitos pelos pesos de 10 até 2.
    2. Some todos os resultados.
    3. Calcule o resto da divisão por 11 (soma % 11).
    4. Se o resto for menor que 2, o primeiro dígito é 0.
       Caso contrário, o primeiro dígito é 11 - resto.

Exiba o CPF parcial com 10 dígitos (9 + 1º dígito verificador).

Exemplo:
    Digite 9 dígitos: 123456789
    CPF parcial: 123.456.789-0   (formato opcional)
"""

cpf = input("Digite os 9 primeiros dígitos do CPF: ")

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
