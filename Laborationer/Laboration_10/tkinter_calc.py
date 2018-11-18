from tkinter import *
from calcCommand import *


class tkCalc():

    def __init__(self):
        self.root = Tk()
        self.var = StringVar()
        self.var.set("")
        self.ans = StringVar()
        self.ans.set("")

    def windowTopLevel(self,xSize, ySize):
        self.root.overrideredirect(1)
        self.root.geometry(str(xSize) + 'x' +str(ySize))
        self.title = Frame(self.root, bg='lightBlue', relief='raised', bd=2)
        self.close = Button(self.title, text='X', command=self.root.destroy)
        self.text = Label(self.title, text="En fin miniräknare", bg="lightblue")
        self.title.pack(expand=1, fill=X)
        self.close.pack(side=RIGHT)
        self.text.pack(side=LEFT)
        self.title.bind('<B1-Motion>', self.move_window)
        self.window = Frame(self.root)
        self.window.pack()

    def move_window(self, event):
        self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    def checkInput(self):
        try:
            Var = float(self.var.get())
            return True
        except ValueError:
            print("Tal måste matas in!")
            return False

    def buttonPress(self, text):
        if text == "Push":
            if self.checkInput():
                S.push(int(self.var.get()))
            self.var.set("")

        elif text == "+":
            print("Wow, plus, kanske ska implementera detta")
            Q.enqueue(text)
        elif text == "-":
            print("Wow, minus, kanske ska implementera detta")
        elif text == "*":
            print("Wow, gånger, kanske ska implementera detta")
        elif text == "/":
            print("Wow, division, kanske ska implementera detta")
        elif text == "^":
            print("Wow, upphöjt till, kanske ska implementera detta")
        elif text == "=":
            print("Wow, likhet, kanske ska implementera detta")
            var1 = S.pop()
            var2 = S.pop()
            op = Q.dequeue()
            if op == "+":
                Var = var2 + var1
            S.push(Var)
            self.ans.set(str(Var))

        elif text == "EXIT":
            quit("Då packar vi ihop för denna gången, ha det bra!")
        elif text == "Help":
            print("""Skriv in tal i inmatningsfältet. 
                    Knappen push pushar då talet till stacken.
                    Operatorerna pushas till kön, likhetstecken tar ut två operander ur stacken och en
                    operator ur kön och applicerar operatorn mellan dessa för att sedan pusha svaret tillbaka till stacken.
                    Exit knappen avslutar programmet.""")

    def buttons(self, TEXT, COMMAND, WIDTH, HEIGHT, SIDE, COLOUR=None):
        if COLOUR == None:
            self.button = Button(self.row, text=TEXT, command=COMMAND)
        else:
            self.button = Button(self.row, text=TEXT, command=COMMAND, fg=COLOUR)

        self.button.config(width=WIDTH,height=HEIGHT)
        self.button.pack(side=SIDE)

    def label(self, TEXT, SIDE, ANCHOR):
        self.name = Label(self.row, text=TEXT)
        self.name.pack(side=SIDE, anchor=ANCHOR)

    def entryIn(self, WIDTH, COLOUR, SIDE, ANCHOR):
        self.entryBox = Entry(self.row, textvariable=self.var, bg=COLOUR)
        self.entryBox.config(width=WIDTH)
        self.entryBox.pack(side=SIDE, anchor=ANCHOR)

    def entryOut(self, WIDTH, COLOUR, SIDE, ANCHOR):
        self.entryBox = Entry(self.row, textvariable=self.ans, bg=COLOUR)
        self.entryBox.config(width=WIDTH)
        self.entryBox.pack(side=SIDE, anchor=ANCHOR)

    def rowGeometry(self):
        self.row = Frame(self.window)

    def rowPack(self, SIDE=None):
        if not SIDE == None:
            self.row.pack(side=SIDE)
        else:
            self.row.pack()

    def mainloop(self):
        self.root.overrideredirect(False)
        self.window.mainloop()


myCalc = tkCalc()
myCalc.windowTopLevel(400, 160)
myCalc.rowGeometry()
myCalc.label("Inmatning: ", LEFT, N)
myCalc.entryIn(40, "yellow", LEFT, N)
myCalc.rowPack(TOP)
myCalc.rowGeometry()
myCalc.label("SvarsRuta:  ", LEFT, N)
myCalc.entryOut(40, "yellow", LEFT, N)
myCalc.rowPack()
myCalc.rowGeometry()
myCalc.buttons("+", lambda: myCalc.buttonPress("+"), 10, 2, LEFT)
myCalc.buttons("-", lambda: myCalc.buttonPress("-"), 10, 2, LEFT)
myCalc.buttons("*", lambda: myCalc.buttonPress("*"), 10, 2, LEFT)
myCalc.buttons("/", lambda: myCalc.buttonPress("/"), 10, 2, LEFT)
myCalc.buttons("^", lambda: myCalc.buttonPress("^"), 10, 2, LEFT)
myCalc.rowPack()
myCalc.rowGeometry()
myCalc.buttons("Push", lambda: myCalc.buttonPress("Push"), 10, 2, LEFT)
myCalc.buttons("=", lambda: myCalc.buttonPress("="), 22, 2, LEFT)
myCalc.buttons("Help", lambda: myCalc.buttonPress("Help"), 10, 2, LEFT)
myCalc.buttons("EXIT", lambda: myCalc.buttonPress("EXIT"), 10, 2, LEFT, "red")
myCalc.rowPack()
myCalc.root.bind("<Return>", lambda x: myCalc.buttonPress("Push"))
myCalc.mainloop()