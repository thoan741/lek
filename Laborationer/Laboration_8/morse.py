# Author: Thomas Andersson
# Date: 2018-11-02
# Version 1.7
# En liten ändring som även hanterar felinläsning från hemsidor.

try:
    # myFile = open("morse.d", "r", encoding="utf-8")
    myFile = open("morse.d")
    improvedString = str(myFile.read())
    print(improvedString)
    improvedString = improvedString[:134] + 'Å' + \
                     improvedString[136:142] + 'Ä' + \
                     improvedString[144:149] + 'Ö' + \
                     improvedString[151:]
except FileNotFoundError:
    improvedString = "aa"
"""
Jag öppnar filen morse.d i läsbart läge. Sedan läses filen in och konverteras till en teckensträng.
Å, Ä och Ö läses inte in korrekt så de måste ändras innan jag fortsätter.
"""

import urllib.request

"""
urllib.request är ett bibliotek som låter mig bl.a. att läsa och spara text från hemsidor.
"""
"""
try:
    link = "http://www.nada.kth.se/kurser/su/DA2001/sudata18/laborationer/morse.d"
    f = urllib.request.urlopen(link)
    myFile = f.read()
    myString = str(myFile)[2:-1]
    improvedString = myString[:134] + 'Å' + \
                     myString[142:148] + 'Ä' + \
                     myString[156:161] + 'Ö' + \
                     myString[169:]
except urllib.error.HTTPError:
    improvedString = "aa"
"""
"""
Här snyggas textfilen som laddades ner till. Först konverteras den från bit till sträng.
Sedan tar jag bort onödiga tecken i början av strängen. Bokstäver Å,Ä,Ö sparas inte korrekt, så jag byter ut de tecknen,
samt tar bort en flärp i slutet.
"""


def makeDict(str):
    """
    makeDict skapar ett dictionary ur en teckensträng, där varje bokstav kommer att bli ett keyword
     och paras ihop med den morsesträng som tillhör ordet.
    Try-delen kommer testa om strängen som läses in är på rätt format, annars skicka vidare false.
    :param str: str är en teckensträng där en bokstav kommer först, sedan ett nummer n,
     och sedan en morsekod som är n tecken långt
    :return: Ett dictionary där varje keyword är en bokstav/nummer/symbol som är parat ihop med
     den teckensträng som är morsekoden för den bokstaven.
    """
    key = 0
    numberValue = 1
    aDict = {}
    try:
        while key < len(str):
            aDict[str[key]] = str[key+2:int(str[numberValue])+key+2]
            key = int(str[numberValue])+key+2
            numberValue = key+1
        try:
            str[key - 1]
        except IndexError:
            return False
        return aDict
    except ValueError:
        return False
    except IndexError:
        return False


symbolToMorseDict = makeDict(improvedString)
# Jag skapar ett dictionary med funktionen makeDict och teckensträngen som hämtades in, efter att den korrigerats.
# Denna kan användas för att konvertera symboler,bokstäver och nummer till morsekod.
if symbolToMorseDict:
    morseToSymbolDict = {v: k for k, v in symbolToMorseDict.items()}
# Här skapas ett nytt dictionary med hjälp av det som skapades över, där value och keyword har bytt plats överallt,
# för att då få ett nytt dictionary som konverterar morsetecken till bokstäver,symboler eller siffror.


def inputManagement():
    """
    Denna ser till att programavslut sker korrekt.
    """
    try:
        a = input("Mata in ett meddelande i klartext eller morsekod: ")
        return [a, True]
    except EOFError as e:
        return [e, False]
    except KeyboardInterrupt as e:
        return [e, False]


def convertSymbolsToMorse(msg, aDict):
    """
    Konverterar ett meddelande från bokstäver/siffror/symboler till morse.
    :param msg: Denna parameter innehåller en teckensträng.
    :param aDict: Ett dictionary med bokstäver som keyword och motsvarande morsetecken
     som värde i en teckensträng.
    :return: Returnerar den omvandlade teckensträngen om möjligt, annars returneras falskt samt vart problem uppstod.
    """
    b = ''
    for i in msg:
        if i.upper() in aDict:
            a = aDict[i.upper()]
            b = b + a + ' '
        elif i == ' ':
            b = b + ' '
        else:
            return [i, False]

    return [b, True]


def convertMorseToSymbols(msg, aDict):
    """
    Konverterar ett morsemeddelande till bokstäver.
    :param msg: msg kommer vara en teckensträng, som förväntas innehålla morsetecken.
    :param aDict: dictionary som konverterar morsekod till bokstäver.
    :return: returnerar ett morsemeddelande omvandlat till bokstäver om det går, annars returneras False och
     vart i textsträngen problemet uppstod..
    """
    msg = msg.split("  ")
    last = "."
    res = ""
    for x in msg:
        x = x.split()
        for i in x:
            if last in [".", "!", "?"]:
                if i in aDict:
                    res += aDict[i]
                    last = aDict[i]
                else:
                    return [i, False]
            else:
                if i in aDict:
                    res += aDict[i].lower()
                    last = aDict[i]
                else:
                    return [i, False]
        res = res + ' '
    return [res, True]


"""
Splitta på enkla mellanslag
"""