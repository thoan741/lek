d = 0        #värdet som efterfrågas
n = 1        #värdet som testas
counter = 0  #räknare
s = 0        #variabel som enbart används för att kolla om det finns någon lösning
a = 0
b = 0
c = 0

while counter < 6:                            #kör tills dess att vi hittar 6 tal på följd kan lösas
    s = 0                                     #nollställer värdet på s
    for a in range(0,n):                      #försöker hitta en lösning
        for b in range(0,n):                  #samma som ovan
            for c in range(0,n):              #samma som ovan
                if 6*a + 9*b + 20*c == n:     #ser om det finns en lösning
                    s = 1                     #ändrar värde på s om lösning finns
    if s == 1:                                #kollar om värdet på ändrats
        counter = counter + 1                 #räknar upp om lösning finns
        print("delbar")                       
    else:                                     #om lösning ej finns gör detta
        counter = 0                           #nollställer räknaren
        d = n                                 #sparar senaste värde på n som ej hade lösning
        print("icke delbar")
    n = n+1                                   #räknar upp n

print(d)     #största möjliga värde som ej kan uppnås