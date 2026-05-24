# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([product.price for product in self._products])

    def insert_products(self, *products):
        self._products.extend(products)

    def listar_produtos(self):
        for product in self._products:
            print(product.name, product.price)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
p1, p2 = Product("Pen", 1.20), Product("T-shirt", 30)
cart.insert_products(p1, p2)
cart.listar_produtos()
print(cart.total())
