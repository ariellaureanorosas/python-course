"""
GABARITO 17 - Gerenciador de Tarefas com JSON
"""

import json
import os


def carregar_tarefas(nome_arquivo: str) -> list[str]:
    """Carrega a lista de tarefas de um arquivo JSON.

    Args:
        nome_arquivo: Caminho do arquivo JSON.

    Returns:
        Lista de tarefas, ou lista vazia se arquivo não existir.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados.get('tarefas', [])
    except FileNotFoundError:
        return []


def salvar_tarefas(nome_arquivo: str, tarefas: list[str]) -> None:
    """Salva a lista de tarefas em um arquivo JSON.

    Args:
        nome_arquivo: Caminho do arquivo JSON.
        tarefas: Lista de tarefas a salvar.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump({'tarefas': tarefas}, arquivo, indent=2, ensure_ascii=False)


def adicionar_tarefa(nome_arquivo: str, tarefa: str) -> None:
    """Adiciona uma nova tarefa ao arquivo JSON.

    Args:
        nome_arquivo: Caminho do arquivo JSON.
        tarefa: Descrição da tarefa.
    """
    tarefas = carregar_tarefas(nome_arquivo)
    tarefas.append(tarefa)
    salvar_tarefas(nome_arquivo, tarefas)


def remover_tarefa(nome_arquivo: str, indice: int) -> str | None:
    """Remove uma tarefa pelo índice.

    Args:
        nome_arquivo: Caminho do arquivo JSON.
        indice: Índice da tarefa a remover.

    Returns:
        A tarefa removida, ou None se o índice for inválido.
    """
    tarefas = carregar_tarefas(nome_arquivo)
    try:
        tarefa_removida = tarefas.pop(indice)
        salvar_tarefas(nome_arquivo, tarefas)
        return tarefa_removida
    except IndexError:
        return None


def renomear_arquivo_json(origem: str, destino: str) -> None:
    """Renomeia o arquivo JSON de tarefas.

    Args:
        origem: Nome atual do arquivo.
        destino: Novo nome do arquivo.
    """
    try:
        os.rename(origem, destino)
    except FileNotFoundError:
        pass
