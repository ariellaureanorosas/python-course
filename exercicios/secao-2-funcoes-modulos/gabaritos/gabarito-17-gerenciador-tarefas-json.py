"""
Gabarito EXERCÍCIO 17 - Gerenciador de Tarefas com JSON

Raciocínio sênior
-----------------
O JSON é o "banco de dados de uma tarefa": carregar, salvar,
adicionar, remover e renomear são as 5 operações de persistência.
carregar_tarefas é a "leitura tolerante" — arquivo inexistente
devolve lista vazia (primeiro uso do programa). remover_tarefa
devolve str | None: None sinaliza índice inválido em vez de
levantar IndexError — contrato explícito e sem surpresa para
quem chama. O salvar usa indent=2 e ensure_ascii=False para o
arquivo ficar legível e conservar acentos.
Alternativas descartadas: listas em memória sem persistência
(o cliente pede JSON), exceção em índice inválido (None é o
contrato do enunciado).
"""

import json
import os


def carregar_tarefas(
    nome_arquivo: str,
) -> list[str]:
    """Retorna lista de tarefas do arquivo JSON ou lista vazia.

    Se o arquivo nao existir, retorna lista vazia.

    Parametros
    ----------
    nome_arquivo : str
        Caminho do arquivo JSON.

    Returns
    -------
    list[str]
        Lista de tarefas.

    Exemplos
    --------
    >>> import tempfile, os
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
) -> None:
    """Salva lista de tarefas em arquivo JSON com indentacao.

    Parametros
    ----------
    nome_arquivo : str
        Caminho do arquivo JSON.
    tarefas : list[str]
        Lista de tarefas a salvar.

    Exemplos
    --------
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
) -> None:
    """Adiciona uma nova tarefa ao final da lista no arquivo JSON.

    Parametros
    ----------
    nome_arquivo : str
        Caminho do arquivo JSON.
    tarefa : str
        Descricao da nova tarefa.

    Exemplos
    --------
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
) -> str | None:
    """Remove tarefa pelo indice e retorna a tarefa removida.

    Se o indice for invalido, retorna None sem modificar o arquivo.

    Parametros
    ----------
    nome_arquivo : str
        Caminho do arquivo JSON.
    indice : int
        Indice (0-based) da tarefa a remover.

    Returns
    -------
    str | None
        A tarefa removida, ou None se o indice for invalido.

    Exemplos
    --------
    >>> import tempfile, os
    >>> tmp = tempfile.mktemp(suffix='.json')
    >>> adicionar_tarefa(tmp, 'A')
    >>> adicionar_tarefa(tmp, 'B')
    >>> remover_tarefa(tmp, 1)
    'B'
    >>> carregar_tarefas(tmp)
    ['A']
    >>> remover_tarefa(tmp, 99)
    >>> os.remove(tmp)
    """
    tarefas = carregar_tarefas(nome_arquivo)
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        salvar_tarefas(nome_arquivo, tarefas)
        return tarefa_removida
    return None


def renomear_arquivo_json(
    origem: str,
    destino: str,
) -> None:
    """Renomeia o arquivo JSON de tarefas.

    Parametros
    ----------
    origem : str
        Caminho atual do arquivo.
    destino : str
        Novo caminho do arquivo.

    Raises
    ------
    FileNotFoundError
        Se o arquivo de origem nao existir.

    Exemplos
    --------
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

# Onde você provavelmente divergiu:
# - deixou remover_tarefa levantar IndexError quando o índice é
#   inválido (o contrato do enunciado é retornar None — quem chama
#   pode decidir o que fazer sem try/except)
# - usou os.rename sem tratar FileNotFoundError (o erro bruto
#   "No such file or directory" não informa o caminho do usuário)
# - salvou com ensure_ascii=True (o padrão) — "Tarefa de #compras"
#   virava \uXXXX no arquivo; ensure_ascii=False preserva o texto
# - esqueceu indent=2 — o arquivo virava uma linha única ilegível