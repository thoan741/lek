operatorList = ["+", "-", "*", "/", "quotient", "<", "=", "and", "or"]

dataList = ["int", "real", "bool"]


def ifValid(string):
    string = string.split()
    if not string[0] in operatorList:
        return [False, 0]
    elif not len(string) == 3:
        return [False, 1]
    else:
        if not string[1] in dataList or not string[2] in dataList:
            return [False, 2]
        if not string[1] == string[2]:
            return [False, 3, string[0]]
        elif string[1] in dataList:
            return validOperations(string)
        else:
            return [False, 4]

def whereToStart(string):
    a = 0
    b = 0
    c = 0
    startIdx = 0
    slutIdx = 0
    for i in range(len(string)):
        if string[i] == "(":
            if a > b:
                startIdx = i
                b = a
            a += 1
        elif string[i] == ")":
            if a > c:
                slutIdx = i
                c = a
            a -= 1
    if not a == 0:
        return [1, False]
    else:
        return [startIdx, slutIdx]

def validOperations(str):
    if str[0] in operatorList[:4]:
        if str[1] == "bool":
            return [False, 5, str[0]]
        else:
            return [True, str[1]]
    elif str[0] == operatorList[4]:
        if str[1] == "int":
            return [True, "int"]
        else:
            return [False, 6, str[0], str[1]]
    elif str[0] in operatorList[5:7]:
        if str[1] == "bool":
            return [False, 7]
        else:
            return [True, "bool"]
    elif str[0] in operatorList[7:]:
        return [True, str[1]]


def Check(str):
    while len(str.split()) > 1:
        x = whereToStart(str)
        if not x[1]:
            print("Parentesfel!")
            return
        y = x[0]
        z = x[1]

        if ifValid(str[y+1:z])[0]:
            str = str[:y] + ifValid(str[y + 1:z])[1] + str[z + 1:]
        else:
            a = ifValid(str[y+1:z])
            if a[1] == 0:
                print("Efter vänsterparentes måste en giltig operator komma.")
            elif a[1] == 1:
                print("Operatorn måste efterföljas av exakt två operander.")
            elif a[1] == 2:
                print("Operanderna måste skrivas som 'real', 'bool' eller 'int'.")
            elif a[1] == 3:
                print ("Operatorn", "'" + a[2] + "'", "måste ha operander av samma (numeriska) typ!")
            elif a[1] == 5:
                print("Operatorn", "'" + a[2] +"'",  "accepterar inte booleska operander!")
            elif a[1] == 6:
                print("Operatorn 'quotient' fungerar enbart med heltal som operander!")
            elif a[1] == 7:
                print("Storleksjämförelser kan ej göras med booleanska operander.")
            return
    if str in dataList:
        print(str)
    else:
        print("Mellan varje operator och operand måste ett mellanslag användas, glöm ej.")


# Check('(+ int (+ int int))')

# Check('(+ (* (+ int int) (* int int)) (* int (quotient int int)))')
# Check('(123)')
# Check('(+ int (+ int int)')
# Check('(< int (+ int int))')
# Check('(< int (+ inte int))')
# Check('(< int int)')
# Check('(* bool bool)')
# Check('(+ bool bool)')
# Check('(quotient int int)')
# Check('(* int (+ real int))')