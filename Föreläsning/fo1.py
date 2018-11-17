#Föreläsning 1
import time
print("hej")
print("hur är det?")    #skriver ut på två olika rader

print("hej, ",end="*")
print("hur är det?") #skriver ut på en rad, end="*" tar bort radbytet och lägger till * efter utskriften hej

print("hej","MEJ","NEJ",sep="*") #lägger till * efter varje utskrift utan sista innan sep
print("hej","MEJ","NEJ",sep="!",end="?") 
print("")


age = 27
name = "Thomas"
length = 1.90
print(age, name, length)

print(type(age))
print(type(name))
print(type(length))

length = 1.80

print(length+5)

#variabelnamn får inte börja med siffror
#använd korta och beskrivande variabelnamn
#var konsekvent vid val av variabelnamn
#följ traditionella namn
#case sensitive

time.sleep(0)

v = "e"
n = 'e'

#input("?\n") #förväntar sig en inmatning från tangentbordet. \n betyder byt rad

#indata = input("ange en siffra: ")

#print("du matade in siffran: ", indata)

def enfunktion():
    """denna funktion är oanvändbar""" #inte kommentar, hjälp om man kör help
    print("skriver ut något roligt?")

enfunktion()

print("ab" + "ba")  #=> abba

#age = input("hur gammal är du? ")
#age = int(age)
#exage = age + 4.5
#print("du kommer att vara ", exage, "när du tar examen")

#jämförelseoperander
# == jämför om lika
# != jämför om inte lika
# < 
# <=
# >
# >=

A="hej"
B="hej"
print(A is B)

#C=input("mata in hej:")

#print(C)
#print(A is C)

bokpris = 5
#bokpris = int(input("vad kostar boken?"))

if bokpris > 500:
    print("dyr bok")
    print("ingen affär")
elif bokpris > 300:
    print("dyr men jag behöver den")
else:
    print("billig")

varv=0

while varv < 3:
    print("hej")
    varv = varv + 1