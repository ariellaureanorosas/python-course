"""
GABARITO — EXERCÍCIO 19 — Validador de CPF Completo

Valida CPF usando a lógica completa: limpeza com re.sub(), cálculo
do 1º e 2º dígitos verificadores, rejeição de sequências iguais.
"""

import re

cpf: str = input("Digite o CPF: ")

cpf_limpo: str = re.sub(r"\D", "", cpf)

if len(cpf_limpo) != 11:
    print("CPF inválido (deve ter 11 dígitos).")
else:
    if cpf_limpo == cpf_limpo[0] * len(cpf_limpo):
        print("CPF inválido (todos os dígitos iguais).")
    else:
        nove_digitos: str = cpf_limpo[:9]

        soma_primeiro: int = 0
        peso: int = 10
        for digito in nove_digitos:
            soma_primeiro += int(digito) * peso
            peso -= 1

        resto: int = soma_primeiro % 11
        primeiro_digito: int = 0 if resto < 2 else 11 - resto

        dez_digitos: str = nove_digitos + str(primeiro_digito)

        soma_segundo: int = 0
        peso = 11
        for digito in dez_digitos:
            soma_segundo += int(digito) * peso
            peso -= 1

        resto = soma_segundo % 11
        segundo_digito: int = 0 if resto < 2 else 11 - resto

        cpf_calculado: str = f"{nove_digitos}{primeiro_digito}{segundo_digito}"

        if cpf_limpo == cpf_calculado:
            print("CPF válido")
        else:
            print("CPF inválido")
