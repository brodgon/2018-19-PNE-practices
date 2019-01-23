print('Hello')
print('Just testing PyCharm IDE')
print('HEY')
print('testing....2')
print('testing....1')

print('Printing numbers from 1 to 20')
for  i in range(20):
    print(i+1)


def sumn(x):
    total=0
    for i in range(x):
        total=total+i+1
    return total
#--Main program
num=int(input('Enter a number'))
total_sum= sumn(num)
print('The total sum is {}',format(total_sum))

