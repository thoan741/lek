# Lektionshandledning:

# Mail: clindeb@kth.se

class Nod:

    def __init__(self, t):
        self.tal = t
        self.v = None
        self.h = None


class BinTree:

    def __init__(self):
        self.rot = None

    def insert(self, t):
        innan_hr = self.rot
        hr = self.rot
        n = Nod(t)
        if self.rot == None:
            self.rot = n
        else:
            if t > self.rot.tal:
                self.rot.h = self.rec_insert(self.rot.h, t)
            else:
                self.rot.v = self.rec_insert(self.rot.v, t)

    def rec_insert(self, rot, t):
        if rot == None:
            return Nod(t)
        elif rot.tal > t:
            rot.v = self.rec_insert(rot.v, t)
        else:
            rot.h = self.rec_insert(rot.h, t)
        return rot

    def rec_show(self, rot):
        if rot == None:
            return
        else:
            print(rot.tal)
            self.rec_show(rot.v)
            self.rec_show(rot.h)

    def show(self):
        self.rec_show(self.rot)