"""
Gabarito 05 — Sistema de Login Simples
"""

USUARIO: str = 'ADMIN'
SENHA: str = '1234'

tentativas: int = 3

while tentativas > 0:
    usuario_input: str = input('Usuário: ')
    senha_input: str = input('Senha: ')

    if usuario_input == USUARIO and senha_input == SENHA:
        print('Acesso concedido!')
        tentativas = 0
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f'Usuário ou senha incorretos. {tentativas} tentativa(s) restante(s).')
        else:
            print('Acesso bloqueado!')
