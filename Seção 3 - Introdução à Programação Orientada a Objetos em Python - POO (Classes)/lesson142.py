# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯


class Caneta:
    def __init__(self, cor):
        # self._cor = cor -> Convenção de não mexer fora da classe
        self.set_cor = cor
        self._cor_tampa = None

    @property
    def get_cor(self):
        print("Estou no Getter")
        return self._cor

    @get_cor.setter
    def set_cor(self, valor):
        print("Estou no Setter")
        self._cor = valor

    @property
    def get_cor_tampa(self):
        return self._cor_tampa

    @get_cor_tampa.setter
    def set_cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta("Azul")
caneta.set_cor = "Rosa"
caneta.set_cor_tampa = "Azul"
print(caneta.get_cor)
print(caneta.get_cor_tampa)
