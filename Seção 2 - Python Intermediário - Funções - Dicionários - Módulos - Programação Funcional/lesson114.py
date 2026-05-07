# FILTER -> It is a functional filter


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

print_iter(products)

# new_products = [product for product in products if product["price"] > 20]

new_products = filter(lambda product: product["price"] > 20, products)
print_iter(new_products)
