"""
Gabarito EXERCÍCIO 05 - Sistema de Login Simples

Raciocínio sênior
-----------------
A condição do while usa tentativas_restantes como "combustível" do
laço: quando zera, o laço termina sozinho — sem break (que o
enunciado proíbe) e sem variável extra de saída.
O plural é tratado com a variável plural porque a mensagem muda
com a quantidade de tentativas — detalhe de UX que um sênior não
deixa passar.
Alternativas descartadas: break dentro do if de acerto (mais curto,
mas o enunciado exige controle pelo próprio while).
"""

USUARIO: str = 'Ariel'
SENHA: str = 'Ariel@2007'
TENTATIVAS_MAXIMAS: int = 3

tentativas_restantes: int = TENTATIVAS_MAXIMAS

while tentativas_restantes > 0:
    usuario_input: str = input('Usuário: ')
    senha_input: str = input('Senha: ')

    if usuario_input == USUARIO and senha_input == SENHA:
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

# Onde você provavelmente divergiu:
# - usou break para sair no acerto (funciona, mas contraria o
#   enunciado; aqui o controle é o próprio estado do while)
# - usou nomes como USER_CORRETO em vez das constantes USUARIO e
#   SENHA pedidas no enunciado
# - esqueceu o plural: "1 tentativa restante" vs "2 tentativas restantes"
# - zerou tentativas_restantes no acerto em vez de usar uma flag
#   adicional (uma variável a menos = menos estado para errar)