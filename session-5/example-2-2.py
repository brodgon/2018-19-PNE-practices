from Bases import count_bases

sequences = []

s1 = input("Please enter a valid sequence 1: ")
s2 = input("Please enter a valid sequence 2: ")

sequences.append(s1)
sequences.append(s2)


for i in range(len(sequences)):
    base_count = count_bases(sequences[i])
    # Calculate the total sequence length
    tl = len(sequences[i])
    if tl > 0:
        # Calculate percentages if possible
        perca = round(100.0 * base_count['A'] / tl, 1)
        percg = round(100.0 * base_count['G'] / tl, 1)
        percc = round(100.0 * base_count['C'] / tl, 1)
        perct = round(100.0 * base_count['T'] / tl, 1)

        # Print results
        print("Sequence", i+1, " is {} bases in length".format(tl))
        print("Base A")
        print(" Counter: {}".format(base_count['A']))
        print(" Percentage: {}%".format(perca))
        print("Base G")
        print(" Counter: {}".format(base_count['G']))
        print(" Percentage: {}%".format(percg))
        print("Base C")
        print(" Counter: {}".format(base_count['C']))
        print(" Percentage: {}%".format(percc))
        print("Base T")
        print(" Counter: {}".format(base_count['T']))
        print(" Percentage: {}%".format(perct))

    else:
        # Deals with possible Zero division
        print("Total length is 0")
        print("We cannot work with empty sequence")
        print("Rerun the program and try again introducing a valid one!")
    print("\n")

print("---Program finishes here!---")





