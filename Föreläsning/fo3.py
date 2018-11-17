#fo3

#plista= ['s','v','m','mp','fp','c','kd']
#try:
#    i=int(input("Ange index: "))
#    parti = plista[i]
#except:
#    print ("Något fel inträffade")

#plista= ['s','v','m','mp','fp','c','kd']
#try:
#    i= int(input('Ange index: '))
#    parti = plista[i]
#except IndexError as indx:
#    print ('ogilltigt index' ,indx)
#except ValueError:
#    print ('index maste var ett tal')
#except:
#    print('uppstod något okänd fel!')

#indata = input("mata in: ")
#if indata=="fem":
#    pass
#    print("hej")

#def calc(a,b):
#    return a*b+b

#r=calc(2,3)
#print(r)

def bmi(langd,vikt):
    return vikt / (langd*langd)

print(bmi(1.70,65))
print(bmi(vikt=65,langd=70))

x = 10
def change():
    global x
    x = x / 2

print(x)
change()
print(x)
