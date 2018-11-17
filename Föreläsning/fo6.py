class Nod:
    def __init__(self,e):
        self.value = e
        self.next = None

class myQueue:

    def __init__(self):
        self.b = None
        self.s = None

    def full(self):
        return False

    def empty(self):
        return self.b == None

    def enqueue(self, e):
        n = Nod(e)
        if self.empty():
            self.b = n
            self.s = n
        else:
            self.s.next = n
            self.s = n


    def dequeue(self):
        if not self.empty():
            ret = self.b.value
            self.b = self.b.next
            return ret
        else:
            return None


    def show(self):
        h = self.b
        while h != None:
            print(h.value)
            h = h.next


kon = myQueue()

while True:
    indata = input("Ange ett kommando: ")

    if indata == "visa":
        kon.show()
    elif indata == "tom?":
        if kon.empty():
            print("Kön är tom!")
        else:
            print("Kön är inte tom!")
    elif indata == "lägg till":
        sak = input("vad?")
        status = kon.enqueue(sak)
        if status:
            print("Det gick bra!")
        else:
            print("Kön är nog full")
    elif indata == "nästa i kön":
        print(kon.dequeue())
    else:
        print("fel kommando, försök igen!")


