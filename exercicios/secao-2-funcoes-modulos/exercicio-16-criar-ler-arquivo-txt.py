"""
EXERCÍCIO 16 - Criar e Ler Arquivo TXT

Tópicos: open(), modos (r, w, a), with, write, read, readline, readlines,
         writelines, seek, strip, encoding
Aulas: 119-122

Crie as funções abaixo para manipulação de arquivos TXT.

1. Função `escrever_arquivo(nome_arquivo: str, linhas: list[str]) -> None`
   - Abre arquivo no modo 'w' com encoding utf-8
   - Usa with para garantir fechamento
   - Escreve cada elemento de `linhas` como uma linha no arquivo
   - Adiciona quebra de linha ao final de cada linha

2. Função `ler_arquivo(nome_arquivo: str) -> list[str]`
   - Abre arquivo no modo 'r' com encoding utf-8
   - Usa with
   - Retorna lista com cada linha do arquivo, SEM as quebras de linha (use strip)
   - Trata FileNotFoundError: retorna lista vazia

3. Função `adicionar_linha(nome_arquivo: str, linha: str) -> None`
   - Abre arquivo no modo 'a' com encoding utf-8
   - Adiciona uma nova linha ao final do arquivo

4. Função `ler_primeiras_linhas(nome_arquivo: str, n: int) -> list[str]`
   - Abre arquivo no modo 'r' com encoding utf-8
   - Usa readline() em loop para ler apenas as primeiras `n` linhas
   - Retorna lista sem quebras de linha
   - Se arquivo não existir, retorna lista vazia
"""


def escrever_arquivo(nome_arquivo: str, linhas: list[str]) -> None:
    ...


def ler_arquivo(nome_arquivo: str) -> list[str]:
    ...


def adicionar_linha(nome_arquivo: str, linha: str) -> None:
    ...


def ler_primeiras_linhas(nome_arquivo: str, n: int) -> list[str]:
    ...
