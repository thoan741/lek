# Author: Thomas Andersson
# Date: 2018-11-09


operatorList = ["+", "-", "*", "/", "quotient", "<", ">", "=", "and", "or"]
"""
Här skapas en lista innehållandes alla giltiga operatorer.
"""
operandList = ["int", "real", "bool"]
"""
En lista innehållandes alla giltiga operander.
"""


def check(string):
    """
    Huvudprogrammet, det är denna som körs och den kommer att med hjälp av nedanstående funktioner, beräkna resultatet,
     en parentes i taget, där den börjar med den innersta.
    :param string: Den sträng som ska beräknas.
    :return: Returnerar värdetypen när alla operationer utförts, eller ett felmeddelande, om det finns fel i den
     inmatade strängen.
    """
    try:
        while len(string.split()) > 1:
            a = indexOfInner(string)
            if not a[1]:
                print("Parentesfel!")
                return
            elif a[1] == True:
                print("Glömde du bort parenteser?")
                return
            elif a[1] == "a":
                print("Efter att den yttersta parenteserna stängs får inga fler tecken förekomma.")
                return
            elif a[1] == "b":
                print("Glömde du skriva någonting innanför parenteserna?")
            elif not whichOperation(string[a[0]+1:a[1]])[0]:
                b = whichOperation(string[a[0]+1:a[1]])
                if b[1] == 1:
                    print("Det verkar som att någon av operanderna inte överensstämmer med de fördefinierade.")
                elif b[1] == 2:
                    print("Det verkar som att operatorn inte överensstämmer med de fördefinierade.")
                elif b[1] == 3:
                    print("Varje operation är binär, dvs inom varje parentes måste en "
                          "operator efterföljas av exakt två operander.")
                else:
                    if b[2] in operatorList[:4]:
                        print("Operatorn", "'" + b[2] + "'", "accepterar inte booleska operander!")
                    elif b[2] == operatorList[4]:
                        print("Operatorn", "'" + b[2] + "'", "accepterar inte operander av typ", "'" + b[1] + "'!")
                    elif b[2] in operatorList[5:8]:
                        print("Operatorn", "'" + b[2] + "'", "accepterar inte booleska operander!")
                    else:
                        print("Operatorn", "'" + b[2] + "'", "accepterar inte ett booliskt och ett nummeriskt värde!")
                return
            string = string[:a[0]] + whichOperation(string[a[0]+1:a[1]])[1] + string[a[1]+1:]
        if string in operandList:
            print(string)
        elif string in operatorList:
            print("En operator måste skrivas inom parentes med två efterföljande operander.")
        elif not string:
            print("Råkade du köra programmet med en tom sträng?")
        elif string == '()':
            print("Glömde du skriva någonting innanför parenteserna?")
        else:
            print("Hmm, nu blev det fel, det som skrevs in är inte ett godkänt syntax,"
                  " kanske så glömde du bara bort mellanslag?")
        return
    except AttributeError:
        print("Schemesyntaxen måste skrivas som en sträng")
        return


def indexOfInner(string):
    """
    Bestämmer indexen för den innersta parentesen.
    :param string: Läser in hela teckensträngen som matas in.
    :return: Denna funktion tar reda på vilken beräkning som ska ske först i strängen, och kommer att returnera
     startindex och slutindex för den innersta parentesen i strängen.
    """
    a = 0
    b = 0
    c = 0
    startIdx = 0
    slutIdx = 0
    for i in range(len(string)):
        if a < 0:
            return [False, False]
        elif a == 0 and slutIdx != 0:
            return [False, "a"]
        elif string[i] == "(":
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
        return [False, False]
    if slutIdx == 0:
        return [False, True]
    else:
        return [startIdx, slutIdx]


def whichOperation(string):
    """
    Denna funktion skapar en lista av teckensträngen som hämtas in. Den ser till att listans längd är korrekt eftersom
     att operatorerna endast hanterar två operander. Den avläser om den inlästa strängen är på rätt form och om den är
     det, bestämmer den vilken av operatorfunktionerna som ska köras. Annars skickas parametrar vidare,
     där huvudprogrammet bestämmer vilket felmeddelande som ska skrivas ut.
    :param string: Denna sträng kommer vid första körningen att vara den innersta parentesen i den sträng som matas in,
     som bestämts med hjälp av indexOfInner.
    :return: Denna returnerar svaret av en beräkning till huvudprogrammet.
    """
    string = string.split()
    if not len(string) == 3:
        return [False, 3]
    elif string[1] in operandList and string[2] in operandList:
        if string[0] in operatorList:
            if string[0] in operatorList[:3]:
                return mulSubAddRules(string)
            elif string[0] == operatorList[3]:
                return divRules(string)
            elif string[0] == operatorList[4]:
                return quotientRules(string)
            elif string[0] in operatorList[5:8]:
                return compareRules(string)
            elif string[0] in operatorList[8:]:
                return andOrRules(string)
        else:
            return [False, 2]
    else:
        return [False, 1]


