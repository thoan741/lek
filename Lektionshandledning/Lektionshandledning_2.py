# Uppgift 7

def sifferSumma1(n):
    sifferSträng = str(n)
    Summa = 0
    for tecken in sifferSträng:
        Summa += int(tecken)
    return Summa

# alternativt

def siffersumma2(n):
    Summa = 0
    while n:          # siffran 0 är false, alla andra är true
        Summa += n%10
        n = n // 10  # alternativt n//= 10
    return Summa

# map(funktion,iterabel)
# ett tredje sätt på en rad

def siffersumma3(n):
    return sum(map(int, str(n)))

# range(4) = [0,1,2,3]

# range(1,5] = [1,2,3,4]

# range(1,12,2) = [1,3,5,7,9,11]

# Uppgift 8

def add_vectors(vec1,vec2):
    sum_vector=[]
    for i in range(len(vec1)):
        sum_vector.append(vec1[i]+vec2[i])
    return sum_vector

# ls = [1,2]
# ls.extend([1,2,3]) = [1,2,1,2,3]

# ls = [1,2]
# ls.append([1,2,3]) = [1,2,[1,2,3]]

# Nästlade loopar

for c in ['A','B','C']:
    for i in [1,2,3]:
        print(c,i)      # => A 1 sen A 2 sen A 3 sen B 1 sen B 2 sen B 3 sen C 1 sen C 2 sen C 3

for i in range(5):
    for j in range(i):
        print('*', end="")
    print()                     # => i = 0, inre kommer inte köras. i = 1, inre körs 1 gång, osv... upp till i = 4.
#                                 utskrift bli * (ny rad) ** (ny rad) *** (ny rad) ****



