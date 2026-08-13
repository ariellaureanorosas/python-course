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
import os
import time

TEXTO = """[i] Inserir item
[a] Apagar item (pelo índice)
[l] Listar itens (com índices)
[s] Sair

Digite sua opção: """


def limpar_tela() -> None:
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")


lista_compras: list[str] = []
while True:
    input_lista: str = input(TEXTO).lower().strip()

    if not input_lista:  # INPUT
        print("ERRO: O input não pode ser enviado vazio")
        continue

    elif input_lista == "i":  # INSERIR
        adicionar: str = input("Digite o que você quer adicionar: ")
        if adicionar:
            lista_compras.append(adicionar)
            print(f"Adicionado na lista: {adicionar}")
        else:
            print("Item não pode estar vazio")

        limpar_tela()

    elif input_lista == "l":  # LISTAR
        if not lista_compras:
            print("A lista está vazia")
        else:
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i} - {item}")

        limpar_tela()

    elif input_lista == "a":  # APAGAR
        try:
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i} - {item}")
            indice_apagar = int(input("Digite o número do indice para apagar: "))
            removido: str = lista_compras.pop(indice_apagar - 1)
            print(f"Item: {removido} - Foi removido")

            limpar_tela()
        except ValueError, IndexError:
            print("ERRO: Indíce Inválido")

    elif input_lista == "s":
        print("Você decidiu sair...")
        break

    else:
        print("Digite as opções corretamente")
        limpar_tela()
