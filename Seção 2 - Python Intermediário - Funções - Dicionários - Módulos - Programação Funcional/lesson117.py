# Functions recursive and recursion
# - Functions that can be called back
# - Useful for breaking large problems down into smaller parts
# - Every recursive function must have:
# -> A problem that can be broken down smaller parts
# -> A recursive case that solves the small problem
# -> A base case that terminates the recursion
# - factorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
