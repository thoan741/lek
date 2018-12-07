from tkinter import *
from calcCommand import *


class tkCalc():
    """
    Jag skapar en klass för att göra kalkylatorns gränssnitt.
    """

    def __init__(self):
        """
        När en instans av klassen tkCalc skapas, är detta konstruktorn som initierar skapandet.
        """
        self.root = Tk()
        self.var = StringVar()
        self.var.set("")
        self.ans = StringVar()
        self.ans.set("")


    def windowTopLevel(self,xSize, ySize):
        """
        När denna funktion kallas i en instans av klassen, skapas "Top-level" menyn för kalkyatorn.
        :param xSize: Bestämmer kalkylatorns storlek i x-led
        :param ySize: Bestämmer kalkylatorns storlek i y-led
        :return:
        """
        self.root.overrideredirect(True)
        self.root.geometry(str(xSize) + 'x' +str(ySize))
        self.title = Frame(self.root, bg='lightBlue', relief='raised', bd=2)
        self.close = Button(self.title, text='X', command=self.root.destroy)
        self.withdraw_mode = Button(self.title, text='_', command=self.make_small)
        self.text = Label(self.title, text="En fin miniräknare", bg="lightblue")
        self.title.pack(expand=1, fill=X)
        self.close.pack(side=RIGHT)
        self.withdraw_mode.pack(side=RIGHT)
        self.text.pack(side=LEFT)
        self.title.bind('<B1-Motion>', self.move_window)
        self.window = Frame(self.root)
        self.window.pack()

    def make_small(self):
        """
        används för att minimera fönstret.
        """
        self.root.overrideredirect(False)
        self.root.iconify()

    def move_window(self, event):
        """
        Gör så att fönstret kan flyttas.
        """
        self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    def checkInput(self):
        """
        Kollar om det som matas in i inmatningsrutan är ett tal.
        """
        try:
            float(self.var.get())
            return True
        except ValueError:
            print(self.var.get() + " är inte ett tal!")
            return False

    def buttonPress(self, text):
        """
        Beroende på vilken knapp på kalylatorn som trycks ned, bestämmer denna funktion vad som ska göras.
        """
        if text == "Push":
            if self.checkInput():
                if not S.full():
                    S.push(float(self.var.get()))
                else:
                    print("Stacken är full!")
            self.var.set("")

        elif text == "=":
            if Q.empty():
                self.ans.set("")
            else:
                doCommands()
                if not S.empty():
                    save = S.pop()
                    self.ans.set(save)
                    S.push(save)


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
            self.ans.set("")
        elif text == "Help":
            print("""Skriv in tal i inmatningsfältet. \n Knappen push pushar då talet till stacken. \nOperatorerna pushas till kön, likhetstecken tar ut två operander ur stacken och en \n operator ur kön och applicerar operatorn mellan dessa för att sedan pusha svaret tillbaka till stacken. \n Exit knappen avslutar programmet.""")

    def buttons(self, TEXT, COMMAND, WIDTH, HEIGHT, SIDE, COLOUR=None):
        """
        Skapar en ny knapp på kalkylatorn.
        """
        if COLOUR == None:
            self.button = Button(self.row, text=TEXT, command=COMMAND)
        else:
            self.button = Button(self.row, text=TEXT, command=COMMAND, fg=COLOUR)

        self.button.config(width=WIDTH,height=HEIGHT)
        self.button.pack(side=SIDE)

    def label(self, TEXT, SIDE, ANCHOR):
        """
        skapar en textsträng på kalkylatorn
        """
        self.name = Label(self.row, text=TEXT)
        self.name.pack(side=SIDE, anchor=ANCHOR)

    def entry(self, WIDTH, COLOUR, SIDE, ANCHOR, var, TEXTCOLOUR=None):
        """
        skapar en inmatningsruta på kalkylatorn
        """
        if not TEXTCOLOUR == None:
            self.entryBox = Entry(self.row, textvariable=var, bg=COLOUR, fg=TEXTCOLOUR)
        else:
            self.entryBox = Entry(self.row, textvariable=var, bg=COLOUR)
        self.entryBox.config(width=WIDTH)
        self.entryBox.pack(side=SIDE, anchor=ANCHOR)

    def newRow(self):
        """
        öppnar en ny rad på kalkylatorn där knappar, inmatningsfält eller textsträngar kan packas in i.
        """
        self.row = Frame(self.window)

    def rowPack(self, SIDE=None):
        """
        Packar ihop raden som öppnades i funktionen ovan, när ett godtyckligt antal knappar och dylikt packats in.
        """
        if not SIDE == None:
            self.row.pack(side=SIDE)
        else:
            self.row.pack()

    def Mainloop(self):
        self.root.overrideredirect(False)
        self.window.mainloop()


