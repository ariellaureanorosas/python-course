"""
Gabarito 07 — Analisador de Nome com Slicing
"""

nome_completo: str = input('Nome completo: ')

# Maiúsculas e minúsculas
print(f'Maiúsculas: {nome_completo.upper()}')
print(f'Minúsculas: {nome_completo.lower()}')

# Total de letras (sem espaços)
total_letras: int = len(nome_completo) - nome_completo.count(' ')
print(f'Total de letras: {total_letras}')

# Primeiro nome
primeiro_espaco: int = nome_completo.find(' ')
primeiro_nome: str = nome_completo[:primeiro_espaco] if primeiro_espaco != -1 else nome_completo
print(f'Primeiro nome: {primeiro_nome} ({len(primeiro_nome)} letras)')

# Último sobrenome
ultimo_espaco: int = nome_completo.rfind(' ')
ultimo_sobrenome: str = nome_completo[ultimo_espaco + 1:] if ultimo_espaco != -1 else ''
print(f'Último sobrenome: {ultimo_sobrenome}')

# Nome invertido
nome_invertido: str = nome_completo[::-1]
print(f'Nome invertido: {nome_invertido}')
