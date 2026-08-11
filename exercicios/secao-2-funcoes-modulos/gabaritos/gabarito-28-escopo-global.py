"""
Gabarito EXERCÍCIO 28 - Escopo Global

Raciocínio sênior
-----------------
incrementar/zerar precisam de `global`: sem ela, `CONTADOR += 1`
criaria um CONTADOR LOCAL e levantaria UnboundLocalError (a variável
foi "usada antes de declará-la local"). consultar NÃO precisa da
palavra: LER global é livre — a resolução de nomes busca local,
envolvente, global e builtins (LEGB). somar_local mostra o caminho
recomendado no dia a dia: funções puras que devolvem valores em vez
de dependerem de estado global — mais fácil de testar e de rastrear.
O global só se justifica quando o estado compartilhado É o objetivo
(contadores, configuração).

Atenção ao doctest: cada docstring roda com uma CÓPIA do globals,
mas `global` altera o MÓDULO real — por isso os exemplos usam apenas
as funções (incrementar/zerar/consultar) e nunca leem `CONTADOR`
direto (ler direto leria a cópia, não o global).
"""

CONTADOR = 0


def incrementar() -> int:
    """Soma 1 à variável global CONTADOR e devolve o novo valor.

    Parâmetros
    ----------
    (nenhum)

    Retorna
    -------
    int
        Valor atualizado do contador.

    Exemplos
    --------
    >>> incrementar()
    1
    >>> incrementar()
    2
    """
    global CONTADOR
    CONTADOR += 1
    return CONTADOR


def zerar() -> None:
    """Zera a variável global CONTADOR.

    Parâmetros
    ----------
    (nenhum)

    Retorna
    -------
    None

    Exemplos
    --------
    >>> zerar()
    >>> consultar()
    0
    """
    global CONTADOR
    CONTADOR = 0


def consultar() -> int:
    """Lê a variável global CONTADOR (ler não exige `global`).

    Parâmetros
    ----------
    (nenhum)

    Retorna
    -------
    int
        Valor atual do contador.

    Exemplos
    --------
    >>> consultar()
    0
    """
    return CONTADOR


def somar_local(a: int, b: int) -> int:
    """Soma dois números usando apenas escopo local.

    Parâmetros
    ----------
    a : int
        Primeira parcela.
    b : int
        Segunda parcela.

    Retorna
    -------
    int
        a + b.

    Exemplos
    --------
    >>> somar_local(2, 3)
    5
    """
    resultado = a + b
    return resultado


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(incrementar())
    print(incrementar())
    print(consultar())
    zerar()
    print(consultar())

# Onde você provavelmente divergiu:
# - esqueceu o `global CONTADOR` em incrementar: UnboundLocalError
# - declarou `global` em consultar (compila, mas é ruído — ler é livre)
# - reconstruiu o contador devolvendo um valor novo e reatribuindo
#   fora (funciona, mas o exercício pede o estado global)
# - nos doctests, assumiu que o valor do contador continua entre
#   docstrings (cada docstring roda em namespace copiado — por isso
#   os resets explícitos `CONTADOR = 0`)