def criar_multiplicador(multiplicador: int):
    def multiplicar(numero: int) -> int:
        return numero * multiplicador
    return multiplicar


if __name__ == "__main__":
    dobro = criar_multiplicador(2)
    triplo = criar_multiplicador(3)
    print(f"Dobro de 5: {dobro(5)}")
    print(f"Triplo de 5: {triplo(5)}")
