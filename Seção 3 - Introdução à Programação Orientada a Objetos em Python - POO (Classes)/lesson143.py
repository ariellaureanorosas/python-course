# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
class Foo:
    def __init__(self):
        self.public = "Publico"
        self._protected = "Protegido"
        self.__private = "Privado"

    def metodo_publico(self):
        self._metodo_protegido()
        self.__metodo_privado()
        return "Você está no public"

    def _metodo_protegido(self):
        print("Método Protegido")
        return "Você está no protected"

    def __metodo_privado(self):
        print("Método Privado")
        return "Você está no private"


f = Foo()
print(f.metodo_publico())
