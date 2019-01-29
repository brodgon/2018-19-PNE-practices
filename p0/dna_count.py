# Exercise 4

print('---This is the solution for exercise 4---', "\n")

dna_sequence= input('Introduce a DNA sequence: ')
print('Total length: ', len(dna_sequence))
A = 0
G = 0
C = 0
T = 0

for i in range(len(dna_sequence)):
    if dna_sequence[i] == 'A':
        A +=1
    elif dna_sequence[i] == 'G':
        G +=1
    elif dna_sequence[i] == 'C':
        C +=1
    elif dna_sequence[i] == 'T':
        T +=1
    else:
        print(dna_sequence[i], 'do not code into a base')

print('A: ', A)
print('C: ', C)
print('T: ', T)
print('G ', G)

