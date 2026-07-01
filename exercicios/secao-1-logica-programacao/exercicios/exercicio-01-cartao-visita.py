"""
Exercício 01 — Cartão de Visita com print()

Use a função print() com os parâmetros sep e end para exibir um
cartão de visita no formato abaixo.

Regras:
  - O nome, o telefone e o email devem estar armazenados em variáveis.
  - Use sep para separar as seções do cartão com uma linha de
    caracteres "=" (ex.: ==========).
  - Use end para controlar a quebra de linha entre os blocos.
  - A saída final deve ocupar EXATAMENTE 6 linhas (incluindo a linha
    vazia entre o telefone e o email).

Exemplo de saída esperada:
====================
Nome: Maria Silva
Telefone: (11) 99999-0000
Email: maria@email.com
====================

Dica: você pode usar print com sep="\n" e end="\n\n" para controlar
as quebras. Ou pode simplesmente chamar print() vazio para pular linha.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
SEPARADOR = "=" * 30

nome: str = input("Digite seu nome: ")
telefone: int = input("Digite seu telefone: ")
email: str = input("Digite seu email: ")

print(SEPARADOR)
print(nome, telefone, email, sep="\n")
print(SEPARADOR)
