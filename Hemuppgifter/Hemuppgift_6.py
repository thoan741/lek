# 27 a)

def insertFirst(L, e):
    """
    pre: Listan L måste existera, ursprungligen skapad av createList. fullList(L) måste ge False.
    post: Elementet e har lagts till längst fram i listan L. Om Listan L var tom innan har e blivit det
     enda elementet i L.
    """
    setFirst(L)
    insertBefore(L, e)

# 27 c)
def removeFirst(L)
    """
    pre: Listan L måste existera, ursprungligen skapad av createList. emptyList(L) måste ge False.
    post: Det första elementet i listan har tagits bort. om
    """

    setFirst(L)
    removeFromList(L)

# 27 e)

def setMiddle(L):
    """
    pre: Listan L måste existera, ursprungligen skapad av createList. emptyList(L) måste ge False.
    post: Pekaren pekar på det mittersta elementet. Om listan innehåller ett jämt antal element,
     finns två element som kan ses som mittersta, i detta fall kommer det vara det senare elementet
     som pekaren pekar på.
    """
    i = listSize(L) // 2
    setPosition(L, i)






# 27 h)

def reverse(L):
    """
    pre: L existerar och har skapats av createList, och emptyList(L) ger False.
    post: Listan L har vänts. Om L endast innehöll ett element är listan L oförändrad.
    """
    p1 = 0
    p2 = listSize(L) - 1
    while p1 < p2:
        interchange(L, p1, p2)
        p1 += 1
        p2 -= 1

