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


import json
import os


def verificacao_lista(lista):
    if not lista:
        print("\nNenhum item a Mostrar")
        return False
    return True


def listar_tarefas(lista_das_tarefas):
    if not verificacao_lista(lista_das_tarefas):
        return
    tarefas_formatadas = "\n".join(
        f"{i}. {tarefa}" for i, tarefa in enumerate(lista_das_tarefas, start=1)
    )
    print(f"\n📋 SUAS TAREFAS:\n{tarefas_formatadas}")


def desfazer_tarefas(lista_das_tarefas, lista_tarefas_refazer):
    if not verificacao_lista(lista_das_tarefas):
        return None
    removido = lista_das_tarefas.pop()
    lista_tarefas_refazer.append(removido)
    mostrar_mensagem(removido, "🗑️ removido:", lista_das_tarefas)
    return removido


def refazer_tarefas(lista_das_tarefas, lista_tarefas_refazer):
    if not verificacao_lista(lista_tarefas_refazer):
        return None
    adicionado = lista_tarefas_refazer.pop()
    lista_das_tarefas.append(adicionado)
    mostrar_mensagem(adicionado, "♻️ Restaurado:", lista_das_tarefas)
    return adicionado


def adicionar_tarefas(tarefa, lista_das_tarefas):
    if tarefa.strip().isdigit():
        return None
    lista_das_tarefas.append(tarefa)
    mostrar_mensagem(tarefa, "✅ adicionada:", lista_das_tarefas)
    return tarefa


def mostrar_mensagem(tarefa, acao, lista):
    print(f"\n{acao} {tarefa}")
    if lista:
        listar_tarefas(lista)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, "r", encoding="utf8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não existe")
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, "lesson127.json")
lista_tarefas = ler([], CAMINHO_ARQUIVO)
lista_refazer = []

while True:
    print("\nComandos: listar, desfazer, refazer, SAIR")
    entrada = input("Digite uma tarefa ou comando: ")

    comandos = {
        "listar": lambda: listar_tarefas(lista_tarefas),
        "desfazer": lambda: desfazer_tarefas(lista_tarefas, lista_refazer),
        "refazer": lambda: refazer_tarefas(lista_tarefas, lista_refazer),
        "adicionar": lambda: adicionar_tarefas(entrada, lista_tarefas),
        "clear": lambda: os.system("cls" if os.name == "nt" else "clear"),
    }

    if entrada == "SAIR":
        break

    comando = comandos.get(entrada, comandos["adicionar"])
    comando()
    salvar(lista_tarefas, CAMINHO_ARQUIVO)
