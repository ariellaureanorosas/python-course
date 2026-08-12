"""
EXERCÍCIO 05 — Sistema de Login Simples

Tópicos: constantes, while, operador and, controle de fluxo

Crie um sistema de login com usuário e senha fixos.

Regras:
  - Defina USUARIO e SENHA como constantes (nomes MAIÚSCULOS).
  - O usuário tem 3 tentativas para acertar.
  - A validação deve usar o operador and (usuário E senha corretos).
  - Use um laço while para controlar as tentativas.
  - Se acertar, exiba "Acesso concedido!" e saia do laço.
  - Se errar, informe quantas tentativas restam.
  - Após 3 tentativas erradas, exiba "Acesso bloqueado!".
  - O programa NÃO pode usar break (use controle de fluxo no while).

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

USUARIO = "Ariel"
SENHA = "12345"
tentativas: int = 3

while tentativas > 0:
    input_usuario: str = input("Digite seu nome de Usuario: ")
    input_senha: str = input("Digite sua senha: ")
    if input_usuario == USUARIO and input_senha == SENHA:
        print("Acesso concedido")
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Acesso negado, agora você tem {tentativas} tentativas")
        else:
            print("Acesso Bloqueado")
