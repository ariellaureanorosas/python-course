"""
Gabarito EXERCÍCIO 09 - Decorator de Log

Raciocínio sênior
-----------------
log_execucao é um decorator: recebe uma função e devolve UMA OUTRA
(wrapper) que embrulha a original. O @wraps é obrigatório — sem ele,
func.__name__ do decorado viraria 'wrapper' e quebraria introspecção,
profiling e docstrings da função decorada. Esse é o padrão canônico
de decorator em Python: *args/**kwargs garantem que o wrapper
funcione para QUALQUER assinatura de função.
Alternativas descartadas: embrulhar na mão em cada função (repetia
o log), modificar a função original (viola o princípio open/closed).
"""

from functools import wraps


def log_execucao(func):
    """Decorator que registra a execução de uma função.

    Parametros
    ----------
    func : Callable
        Função a ser decorada.

    Returns
    -------
    Callable
        Wrapper que imprime entrada/saída e retorna o resultado.

    Exemplos
    --------
    >>> @log_execucao
    ... def somar(a: int, b: int) -> int:
    ...     return a + b
    >>> somar(3, 5)
    Executando somar com argumentos ((3, 5), {})
    Resultado: 8
    8
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f'Executando {func.__name__} com argumentos ({args}, {kwargs})'
        )
        resultado = func(*args, **kwargs)
        print(f'Resultado: {resultado}')
        return resultado
    return wrapper


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    @log_execucao
    def somar(a: int, b: int) -> int:
        return a + b

    somar(3, 5)

# Onde você provavelmente divergiu:
# - esqueceu o @wraps (func.__name__ vira 'wrapper' — o decorado
#   perde identidade; é a linha que um sênior nunca esquece)
# - colocou o print do resultado DIRETO no retorno do func
#   (print(resultado) antes de return resultado — a ordem importa:
#   primeiro loga, depois devolve)
# - chamou func() sem passar *args/**kwargs (quebra com funções de
#   2+ parâmetros)