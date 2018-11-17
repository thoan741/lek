import math

# Uppgift 4b)



def intCheck():
    talString = input("Mata in ett heltal tack: ")

    try:
        tal = int(talString)
        print("Du matade in: ", tal)
    except ValueError:
        print(talString , "är inte ett heltal, försök igen!")
        intCheck()

intCheck()

# Uppgift 5

def kast():
    v = input("Vilken hastighet?: ")
    α = input("Vilken vinkel? (i grader): ")
    try:
        v = float(v)
        α = float(α)
        g = 9.82
        α = α * math.pi / 180
        d = v ** 2 * math.sin(2 * α) / g
        h = v ** 2 * math.sin(α) * math.sin(α) / (2*g)
        x = (d, h)
        print(x)
    except ValueError:
        print("Hastighet och gradtal måste matas in som siffror!")


kast()






# Uppgift 6:

def ifTriangle():
    a = input("mata in längden av en första linje: ")
    b = input("mata in längden av en andra linje: ")
    c = input("mata in längden av en tredje linje: ")

    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a < b + c and b < a + c and c < a + b:
            print("True")
        else:
            print("False")
    except ValueError:
        print("Mata in längderna som tal, tack!")


ifTriangle()