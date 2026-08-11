"""
Gabarito EXERCÍCIO 09 - Validador de Senha com Critérios

Raciocínio sênior
-----------------
Quatro flags booleanas representam os quatro critérios; um único
for percorre a senha uma vez e liga as flags — nenhum critério é
verificado "fora" com funções mágicas (all(), sum() de bools), o
que mantém a leitura linear para quem está aprendendo.
As mensagens usam o padrão [OK]/[FALHOU] do exemplo, e só quando
todos os critérios passam é que "Senha válida!" aparece.
Alternativas descartadas: regex ou any()/all() — mais compacto,
porém menos didático nesta etapa do curso.
"""

TAMANHO_MINIMO: int = 8

senha: str = input('Digite a senha: ')

tem_tamanho_minimo: bool = len(senha) >= TAMANHO_MINIMO
tem_digito: bool = False
tem_maiuscula: bool = False
tem_minuscula: bool = False

for caractere in senha:
    if caractere.isdigit():
        tem_digito = True
    if caractere.isupper():
        tem_maiuscula = True
    if caractere.islower():
        tem_minuscula = True

print(
    f'[OK] Mínimo de {TAMANHO_MINIMO} caracteres.'
    if tem_tamanho_minimo
    else f'[FALHOU] Mínimo de {TAMANHO_MINIMO} caracteres.'
)
print('[OK] Contém número.' if tem_digito else '[FALHOU] Contém número.')
print('[OK] Contém maiúscula.' if tem_maiuscula else '[FALHOU] Contém maiúscula.')
print('[OK] Contém minúscula.' if tem_minuscula else '[FALHOU] Contém minúscula.')

if tem_tamanho_minimo and tem_digito and tem_maiuscula and tem_minuscula:
    print('Senha válida!')

# Onde você provavelmente divergiu:
# - usou expressões regulares ou any()/all() (funcionam, mas o
#   enunciado pede o for com in + isdigit/isupper/islower)
# - contou caracteres (x.isdigit()) por categoria em vez de flags —
#   aqui só precisamos saber se EXISTE, não quantos
# - colocou os prints de [OK]/[FALHOU] dentro do for (repetiriam
#   para cada caractere; aqui eles rodam uma vez após o laço)
# - esqueceu que espaços vazios e símbolos existem: "ab cd EF" tem
#   minúsculas e maiúsculas — o validador avalia cada caractere