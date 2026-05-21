"""
EXERCÍCIO 19 — Validador de CPF Completo

Receba um CPF do usuário (pode vir formatado ou só os números).
O programa deve validar o CPF seguindo os passos:

    1. Usar re.sub() para remover tudo que não for dígito (\D).
    2. Verificar se a string tem exatamente 11 dígitos.
    3. Rejeitar CPFs com todos os dígitos iguais
       (ex.: 111.111.111-11, 222.222.222-22).
    4. Calcular o 1º dígito verificador (pesos 10 a 2).
    5. Calcular o 2º dígito verificador (pesos 11 a 2).
    6. Comparar os dígitos calculados com os informados.
    7. Exibir "CPF válido" ou "CPF inválido".

Exemplo:
    Digite o CPF: 529.982.247-25
    CPF válido

Dica: import re e use re.sub(r'\D', '', cpf) para limpar.
"""

import re

cpf = input("Digite o CPF: ")

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
