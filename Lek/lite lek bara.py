def siffersumma():
    tal = input("skriv in ett heltal: ")
    res = 0
    try:
        tal = int(tal)
        while tal != 0:
            res = res + tal % 10
            tal = tal // 10
        print("Siffersumman är: ", res)
    except ValueError:
        print("Skriv in ett heltal, tack.")

siffersumma()