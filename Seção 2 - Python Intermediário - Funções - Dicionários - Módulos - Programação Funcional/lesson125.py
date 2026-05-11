# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os


def verificacao_lista(lista):
    if not lista:
        print("\nNada a fazer\n")
        return False
    return True


def listar_tarefas(lista_das_tarefas):
    if not verificacao_lista(lista_das_tarefas):
        return
    tarefas_formatadas = "\n".join(
        f"{i}. {tarefa}" for i, tarefa in enumerate(lista_das_tarefas, start=1)
    )
    print(f"\n📋 SUAS TAREFAS:\n{tarefas_formatadas}\n")


def desfazer_tarefas(lista_das_tarefas, lista_tarefas_refazer):
    if not verificacao_lista(lista_das_tarefas):
        return None
    removido = lista_das_tarefas.pop()
    lista_tarefas_refazer.append(removido)
    return removido


def refazer_tarefas(lista_das_tarefas, lista_tarefas_refazer):
    if not verificacao_lista(lista_tarefas_refazer):
        return None
    adicionado = lista_tarefas_refazer.pop()
    lista_das_tarefas.append(adicionado)
    return adicionado


def adicionar_tarefas(tarefa, lista_das_tarefas):
    if tarefa.strip().isdigit():
        return None
    lista_das_tarefas.append(tarefa)
    return tarefa


lista_tarefas = []
lista_refazer = []

while True:
    print("Comandos: listar, desfazer, refazer, SAIR")
    entrada = input("Digite uma tarefa ou comando: ")

    if entrada.lower() == "listar":
        listar_tarefas(lista_tarefas)
        continue

    elif entrada.lower() == "desfazer":
        tarefa = desfazer_tarefas(lista_tarefas, lista_refazer)
        if tarefa is not None:
            print(f"\n{tarefa} foi removido")
            listar_tarefas(lista_tarefas)
        continue

    elif entrada.lower() == "refazer":
        tarefa = refazer_tarefas(lista_tarefas, lista_refazer)
        if tarefa is not None:
            print(f"\n{tarefa} foi adicionado(a) a lista")
            listar_tarefas(lista_tarefas)
        continue

    elif entrada == "SAIR":
        break

    elif entrada == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        continue

    else:
        resultado = adicionar_tarefas(entrada, lista_tarefas)
        if resultado is not None:
            print(f"\n{resultado} foi adicionado(a) a lista")
            listar_tarefas(lista_tarefas)
        continue
