"""
GABARITO 16 - Criar e Ler Arquivo TXT
"""


def escrever_arquivo(nome_arquivo: str, linhas: list[str]) -> None:
    """Escreve uma lista de linhas em um arquivo.

    Args:
        nome_arquivo: Caminho do arquivo.
        linhas: Lista de strings a serem escritas.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for linha in linhas:
            arquivo.write(linha + '\n')


def ler_arquivo(nome_arquivo: str) -> list[str]:
    """Lê todas as linhas de um arquivo.

    Args:
        nome_arquivo: Caminho do arquivo.

    Returns:
        Lista de linhas sem quebras de linha, ou lista vazia se não existir.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        return []


def adicionar_linha(nome_arquivo: str, linha: str) -> None:
    """Adiciona uma linha ao final do arquivo.

    Args:
        nome_arquivo: Caminho do arquivo.
        linha: String a ser adicionada.
    """
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(linha + '\n')


def ler_primeiras_linhas(nome_arquivo: str, n: int) -> list[str]:
    """Lê apenas as primeiras N linhas do arquivo.

    Args:
        nome_arquivo: Caminho do arquivo.
        n: Número de linhas a ler.

    Returns:
        Lista com as primeiras N linhas sem quebras de linha.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas: list[str] = []
            for _ in range(n):
                linha = arquivo.readline()
                if not linha:
                    break
                linhas.append(linha.strip())
            return linhas
    except FileNotFoundError:
        return []
