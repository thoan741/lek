#föreläsning 6

import random

#slumptal exempel:

info = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(10000):
    info[random.randint(1, 6)] += 1
for i in info:
    print (i, ':', info[i])

#alternativt

info = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(10000):
    info[random.choice([1, 2, 3, 4, 5, 6])] += 1

folk = ['Kalle', 'Eva', 'Lisa', 'Johan',
'Johanna', 'Anders', 'Jessica',
'Per', 'Leo']
rest = []
lag1 = random.sample(folk, 3)
for i in folk:
    if i not in lag1:
        rest.append(i)
lag2 = random.sample(rest, 3)
print('lag 1:', lag1)
print('lag 2:', lag2)

a = [1, 2, 3, 4, 5]

random.shuffle(a)

print(a)

# Antag att vi har två mängder, A och B samt ett element x
# len(A) antalet element i A
# x in A True om x är ett element i A
# x not in A True om x inte är ett element i A
# A.isdisjoint(B) True om A inte har några element gemensamma med B
# A.issubset(B) True om A ⊆ B
# A <= B som ovan
# A < B True om A ⊂ B
# A.issuperset(B) True om A ⊇ B
# A >= B som ovan
# A > B True om A ⊃ B

a = {1,2,3}

print(a)

a ={1,2,3,1,2,3}   # måsvingar används för att skapa mängder, dubbletter tas bort

print(a)

B = {1,2,3}
x = 4

A = B.copy() # Låt A bli en kopia av B
A.add(x)     # Lägger till elementet x till mängden A
A.remove(x)  # Tar bort x från mängden A
#              ger ett "KeyError" om A inte innehåller x
A.discard(x) # Tar bort x från mängden A om x finns i A
A.pop()      # Tar bort ett godtyckligt element från mängden A
A.clear()    # Tömmer mängden A

# A.union(B [, ...]) A ∪ B . . .
# A | B [ | ...] samma som ovan
# A.intersection(B [, ...]) A ∩ B . . .
# A & B [ & ...] samma som ovan
# A.difference(B [, ...]) A \ B . . .
# A - B [ - ...] samma som ovan
# A.symmetric difference(B) A ∆ B = (A ∪ B) \ (A ∩ B)
