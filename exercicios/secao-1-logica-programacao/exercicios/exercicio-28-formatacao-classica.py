"""
EXERCÍCIO 28 — Formatação clássica: % e .format()

Tópicos: %s, %d, %.2f, .format(), alinhamento < > ^

Um sistema legado ainda usa as formatações antigas. Faça um
relatório de estoque que exibe:

  1. Com a sintaxe % : "Produto: %s | Quantidade: %d | Preço: R$ %.2f"
     para produto = "Caneca", quantidade = 12, preco = 19.90.
  2. Com .format() : o mesmo relatório, preço com 2 casas decimais:
     "Produto: {0} | Quantidade: {1} | Preço: R$ {2:.2f}".
  3. Com .format() e alinhamento (< e >) : uma tabela de 2 linhas
     (nome + total) com larguras 10 e 6, igual ao exemplo abaixo.

Exemplo de saída esperada (sem input):
Produto: Caneca | Quantidade: 12 | Preço: R$ 19.90
Produto: Caneca | Quantidade: 12 | Preço: R$ 19.90
Caneca    | 50.0
Garrafa   |100.0

Dica: {:<10} alinha à esquerda em 10 posições; {:>6} alinha à
direita em 6. Para números use "{}".format(50.0).

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========