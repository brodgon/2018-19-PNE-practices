print('This program will create a function to sum the n first integers introduced by the user')


def summing(n):
    total = 0
    for i in range(n):
        total = total + i + 1
    return total

# - - - Main program - -


try:
    num = int(input('Enter a valid number: '))
    total_sum = summing(num)
    print('The total sum from 0 to the number introduced is ', format(total_sum))
except:
    if ValueError:
        print('An integer must be introduced to perform the operation')



