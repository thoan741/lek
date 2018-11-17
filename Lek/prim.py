candidate = 1 #kandidaten som testas
counter = 1 #antal primtal som hittats
number = int(input('hitta primtal nummer:'))


while counter < number: #stanna vid 1000:e primtalet
    test = 3 #talet vi delar kandidaten med
    candidate = candidate + 2 #testar bara udda nummer
    while candidate%test > 0: #hitta lägsta nummer som kandidaten är delbar med
        test = test + 2 #öka test med 1 om det ej returnerar ett heltal

    if candidate == test: #om det lägsta tal kandidaten är delbar med är sig själv
            counter = counter + 1 #lägg då till det som primtal

print(candidate) #utskrift när 1000:e primtalet hittas.