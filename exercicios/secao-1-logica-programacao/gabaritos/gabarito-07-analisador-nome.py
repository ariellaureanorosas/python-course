"""
Gabarito EXERCÍCIO 07 - Analisador de Nome com Slicing

Raciocínio sênior
-----------------
Cada informação é calculada uma única vez e guardada em variável
nomeada (total_letras, primeiro_nome, ...) — nada de repetir
expressões longas dentro dos prints.
O caso de nome sem espaço (nome único) é tratado com ternário:
.find() devolve -1 e o código cai no valor completo. Isso mostra
que "dados de borda" fazem parte do problema, não é frescura.
Alternativas descartadas: .split() direto — mais curto, mas o
exercício pede explicitamente slicing + find/rfind.
"""

nome_completo: str = input("Nome completo: ")

print(f"Maiúsculas: {nome_completo.upper()}")
print(f"Minúsculas: {nome_completo.lower()}")

total_letras: int = len(nome_completo) - nome_completo.count(" ")
print(f"Total de letras: {total_letras}")

primeiro_espaco: int = nome_completo.find(" ")
primeiro_nome: str = (
    nome_completo[:primeiro_espaco] if primeiro_espaco != -1 else nome_completo
)
print(f"Primeiro nome: {primeiro_nome} ({len(primeiro_nome)} letras)")

ultimo_espaco: int = nome_completo.rfind(" ")
ultimo_sobrenome: str = (
    nome_completo[ultimo_espaco + 1 :] if ultimo_espaco != -1 else ""
)
print(f"Último sobrenome: {ultimo_sobrenome}")

print(f"Nome invertido: {nome_completo[::-1]}")

# Onde você provavelmente divergiu:
# - usou split() em todo lugar (resolve, mas o enunciado pede
#   slicing + find/rfind)
# - calculou len(nome_completo.split()[0]) várias vezes dentro dos
#   prints (aqui o primeiro_nome é calculado uma vez só)
# - tratou apenas o caso comum e quebrou com nome de uma palavra só
#   (aqui o ternário com primeiro_espaco != -1 cobre esse caso)
# - usou replace(' ', '') em vez de len - count(' ')
