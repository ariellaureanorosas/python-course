"""
Validador de CPF Completo

Valida um CPF utilizando o algoritmo completo: limpeza com re.sub(),
cálculo do primeiro e segundo dígitos verificadores, e rejeição de
sequências com todos os dígitos iguais.
"""

import re

DIGITOS_CPF: int = 11
DIGITOS_NOVE: int = 9
DIGITOS_DEZ: int = 10
PESO_PRIMEIRO: int = 10
PESO_SEGUNDO: int = 11
DIVISOR_CPF: int = 11
LIMITE_RESTA: int = 2

cpf_informado: str = input("Digite o CPF para validação: ")
cpf_limpo: str = re.sub(r"\D", "", cpf_informado)

if len(cpf_limpo) != DIGITOS_CPF:
    print(f"Erro: o CPF deve conter exatamente {DIGITOS_CPF} dígitos.")

elif cpf_limpo == cpf_limpo[0] * DIGITOS_CPF:
    print("Erro: CPF inválido — todos os dígitos são iguais.")

else:
    nove_primeiros: str = cpf_limpo[:DIGITOS_NOVE]

    soma_primeiro: int = 0
    peso_atual: int = PESO_PRIMEIRO
    for digito in nove_primeiros:
        soma_primeiro += int(digito) * peso_atual
        peso_atual -= 1

    resto_primeiro: int = soma_primeiro % DIVISOR_CPF
    primeiro_digito: int = (
        0 if resto_primeiro < LIMITE_RESTA else DIVISOR_CPF - resto_primeiro
    )

    dez_primeiros: str = nove_primeiros + str(primeiro_digito)

    soma_segundo: int = 0
    peso_atual = PESO_SEGUNDO
    for digito in dez_primeiros:
        soma_segundo += int(digito) * peso_atual
        peso_atual -= 1

    resto_segundo: int = soma_segundo % DIVISOR_CPF
    segundo_digito: int = (
        0 if resto_segundo < LIMITE_RESTA else DIVISOR_CPF - resto_segundo
    )

    cpf_calculado: str = f"{nove_primeiros}{primeiro_digito}{segundo_digito}"

    if cpf_limpo == cpf_calculado:
        print("CPF válido.")
    else:
        print("CPF inválido — dígitos verificadores não conferem.")
