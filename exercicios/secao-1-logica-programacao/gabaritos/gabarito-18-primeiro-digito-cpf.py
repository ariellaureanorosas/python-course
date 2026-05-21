"""
GABARITO — EXERCÍCIO 18 — Primeiro Dígito Verificador do CPF

Recebe 9 dígitos, calcula o primeiro dígito verificador pela lógica
das aulas 63-65 e exibe o CPF parcial com 10 dígitos.
"""

cpf: str = input("Digite os 9 primeiros dígitos do CPF: ")

if len(cpf) != 9 or not cpf.isdigit():
    print("Erro: digite exatamente 9 números.")
else:
    soma: int = 0
    peso: int = 10

    for digito in cpf:
        soma += int(digito) * peso
        peso -= 1

    resto: int = soma % 11
    primeiro_digito: int = 0 if resto < 2 else 11 - resto

    cpf_parcial: str = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{primeiro_digito}"
    print(f"CPF parcial: {cpf_parcial}")
