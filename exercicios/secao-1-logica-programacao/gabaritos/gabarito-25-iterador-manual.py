"""
Gabarito EXERCÍCIO 25 - Iterando na mão com iter() e next()

Raciocínio sênior
-----------------
O que o for faz "escondido" fica explícito aqui: iter() pega o objeto
iterador e next() puxa um elemento por vez; quando acaba, next()
levanta StopIteration — o for captura isso internamente e sai. O
primeiro try/except é o "loop manual": while True + StopIteration +
break. O segundo reutiliza o MESMO iterador já esgotado para provar
que a leitura além do fim continua falhando — o iterador não "volta".

Alternativas descartadas: iterar com for (o exercício é exatamente
fazer o que o for faz); recriar o iterador para o 2º teste (não
provaria que o original está esgotado).
"""

frutas: list[str] = ["maca", "banana", "uva", "manga"]
iterador_frutas = iter(frutas)

while True:
    try:
        fruta: str = next(iterador_frutas)
    except StopIteration:
        break
    print(fruta)

try:
    next(iterador_frutas)
except StopIteration:
    print("Iterador esgotado.")

# Onde você provavelmente divergiu:
# - usou enumerate ou índice com while (perde a lição de iterador)
# - capturou StopIteration numa exceção genérica (o resto do programa
#   silenciaria erros reais)
# - para o 2º teste, recriou o iterador (sem prova de esgotamento)
# - esqueceu o print dentro do loop, consumindo os itens sem exibir
# - tratou o fim com uma variável contador em vez de try/except