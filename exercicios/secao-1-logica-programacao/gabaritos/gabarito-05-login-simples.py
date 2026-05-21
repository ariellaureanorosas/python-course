"""
Sistema de login com três tentativas. Usuário e senha predefinidos
em constantes.
"""

USUARIO_VALIDO: str = 'ADMIN'
SENHA_VALIDA: str = '1234'
TENTATIVAS_MAXIMAS: int = 3

tentativas_restantes: int = TENTATIVAS_MAXIMAS

while tentativas_restantes > 0:
    usuario_input: str = input('Usuário: ')
    senha_input: str = input('Senha: ')

    if usuario_input == USUARIO_VALIDO and senha_input == SENHA_VALIDA:
        print('Acesso concedido!')
        tentativas_restantes = 0
    else:
        tentativas_restantes -= 1
        if tentativas_restantes == 0:
            print('Acesso bloqueado!')
        else:
            plural: str = '' if tentativas_restantes == 1 else 's'
            print(
                'Usuário ou senha incorretos. '
                f'{tentativas_restantes} tentativa{plural} restante{plural}.'
            )
