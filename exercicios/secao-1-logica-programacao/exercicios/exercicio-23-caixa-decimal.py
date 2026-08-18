"""
EXERCÍCIO 23 — Caixa com decimal.Decimal

Tópicos: decimal.Decimal, round(), aritmética

Uma loja quer eliminar erros de centavos no caixa. Receba do usuário
os preços de 3 produtos (como texto, sem converter para float) e
calcule:

  - O total da compra usando decimal.Decimal a partir da string
    digitada, para não herdar o erro de ponto flutuante do float.
  - Um desconto de 10% sobre o total, arredondado para 2 casas
    decimais com round().
  - Exiba: total, desconto e total final, todos com 2 casas decimais.

Exemplo de saída esperada (entradas: 19.90, 10.10 e 5.00):
Total: 35.00 | Desconto 10%: 3.50 | Total final: 31.50

Dica: Decimal("19.90") preserva o valor exato; Decimal(19.90) carrega
o erro de ponto flutuante — por isso a leitura pode ser direto do
input() (que devolve string).

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
from decimal import Decimal

PORCENTAGEM = Decimal("0.10")
precos: list[Decimal] = []

for indice in range(1, 4):
    input_preco: str = input(f"Digite o {indice} preço: ")
    precos.append(Decimal(input_preco))

total = sum(Decimal(p) for p in precos)
desconto: Decimal = round((total * PORCENTAGEM), 2)
total_final: Decimal = total - desconto

numeros_formatados: str = ", ".join(str(decimais) for decimais in precos)
print(
    f"Entradas: {numeros_formatados} | Total: {total:.2f} | Desconto 10%: {desconto:.2f} | Total final: {total_final:.2f}"
)
