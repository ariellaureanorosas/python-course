r"""
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

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
while True:
    cpf_input: str = input("Digite o CPF: ")
    cpf_limpo: str = re.sub(r"\D", "", cpf_input)

    if len(cpf_limpo) != 11:
        print("Digite 11 digitos")
        continue
    elif cpf_limpo == cpf_limpo[0] * 11:
        print("ERRO: Todos os digitos são iguais")
        continue
    else:
        nove_primeiros: str = cpf_limpo[:9]
        resultado_digito_10 = sum(
            int(digito) * (10 - indice) for indice, digito in enumerate(nove_primeiros)
        )

        digito_10: int = (
            0 if (resultado_digito_10 % 11) < 2 else 11 - (resultado_digito_10 % 11)
        )

        dez_primeiros: str = nove_primeiros + str(digito_10)

        resultado_digito_11 = sum(
            int(digito) * (11 - indice) for indice, digito in enumerate(dez_primeiros)
        )

        digito_11: int = (
            0 if (resultado_digito_11 % 11) < 2 else 11 - (resultado_digito_11 % 11)
        )

        cpf_calculado: str = f"{nove_primeiros}{digito_10}{digito_11}"

        if cpf_limpo == cpf_calculado:
            print("CPF válido")
        else:
            print("CPF inválido")
        break
