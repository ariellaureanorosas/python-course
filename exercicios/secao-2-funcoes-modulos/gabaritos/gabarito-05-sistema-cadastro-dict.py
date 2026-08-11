"""
Gabarito EXERCÍCIO 05 - Sistema de Cadastro com Dict

Raciocínio sênior
-----------------
Três funções com uma responsabilidade cada: criar (monta o dict),
atualizar (retorna um NOVO dict — não muta o original) e listar
(retorna as chaves). O padrão "não modificar o argumento recebido"
é o que permite chamar criar_pessoa/atualizar_pessoa em sequência
sem efeitos colaterais: p2 = atualizar_pessoa(p1, ...) preserva p1.
A cópia com dict(**dados) e update() é intencional: **dados captura
as chaves/valores dinâmicos e update() os acrescenta — essa é a
"mesa de edição segura" de um dict imutável.
Alternativas descartadas: deepcopy() (desnecessário para dados
simples; dict de valores escalares copia profundamente com dict());
mutar o dict original (quebra o princípio de não-surpresa).
"""


def criar_pessoa(nome: str, idade: int, email: str) -> dict:
    """Cria um dict de pessoa com nome, idade e email.

    Parametros
    ----------
    nome : str
        Nome da pessoa.
    idade : int
        Idade da pessoa.
    email : str
        E-mail da pessoa.

    Returns
    -------
    dict
        Dict com as chaves 'nome', 'idade' e 'email'.

    Exemplos
    --------
    >>> p = criar_pessoa('Ana', 25, 'ana@email.com')
    >>> p['nome']
    'Ana'
    >>> p['idade']
    25
    """
    return dict(nome=nome, idade=idade, email=email)


def atualizar_pessoa(pessoa: dict, **dados) -> dict:
    """Retorna um novo dict da pessoa atualizado com **dados.

    A pessoa original não é modificada (cópia superficial).

    Parametros
    ----------
    pessoa : dict
        Dict original da pessoa.
    **dados : dict
        Novos campos ou valores a atualizar (ex.: idade=26).

    Returns
    -------
    dict
        Novo dict com os dados atualizados.

    Exemplos
    --------
    >>> p1 = criar_pessoa('Ana', 25, 'ana@email.com')
    >>> p2 = atualizar_pessoa(p1, idade=26)
    >>> p2['idade']
    26
    >>> p1['idade']
    25
    """
    copia = dict(pessoa)
    copia.update(dados)
    return copia


def listar_chaves(pessoa: dict) -> list:
    """Retorna a lista das chaves do dict.

    Parametros
    ----------
    pessoa : dict
        Dict a inspecionar.

    Returns
    -------
    list
        Lista das chaves na ordem de inserção.

    Exemplos
    --------
    >>> p = criar_pessoa('Ana', 25, 'ana@email.com')
    >>> listar_chaves(p)
    ['nome', 'idade', 'email']
    """
    return list(pessoa.keys())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    p1 = criar_pessoa('Ana', 25, 'ana@email.com')
    p2 = atualizar_pessoa(p1, idade=26)
    print(p2)
    print(listar_chaves(p2))

# Onde você provavelmente divergiu:
# - usou deepcopy para copiar o dict (desnecessário para valores
#   simples; dict() já copia o que importa aqui)
# - MUTOU o dict original (p1['idade'] = 26) em vez de retornar
#   um novo — quem chamou continua refletindo a mudança
# - retornou pessoa.keys() direto (é uma view, muda se o dict
#   mudar; list() congela a lista de chaves)