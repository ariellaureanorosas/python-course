"""
EXERCÍCIO 17 - Gerenciador de Tarefas com JSON

Tópicos: JSON (json.dump, json.load, ensure_ascii, indent),
         open(), FileNotFoundError, os.remove/os.unlink, os.rename
Aulas: 125-127

Implemente um gerenciador de tarefas simples com persistência em JSON.

O arquivo JSON terá o formato:
    {"tarefas": ["Tarefa 1", "Tarefa 2", ...]}

1. Função `carregar_tarefas(nome_arquivo: str) -> list[str]`
   - Tenta carregar a lista de tarefas do JSON
   - Se arquivo não existir, retorna lista vazia
   - Usa json.load()

2. Função `salvar_tarefas(nome_arquivo: str, tarefas: list[str]) -> None`
   - Salva a lista de tarefas no JSON com indent=2 e ensure_ascii=False
   - Usa json.dump()

3. Função `adicionar_tarefa(nome_arquivo: str, tarefa: str) -> None`
   - Carrega tarefas existentes
   - Adiciona nova tarefa
   - Salva de volta

4. Função `remover_tarefa(nome_arquivo: str, indice: int) -> str | None`
   - Carrega tarefas existentes
   - Remove a tarefa no índice informado (se válido)
   - Salva de volta
   - Retorna a tarefa removida ou None se índice inválido

5. Função `renomear_arquivo_json(origem: str, destino: str) -> None`
   - Usa os.rename para renomear o arquivo
   - Trata FileNotFoundError
"""

import json
import os


def carregar_tarefas(nome_arquivo: str) -> list[str]:
    ...


def salvar_tarefas(nome_arquivo: str, tarefas: list[str]) -> None:
    ...


def adicionar_tarefa(nome_arquivo: str, tarefa: str) -> None:
    ...


def remover_tarefa(nome_arquivo: str, indice: int) -> str | None:
    ...


def renomear_arquivo_json(origem: str, destino: str) -> None:
    ...
