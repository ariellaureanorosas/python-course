def _validar_arquivo_existe(nome_arquivo: str, /) -> None:
    """Valida se arquivo existe; levanta FileNotFoundError se nao."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        raise FileNotFoundError(
            f'Arquivo nao encontrado: {nome_arquivo}'
        )


def escrever_arquivo(
    nome_arquivo: str,
    linhas: list[str],
    /,
) -> None:
    """Escreve linhas em um arquivo, sobrescrevendo se ja existir.

    Parametros:
        nome_arquivo: Caminho do arquivo.
        linhas: Lista de strings a serem escritas.

    Exemplos:
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.txt')
    >>> escrever_arquivo(tmp, ['linha1', 'linha2'])
    >>> ler_arquivo(tmp)
    ['linha1', 'linha2']
    >>> os.remove(tmp)
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linha + '\n' for linha in linhas)


def ler_arquivo(
    nome_arquivo: str,
    /,
) -> list[str]:
    """Retorna lista de linhas do arquivo sem quebras de linha.

    Parametros:
        nome_arquivo: Caminho do arquivo.

    Returns:
        Lista de strings, uma por linha.

    Raises:
        FileNotFoundError: Se o arquivo nao existir.

    Exemplos:
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.txt')
    >>> escrever_arquivo(tmp, ['alpha', 'beta'])
    >>> ler_arquivo(tmp)
    ['alpha', 'beta']
    >>> os.remove(tmp)
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]


def adicionar_linha(
    nome_arquivo: str,
    linha: str,
    /,
) -> None:
    """Adiciona uma linha ao final do arquivo (modo append).

    Parametros:
        nome_arquivo: Caminho do arquivo.
        linha: String a ser adicionada.

    Raises:
        FileNotFoundError: Se o arquivo nao existir.

    Exemplos:
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.txt')
    >>> escrever_arquivo(tmp, ['um'])
    >>> adicionar_linha(tmp, 'dois')
    >>> ler_arquivo(tmp)
    ['um', 'dois']
    >>> os.remove(tmp)
    """
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(linha + '\n')


def ler_primeiras_linhas(
    nome_arquivo: str,
    n: int,
    /,
) -> list[str]:
    """Retorna as primeiras N linhas do arquivo sem quebras.

    Se o arquivo tiver menos que N linhas, retorna ate onde conseguir.

    Parametros:
        nome_arquivo: Caminho do arquivo.
        n: Numero de linhas a ler.

    Returns:
        Lista com ate N strings.

    Raises:
        FileNotFoundError: Se o arquivo nao existir.

    Exemplos:
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.txt')
    >>> escrever_arquivo(tmp, ['a', 'b', 'c', 'd'])
    >>> ler_primeiras_linhas(tmp, 2)
    ['a', 'b']
    >>> ler_primeiras_linhas(tmp, 10)
    ['a', 'b', 'c', 'd']
    >>> os.remove(tmp)
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas: list[str] = []
        for _ in range(n):
            linha = arquivo.readline()
            if not linha:
                break
            linhas.append(linha.strip())
        return linhas


if __name__ == '__main__':
    import doctest
    doctest.testmod()
