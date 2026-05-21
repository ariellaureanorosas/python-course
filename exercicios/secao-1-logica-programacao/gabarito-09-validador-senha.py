"""
Gabarito 09 — Validador de Senha com Critérios
"""

senha: str = input('Digite a senha: ')

tem_8_caracteres: bool = len(senha) >= 8
tem_numero: bool = False
tem_maiuscula: bool = False
tem_minuscula: bool = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True
    if caractere.isupper():
        tem_maiuscula = True
    if caractere.islower():
        tem_minuscula = True

if not tem_8_caracteres:
    print('[FALHOU] Mínimo de 8 caracteres.')
else:
    print('[OK] Mínimo de 8 caracteres.')

if tem_numero:
    print('[OK] Contém número.')
else:
    print('[FALHOU] Contém número.')

if tem_maiuscula:
    print('[OK] Contém maiúscula.')
else:
    print('[FALHOU] Contém maiúscula.')

if tem_minuscula:
    print('[OK] Contém minúscula.')
else:
    print('[FALHOU] Contém minúscula.')

if tem_8_caracteres and tem_numero and tem_maiuscula and tem_minuscula:
    print('Senha válida!')
