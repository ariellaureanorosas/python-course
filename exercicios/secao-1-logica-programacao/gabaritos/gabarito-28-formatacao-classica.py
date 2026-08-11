"""
Gabarito EXERCÍCIO 28 - Formatação clássica: % e .format()

Raciocínio sênior
-----------------
A sintaxe % aplica os operadores à TUPla de argumentos — a ordem
conta e o número de %s/%d precisa bater com a da tupla (erro comum:
preencher no print e a tupla ter menos itens). O .format() trabalha
com índices ({0}, {2:.2f}) que reutilizam operandos sem repeti-los.
O alinhamento monta a tabela com LARGURAS FIXAS: {:<10} empurra o
nome para a esquerda de um campo de 10 e {:>6} encosta o número na
direita — as colunas batem por construção, sem espaços digitados à
mão. Python 3.x ainda suporta % por compatibilidade legada; código
novo prefere f-strings, mas ler esse relatório antigo é obrigação de
quem herda sistemas.

Alternativas descartadas: f-strings (melhor prática atual, mas o
exercício pede exatamente o formato legado); alinhamento manual com
espaços digitados (quebra quando o conteúdo muda de tamanho).
"""

produto: str = "Caneca"
quantidade: int = 12
preco: float = 19.90

print("Produto: %s | Quantidade: %d | Preço: R$ %.2f" % (produto, quantidade, preco))
print("Produto: {0} | Quantidade: {1} | Preço: R$ {2:.2f}".format(produto, quantidade, preco))

print("{:<10}| {:>6}".format("Caneca", 50.0))
print("{:<10}| {:>6}".format("Garrafa", 100.0))

# Onde você provavelmente divergiu:
# - esqueceu o parêntese da tupla no %: "... R$ %.2f" % produto, 12, 19.9
#   (o print recebe 3 argumentos e só a string é formatada)
# - usou {1} e {2} fora de ordem no .format(), trocando quantidade e preço
# - esqueceu o :.2f no {2} — o preço vinha "19.9" e não "19.90"
# - escreveu o alinhamento como {:>10} para o nome (a regra pede
#   esquerda para nome e direita para número)
# - usou %d com float (%.2f) — %d trunca para inteiro silenciosamente