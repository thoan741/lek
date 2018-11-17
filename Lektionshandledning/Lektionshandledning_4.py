# Lektionshandledning 4

"""
Slicing:
ls = [1,2,3,4]
ls[0] => 1
ls[0:3] => [1,2,3]
ls[:3] => [1,2,3]
ls[2:] => [3,4]
ls2 = ls[:] => ls2 = [1,2,3,4] #skillnaden mellan detta och att skriva ls2 = ls1 är att vi här skapar en kopia,
annars pekar de på samma element.
ls[0:4:2] = [1,3]

List Comprehensions:
[x for x in range(5)] => [0,1,2,3,4]
[x**2 for x in range(5)] => [0,1,4,9,16]
[x ** 2 for x in range(100) if (x % 3) =) 0] => [0,9....]
"""

# Uppgift 15:

myTwoByTwo = [[1, 2], [3, 4]]

def det(M):
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    else:
        for i in range(len(M)):
            result = 0
            A_i = [row[1:] for row in M]    #tar bort kolumn 0.
            A_i = A_i[:i]+A_i[i+1:]
            result += (-1)**i * M[i][0] * det(A_i)
        return result

print(det(myTwoByTwo))
myThreeByThree = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(det(myThreeByThree))

# Uppgift 16:

# a)

while True:
    try:
        tal = input("Mata in ett heltal: ")
        tal = int(tal)
        print("Du skrev:", tal)
    except ValueError:
        print("'" + str(tal)+ "'", "är inte ett heltal!")
        # man kan i slutet av print skriva sep="", då ändras separatorn.
        
