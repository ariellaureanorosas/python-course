"""
Primeiro Dígito Verificador do CPF

Solicita os 9 primeiros dígitos de um CPF, calcula o primeiro
dígito verificador conforme o algoritmo oficial e exibe o CPF
parcial com 10 dígitos formatado.
"""

DIGITOS_NOVE: int = 9
PESO_INICIAL: int = 10
DIVISOR_CPF: int = 11
LIMITE_RESTA: int = 2

cpf_digitado: str = input("Digite os 9 primeiros dígitos do CPF: ")

if not cpf_digitado.isdigit():
    print("Erro: digite apenas números.")
elif len(cpf_digitado) != DIGITOS_NOVE:
    print(f"Erro: digite exatamente {DIGITOS_NOVE} números.")
else:
    soma_produtos: int = 0
    peso_atual: int = PESO_INICIAL

    for digito in cpf_digitado:
        soma_produtos += int(digito) * peso_atual
        peso_atual -= 1

    resto_divisao: int = soma_produtos % DIVISOR_CPF
    primeiro_digito: int = (
        0 if resto_divisao < LIMITE_RESTA else DIVISOR_CPF - resto_divisao
    )

    cpf_parcial: str = (
        f"{cpf_digitado[:3]}.{cpf_digitado[3:6]}."
        f"{cpf_digitado[6:DIGITOS_NOVE]}-{primeiro_digito}"
    )
    print(f"CPF parcial: {cpf_parcial}")
