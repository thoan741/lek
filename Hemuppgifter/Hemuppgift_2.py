# Hemuppgift 2

square = lambda x: x*x

harm = lambda x: 1/x

summa = lambda x: x

# Uppgift 9

# a)

def summering(var1, var2):
    res = 0
    for tal in range(var1, var2+1):
        res += tal
    return res

a = summering(1,5)

print(a)

# 9b)

def harmSum(var1, var2):
    res = 0
    while not var1 > var2:
        res = res + 1/var1
        var1 += 1
    return res

a = harmSum(3, 7)

print(a)

# 9c)

def funcSum(var1, var2, op):
    res = 0
    while not var1 > var2:
        res = res + op(var1)
        var1 += 1
    return res



a = funcSum(1, 5, summa)
b = funcSum(3, 7, harm)
c = funcSum(1, 3, square)

print(a)
print(b)
print(c)

# uppgift 10

def do_to_each(op, ls):
    b = 0
    for a in ls:
        ls[b] = op(a)
        b += 1
    return ls


def doToEach(op, ls):
    a = []
    for b in ls:
        c = op(b)
        a.append(c)
    return a

a = do_to_each(square, [1, 2, 3, 4])
b = doToEach(square, [1, 2, 3, 4])

print(a)
print(b)

