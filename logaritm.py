import math

candidate = 1 #kandidaten som testas
counter = 1 #antal primtal som hittats
logarithm = math.log(2) #värdet av primtalens logarithm

while counter < 10000: #stanna vid det angivna primtalet
    test = 3 #talet vi börjar dela kandidaten med
    candidate = candidate + 2 #testar bara udda nummer
    while candidate%test > 0: #hitta lägsta nummer som kandidaten är delbar med
        test = test + 2 #öka test med 2 om det ej returnerar ett heltal

    if test > math.sqrt(candidate): #om det lägsta tal kandidaten är delbar med är sig själv
            counter = counter + 1 #lägg då till det som primtal
            logarithm = logarithm + math.log(candidate) #lägger till logaritmen av kandidaten om den är ett primtal

print(" Primtalet är " + str(candidate)) #värdet av det n:te primtalet
print(" Logaritmen för dessa är " + str(logarithm)) #alla primtals logaritm fram till n:te primtalet adderade
print(" Förhållandet mellan dem är " + str(logarithm/candidate)) #förhållandet mellan dessa två

