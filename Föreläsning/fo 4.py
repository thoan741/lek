#fo 4

#hashtabell

#skapas med måsvingar {} och par av nyckel och värde, t.ex:

Ht ={1:"jan", 12:"dec", 5:"maj"}

#kan skapas med dict()
ht=dict()
ht[1]="jan"
ht[12]="dec"
ht[5]="maj"

print(ht)

print (ht[1]) #skriver ut jan
print (ht[5]) #skriver ut maj

if 15 in ht:
    x = ht[15] #x odefinierad ty ht[15] finns ej

nycklar = [1,2,5,7,"hej"]
varden= ["ett", "tva", "fem", "sju","hi"]

d=dict(zip(nycklar,varden))

print(d)

# Hashtabell kan skapas från två listor
# som att dra ihop ett blixtlås:
keys= [1,12,5]
values=["jan","dec","maj"]
parvis=zip(keys,values)
ht=dict(parvis)

#ytterligare operationer
#Antalet element i tabellen:
len(ht)
#Ta bort element:
del ht[12]
#Kopiera hela tabellen:
htcopy = ht.copy()

#try och except är reserverade ord
#som används för hantering av
#exekveringsfel.
plista= ['s','v','m','mp','fp','c','kd']
try:
    i=input("Ange index: ")
    i=int(i)
    parti=plista[i]
except:
    print ("Nagot fel intraffade") 

#klass och instans
#en klass är en mall för ett objekt, t.ex. bil, konto
#ett objekt är är en typ av en klass, t.ex. den röda bilen

#instansering

class Kurs(object):
    pass

k1=Kurs()
k1.bet = "prgi13"
print (k1.bet)
k2=Kurs()
k2.bet = "datae12"
print(k2.bet)

#try:
#Kod som kan orsaka något typ
#av exekveringsfel
#except:
#Kod som exekveras om och
#endast om det blir något fel i
#kodblocket efter try

#Kod i blocket mellan try: och
#except: börjar exekvera, men så
#fort ett fel uppstår i någon rad
#avbryts exekveringen direkt,
#resterande rader i blocket
#exekveras inte och koden som
#finns i blocket efter except: börjar
#exekvera i stället.
# Ett exempel:

plista= ['s','v','m','mp','fp','c','kd']
try:
    i=input('Ange index: ')
    i=int(i)
    parti = plista[i]
except IndexError:
    print ("ogilltigt index")
except ValueError:
    print ("index måste var ett tal")
except:
    print ("uppstod något okänd fel!")  


class Person:

    def __init__(self,n,a):
        self.namn = n
        self.alder = a

p = Person("Kalle",12)
p2 = Person("Petra",20)

print(p.namn,p.alder)
print(p2.namn,p2.alder)

class polygon:


    def __init__(self,listaAvLinjer):

        self.linjer=listaAvLinjer

    def omkrets(self):
        omk=0
        for l in self.linjer:
            omk=omk+l
        return omk
    
    def area(self):
        return 4711

class Rektangel(polygon):

    def __init__(self,l1,l2):
        super(Rektangel, self).__init__([l1,l2,l1,l2])

    def area(self):
        return  self.linjer[0]*self.linjer[1]


class Kvadrat(Rektangel):

    def __init__(self,l1):
        super(Kvadrat,self).__init__(l1,l1)


r=Rektangel(12,30)
print(r.omkrets())
print(r.area())
a=Kvadrat(5)

print(a.area())
print(a.omkrets())


class kurs(object):
    totAntalStuds= 0

    def __init__(self, namn, beteckning):
        self.namn = namn
        self.bet = beteckning
        self.antal = 0

    def sattAntalStudenter(self,a):
        self.antal=a
        kurs.totAntalStuds += a


k1=kurs("Datalogi I", "sudata12")
print(k1.antal)
k1.sattAntalStudenter(65)
print(k1.antal)