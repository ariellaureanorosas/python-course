"""
Exercício 09 — Validador de Senha com Critérios

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
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
