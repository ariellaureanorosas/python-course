"""
EXERCÍCIO 25 — Iterando na mão com iter() e next()

Tópicos: iter(), next(), StopIteration, while, try/except

Todo for do Python usa iter() e next() por baixo dos panos. Agora
você vai fazer isso explicitamente:

  - Crie a lista ["maca", "banana", "uva", "manga"] e um iterador
    com iter().
  - Percorra TODOS os elementos usando next() dentro de um while,
    capturando StopIteration com try/except para encerrar, e
    imprimindo cada fruta.
  - Ao final, chame next() UMA vez a mais no mesmo iterador, capture
    StopIteration e exiba "Iterador esgotado.".

Saída esperada (sem nenhum input):
maca
banana
uva
manga
Iterador esgotado.

Dica: while True + try/except StopIteration com break é o padrão;
depois do loop, um segundo try/except confirma o iterador esgotado.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========