"""
Gabarito EXERCÍCIO 20 - Positional-Only e Keyword-Only

Raciocínio sênior
-----------------
Os três mecanismos de assinatura aparecem com papéis reais:
`/` (positional-only) impede que alguém trave o código passando o
nome do parâmetro errado (ex.: valor=... num cálculo abreviado);
`*` (keyword-only) força clareza em configs com vários defaults
(idade/ativo em criar_usuario; pares/expoente em pipelines);
e combinados, `/`, `*` garantem uma "faca de dois gumes": quem
chama REDUZ a ambiguidade para o programador que lê depois.
O gabarito documenta o contrato em cada docstring e demonstra
que a posição do argumento é parte da API — reverter a chamada
com erro de API buga a assinatura, não a lógica.
"""


def calcular(
    valor: float,
    /,
    taxa: float,
    *,
    desconto: float = 0.0,
) -> float:
    """Retorna resultado de valor * taxa - desconto.

    Parametros
    ----------
    valor : float
        Posicional apenas (nao pode ser nomeado).
    taxa : float
        Posicional ou nomeado.
    desconto : float, opcional
        Nomeado apenas, padrao 0.0.

    Returns
    -------
    float
        Resultado do calculo.

    Exemplos
    --------
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

    Parametros
    ----------
    nome : str
        Posicional apenas.
    email : str
        Posicional ou nomeado.
    idade : int, opcional
        Nomeado apenas, padrao 0.
    ativo : bool, opcional
        Nomeado apenas, padrao True.

    Returns
    -------
    dict[str, str | int | bool]
        Dicionario com dados do usuario.

    Exemplos
    --------
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

    Todos os parametros sao nomeados apenas (keyword-only): não há
    argumentos posicionais nesta assinatura.

    Parametros
    ----------
    produto : str
        Nome do produto.
    quantidade : int
        Quantidade vendida.
    preco_unitario : float
        Preco unitario.

    Returns
    -------
    dict[str, str | int | float]
        Dicionario com produto, quantidade, preco_unitario e total.

    Exemplos
    --------
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

# Onde você provavelmente divergiu:
# - confundiu positional-only (`/`) com keyword-only (`*`) — `/` está
#   ANTES na assinatura e proíbe nomear; `*` está depois e exige nomear
# - tentou chamar registrar_venda('Caneta', 2, 1.5) — vai falhar com
#   TypeError: precisa de kwargs; a assinatura é o contrato
# - colocou `/` no MEIO da assinatura sem motivo (aqui cada uso tem
#   um propósito: proteger o nome do parâmetro ou forçar clareza)
# - esqueceu que `*` no início (registrar_venda) zera as posições
#   livres: TUDO vira keyword-only