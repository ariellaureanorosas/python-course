# Combinations, Permutations e Product - Itertools
# Combinação - order doesn't matter - iterable + size
# Permutação - order doesn't matter
# Product - order is important and reapeats unique values

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


people = ["joão", "Joana", "Luiz", "letícia"]

t_shirts = [["black", "white"], ["p", "m", "g"], ["masculino", "feminino", "unisex"]]

print_iter(combinations(people, 3))
print_iter(permutations(people, 2))
print_iter(product(*t_shirts))
