# The problem of Immutable parameters in functions python
def add_clients(name, lista=None):
    if lista is None:
        lista = []
    lista.append(name)
    return lista


client1 = add_clients("Luiz")
add_clients("Ariel", client1)

client2 = add_clients("Helena")
add_clients("Moreira", client2)

print(client1)
print(client2)
