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
