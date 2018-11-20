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
            float(self.var.get())
            return True
        except ValueError:
            print("Tal måste matas in!")
            return False

    def buttonPress(self, text):
        if text == "Push":
            if self.checkInput():
                S.push(float(self.var.get()))
            self.var.set("")

        elif text == "=":
            doCommands()
            if not S.empty():
                save = S.pop()
                self.ans.set(save)
                S.push(save)

        elif text == "=":
            print("Wow, likhet, kanske ska implementera detta")
            var1 = S.pop()
            var2 = S.pop()
            op = Q.dequeue()
            if op == "+":
                Var = var2 + var1
            S.push(Var)
            self.ans.set(str(Var))


        elif text in operator:
            if not Q.full():
                Q.enqueue(text)
            else:
                print("Kön är full!")

        elif text == "EXIT":
            quit("Programavslutning!")
        elif text == "Töm":
            print("Stacken är nu tömd!")
            clearStack()
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

    def entry(self, WIDTH, COLOUR, SIDE, ANCHOR, var, TEXTCOLOUR=None):
        if not TEXTCOLOUR == None:
            self.entryBox = Entry(self.row, textvariable=var, bg=COLOUR, fg=TEXTCOLOUR)
        else:
            self.entryBox = Entry(self.row, textvariable=var, bg=COLOUR)
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
        #self.root.overrideredirect(False)
        self.window.mainloop()


myCalc = tkCalc()
myCalc.windowTopLevel(400, 153)
myCalc.rowGeometry()
myCalc.label("Inmatning: ", LEFT, N)
myCalc.entry(40, "yellow", LEFT, N, myCalc.var)
myCalc.rowPack(TOP)
myCalc.rowGeometry()
myCalc.label("Svarsruta:   ", LEFT, N)
myCalc.entry(40, "darkBlue", LEFT, N, myCalc.ans, "white")
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
myCalc.buttons("=", lambda: myCalc.buttonPress("="), 10, 2, LEFT)
myCalc.buttons("Töm", lambda: myCalc.buttonPress("Töm"), 10, 2, LEFT)
myCalc.buttons("Help", lambda: myCalc.buttonPress("Help"), 10, 2, LEFT)
myCalc.buttons("EXIT", lambda: myCalc.buttonPress("EXIT"), 10, 2, LEFT, "red")
myCalc.rowPack()
myCalc.root.bind("<Return>", lambda x: myCalc.buttonPress("Push"))
myCalc.mainloop()