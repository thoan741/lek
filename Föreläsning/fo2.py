#fo2

#listor skapas med hakparenteser [a, b, c, d]
[["hej", 151] , 10.59] #första elementet är en lista
lista = [1, 2, "hej"]
lista = lista + [4, 5] #lägg till [4, 5] längst bak i listan lista
print(lista)

lista = [1,2]
lista = lista * 3 #lista * 3 blir [1,2,1,2,1,2]

print(lista)

#indexvärde för listor, första element fås med index 0

lista = [12,13,14,15,16]

print(lista[2]) #skriver ut index 2 i listan, alltså tredje värdet.

lista2 = lista[1:4] #lista2 blir en lista från och med index 1 till index 4 men ej innehållandes index 4.
print(lista2)

lista=[5,6,7,4,3,1,9]
lista2 = lista[1:6:2] #lista2 blir en lista med vartannat element mellan index 1 och index 6 i lista
print(lista2)

lista=[1,2,3,4,5,6]
lista[1:3]="897"   #index 1 och index 2 byts ut mot 8, 9 och 7
print(lista)

s="blahonga"
print(s[3:6]) #skriver ut hon, vilket är index 3,4,5 i strängen "blahonga"

lista= [1,2,3,4,5,6]
lista[1:3] = "a" #ny lista blir [1,a,4,5,6]
lista[4]= "hej" #ny lista blir [1,a,4,5,'hej']
print(lista)

lista = [1,2,3,4,5,6]
del lista[1:3] #tar bort element från och med index 1 till index 3
print(lista) 

lista = [1,2,3,4,5,6]
lista.reverse() #vänder på listan
print(lista)
lista = [1,4,3,6,5,2]
lista.sort() #sorterar lista i storleksordning, kraschar om det finns element utan värde
print(lista)

lista = [1,3,4,6,2,5]
lista.sort()
lista.reverse()
print(lista)

lista.append(0)  #lägger till element längst bak
lista.extend([-1,-2,-3]) #lägger till en lista längst bak
print(lista)

#en tupel är en omuterbar lista, skrivs med vanlig parentes
a = (1,2,3)
#kan ej ändra i listan
list(a)
#skapar en lista av element i en tupel

#tupler kan konkateneras (ihopläggning av två strängar):
tupel = (1,2,3) + (4,5,6) 
print(tupel)
#tupler kan upprepas
tupel = (1,2,3)
print(tupel * 3)

print(tupel[1]) #kan även ta index på tupler
# tupel[1] = 33, fungerar ej, kan inte ändra värde i tupel

#strängar

state="urbra"
del1=state[0:2]
del2=state[2:] 
del3=state[:3]

print(len([1,2,5])) 

if 3 in [1,2,3]:
    print("3 finns i listan")
else:
    print("3 finns inte i listan")

lista = [12,13,14,15,16]
for x in lista:
    print(x , "",end="") 

i=0
while i < 10:
    print(i)
    i=i+1 #kan också skrivas i += 1

i=0
#while i<10:
#    print("hej ",end="")
#    if i>6:
#        continue  #kör inte det som står under om if satsen uppfylls
#    i +=1

while i<10:
    print("hej ",end="")
    if i>6:
        break  
    i +=1

for i in [0,1,2,3,4,5,6,7,8,9]:
    print("hej ",end="")
    if i>6:
        continue    
    print(i)
else:
    print("ocksa else delen!")

list(range(6,1,-1))
list(range(10,0,-2)) 

import random
random.randint(0,6)
r = random.random()
t = random.randrange(3,6) 
import math

lista = [1,2,3,[1,7], 9]
lista2 = lista[2:4]
lista[3][1]= 77 #här ändras den inre listan även i lista2
lista[2] = 5 #lista2 ändras inte

print(lista2)