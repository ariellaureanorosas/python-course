from functools import wraps


def log_execucao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__} com argumentos ({args}, {kwargs})")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper


if __name__ == "__main__":
    @log_execucao
    def somar(a: int, b: int) -> int:
        return a + b

    somar(3, 5)
