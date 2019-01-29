print("\n",'---This is the solution for exercise 5---',"\n")

with open('dna_seq.txt', 'r') as f:
    for line in f:
        line = line.rstrip("\n")
        print(line)
        print('Total length: ', len(line))
        A = 0
        G = 0
        C = 0
        T = 0

        for i in range(len(line)):
            if line[i] == 'A':
                A += 1
            elif line[i] == 'G':
                G += 1
            elif line[i] == 'C':
                C += 1
            elif line[i] == 'T':
                T += 1

        print('A: ', A)
        print('C: ', C)
        print('T: ', T)
        print('G ', G)
        print("\n")

