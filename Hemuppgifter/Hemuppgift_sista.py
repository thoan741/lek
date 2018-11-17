# 28,29,30,32,33

import random

# Uppgift 28)

# 28a)

# Palindrom, skriv program som kollar om textsträng är äkta palindrom


def truePalindrom():
    string = input("Skriv in något: ")
    string = string.upper()
    if string == string[::-1]:
        print("Detta är ett äkta palindrom!")
    else:
        print("Detta är inte ett äkta palindrom!")

#28b)

def palindrom():
    string = input("skriv in något: ")
    string = string.replace(" ", "")
    string = string.upper()
    if string == string[::-1]:
        print("Detta är ett oäkta palindrom!")
    else:
        print("Detta är inte ett oäkta palindrom!")

# Uppgift 29 blackbox:

# a) en funktion som återsänder det största av sina tre argument.

"""
3 Tester när var och ett är större än de andra, test när alla är samma.
Testa negativa tal och flyttal, se om något konstigt inträffar då.
"""

# b) en funktion som returnerar kvadratroten ur sitt enda argument:

"""
Test med 0 som invärde, test med ett positivt tal, och test med negativt.
"""








# c) En funktion som återsänder den minsta gemensamma multipeln för sina två heltalsargument. (MGM)

"""
Två skilda primtal (t.ex 3 och 5). Borde här ge produkten av dessa primtal
Två tal som i sig är uppbyggt av minst ett primtal som är samma. (t.ex 6 och 4). 
Borde här ge produkten delat med största gemensamma delaren.
Två tal där ett av talen är 0 (kanske inte måste testas eftersom båda tal måste vara positiva enligt definitionen.
Samma som raden ovan för negativa tal.
Två tal där det ena är en multipel av det andra (t.ex 4 och 8). Borde då returnera det största av talen.
"""

# Uppgift 30

# Glassbox tester för:

# if a < b:
#     if c > d: x = 1
#     elif c == d: x = 2
#     else: x = 3
# elif a == b: x = 4
# elif c == d: x = 5
# else: x = 6

"""
I glassbox ska alla vägar genomlöpas:
T.ex:
a = 1, b = 2, c = 4, d = 3 
a = 1, b = 2, c = 3, d = 3
a = 1, b = 2, c = 3, d = 4
a = 1, b = 1, c = 2, d = 3
a = 2, b = 1, c = 3, d = 3
a = 2, b = 1, c = 2, d = 3

"""















# Uppgift 32)

def headsOrTails():
    coin_toss = 100000
    my_dict = {"Krona": 0, "Klave": 0}
    while coin_toss > 0:
        i = random.randint(0, 1)
        if i == 0:
            my_dict["Krona"] += 1
        else:
            my_dict["Klave"] += 1
        coin_toss -= 1
    for i in my_dict:
        print(i + ": \t", my_dict[i])
headsOrTails()

# Uppgift 33)


def lottery():
    lottery_no = list(range(1, 101))
    win_no = 1
    number_of_wins = 15
    while number_of_wins > 0:
        lottery_no = random.sample(lottery_no, number_of_wins)
        winning_ticket = lottery_no[0]
        lottery_no = lottery_no[1:]
        if win_no == 1:
            print("Lott nr", winning_ticket, "får högsta vinsten")
        elif win_no == 2:
            print("Lott nr", winning_ticket, "får näst högsta vinsten")
        else:
            print("Lott nr", winning_ticket, "får vinst nr", win_no)
        win_no += 1
        number_of_wins -= 1
    print("Slut på vinstlistan!")