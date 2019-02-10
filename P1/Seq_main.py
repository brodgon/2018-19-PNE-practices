from Seq import Seq

# First we are going to invoke the strings

s1 = Seq("AGCTGTACGTAAC")
s2 = Seq("CAGCG")
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())

sequences = [s1, s2, s3, s4]
print("\n")
for i in range(len(sequences)):
    tlb= sequences[i].len()
    countinga = sequences[i].strbases.count('A')
    countingc = sequences[i].strbases.count('C')
    countingg = sequences[i].strbases.count('G')
    countingt = sequences[i].strbases.count('T')
    perca = Seq.perc(sequences[i], 'A')
    percc = Seq.perc(sequences[i], 'C')
    percg = Seq.perc(sequences[i], 'G')
    perct = Seq.perc(sequences[i], 'T')
    print("Sequence {}: {}".format(i+1, sequences[i].strbases))
    print("     Length: {}".format(tlb))
    print("     Bases count: A:{}, C:{}, G:{}, T:{}".format(countinga,countingc,countingg,countingt))
    print("     Bases percentage: A:{}%, C:{}%, G:{}%, T:{}%".format(perca, percc, percg, perct))

print("\n", "This is the end of the program!")
