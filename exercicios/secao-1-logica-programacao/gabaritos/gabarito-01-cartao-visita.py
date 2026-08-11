"""
Gabarito EXERCÍCIO 01 - Cartão de Visita com print()

Raciocínio sênior
-----------------
Os dados (nome, telefone, email) são variáveis e a exibição é uma
responsabilidade separada: nada de calcular dentro do print.
O separador é uma constante porque é o "contrato visual" do cartão —
se mudar o tamanho, muda em um único lugar.
Alternativas descartadas: montar a saída inteira numa string gigante
com f-string (mistura apresentação com dados e dificulta ajustar
uma linha isolada).
"""

SEPARADOR: str = '=' * 20

nome: str = 'Maria Silva'
telefone: str = '(11) 99999-0000'
email: str = 'maria@email.com'

print(SEPARADOR)
print(f'Nome: {nome}')
print(f'Telefone: {telefone}')
print(f'Email: {email}')
print(SEPARADOR)

# Onde você provavelmente divergiu:
# - usou input() para coletar os dados (a especificação só pede
#   variáveis fixas — o exercício treina print/sep/end, não o input)
# - escreveu "E-mail" com hífen (o enunciado define "Email:")
# - repetiu '=' * 20 inline em vez de usar a constante SEPARADOR
# - tentou forçar 6 linhas com um print() vazio; aqui são exatamente 5
# - anotou telefone como int (input de telefone é texto: "(11) 99999-0000")