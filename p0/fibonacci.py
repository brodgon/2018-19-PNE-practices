# - - - Solution for exercise 5 - - -

print("Fibonacci´s succession starts with numbers 0 and 1 and, from these, each term is the sum of the last two")


def fibonacci(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
