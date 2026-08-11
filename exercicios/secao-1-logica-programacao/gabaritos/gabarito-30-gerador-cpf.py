"""
Gabarito EXERCÍCIO 30 - Gerador de CPF

Raciocínio sênior
-----------------
O gerador é a "função inversa" da validação (nota 13 e exercício 19):
em vez de conferir um CPF, ele sorteia 9 dígitos e REUSA o mesmo
cálculo de pesos regressivos para fabricar os 2 dígitos verificadores.
A função validar_cpf é mantida aqui como teste de sanidade: se o
gerador estiver errado, o "válido" nunca aparece e o bug surge na
hora. A lógica de validação foi copiada do gabarito-19 em vez de
importada — arquivos com hífen no nome não podem ser importados, e
como módulos/import são assunto da Seção 2, reproduzir a função faz
o exercício rodar sozinho.
"""

import random


def validar_cpf(cpf: str) -> bool:
    cpf_limpo: str = cpf.replace(".", "").replace("-", "")

    if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
        return False

    soma_1 = 0
    for i in range(9):
        soma_1 += int(cpf_limpo[i]) * (10 - i)
    digito_1 = 0 if (soma_1 * 10) % 11 > 9 else (soma_1 * 10) % 11

    soma_2 = 0
    for i in range(10):
        soma_2 += int(cpf_limpo[i]) * (11 - i)
    digito_2 = 0 if (soma_2 * 10) % 11 > 9 else (soma_2 * 10) % 11

    return cpf_limpo == cpf_limpo[:9] + str(digito_1) + str(digito_2)


def gerar_cpf() -> str:
    nove_digitos: str = ""
    for _ in range(9):
        nove_digitos += str(random.randint(0, 9))

    soma_1 = 0
    for i in range(9):
        soma_1 += int(nove_digitos[i]) * (10 - i)
    digito_1 = 0 if (soma_1 * 10) % 11 > 9 else (soma_1 * 10) % 11

    dez_digitos: str = nove_digitos + str(digito_1)
    soma_2 = 0
    for i in range(10):
        soma_2 += int(dez_digitos[i]) * (11 - i)
    digito_2 = 0 if (soma_2 * 10) % 11 > 9 else (soma_2 * 10) % 11

    cpf: str = nove_digitos + str(digito_1) + str(digito_2)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


for _ in range(3):
    cpf_gerado: str = gerar_cpf()
    if validar_cpf(cpf_gerado):
        print(f"{cpf_gerado} — válido")
    else:
        print(f"{cpf_gerado} — INVÁLIDO")

# Onde você provavelmente divergiu:
# - tentou `from gabarito-19-validador-cpf import validar_cpf`
#   (nomes com hífen não são importáveis — por isso a cópia local)
# - usou random.randrange(9) (nunca sorteia o 9) ou random.choices
# - errou o limite do range no 2º dígito: range(10) com peso 11-i,
#   não range(9)
# - usou (soma % 11) em vez de ((soma * 10) % 11) — a regra do
#   ministério trata resto 10 como dígito 0
# - esqueceu a formatação XXX.XXX.XXX-XX (retornou só dígitos)
# - não validou o CPF gerado — o teste de sanidade é o que prova o código