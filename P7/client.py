import http.client
import json
import termcolor
from Seq import Seq
import collections


PORT = 80
SERVER = 'rest.ensembl.org'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
sequence = json.loads(data1)
termcolor.cprint("We are working with the following sequence: {}".format(sequence['seq']), "blue")
FRATgene = Seq(sequence["seq"])
tl = FRATgene.len()
print("This sequences has a total length of {} basis".format(tl))
countT = FRATgene.strbases.count('T')
print("We find {} Thymine (T) bases in FRAT1 gene".format(countT))
frequent = collections.Counter(FRATgene.strbases).most_common(1)[0]

print("The most popular character we find is {} which appears in {} %".format(frequent[0], Seq.perc(FRATgene, frequent[0])))
perca = Seq.perc(FRATgene, 'A')
percc = Seq.perc(FRATgene, 'C')
percg = Seq.perc(FRATgene, 'G')
perct = Seq.perc(FRATgene, 'T')
print("The total percentages of the bases are: ")
print("     A : {} %".format(perca))
print("     T : {} %".format(perct))
print("     C : {} %".format(percc))
print("     G : {} %".format(percg))


print("CONTENT: ")

