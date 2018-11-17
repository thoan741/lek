from projectLibrary import *

printPlan(spelPlan)


def runFile(a):

    if a == 0:
        rad = int(input("I vilken rad vill du stoppa in ditt X? (1-3):"))
        tal = int(input("I vilken kolumn? (1-3):"))
        pos = (rad - 1) * 3 + tal - 1
        if 1 == spotTaken(spelPlan, pos):
            updatePlan("X", spelPlan, pos)
            printPlan(spelPlan)
            if winningXMove(spelPlan) == 1:
                print("Grattis X, du vann!")
            else:
                runFile(1)
        else:
            print("Denna plats var ju redan upptagen, försök igen!")
            runFile(0)
    else:
        rad = int(input("I vilken rad vill du stoppa in ditt O? (1-3):"))
        tal = int(input("I vilken kolumn? (1-3):"))
        pos = (rad - 1) * 3 + tal - 1
        if 1 == spotTaken(spelPlan, pos):
            updatePlan("O", spelPlan, pos)
            printPlan(spelPlan)
            if winningXMove(spelPlan) == 1:
                print("Grattis O, du vann!")
            else:
                runFile(0)
        else:
            print("Denna plats var ju redan upptagen, försök igen!")
            runFile(1)


runFile(0)
