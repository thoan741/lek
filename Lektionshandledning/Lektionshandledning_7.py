# Lektionshandledning 7, uppgift 31,34

import random

# Uppgift 31
def guessNumber():
    goal = random.randint(1, 99)
    burn_limit = 7
    num_guesses = 0
    max_guesses = 20
    extra_credit_limit = 5
    correct_guess_made = False
    while num_guesses < max_guesses and correct_guess_made == False:
        guess = int(input("Gissa ett tal mellan 1 och 99: "))
        num_guesses += 1
        if abs(guess-goal) < burn_limit and guess != goal:
            print("Det bränns!")
        if guess < goal:
            print("Du måste gissa högre!")
        elif guess > goal:
            print("Du måste gissa lägre!")
        else:
            correct_guess_made = True
            print("Du gissade rätt efter", num_guesses, "gissningar, grattis!")
            if num_guesses < extra_credit_limit:
                print("Och du gjorde det på färre än ", extra_credit_limit, "gissningar! Wow!")
    if correct_guess_made == False:
        print("Ajdå! Du har bara", max_guesses, "på dig...")


# Uppgift 34 på två sätt!
def stonePaperScissors():
    print("Välkommen")

    player_wins, cpu_wins, even_rounds = 0, 0, 0
    round_limit = 10
    rounds_played = 0
    while rounds_played < round_limit:
        player_move = input("sten,sax eller påse: ")
        cpu_move = random.choice(["sten", "sax", "påse"])
        if player_move == cpu_move:
            print("oavgjort")
            even_rounds += 1
        elif player_move == "sten":
            if cpu_move == "sax":
                print("Du valde sten och jag valde sax, du vinner!")
                player_wins += 1
            else:
                print("Du valde sten och jag valde påse, jag vinner!")
                cpu_wins += 1
        elif player_move == "sax":
            if cpu_move == "påse":
                print("Du valde sax och jag valde påse, du vinner!")
                player_wins += 1
            else:
                print("Du valde sax och jag valde sten, jag vinner!")
                cpu_wins += 1
        elif player_move == "påse":
            if cpu_move == "sten":
                print("Du valde påse och jag valde sten, du vinner!")
                player_wins += 1
            else:
                print("Du valde påse och jag valde sax, jag vinner!")
                cpu_wins += 1
        rounds_played += 1


# Enklare sätt:

def stenSaxPåse():
    win_list = [0,0,0]
    tie_msg = "Oavgjort!"
    lose_msg = "Du förlorade!"
    win_msg = "Du vann!"
    result_table = {"sten":{"sten":[tie_msg,[0,0,1]],
                            "påse": [lose_msg,[0,1,0]],
                            "sax": [win_msg,[1,0,0]]},
                    "påse":{"påse":[tie_msg,[0,0,1]],
                            "sax": [lose_msg,[0,1,0]],
                            "sten": [win_msg,[1,0,0]]},
                    "sax": {"sax":[tie_msg,[0,0,1]],
                            "sten": [lose_msg,[0,1,0]],
                            "påse": [win_msg,[1,0,0]]}}
    for i in range(10):
        player_move = input("sten,sax eller påse? ")
        cpu_move = random.choice(["sten","sax","påse"])
        result = result_table[player_move][cpu_move]
        print("Du valde", player_move, "och jag valde", cpu_move, ":", result[0])
        win_list = list(map(lambda x,y: x+y, win_list, result[1]))
    print("ställningen:")
    print("Du \t:", win_list[0], "gånger")
    print("Jag \t:", win_list[1], "gånger")
    print("Oavgjort:", win_list[2], "gånger")


# stenSaxPåse()

"""
Tester:
unittest
blackbox
glassbox
doctest
"""


def isEven(n):
    """
    >>> isEven(4)
    True
    >>> isEven(-4)
    True
    >>> isEven(7)
    False
    >>> isEven(0)
    True

    """
    if n > 0 and n%2 ==0:
        return True
    elif n < 0 and n%2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Python isEven.py -v
"""
Blackbox:
Programmet är en svart låda. Indata och utdata.


Glassbox:
Testar alla möjliga vägar genom programmet.
"""