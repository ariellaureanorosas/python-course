def calcular(
    valor: float,
    /,
    taxa: float,
    *,
    desconto: float = 0.0,
) -> float:
    """Retorna resultado de valor * taxa - desconto.

    Parametros:
        valor: Posicional apenas (nao pode ser nomeado).
        taxa: Posicional ou nomeado.
        desconto: Nomeado apenas, padrao 0.0.

    Returns:
        Resultado do calculo.

    Exemplos:
    >>> calcular(100.0, 0.1, desconto=5.0)
    5.0
    >>> calcular(200.0, 0.05)
    10.0
    >>> calcular(50.0, 0.2, desconto=2.0)
    8.0
    """
    return valor * taxa - desconto


def criar_usuario(
    nome: str,
    /,
    email: str,
    *,
    idade: int = 0,
    ativo: bool = True,
) -> dict[str, str | int | bool]:
    """Retorna dicionario representando um usuario.

    Parametros:
        nome: Posicional apenas.
        email: Posicional ou nomeado.
        idade: Nomeado apenas, padrao 0.
        ativo: Nomeado apenas, padrao True.

    Returns:
        Dicionario com dados do usuario.

    Exemplos:
    >>> criar_usuario('Ana', 'ana@email.com')
    {'nome': 'Ana', 'email': 'ana@email.com', 'idade': 0, 'ativo': True}
    >>> criar_usuario('Joao', 'joao@email.com', idade=25, ativo=False)
    {'nome': 'Joao', 'email': 'joao@email.com', 'idade': 25, 'ativo': False}
    """
    return {
        'nome': nome,
        'email': email,
        'idade': idade,
        'ativo': ativo,
    }


def registrar_venda(
    *,
    produto: str,
    quantidade: int,
    preco_unitario: float,
) -> dict[str, str | int | float]:
    """Retorna dicionario com dados da venda e total calculado.

    Todos os parametros sao nomeados apenas (keyword-only).

    Parametros:
        produto: Nome do produto.
        quantidade: Quantidade vendida.
        preco_unitario: Preco unitario.

    Returns:
        Dicionario com produto, quantidade, preco_unitario e total.

    Exemplos:
    >>> registrar_venda(produto='Caneta', quantidade=10, preco_unitario=1.5)
    {'produto': 'Caneta', 'quantidade': 10, 'preco_unitario': 1.5, 'total': 15.0}
    """
    return {
        'produto': produto,
        'quantidade': quantidade,
        'preco_unitario': preco_unitario,
        'total': quantidade * preco_unitario,
    }


if __name__ == '__main__':
    import doctest
    doctest.testmod()
