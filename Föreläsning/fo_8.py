#sökning i oordnad lista:

def search(lista, nyckel):
    location = None
    idx = 0
    last = len(lista)
    while idx < last and location == None:
        if lista[idx] == nyckel:
            location = idx
        else:
            idx += 1
    return location

# alt

def search2(lista, nyckel):
    location = None
    idx = 0
    last = len(lista)
    lista.append(nyckel)
    while location == None:
        if lista[idx] == nyckel:
            location = idx
        else:
            idx += 1
    if location < last:
        return location
    else:
        return None
