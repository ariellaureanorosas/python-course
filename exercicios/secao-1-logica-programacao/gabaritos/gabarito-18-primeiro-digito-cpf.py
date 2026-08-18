"""
Gabarito EXERCÍCIO 18 - Primeiro Dígito Verificador do CPF

Raciocínio sênior
-----------------
A validação acontece em camadas antes do cálculo: o dado precisa
ser só dígitos (isdigit) e ter exatamente 9 números (len == 9) —
se não, mensagem clara. Só então o loop pesa cada dígito com o
peso decrescente de 10 a 2.
A regra do dígito (resto < 2 → 0, senão 11 - resto) está em uma
constante DIVISOR_CPF = 11 e no ternário legível; LIMITE_RESTA = 2
documenta o limiar da regra oficial.
O fatiamento da formatação final ([:3], [3:6], [6:9]) reproduz o
formato 123.456.789-0 do exemplo.

Alternativas descartadas: enumerate() com cálculo de peso por índice
(mais compacto, porém menos explícito que o peso_atual decrescente
que acompanha a definição do algoritmo).
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

# Onde você provavelmente divergiu:
# - não validou entrada (isdigit + len) e quebrou com "12ab34" ou
#   com um CPF de 8 números
# - inverteu a regra do dígito (11 - resto quando resto < 2, ou 0 no
#   caso contrário — a lógica correta é: resto < 2 → 0)
# - usou peso fixo 10 para todos os dígitos no loop, em vez de
#   decrescer 10, 9, ..., 2
# - calculou o peso com enumerate(..., start=PESO_INICIAL) e errou o
#   decremento no caso de 9 dígitos (aqui o fim do loop deixa
#   peso_atual = 1, sem efeito colateral)
