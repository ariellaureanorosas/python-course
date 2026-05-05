# Decoradores com parâmetros
def fabrica_decoradoras(a=None, b=None, c=None):
    def fabrica_funcao(func):
        print(func.__name__)

        def aninhada(*args, **kwargs):
            print("Aninhada")
            res = func(*args, **kwargs)
            return res

        return aninhada

    return fabrica_funcao


@fabrica_decoradoras(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_decoradoras()
multiplicacao = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
dez_vezes_cinco = multiplicacao(10, 5)
print(dez_vezes_cinco)
