import random

a = random.randint(0,100)
x = 0

def gissaNumret(c):
    nummer = input("Jag tänker på ett heltal mellan 0 och 100, gissa vilket! ")
    c = c + 1
    try:
        nummer = int(nummer)
        if nummer == a:
            print("Grattis, du gissade rätt! Och det tog ju bara", c, "försök!")
        elif abs(nummer - a) < 3:
            print("Nu bränns det rejält, försök igen!")
            gissaNumret(c)
        elif abs(nummer - a) < 8:
            print("Nu bränns det, försök igen!")
            gissaNumret(c)
        elif nummer > a:
            print("För högt, försök igen!")
            gissaNumret(c)
        else:
            print("För lågt, försök igen!")
            gissaNumret(c)
    except ValueError:
        print("Detta var ju inte ett heltal, försök igen!")
        gissaNumret(c)

gissaNumret(x)