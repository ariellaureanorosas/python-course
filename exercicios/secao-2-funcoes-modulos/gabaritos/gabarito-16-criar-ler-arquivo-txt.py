"""
Gabarito EXERCÍCIO 16 - Criar e Ler Arquivo TXT

Raciocínio sênior
-----------------
Quatro funções cobrem o ciclo de vida de um arquivo TXT: escrever
(w), ler (r), adicionar (a) e ler parcial (readline em loop). O
`with` garante fechamento automático mesmo em erro — fechar na mão
com close() vaza descritor se algo falhar no meio.
ler_arquivo e ler_primeiras_linhas tratam arquivo inexistente e
devolvem lista vazia (não quebram o fluxo). A tipagem explícita
(list[str]) e o encoding utf-8 nos dois sentidos são o padrão
profissional: arquivo lido sem encoding errado muda acentos.
Alternativas descartadas: read() + splitlines() (espalha o
strip por linha igual, mas readlines + strip é o padrão direto).
"""


def escrever_arquivo(
    nome_arquivo: str,
    linhas: list[str],
) -> None:
    """Escreve linhas em um arquivo, sobrescrevendo se ja existir.

    Parametros
    ----------
    nome_arquivo : str
        Caminho do arquivo.
    linhas : list[str]
        Lista de strings a serem escritas.

    Exemplos
    --------
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
) -> list[str]:
    """Retorna lista de linhas do arquivo sem quebras de linha.

    Se o arquivo nao existir, retorna lista vazia.

    Parametros
    ----------
    nome_arquivo : str
        Caminho do arquivo.

    Returns
    -------
    list[str]
        Lista de strings, uma por linha.

    Exemplos
    --------
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.txt')
    >>> escrever_arquivo(tmp, ['alpha', 'beta'])
    >>> ler_arquivo(tmp)
    ['alpha', 'beta']
    >>> os.remove(tmp)
    >>> ler_arquivo('arquivo_inexistente.txt')
    []
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        return []


def adicionar_linha(
    nome_arquivo: str,
    linha: str,
) -> None:
    """Adiciona uma linha ao final do arquivo (modo append).

    Se o arquivo nao existir, o modo 'a' o cria.

    Parametros
    ----------
    nome_arquivo : str
        Caminho do arquivo.
    linha : str
        String a ser adicionada.

    Exemplos
    --------
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
) -> list[str]:
    """Retorna as primeiras N linhas do arquivo sem quebras.

    Se o arquivo tiver menos que N linhas, retorna ate onde
    conseguir. Se o arquivo nao existir, retorna lista vazia.

    Parametros
    ----------
    nome_arquivo : str
        Caminho do arquivo.
    n : int
        Numero de linhas a ler.

    Returns
    -------
    list[str]
        Lista com ate N strings.

    Exemplos
    --------
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.txt')
    >>> escrever_arquivo(tmp, ['a', 'b', 'c', 'd'])
    >>> ler_primeiras_linhas(tmp, 2)
    ['a', 'b']
    >>> ler_primeiras_linhas(tmp, 10)
    ['a', 'b', 'c', 'd']
    >>> os.remove(tmp)
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Onde você provavelmente divergiu:
# - deixou o FileNotFoundError subir (o enunciado pede retorno
#   vazio quando o arquivo não existe — o caller não precisa tratar
#   exceção para "só checar se há algo")
# - usou arquivo.open() fora de with e esqueceu close() no fim
#   (vaza descritor; with é o padrão incontestável)
# - leu com read() e fez split('\n') — a última linha sem quebra
#   vaza no strip; readlines já separa tudo
# - escreveu sem encoding='utf-8' (acentos quebrados no Windows)