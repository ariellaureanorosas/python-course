# Variáveis livres + nonlocal (Locals, Globals)


# def fora(numero):
#     a = numero

#     def dentro():
#         print(locals())
#         return a  # Variável Livre

#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


# def concatenar(string_inicial):
#     valor_final = string_inicial

#     def interna(valor_a_concatenar=""):
#         nonlocal valor_final
#         valor_final += valor_a_concatenar
#         return valor_final

#     return interna


# c = concatenar("a")
# print(c("b"))  # ab
# print(c("c"))  # abc
# final = c()
# print(final)  # abc


# DESAFIO CHATGPT PARA FIXAÇÃO DE CONTEÚDO:


def contador():
    contador = 0

    def conta():
        nonlocal contador
        contador += 1
        return contador

    return conta


c = contador()
print(c())
print(c())
print(c())
