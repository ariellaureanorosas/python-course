"""
Gabarito EXERCÍCIO 23 - Caixa com decimal.Decimal

Raciocínio sênior
-----------------
A lição da aula 57 é o erro clássico da matemática de ponto flutuante:
Decimal(19.90) reproduz a representação binária imprecisa do float,
enquanto Decimal("19.90") pega o texto exato. Por isso a leitura vai
DIRETO do input() (que já devolve string) para o Decimal, sem passar
por float. O desconto usa round(total * Decimal("0.10"), 2) — o
arredondamento acontece na MESMA precisão decimal, sem nunca virar
float. O print usa :.2f, que o Decimal suporta nativamente.

Alternativas descartadas: somar com float e arredondar no fim —
esconde o problema em vez de eliminá-lo (0.1 + 0.2 != 0.3).
"""

from decimal import Decimal

preco1: Decimal = Decimal(input("Preço do produto 1: "))
preco2: Decimal = Decimal(input("Preço do produto 2: "))
preco3: Decimal = Decimal(input("Preço do produto 3: "))

total: Decimal = preco1 + preco2 + preco3
desconto: Decimal = round(total * Decimal("0.10"), 2)
total_final: Decimal = round(total - desconto, 2)

print(f"Total: {total:.2f} | Desconto 10%: {desconto:.2f} | Total final: {total_final:.2f}")

# Onde você provavelmente divergiu:
# - converteu o input com float() primeiro (traz o erro de precisão
#   de volta — o enunciado pede texto direto no Decimal)
# - usou Decimal(0.10) ou 0.10 puro no desconto (mesma armadilha)
# - arredondou só o total_final e não o desconto (a soma pode
#   divergir 1 centavo ao apresentar os dois)
# - usou round() sem o 2º argumento (arredonda para inteiro!)
# - esqueceu :.2f — Decimal exibe "35.00" correto, mas o padrão
#   pede exibir com 2 casas sempre