from Seq import Seq

# First we are going to invoke the strings

s1 = Seq("AGTCCAGTGCAG")
s2 = Seq("CAGCG")
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())


sequences = [s1, s2, s3, s4]

for i in range(len(sequences)):
    tlb= sequences[i].len()
    print(tlb)