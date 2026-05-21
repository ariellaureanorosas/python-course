from functools import wraps

NIVEIS_VALIDOS = ("INFO", "WARNING", "ERROR")


def log(nivel: str):
    if nivel not in NIVEIS_VALIDOS:
        raise ValueError(
            f"Nível inválido: '{nivel}'. Use um de {NIVEIS_VALIDOS}"
        )

    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{nivel}] Executando {func.__name__} ({args}, {kwargs})")
            return func(*args, **kwargs)
        return wrapper
    return decorador


if __name__ == "__main__":
    @log("INFO")
    def multiplicar(a: int, b: int) -> int:
        return a * b

    print(multiplicar(4, 5))
