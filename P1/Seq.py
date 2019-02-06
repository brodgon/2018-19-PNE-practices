class Seq:
    strbases: object

    def __init__(self, strbases):
        print("New sequence created")

        self.strbases = strbases

    def len(self):
        tl = len(self.strbases)
        return tl

    def complement(self):
        compd = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G' }
        compseq = ''
        for i in self.strbases:
            compseq += compd[i]
        return compseq

    def reverse(self):
        reverted = self.strbases[::-1]
        return reverted

    def count(base):
        counter = 0
        for i in self.strbases:
            if i == base:
                counter += 1
        return counter

    def perc(base):
        if tl > 0:
           perce = round(100.0 * counter / tl, 1)
        else:
            print("Can't calculate percentages with 0 length")


