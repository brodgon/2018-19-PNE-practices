# - - -  Solution for exercise 6 - - -


def fibonacci(n):
    a = 0
    b = 1
    fib = []
    while a < n:
        fib.append(a)
        a, b = b, a+b
    return fib


# - - - Main Program - - -


try:
    x = int(input('Enter a valid number: '))
    fib = fibonacci(x)
    print('This is Fibonacci´s succession for the number introduced: ', "\n", fib)
    total = 0
    for i in range(len(fib)):
        total = total + fib[i]
    print('The sum of the elements of the previous Fibonacci´s succession is', total)
except:
    if ValueError:
        print('An integer must be introduced to perform the operation')
