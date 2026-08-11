"""
Gabarito EXERCÍCIO 26 - Mutabilidade e Cópias de Listas

Raciocínio sênior
-----------------
O ponto da aula 50 é que `=` NUNCA copia: ele amarra um novo rótulo
ao mesmo objeto (por isso o id() é igual). A mutabilidade só aparece
na comparação com o tipo imutável int — `y += 1` não altera o 5, ele
chama y para apontar para um NOVO objeto 6; o 5 original (de x)
permanece. .copy() é cópia RASA: suficiente aqui, já que os itens
("a", "b") são imutáveis.

Alternativas descartadas: copiar com [:] (funciona, mas .copy() é
mais explícito); o módulo copy.deepcopy (exagero para uma lista de
strings — adiante na Seção 2, na aula 102).
"""

lista_original: list[str] = ["a", "b", "c"]
lista_alias: list[str] = lista_original

print(f"id lista_original: {id(lista_original)}")
print(f"id lista_alias:    {id(lista_alias)}")

lista_alias.append("d")
print(f"Lista original após mudar a alias: {lista_original}")

lista_copia: list[str] = lista_original.copy()
lista_copia.append("e")
print(f"Lista original após mudar a cópia: {lista_original}")

x: int = 5
y: int = x
y += 1
print(f"x = {x}, y = {y}")

# Onde você provavelmente divergiu:
# - escreveu lista_copia = lista_original esperando uma cópia
#   (as duas apontam para o MESMO objeto — o passo 3 mostraria a
#   original mudando junto de novo)
# - usou copy.copy ou deepcopy sem importar o módulo copy
# - tentou provar imutabilidade com int mas usando == em vez de
#   acompanhar os valores x e y
# - esqueceu que append retorna None: lista_alias = lista_alias.append(...)
#   mataria a referência mostrada no passo 1