def decorador(funcao):
    contador = 1

    def interna():
        nonlocal contador
        print(contador)
        funcao()
        contador += 1

    return interna


@decorador
def falar_oi():
    print("oi")


falar_oi()
falar_oi()
