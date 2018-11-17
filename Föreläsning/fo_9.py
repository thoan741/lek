# Föreläsning 9, avbrott.
"""
def funktion(filen):
    lista = [1, 3, 2, 4, 6]
    detBlirFel = True
    while detBlirFel:
        try:
            s=input("ange index: ")
            indx=int(s)
            valtTal = lista[indx]
            f = open(filen)
            detBlirFel = False
        except EOFError as v:
            print("inmatningsfel")
            print(v)
        except ValueError as v:
            print("ett tal måste matas in", v)
        except IndexError as v:
            print("Talet måste vara mellan 0 och 4")
        except:
            raise Exception(filen)
    print(valtTal)

try:
    funktion("en funktion som inte finns:")
except:
"""

