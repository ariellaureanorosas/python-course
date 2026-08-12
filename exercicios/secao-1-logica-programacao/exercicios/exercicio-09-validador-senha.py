"""
EXERCÍCIO 09 — Validador de Senha com Critérios

Tópicos: input(), for, in, métodos de string, if/else

Crie um validador de senhas. O programa deve receber uma senha
e verificar os seguintes critérios:

  a) Pelo menos 8 caracteres de comprimento.
  b) Contém pelo menos 1 dígito numérico (0-9).
  c) Contém pelo menos 1 letra maiúscula (A-Z).
  d) Contém pelo menos 1 letra minúscula (a-z).

Requisitos:
  - Use um laço for com o operador in para percorrer cada caractere
    da senha e fazer as verificações.
  - Para letras, use os métodos .isupper() e .islower().
  - Para dígitos, use .isdigit().
  - Ao final, informe quais critérios foram atendidos e quais
    falharam. Se todos forem atendidos, exiba "Senha válida!".

Exemplo:
  Digite a senha: Abc12
  [FALHOU] Mínimo de 8 caracteres.
  [OK] Contém número.
  [OK] Contém maiúscula.
  [OK] Contém minúscula.

  Digite a senha: MinhaSenha123
  [OK] Mínimo de 8 caracteres.
  [OK] Contém número.
  [OK] Contém maiúscula.
  [OK] Contém minúscula.
  Senha válida!

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

# def senha_forte(senha: str) -> bool:
#     return (
#         len(senha) >= 8
#         and any(letra.isdigit() for letra in senha)
#         and any(letra.isupper() for letra in senha)
#         and any(letra.islower() for letra in senha)
#     )

TAMANHO_MINIMO = 8

numero: bool = False
maiusculo: bool = False
minuscula: bool = False


senha: str = input("Digite sua senha: ")

for letra in senha:
    if letra.isdigit():
        numero = True
    if letra.isupper():
        maiusculo = True
    if letra.lower():
        minuscula = True

print(
    f"[OK] Mínimo de {TAMANHO_MINIMO} caracteres."
    if len(senha) >= TAMANHO_MINIMO
    else f"[FALHOU] Mínimo de {TAMANHO_MINIMO} caracteres."
)
print("[OK] Contém número." if numero else "[FALHOU] Contém número.")
print("[OK] Contém maiúscula." if maiusculo else "[FALHOU] Contém maiúscula.")
print("[OK] Contém minúscula." if minuscula else "[FALHOU] Contém minúscula.")

if (len(senha) >= TAMANHO_MINIMO) and numero and maiusculo and minuscula:
    print("Senha válida")