myCalc = tkCalc()
myCalc.windowTopLevel(400, 183)
myCalc.newRow()
myCalc.label("Inmatning: ", LEFT, N)
myCalc.entry(40, "yellow", LEFT, N, myCalc.var)
myCalc.rowPack(TOP)
myCalc.newRow()
myCalc.label("Svarsruta:   ", LEFT, N)
myCalc.entry(40, "darkBlue", LEFT, N, myCalc.ans, "white")
myCalc.rowPack()
myCalc.newRow()
myCalc.buttons("+", lambda: myCalc.buttonPress("+"), 10, 2, LEFT)
myCalc.buttons("-", lambda: myCalc.buttonPress("-"), 10, 2, LEFT)
myCalc.buttons("*", lambda: myCalc.buttonPress("*"), 10, 2, LEFT)
myCalc.buttons("/", lambda: myCalc.buttonPress("/"), 10, 2, LEFT)
myCalc.buttons("^", lambda: myCalc.buttonPress("^"), 10, 2, LEFT)
myCalc.rowPack()
myCalc.newRow()
myCalc.buttons("Push", lambda: myCalc.buttonPress("Push"), 10, 2, LEFT)
myCalc.buttons("=", lambda: myCalc.buttonPress("="), 10, 2, LEFT)
myCalc.buttons("Töm", lambda: myCalc.buttonPress("Töm"), 10, 2, LEFT)
myCalc.buttons("Help", lambda: myCalc.buttonPress("Help"), 10, 2, LEFT)
myCalc.buttons("EXIT", lambda: myCalc.buttonPress("EXIT"), 10, 2, LEFT, "red")
myCalc.rowPack()
myCalc.newRow()
myCalc.buttons("0", lambda: myCalc.var.set(myCalc.var.get() + "0"), 4, 2, LEFT)
myCalc.buttons("1", lambda: myCalc.var.set(myCalc.var.get() + "1"), 4, 2, LEFT)
myCalc.buttons("2", lambda: myCalc.var.set(myCalc.var.get() + "2"), 4, 2, LEFT)
myCalc.buttons("3", lambda: myCalc.var.set(myCalc.var.get() + "3"), 4, 2, LEFT)
myCalc.buttons("4", lambda: myCalc.var.set(myCalc.var.get() + "4"), 4, 2, LEFT)
myCalc.buttons("5", lambda: myCalc.var.set(myCalc.var.get() + "5"), 4, 2, LEFT)
myCalc.buttons("6", lambda: myCalc.var.set(myCalc.var.get() + "6"), 4, 2, LEFT)
myCalc.buttons("7", lambda: myCalc.var.set(myCalc.var.get() + "7"), 4, 2, LEFT)
myCalc.buttons("8", lambda: myCalc.var.set(myCalc.var.get() + "8"), 4, 2, LEFT)
myCalc.buttons("9", lambda: myCalc.var.set(myCalc.var.get() + "9"), 4, 2, LEFT)
myCalc.buttons(".", lambda: myCalc.var.set(myCalc.var.get() + "."), 4, 2, LEFT)
myCalc.rowPack()
myCalc.root.bind("<Return>", lambda x: myCalc.buttonPress("Push"))
myCalc.Mainloop()


