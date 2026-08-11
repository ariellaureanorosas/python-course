"""
Gabarito EXERCÍCIO 14 - Lista de Compras com Menu

Raciocínio sênior
-----------------
Estrutura de um CRUD de terminal: um laço infinito de menu
(while True) com rotas if/elif/else e continue para opção
inválida. As operações são separadas por responsabilidade —
inserir, apagar, listar, sair.
Antes de apagar, a lista vazia é verificada (if not lista_compras)
para evitar prints de fallback desnecessários; o try/except
(ValueError, IndexError) captura exatamente os dois erros possíveis
de entrada: texto não numérico (ValueError) e índice fora do
range (IndexError) — exceções específicas, não except genérico.

Alternativas descartadas: função para cada operação — mais
organizado em projeto grande, aqui sem dar o assunto antes da aula.
"""

OPCOES_VALIDAS: str = 'ials'

lista_compras: list[str] = []

while True:
    print('\n=== LISTA DE COMPRAS ===')
    print('[i] Inserir item')
    print('[a] Apagar item')
    print('[l] Listar itens')
    print('[s] Sair')

    opcao_usuario: str = input('\nOperação [i/a/l/s]: ').strip().lower()

    if opcao_usuario not in OPCOES_VALIDAS:
        print('Opção inválida. Escolha i, a, l ou s.')
        continue

    if opcao_usuario == 'i':
        novo_item: str = input('Item: ').strip()
        if not novo_item:
            print('Erro: o nome do item não pode estar vazio.')
            continue
        lista_compras.append(novo_item)
        print(f'Item {novo_item} adicionado.')

    elif opcao_usuario == 'a':
        if not lista_compras:
            print('A lista está vazia. Nada para apagar.')
            continue

        print('\nItens cadastrados:')
        for indice, item_atual in enumerate(lista_compras):
            print(f'  [{indice}] {item_atual}')

        try:
            indice_apagar: int = int(input('\nÍndice para apagar: '))
            item_removido: str = lista_compras.pop(indice_apagar)
            print(f'Item {item_removido} apagado.')
        except (ValueError, IndexError):
            print('Índice inválido.')

    elif opcao_usuario == 'l':
        if not lista_compras:
            print('A lista está vazia.')
        else:
            print('\nItens cadastrados:')
            for indice, item_atual in enumerate(lista_compras):
                print(f'  [{indice}] {item_atual}')

    elif opcao_usuario == 's':
        print('Saindo...')
        break

# Onde você provavelmente divergiu:
# - usou except: sozinho (genérico) em vez de (ValueError, IndexError)
#   — o genérico esconde bugs reais de lógica
# - menu em maiúsculas [I]/[A]/[L]/[S] (o enunciado usa minúsculas)
# - não tratou item vazio ou lista vazia — o programa "funciona" mas
#   imprime mensagens feias em borda
# - esqueceu .strip() na opção digitada ("s " não sairia do menu)