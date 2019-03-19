import json
import termcolor

f = open("person.json", "r")

person = json.load(f)    # info from jason read as a dictionary

print()

termcolor.cprint("Name: ", "green", end=' ')
print(person['Firstname'],person["Lastname"])
termcolor.cprint("Age: ", "blue", end=' ')
print(person['Age'])

for i, num in enumerate(person["Phonenumber"]):   # with enumerate function the positions will be shown
    termcolor.cprint("User phone number:{} ".format(i),"red")
    termcolor.cprint("  Type :", "yellow", end='')
    print(num['type'])
    termcolor.cprint("  User phone number: ", "yellow", end='')
    print(num['number'])

