"""
Exibe um cartão de visita formatado com nome, telefone e e-mail.
"""

SEPARADOR: str = '=' * 20

nome: str = 'Maria Silva'
telefone: str = '(11) 99999-0000'
email: str = 'maria@email.com'

print(SEPARADOR)
print(f'Nome: {nome}')
print(f'Telefone: {telefone}')
print()
print(f'E-mail: {email}')
print(SEPARADOR)
