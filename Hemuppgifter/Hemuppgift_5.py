# uppgift 23,24,25,26

# Uppgift 23

def addNumbers():
    try:
        nummerString = open("nummer.txt")

        nummerLista = nummerString.read().split()
    except FileNotFoundError:
        print("Filen finns ej!")
        return

    a = 0

    for i in nummerLista:
        try:
            a = a + float(i)
        except ValueError:
            print("Filen får bara innehålla tal!")
            return

    print(a)
    return a


addNumbers()

# Uppgift 24


def totalPrice():
    file = open("Faktura")
    string = file.read()
    faktura = string.split()
    sum = 0
    for i in range(len(faktura)):
        if faktura[i] == 'Antal:':
            a = int(faktura[i+1])
        elif faktura[i] == 'Pris:':
            b = int(faktura[i+1])
            sum += a*b
    return sum
print(totalPrice())
# Uppgift 25




def makeDict():
    symbolFile = open("text.txt")

    string = symbolFile.read()
    myDict = {}
    myList = []
    for i in string:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    for j in myDict:
        a = str(j) + " förekommer " + str(myDict[j]) +" gånger"
        myList.append(a)
    return myList

print(makeDict())

# Uppgift 26


def countOperators():
    file = input("Ange filnamn: ")
    myFile = open(file)
    myString = myFile.read()
    a = [len(myString.split("=="))-1, "=="]
    b = [len(myString.split(">=")) - 1, ">="]
    c = [len(myString.split("<=")) - 1, "<="]
    d = [len(myString.split(">"))-1, ">"]
    d[0] = d[0] - b[0]
    e = [len(myString.split("<"))-1, "<"]
    e[0] = e[0] - c[0]

    myList = [a, b, c, d, e]
    for i in range(5):
        if myList[i][0]:
            print(myList[i][1], ":", myList[i][0])
        else:
            print(myList[i][1], ": Ingen")


#countOperators()


