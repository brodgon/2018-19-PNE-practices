count_A = 0
count_G= 0
count_C = 0
count_T = 0


with open('CPLX2.txt', 'r') as f:
    for line in f:
        if line.startswith(">"):
            next(f)
        else:
            for i in range(len(line)):
                if line[i] == "A":
                    count_A += 1
                elif line[i] == "G":
                    count_G += 1
                elif line[i] == "C":
                    count_C += 1
                elif line[i] == "T":
                    count_T += 1

print("The number of adenine (A) bases are: ", count_A)
print("The number of cytosine (C) bases are: ", count_C)
print("The number of guanine (G) bases are: ", count_G)
print("The number of thymine (T) bases are: ", count_T)

