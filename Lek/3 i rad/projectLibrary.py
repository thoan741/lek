spelPlan = [".",".",".",".",".",".",".",".","."]

def rad1(plan):
    x = plan[0:3]
    return x

def rad2(plan):
    x = plan[3:6]
    return x

def rad3(plan):
    x =plan[6:9]
    return x

def updatePlan(el, rad, pos):
    rad[pos] = el
    return rad

def printPlan(plan):
    print(rad1(plan))
    print(rad2(plan))
    print(rad3(plan))


def spotTaken(plan,pos):
    if plan[pos] == ".":
        return 1
    else:
        return 0

def winningXRow(plan, rad):
    c = 0
    for a in range(0,3):
        if "X" == rad(plan)[a]:
            c = c + 1
        else:
            c = c
    if c == 3:
        return 1
    else:
        return 0

def winningORow(plan, rad):
    c = 0
    for a in range(0,3):
        if "O" == rad(plan)[a]:
            c = c + 1
        else:
            c = c
    if c == 3:
        return 1
    else:
        return 0

def winningXDiagonal(plan):
    if plan[0] == "O" and plan[4] == "O" and plan[8] == "X":
        return 1
    elif plan[2] == "O" and plan[4] == "O" and plan[6] == "X":
        return 1
    else:
        return 0


def winningODiagonal(plan):
    if plan[0] == "O" and plan[4] == "O" and plan[8] == "O":
        return 1
    elif plan[2] == "O" and plan[4] == "O" and plan[6] == "O":
        return 1
    else:
        return 0




def winXCol(plan):
    c = 0
    for x in range(0,3):
        if "X" == rad1(plan)[x] and "X" == rad2(plan)[x] and "X" == rad3(plan)[x]:
            c = c + 1
        else:
            c = c
    if c == 1:
        return 1
    else:
        return 0


def winOCol(plan):
    c = 0
    for x in range(0, 3):
        if "O" == rad1(plan)[x] and "O" == rad2(plan)[x] and "O" == rad3(plan)[x]:
            c = c + 1
        else:
            c = c
    if c == 1:
        return 1
    else:
        return 0

def winningXMove(plan):

    if winningXRow(plan, rad1) == 1 or winningXRow(plan, rad2) == 1 or winningXRow(plan, rad3) == 1 or winningXDiagonal(plan) == 1:
        return 1
    elif winXCol(plan) == 1:
        return 1
    else:
        return 0


def winningOMove(plan):
    if winningORow(plan, rad1) == 1 or winningORow(plan, rad2) == 1 or winningORow(plan, rad3) == 1 or winningODiagonal(plan) == 1:
        return 1
    elif winOCol(plan) == 1:
        return 1
    else:
        return 0