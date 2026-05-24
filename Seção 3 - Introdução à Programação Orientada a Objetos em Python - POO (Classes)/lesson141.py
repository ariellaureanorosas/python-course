# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta


caneta = Caneta("Azul")
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)

#####################################################
# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print("Get cor da tinta")
#         print("-" * 30)
#         return self.cor_tinta


# caneta = Caneta("Azul")
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
