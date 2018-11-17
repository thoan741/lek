# Lektionshandledning 6

"""
with open ("fil") as f:
kommer stänga automatiskt.

string.count(x) räknar antal förekomster av x i en sträng.

text.remove("x") tar bort alla x ur strängen.
"""

# Uppgift 27


def createList():
    """
    pre: inga
    post: en "lista" har skapats och en referens till listan returneras.
    """


def emptyList(L):
    """
    pre: Listan L måste existera,
     ursprungligen skapad av createList.
    post: Returnerar True om inga element finns i listan,
     False annars.
    """

# 27 b) lägg till ett element sist i en lista.

def insertLast(L,e):
    """
    pre: L måste existera...
     e är ett element som inte redan finns i någon lista.
     listan är inte full.
    post: e har satts in sist i L och L är ett element längre.
    """

    setLast(L)
    insertAfter(L,e)

# 27 d) Ta bort sista element i listan


def removeLast(L):
    """
    pre: L måste existera...
     emptyList(L) måste vara False.
    post: sista elementet i L har tagits bort.
     Om L bara innehåller ett element är nu L tom.
    """
    setLast(L)
    removeFromList(L)

# 27 f)


def createCopy(L):
    """
    pre: L måste existera...
    post: L2 har skapats, är en kopia av L,
     och en referens till till L2 returneras
    """
    L2 = createList()
    setfirst(L)
    if emptyList(L):
        return L2
    while onList(L):
        insertAfter(L2, retrieve(L))
        setLast(L2)
        setNext(L)
    return L2

# 27 g) Lägga till alla element i en lista, längst bak i en annan lista.


def extendFromList(L, L2):
    """
    pre: L och L2 måste existera....
    post: L2 har förlängts med alla element från L.
    """
    setFirst(L)
    setLast(L2)
    while onList(L):
        insertAfter(L2, retrieve(L))
        setLast(L2)
        setNext(L)

# 27 i) Dela upp lista. Listan ska sedan vara tom.


def separateList(L):
    """
    pre: L måste existera...
    post: Referenser till L1 och L2 returneras med element ifrån L omvartannat.
     Om L bara innehåller 1 element, är L2 tom, om L är tom är båda L1 och L2 tomma.
     L kommer att vara tom.
    """
    L1 = createList()
    L2 = createList()
    lists = [L1, L2]
    currentList = 0
    setFirst(L)
    while onList(L):
        insertAfter(lists[currentList], retrieve(L)):
        currentList = (currentList + 1) % 2
        removeFromList(L)
    return L1, L2
