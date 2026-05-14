# Mantendo estados dentro da classe


class Camera:
    def __init__(self, nome, filmando=False, contador_fotos=0):
        self.nome = nome
        self.filmando = filmando
        self.contador_fotos = contador_fotos

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} já está filmando")
            return
        print(f"{self.nome} está filmando")
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando")
            return
        print(f"{self.nome} parou de filmar")
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar enquanto filma")
            return False

        self.contador_fotos += 1
        print("Fotos Tiradas:", self.contador_fotos)
        return True


c1 = Camera("Canon")
c2 = Camera("Sony")
c1.filmar()
c1.filmar()
if not c1.fotografar():
    resposta = input("Parar filmagem? [s/n]: ").lower()
    if resposta == "s":
        c1.parar_filmar()
        c1.fotografar()
print(c1.filmando)
print(c2.filmando)
