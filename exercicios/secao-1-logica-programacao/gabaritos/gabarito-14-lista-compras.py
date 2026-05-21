"""
Lista de Compras com Menu Interativo

Sistema CRUD de lista de compras com menu iterativo, utilizando
lista, laço while e tratamento de exceções com try/except.
"""

OPCOES_VALIDAS: str = "ials"

lista_compras: list = []

while True:
    print("\n=== LISTA DE COMPRAS ===")
    print("[I] Inserir item")
    print("[A] Apagar item")
    print("[L] Listar itens")
    print("[S] Sair")

    opcao_usuario: str = input("\nOperação [I/A/L/S]: ").strip().lower()

    if opcao_usuario not in OPCOES_VALIDAS:
        print("Opção inválida. Escolha I, A, L ou S.")
        continue

    if opcao_usuario == "i":
        novo_item: str = input("Nome do item: ").strip()
        if not novo_item:
            print("Erro: o nome do item não pode estar vazio.")
            continue
        lista_compras.append(novo_item)
        print(f"'{novo_item}' foi adicionado à lista.")

    elif opcao_usuario == "a":
        if not lista_compras:
            print("A lista está vazia. Nada para apagar.")
            continue

        print("\nItens cadastrados:")
        for indice, item_atual in enumerate(lista_compras):
            print(f"  [{indice}] {item_atual}")

        try:
            indice_apagar: int = int(input("\nÍndice do item para remover: "))
            item_removido: str = lista_compras.pop(indice_apagar)
            print(f"'{item_removido}' foi removido da lista.")
        except (ValueError, IndexError):
            print("Erro: índice inválido. Informe um número da lista.")

    elif opcao_usuario == "l":
        if not lista_compras:
            print("A lista está vazia.")
        else:
            print("\nItens cadastrados:")
            for indice, item_atual in enumerate(lista_compras):
                print(f"  [{indice}] {item_atual}")

    elif opcao_usuario == "s":
        print("Encerrando o programa.")
        break
