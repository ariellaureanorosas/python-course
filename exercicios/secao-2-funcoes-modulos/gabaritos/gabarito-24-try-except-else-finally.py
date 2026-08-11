"""
Gabarito EXERCÍCIO 24 - Tratamento de Erros Completo (try/except/else/finally)

Raciocínio sênior
-----------------
`converter_numero` captura a exceção MAIS ESPECÍFICA possível
(ValueError): o except genérico esconderia bugs reais. Em
`divisao_segura`, o `else` carrega o caminho do sucesso — o fluxo
fica "try: tente, except: azar, else: deu certo": quem lê entende
que o else SÓ roda quando a tentativa foi bem-sucedida, sem precisar
de flags. O finally em `analisar_numero` garante o efeito colateral
(registro/print) em QUALQUER desfecho — a diferença para o else é
exatamente essa: else vê o sucesso, finally vê tudo.

Alternativas descartadas: retornos dentro do try sem else (funciona,
mas mistura os dois caminhos); except genérico (mascararia
KeyboardInterrupt e erros de lógica).
"""


def converter_numero(texto: str) -> int | None:
    """Converte texto em int, devolvendo None se não for numérico.

    Parâmetros
    ----------
    texto : str
        Texto a converter.

    Retorna
    -------
    int | None
        Inteiro correspondente ou None em ValueError.

    Exemplos
    --------
    >>> converter_numero("42")
    42
    >>> converter_numero("abc") is None
    True
    """
    try:
        return int(texto)
    except ValueError:
        return None


def divisao_segura(a: float, b: float) -> str:
    """Divide a por b sem explodir; mensagem formatada com 2 casas.

    Parâmetros
    ----------
    a : float
        Dividendo.
    b : float
        Divisor.

    Retorna
    -------
    str
        Resultado com 2 casas ou 'divisão por zero'.

    Exemplos
    --------
    >>> divisao_segura(10, 2)
    '5.00'
    >>> divisao_segura(10, 0)
    'divisão por zero'
    """
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "divisão por zero"
    else:
        return f"{resultado:.2f}"


def analisar_numero(texto: str) -> tuple:
    """Converte e sinaliza sucesso; sempre confirma a validação.

    Parâmetros
    ----------
    texto : str
        Texto a validar.

    Retorna
    -------
    tuple
        (valor, sucesso): int (ou 0) e bool.

    Exemplos
    --------
    >>> analisar_numero("42")
    validacao concluida
    (42, True)
    >>> analisar_numero("abc")
    validacao concluida
    (0, False)
    """
    sucesso: bool = False
    try:
        valor: int = int(texto)
        sucesso = True
    except ValueError:
        valor = 0
    finally:
        print("validacao concluida")
    return valor, sucesso


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(converter_numero("42"))
    print(converter_numero("abc"))
    print(divisao_segura(10, 2))
    print(divisao_segura(10, 0))
    print(analisar_numero("42"))

# Onde você provavelmente divergiu:
# - usou `except:` puro — engole até KeyboardInterrupt; prefira
#   sempre a exceção específica
# - pôs o return do sucesso DENTRO do try (o else existe para isso;
#   lá dentro você mistura fluxo feliz com código arriscado)
# - esqueceu do finally no analisar_numero — a confirmação deixaria
#   de aparecer no caminho do erro
# - tentou `except (ValueError, ZeroDivisionError)` no converter:
#   capturar o que a operação nunca levanta esconde bugs
# - no else, esqueceu que ele corre SÓ após o try completo — quem
#   precisa de "rodou certo?" usa else, não um novo try