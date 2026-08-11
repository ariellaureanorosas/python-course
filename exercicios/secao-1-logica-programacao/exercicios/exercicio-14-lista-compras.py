"""
EXERCÍCIO 14 — Lista de Compras com Menu

Tópicos: listas, while, if/elif/else, enumerate(), try/except

Implemente um CRUD completo de lista de compras com as seguintes opções:

    [i] Inserir item
    [a] Apagar item (pelo índice)
    [l] Listar itens (com índices)
    [s] Sair

Requisitos:
    - Use uma lista para armazenar os itens.
    - Use while True para manter o menu ativo até o usuário sair.
    - Use if/elif/else para as opções.
    - Use append() para inserir.
    - Use pop() ou del para apagar (solicite o índice).
    - Use enumerate() no momento de listar.
    - Trate índices inválidos com try/except.
    - Mostre mensagens de feedback (ex.: "Item apagado", "Índice inválido").

Exemplo de interação:

    Operação [i/a/l/s]: i
    Item: Arroz
    Operação [i/a/l/s]: i
    Item: Feijão
    Operação [i/a/l/s]: l
    0 - Arroz
    1 - Feijão
    Operação [i/a/l/s]: a
    Índice para apagar: 0
    Item Arroz apagado.
    Operação [i/a/l/s]: l
    0 - Feijão
    Operação [i/a/l/s]: s
    Saindo...

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
