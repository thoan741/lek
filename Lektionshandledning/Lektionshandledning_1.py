import math

# from math import sqrt     #importerar bara sqrt från math och kan kalla på sqrt som sqrt(x) istället för math.sqrt(x)
# from math import * #importerar hela math utan att behöva använda math. innan den kallas på. kan uppstå namnkrockar
# kan importera egna python dokument from x import y

# Lektionshandledning_1

# str = string (sträng)
# int = integer (heltal)
# float = float (flyttal/decimaltal)
# bool = boolean (sanningsvärden)


# for-loop används för att gå igenom en sekvens

ls = [1,2,3]

for siffra in ls:    # för varje element i lista, gör det som står nedan
    print(siffra)   # => utskrift 1 2 3

# uppgift 1

numberString = input("mata in ett tal tack: ")
numberSum = 0

for number in numberString:
    numberSum = numberSum + int(number)
    # numberSum += int(number)              #                                               gör samma sak som raden ovan
print("Siffersumman blir: ", numberSum)
#                                                       print("Siffersumman blir: " + str(numberSum)) kan också användas

#uppgift 2

cartesString =input("Mata in en punkt i kartesiska koordinater (exempel: 3,4): ")
x = int(cartesString.split(",")[0])      # split kommer att dela upp strängen i en lista där varje element delas upp vid varje kommatecken (,).
#                                         [0] kommer plocka ut första elementet i listan som fås med split.
y = int(cartesString.split(",")[1])      # På samma sätt hämtas andra variabeln ut här.
r = math.sqrt(x**2 + y**2)               # ** betyder upphöjt till
theta = math.atan2(y,x)                  # leta i pythons officiella dokumentation för att se vilka funktioner som finns definierade i bibliotek.
print("De polära koordinaterna är : ", r , theta)

# Uppgift 3

# Skriv ett program som läser två tal och en operator från en inmatningsrad och beräknar och skriver ut värdet av postfixuttrycket.
# Ex. på dialog:  2 3 + => 5
#                2 3 * => 6

postFixString = input("Skriv in ett uttryck i postfixnotation(2 operander): ")

if postFixString[4] == "+":
    res = int(postFixString[0]) + int(postFixString[2])
elif postFixString[4] == "*":
    res = int(postFixString[0]) * int(postFixString[2])
elif postFixString[4] == "-":
    res = int(postFixString[0]) - int(postFixString[2])
elif postFixString[4] == "/":
    res = int(postFixString[0]) / int(postFixString[2])
print("resultatet blir: ", res)

# kan använda sig av eval för att kolla operand

# 4a)

# felhantering, ska mata in heltal. om heltal, returnera heltal, i annat fall ska felmeddelande komma

talString = input("Mata in ett tal tack: ")
try:                     # try försöker göra något, om det inte går gör den det som står i except
    tal = int(talString)
    print("Du matade in: ", tal)
except ValueError:       # om ValueError uppstår i try, gör detta. ValueError i detta fall, då det är den typen av fel som kan uppstå i try. I andra fall kan det bli andra errormeddelanden.
    print(talString , "är inte ett tal...")

counter = 10

while counter > 0:
    print(counter)
    counter -= 1
print("Woosh!")

# tips för uppgift 4b

# while correctInput == False:

# while everythingSeemsFine():

def myFunction(x,y):
    res = x+y**2
    return res

myResult = myFunction(2,4)
