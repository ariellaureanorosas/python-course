"""
GABARITO 20 - Positional-Only e Keyword-Only
"""


def calcular(
    valor: float,
    /,
    taxa: float,
    *,
    desconto: float = 0,
) -> float:
    """Calcula valor * taxa - desconto com tipos de parâmetros mistos.

    Args:
        valor: Posicional apenas (/).
        taxa: Posicional ou nomeado.
        desconto: Nomeado apenas (*), padrão 0.

    Returns:
        Resultado do cálculo.
    """
    return valor * taxa - desconto


def criar_usuario(
    nome: str,
    /,
    email: str,
    *,
    idade: int = 0,
    ativo: bool = True,
) -> dict:
    """Cria um dicionário de usuário com parâmetros mistos.

    Args:
        nome: Posicional apenas (/).
        email: Posicional ou nomeado.
        idade: Nomeado apenas (*), padrão 0.
        ativo: Nomeado apenas (*), padrão True.

    Returns:
        Dicionário representando o usuário.
    """
    return {
        'nome': nome,
        'email': email,
        'idade': idade,
        'ativo': ativo,
    }


def registrar_venda(
    /,
    *,
    produto: str,
    quantidade: int,
    preco_unitario: float,
) -> dict:
    """Registra uma venda com todos os parâmetros keyword-only.

    Como / aparece antes de *, não há parâmetros posicionais.
    Todos os parâmetros devem ser passados como keyword.

    Args:
        produto: Nome do produto (keyword-only).
        quantidade: Quantidade vendida (keyword-only).
        preco_unitario: Preço unitário (keyword-only).

    Returns:
        Dicionário com dados da venda e total calculado.
    """
    return {
        'produto': produto,
        'quantidade': quantidade,
        'preco_unitario': preco_unitario,
        'total': quantidade * preco_unitario,
    }
