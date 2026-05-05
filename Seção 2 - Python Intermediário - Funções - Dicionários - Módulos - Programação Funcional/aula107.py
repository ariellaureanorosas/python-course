def parametros_decorador(nome):
    def decorador(funcao):
        print("decorador:", nome)

        def sua_nova_funcao(*args, **kwargs):
            res = funcao(*args, **kwargs)
            final = f"{res} {nome}"
            return final

        return sua_nova_funcao

    return decorador


@parametros_decorador(nome="Primeiro")
def soma(x, y):
    return x + y
