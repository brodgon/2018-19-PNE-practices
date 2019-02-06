from Bases import count_bases

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

