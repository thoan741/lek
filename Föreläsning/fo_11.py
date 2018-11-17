# fo 11

def unSortedSearch(key,L):
    # i = 0
    # for k in L:
    #     if k == key:
    #         return i
    #     i += 1

    for i,k in enumerate(L):
        if k == key:
            return i
    return None

    # return L.index(key)


class Nod:

    def __init__(self,t):
        self.tal=t
        self.v = None
        self.h = None


class BinTree:

    def __init__(self,r=None):
        self.rot=r

    def insert(self,t):
        hr = self.rot
        n = Nod(t)
        if self.rot==None:
            self.rot = n
        else:
            if t > self.rot.tal:
                self.rec_insert(self.rot.h, t)
            else:
                self.rec_insert(self.rot.v, t)

    def rec_insert(self, rot, t):
        if rot==None:
            return Nod(t)
        elif rot.tal>t:
            self.rec_insert(rot.h, t)
        else:
            self.rec_insert(rot.v, t)

