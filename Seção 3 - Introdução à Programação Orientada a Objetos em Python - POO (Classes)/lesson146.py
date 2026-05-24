# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def enter_address(self, street, number):
        self.addresses.append(Address(street, number))

    def enter_external_address(self, address):
        self.addresses.append(address)

    def list_addresses(self):
        for address in self.addresses:
            print(address.street, address.number)

    def __del__(self):
        print("ERASING:", self.name)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print("ERASING:", self.street, self.number)


client1 = Client("Maria")
client1.enter_address("Av Brasil", 54)
client1.enter_address("Rua B", 6745)
external_address = Address("Av Saudade", 123213)
client1.enter_external_address(external_address)
client1.list_addresses()

del client1


print(external_address.street, external_address.number)
print("######################## AQUI TERMINA MEU CÓDIGO")
