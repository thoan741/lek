# Uppgift 13

#BMI

def BMI():
    """
    vikt skrivs in kg och längd i cm. längden konverteras till meter innan beräkning.
    värdet rundas till hundradel och jämförs mot alla viktklasser. sedan skrivs BMI och viktklass ut.
    """
    weight = float(input("Ange vikt (i kg): "))
    height = float(input("Ange längd (i cm): "))
    height = height / 100
    a = weight / height ** 2
    # a = float('{:.2f}'.format(a))
    a = round(a, 2)
    if a >= 30:
        b = "Fetma"
    elif a >= 25:
        b = "Övervikt"
    elif a >= 20:
        b = "Normalvikt"
    else:
        b = "Undervikt"
    print("BMI = ", a)
    print("Viktklass = ", b)


BMI()


# Uppgift 14

def read_lines(n):
    """
    En input loopas n gånger, varje gång appendas inskriften i en lista och sedan returneras listan.
    :param n: ett heltal som beskriver hur många inskrifter som ska göras.
    :return: returnerar en lista där varje element är en enskild input.
    """
    a = 0
    b = []
    while a < n:
        c = input("skriv något: ")
        b.append(c)
        a += 1
    return b

print(read_lines(3))