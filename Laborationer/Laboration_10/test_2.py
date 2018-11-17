from tkinter import *

def move_window(event):
    master.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

master = Tk()
master.overrideredirect(1)
master.geometry('400x133')
title_bar = Frame(master, bg='lightblue', relief='raised', bd=2)
close_button = Button(title_bar, text='X', command=master.destroy)
text = Label(title_bar, text="En fin miniräknare", bg="lightblue")
title_bar.pack(expand=1, fill=X)
close_button.pack(side=RIGHT)
text.pack(side=LEFT)
title_bar.bind('<B1-Motion>', move_window)
f = Frame(master)
f.pack()

def funk():
    try:
        variable = int(var.get())
        print(variable)
    except ValueError:
        print("ej heltal")
    var.set("")


def add():
    print("Wow, plus, kanske ska implementera detta")


def sub():
    print("Wow, minus, kanske ska implementera detta")


def mul():
    print("Wow, gånger, kanske ska implementera detta")


def div():
    print("Wow, division, kanske ska implementera detta")


def eq():
    print("Wow, likhet, kanske ska implementera detta")
    var.set("")

def power():
    print("Wow, upphöjt till, kanske ska implementera detta")

def exit():
    quit("Då packar vi ihop för denna gången, ha det bra!")

var = StringVar()
var.set("")
ft = Frame(f)
e = Entry(ft, textvariable=var, bg="yellow")
e.config(width=40)
a = Label(ft, text="Ange ett tal: ")
a.pack(side=LEFT,anchor=N)
e.pack(side=LEFT,anchor=N)
ft.pack(side=TOP)
fm =Frame(f)
b1 = Button(fm, text="+", command=add)
b1.config(width=10, height=2)
b1.pack(side=LEFT)
b2 = Button(fm, text="-", command=sub)
b2.config(width=10, height=2)
b2.pack(side=LEFT)
b3 = Button(fm, text="*", command=mul)
b3.config(width=10, height=2)
b3.pack(side=LEFT)
b4 = Button(fm, text="/", command=div)
b4.config(width=10, height=2)
b4.pack(side=LEFT)
b6 = Button(fm, text="^", command=power)
b6.config(width=10, height=2)
b6.pack(side=LEFT)
fm.pack()
fl = Frame(f)
b = Button(fl, text="Push", command=funk)
b.config(width=10, height=2)
b.pack(side=LEFT)
b5 = Button(fl, text="=", command=eq)
b5.config(width=33, height=2)
b5.pack(side=LEFT)
b7 = Button(fl, text="EXIT", fg="red", command=exit)
b7.config(width=10, height=2)
b7.pack(side=LEFT)
fl.pack(side=LEFT)
master.overrideredirect(False)

f.mainloop()