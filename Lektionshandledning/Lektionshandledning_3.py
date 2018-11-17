# Lektionshandledning 3

a = [0]*5  # Skapar en lista [0,0,0,0,0]

# Uppgift 11

# Skriv en funktion som tar ut indexet för det minsta elementet i en lista.

def index_of_minimum(l):
    if not l:              # ger True om listan är tom. Funkar även på andra typer, 0 ger False, strängar ger "" False.
        raise ValueError("index_of_minimum() arg is an empty sequence")
    l_min =l[0]
    i_min = 0
    for i in range(1,len(l)):
        if l_min > l[i]:
            l_min = l[i]
            i_min = i
    return i_min

print(index_of_minimum([3,2,1,2,3]))
try:
    index_of_minimum([])
except ValueError as e:
    print(repr(e))
    print(str(e))

"""
I python3:
* Ett itererbart objekt är ett objekt vars metod metod __iter__ returnerar en iterator.
* En iterator är ett objekt vars metod __next__ returnerar ett objekt (vanligtvis nästa element)
  och kör raise StopIterator när den har nått slutet.
"""

import random

class MyIterable:

    #def __init__(self):
    #    self.__l = [1, 2, ":D"]
    #    self.__current = -1

    def __init__(self, start, end):
        self.__start = start
        self.__end = end
        self.__current = start -1

    def __iter__(self):          # Måste finnas för att det ska vara itererbart.
        return self

    def __str__(self):
        return "({},{},{})".format(self.__star,self.__end,self.__current)

    def __next__(self):
        self.__current += 1

        if self.__current == self.__end:
            raise StopIteration

    #def __next__(self):          # Måste finnas för att kunna iterera.
    #    r = random.randint(1,10)
    #
    #    if r == 10:
    #        raise StopIteration()

        return self.__current
        #return r


#for i in MyIterable():
#    print(i, end=",")

for i in MyIterable(0,15):
    print(i, end=",")

print("")

obj = MyIterable(0,15)
print(next(obj))
print(next(obj))

# Uppgift 12

# Skriv ett program som läser två tal och en operator från
# en inmatningsrad och beräknar och skriver ut värdet av postfixuttrycket

import operator

operators = {"*":operator.mul, "+":operator.add, "-": operator.sub, "/":operator.truediv}

while True:
    in_str = input("Mata in ett uttryck: ")
    a, b, op = in_str.split()
    a, b = int(a), int(b)
    print(in_str + " = " + str(operators[op](a,b)))
