"""
Valida se uma senha atende aos critérios: mínimo de 8 caracteres,
ao menos um dígito, uma letra maiúscula e uma letra minúscula.
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
