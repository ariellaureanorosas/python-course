import json
import os


def _validar_arquivo_json(nome_arquivo: str, /) -> None:
    """Valida se arquivo existe e contem JSON valido; levanta excecao caso contrario."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            json.load(arquivo)
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo nao encontrado: {nome_arquivo}')
    except json.JSONDecodeError:
        raise ValueError(f'Arquivo nao contem JSON valido: {nome_arquivo}')


def carregar_tarefas(
    nome_arquivo: str,
    /,
) -> list[str]:
    """Retorna lista de tarefas do arquivo JSON ou lista vazia se nao existir.

    Parametros:
        nome_arquivo: Caminho do arquivo JSON.

    Returns:
        Lista de tarefas.

    Raises:
        ValueError: Se arquivo existir mas nao contiver JSON valido.

    Exemplos:
    >>> import tempfile, os, json
    >>> tmp = tempfile.mktemp(suffix='.json')
    >>> with open(tmp, 'w') as f:
    ...     json.dump({'tarefas': ['Estudar', 'Trabalhar']}, f)
    >>> carregar_tarefas(tmp)
    ['Estudar', 'Trabalhar']
    >>> os.remove(tmp)
    >>> carregar_tarefas('nao_existe.json')
    []
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados.get('tarefas', [])
    except FileNotFoundError:
        return []


def salvar_tarefas(
    nome_arquivo: str,
    tarefas: list[str],
    /,
) -> None:
    """Salva lista de tarefas em arquivo JSON com indentacao.

    Parametros:
        nome_arquivo: Caminho do arquivo JSON.
        tarefas: Lista de tarefas a salvar.

    Exemplos:
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.json')
    >>> salvar_tarefas(tmp, ['Comprar pao'])
    >>> carregar_tarefas(tmp)
    ['Comprar pao']
    >>> os.remove(tmp)
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(
            {'tarefas': tarefas},
            arquivo,
            indent=2,
            ensure_ascii=False,
        )


def adicionar_tarefa(
    nome_arquivo: str,
    tarefa: str,
    /,
) -> None:
    """Adiciona uma nova tarefa ao final da lista no arquivo JSON.

    Parametros:
        nome_arquivo: Caminho do arquivo JSON.
        tarefa: Descricao da nova tarefa.

    Raises:
        ValueError: Se arquivo existir mas tiver JSON invalido.

    Exemplos:
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.json')
    >>> adicionar_tarefa(tmp, 'Tarefa 1')
    >>> carregar_tarefas(tmp)
    ['Tarefa 1']
    >>> os.remove(tmp)
    """
    tarefas = carregar_tarefas(nome_arquivo)
    tarefas.append(tarefa)
    salvar_tarefas(nome_arquivo, tarefas)


def remover_tarefa(
    nome_arquivo: str,
    indice: int,
    /,
) -> str:
    """Remove tarefa pelo indice e retorna a tarefa removida.

    Parametros:
        nome_arquivo: Caminho do arquivo JSON.
        indice: Indice (0-based) da tarefa a remover.

    Returns:
        A tarefa removida.

    Raises:
        IndexError: Se o indice for invalido.
        ValueError: Se arquivo existir mas tiver JSON invalido.

    Exemplos:
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.json')
    >>> adicionar_tarefa(tmp, 'A')
    >>> adicionar_tarefa(tmp, 'B')
    >>> remover_tarefa(tmp, 1)
    'B'
    >>> carregar_tarefas(tmp)
    ['A']
    >>> os.remove(tmp)
    """
    tarefas = carregar_tarefas(nome_arquivo)
    tarefa_removida = tarefas.pop(indice)
    salvar_tarefas(nome_arquivo, tarefas)
    return tarefa_removida


def renomear_arquivo_json(
    origem: str,
    destino: str,
    /,
) -> None:
    """Renomeia o arquivo JSON de tarefas.

    Parametros:
        origem: Caminho atual do arquivo.
        destino: Novo caminho do arquivo.

    Raises:
        FileNotFoundError: Se o arquivo de origem nao existir.

    Exemplos:
    >>> import tempfile, os
    >>> tmp_orig = tempfile.mktemp(suffix='.json')
    >>> tmp_dest = tempfile.mktemp(suffix='.json')
    >>> salvar_tarefas(tmp_orig, ['teste'])
    >>> renomear_arquivo_json(tmp_orig, tmp_dest)
    >>> carregar_tarefas(tmp_dest)
    ['teste']
    >>> os.remove(tmp_dest)
    """
    try:
        os.rename(origem, destino)
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo de origem nao encontrado: {origem}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
