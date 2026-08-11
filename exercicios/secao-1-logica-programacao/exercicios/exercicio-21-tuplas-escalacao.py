"""
EXERCÍCIO 21 — Tuplas: Dados Imutáveis

Tópicos: tuplas, index, count, desempacotamento, try/except

Um clube guarda a escalação de um time em uma TUPLA (dados que não
podem mudar durante a partida). O sistema deve:

  - Receber do usuário o nome de um jogador e informar em que posição
    (índice) ele está na escalação, usando .index().
  - Tentar "trocar" um jogador atribuindo um novo valor em uma posição
    (ex.: escalacao[1] = "Novato") e capturar o erro TypeError com
    try/except, exibindo "A escalação é imutável!".
  - Desempacotar a tupla: nome do primeiro jogador, nome do segundo
    e o RESTANTE em uma lista (use * na desempacotação).

Exemplo de saída esperada (entrada: "Maria"):
Maria está na posição 1.
A escalação é imutável!
Principais: João e Maria
Reservas: ['Carlos', 'Ana', 'Pedro']

Dica: .index() levanta ValueError se o nome não existe — trate com
try/except ValueError.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========