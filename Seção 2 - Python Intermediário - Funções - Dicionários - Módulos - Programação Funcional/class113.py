# MAP - to map dataname

from functools import partial


def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


products = [
    {"name": "Product 5", "price": 10.00},
    {"name": "Product 1", "price": 22.32},
    {"name": "Product 3", "price": 10.11},
    {"name": "Product 2", "price": 105.87},
    {"name": "Product 4", "price": 69.90},
]


def increase_price(value, porcentage):
    return round(value * porcentage, 2)


def change_dictionary_key(dictionary):
    return dictionary["price"]


increase_ten_porcentage = partial(increase_price, porcentage=1.1)

# new_products = [
#     {**product, "price": increase_ten_porcentage(change_dictionary_key(product))}
#     for product in products
# ]


def change_product_price(product):
    return {**product, "price": increase_ten_porcentage(change_dictionary_key(product))}


new_products = map(change_product_price, products)


print_iter(products)
print_iter(new_products)
