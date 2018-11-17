# Uppgift 16b, 17a, 18

# 16b)


def valueOfIndex(lst):
    length = len(lst)
    maxIndex = length - 1
    while True:
        indexInput = input("listan innehåller " + str(length) + " element. Välj ett index att skriva ut: ")
        try:
            indexInput = int(indexInput)
            try:
                valueOfIndex = lst[indexInput]
                print("På index", indexInput, "finns elementet", valueOfIndex)
            except IndexError:
                print(indexInput, "är ett för stort index! Indexet måste ligga mellan 0 och", maxIndex)
        except ValueError:
            print("'" + str(indexInput) + "'", "är inte ett heltal. Indexet måste vara ett heltal.")


# valueOfIndex([1, 2, 3, 4, 5, 6, 7, 8])



















# Uppgift 17a)

def indexOfMaximum(lst):
    i = 0
    max = lst[0]
    lst = lst[1:]
    for each in range(len(lst)):
        if max < lst[each]:
            max = lst[each]
            i = each + 1
    return i

print(indexOfMaximum([1, 3, 5, 6, 4, 5, 2]))


def sort(lst):
    for i in range(len(lst)):
        indexOfMax = indexOfMaximum(lst[i:]) + i
        lst[indexOfMax], lst[i] = lst[i], lst[indexOfMax]
    return lst

print(sort([1, 3, 5, 6, 4, 5, 2]))

#alternativt

def sorting(lst):
    for i in range(len(lst)-1):
        m = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]
    return lst


print(sorting([1, 3, 5, 6, 4, 5, 2]))









# Uppgift 18

# Problemet är att efter dag 32767 kan inte räknaren fortsätta säkna upp.

# Ett sätt skulle vara att ha två räknare, båda startar på 0, en som räknas upp för varje dag.
# När den räknaren som räknas upp varje dag når det maximala int-talet, kommer den sättas till 0,
# och den andra räknaren kommer att räknas upp med 1. På så sätt kommer den ena räknaren att räkna upp varje dag fram
# tills max-talet, och då resettas. Den andra räknaren kommer ha koll p hur många gånger maxtalet har nåtts.
# Om man skulle vilja ha koll på ännu fler dagar, som hanterar när även den andra räknaren blir full, skulle en tredje
# räknare kunna införas som resettar den andra räknaren och räknar upp med när den blir full. Och på så sätt
# kan ännu fler räknare införas.

# t.ex
def dayCounter():
    a = 0
    b = 0
    while b < 20 or a < 235:
        if a < 32767:
            a += 1
        else:
            a = 0
            b += 1
    return b, a


print(dayCounter())


# Ett annat sätt kan vara att spara varje siffra i talet på en egen plats i en lista. Och sedan skriva ut talet
# som en teckensträng.





def Counter():
    a = []
    b = []
    c = ""
    while a != [1, 5, 7, 2, 3, 4]:
        if len(a) == 0:
            a.append(1)
        elif a[-1] != 9:
            a[-1] += 1
        else:
            while len(a) > 0 and a[-1] == 9:
                b.append(0)
                a.pop()
            if len(a) == 0:
                a.append(1)
                a = a + b
                b = []
            else:
                a[-1] += 1
                a = a + b
                b = []

    for i in a:
        c = c + str(i)

    return c


print(Counter())
