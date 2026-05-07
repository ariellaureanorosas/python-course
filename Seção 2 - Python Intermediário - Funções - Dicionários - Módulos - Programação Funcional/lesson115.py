# Reduce - reduces an iterable by a value
from functools import reduce

products = [
    {"name": "Product 5", "price": 10.00},
    {"name": "Product 1", "price": 22.32},
    {"name": "Product 3", "price": 10.11},
    {"name": "Product 2", "price": 105.87},
    {"name": "Product 4", "price": 69.90},
]

# total = 0

# for product in products:
#     total += product["price"]

# print(total)
# print(sum([product["price"] for product in products]))


# def reduce_function(accumulator, value):
#     print("accumulator:", accumulator)
#     print("product:", value)
#     print()
#     return accumulator + value


total = reduce(lambda acumulador, product: acumulador + product["price"], products, 0)
print(round(total, 2))