def mulSubAddRules(string):
    """
    Utför en beräkning med 2 operander och en operator. Denna funktion kommer bara köras om strängen som hämtas in är
     på rätt form.
    :param string: Denna parameter kommer vara en lista där första elementet är en av operatorerna '+', '-' eller '*'.
     De andra två elementen i listan kommer att vara element som finns i operandList.
    :return: Returnerar värdetypen som fås när beräkning sker, om det är en giltig operation mellan dessa operandtyper.
     Om det ej är en giltig operation kommer en parameter skickas vidare där denna parameter bestämmer vilket
     felmeddelande som ska skrivas ut.
    """
    if string[1] == "int" and string[2] == "int":
        return [True, "int"]
    elif string[1] in operandList[:2] and string[2] in operandList[:2]:
        return [True, "real"]
    else:
        return [False, "bool", string[0]]



def divRules(string):
    """
    Utför en beräkning med 2 operander och en operator. Denna funktion kommer bara köras om strängen som hämtas in är
     på rätt form.
    :param string: Denna parameter kommer vara en lista där första elementet är operatorn '/'.
     De andra två elementen i listan kommer att vara med element som finns i operandList.
    :return: Returnerar värdetypen som fås när beräkning sker, om det är en giltig operation mellan dessa operandtyper.
     Om det ej är en giltig operation kommer en parameter skickas vidare där denna parameter bestämmer vilket
     felmeddelande som ska skrivas ut.
    """

    if string[1] in operandList[:2] and string[2] in operandList[:2]:
        return [True, "real"]
    else:
        return [False, "bool", string[0]]


def quotientRules(string):
    """
    Utför en beräkning med 2 operander och en operator. Denna funktion kommer bara köras om strängen som hämtas in är
     på rätt form.
    :param string: Denna parameter kommer vara en lista där första elementet är operatorn 'quotient'.
     De andra två elementen i listan kommer att vara med element som finns i operandList.
    :return: Returnerar värdetypen som fås när beräkning sker, om det är en giltig operation mellan dessa operandtyper.
     Om det ej är en giltig operation kommer en parameter skickas vidare där denna parameter bestämmer vilket
     felmeddelande som ska skrivas ut.
    """
    if string[1] == operandList[0] and string[2] == operandList[0]:
        return [True, "int"]
    else:
        if string[1] == operandList[0]:
            return [False, string[2], string[0]]
        else:
            return [False, string[1], string[0]]


def compareRules(string):
    """
    Utför en beräkning med 2 operander och en operator. Denna funktion kommer bara köras om strängen som hämtas in är
     på rätt form.
    :param string: Denna parameter kommer vara en lista där första elementet är en av operatorerna '<', '>' eller '='.
     De andra två elementen i listan kommer att vara med element som finns i operandList.
    :return: Returnerar värdetypen som fås när beräkning sker, om det är en giltig operation mellan dessa operandtyper.
     Om det ej är en giltig operation kommer en parameter skickas vidare där denna parameter bestämmer vilket
     felmeddelande som ska skrivas ut.
    """
    if string[1] in operandList[:2] and string[2] in operandList[:2]:
        return [True, "bool"]
    else:
        return [False, "bool", string[0]]


def andOrRules(string):
    """
    Utför en beräkning med 2 operander och en operator. Denna funktion kommer bara köras om strängen som hämtas in är
     på rätt form.
    :param string: Denna parameter kommer vara en lista där första elementet är en av operatorerna 'or' eller 'and'.
     De andra två elementen i listan kommer att vara med element som finns i operandList.
    :return: Returnerar värdetypen som fås när beräkning sker, om det är en giltig operation mellan dessa operandtyper.
     Om det ej är en giltig operation kommer en parameter skickas vidare där denna parameter bestämmer vilket
     felmeddelande som ska skrivas ut.
    """
    if string[1] in operandList[:2] and string[2] in operandList[:2]:
        return [True, string[2]]
    elif string[1] == string[2] == operandList[2]:
        return [True, "bool"]
    else:
        return [False, "bool", string[0]]