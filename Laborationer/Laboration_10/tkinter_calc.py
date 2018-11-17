from tkinter import *
import calcQueue
import calcStack

class tkCalc():

    def __init__(self):
        self.root = Tk()
        self.var = StringVar()
        self.var.set("")

    def windowTopLevel(self,xSize, ySize):
        self.root.overrideredirect(1)
        self.root.geometry(str(xSize) +'x' +str(ySize))
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

    def calcInput(self):
        try:
            variable = int(self.var.get())
            print(variable)
        except ValueError:
            print("ej heltal")
        self.var.set("")

    def push(self):
        try:
            variable = int(self.var.get())
            print(variable)
        except ValueError:
            print("ej heltal")
        self.var.set("")

    def add(self):
        print("Wow, plus, kanske ska implementera detta")

    def sub(self):
        print("Wow, minus, kanske ska implementera detta")

    def mul(self):
        print("Wow, gånger, kanske ska implementera detta")

    def div(self):
        print("Wow, division, kanske ska implementera detta")

    def eq(self):
        print("Wow, likhet, kanske ska implementera detta")

    def pwr(self):
        print("Wow, upphöjt till, kanske ska implementera detta")

    def exit(self):
        quit("Då packar vi ihop för denna gången, ha det bra!")

    def printHelp(self):
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
        self.label = Label(self.row, text=TEXT)
        self.label.pack(side=SIDE, anchor=ANCHOR)

    def entry(self, WIDTH, COLOUR, SIDE, ANCHOR):
        self.entry = Entry(self.row, textvariable=self.var, bg=COLOUR)
        self.entry.config(width=WIDTH)
        self.entry.pack(side=SIDE, anchor=ANCHOR)

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
myCalc.windowTopLevel(400, 133)
myCalc.rowGeometry()
myCalc.label("Inmatningsruta: ", LEFT, N)
myCalc.entry(40, "yellow", LEFT, N)
myCalc.rowPack(TOP)
myCalc.rowGeometry()
myCalc.buttons("+", myCalc.add, 10, 2, LEFT)
myCalc.buttons("-", myCalc.sub, 10, 2, LEFT)
myCalc.buttons("*", myCalc.mul, 10, 2, LEFT)
myCalc.buttons("/", myCalc.div, 10, 2, LEFT)
myCalc.buttons("^", myCalc.pwr, 10, 2, LEFT)
myCalc.rowPack()
myCalc.rowGeometry()
myCalc.buttons("Push", myCalc.push, 10, 2, LEFT)
myCalc.buttons("=", myCalc.eq, 22, 2, LEFT)
myCalc.buttons("Help", myCalc.printHelp, 10, 2, LEFT)
myCalc.buttons("EXIT", myCalc.exit, 10, 2, LEFT, "red")
myCalc.rowPack()
myCalc.mainloop()