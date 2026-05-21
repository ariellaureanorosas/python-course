"""
GABARITO — EXERCÍCIO 14 — Lista de Compras com Menu

CRUD completo com menu interativo usando lista, while e tratamento de
erros com try/except.
"""

import os

lista_compras: list = []

while True:
    print("\nOperações disponíveis:")
    print("[i] Inserir item")
    print("[a] Apagar item")
    print("[l] Listar itens")
    print("[s] Sair")

    opcao: str = input("\nOperação [i/a/l/s]: ").strip().lower()

    if opcao == "i":
        item: str = input("Item: ").strip()
        if item:
            lista_compras.append(item)
            print(f"'{item}' adicionado com sucesso.")
        else:
            print("Item inválido.")

    elif opcao == "a":
        if not lista_compras:
            print("Lista vazia. Nada para apagar.")
            continue

        for indice, item in enumerate(lista_compras):
            print(f"{indice} - {item}")

        try:
            indice_apagar: int = int(input("Índice para apagar: "))
            item_apagado: str = lista_compras.pop(indice_apagar)
            print(f"Item '{item_apagado}' apagado.")
        except (ValueError, IndexError):
            print("Índice inválido. Tente novamente.")

    elif opcao == "l":
        if not lista_compras:
            print("Lista vazia.")
        else:
            print("\nLista de compras:")
            for indice, item in enumerate(lista_compras):
                print(f"{indice} - {item}")

    elif opcao == "s":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Escolha i, a, l ou s.")
