def count_bases(seq):
    """Counting the number of bases in the sequence"""

    # counter for the bases
    a = 0
    c = 0
    g = 0
    t = 0

    for b in seq:
        if b == 'A':
            a += 1
        elif b == 'G':
            g += 1
        elif b == 'T':
            t += 1
        elif b == 'C':
            c += 1
    # Creates a dictionary with the bases and counters
    bases_dict = {'A': a, 'G': g, 'C': c, 'T': t}
    # return the result
    return bases_dict


"""Main program"""
s = input("Please enter a valid sequence: ")
base_count = count_bases(s)
# Calculate the total sequence length
tl = len(s)
if tl > 0:
    # Calculate percentages if possible
    perca = round(100.0 * base_count['A'] / tl, 1)
    percg = round(100.0 * base_count['G'] / tl, 1)
    percc = round(100.0 * base_count['C'] / tl, 1)
    perct = round(100.0 * base_count['T'] / tl, 1)

    # Print results
    print("This sequence is {} bases in length".format(tl))
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

print("---Program finishes here!---")
