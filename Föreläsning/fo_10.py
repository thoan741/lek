# Föreläsning 10, grafik.

# import re

# encoding i open, kolla vad den gör, utf8 är bäst

# http://effbot.org/tkinterbook/

# Tkinter är ett paket för grafikgränssnitt.

# Tk är en huvudklass, måste skapa en instans innan kan köras.
# mainloop kommer köras tills den stängs, senare kod exekveras inte innan den stängs av.

# Button(p, text ="click here!") måste ha som första invariabel en första parameter som måste vara en instans
# av klassen Tk. textbiten ger en textsträng som kan klickas på. command= funktion kan läggas till som en tredje
# parameter och då körs en funktion när knappen klickas på.

from tkinter import *

# t = Tk()
# t.mainloop()

# def enfunktion(knapp):
#     print("knapp", knapp, " fungerar!")

# p = Tk()
# b = Button(p, text= "click here please", command= lambda: enfunktion("1"))
# b.pack()
# b2 = Button(p, text= "click here please", command= lambda: enfunktion("2"))
# b2.pack()
# p.mainloop()

# Canvas:
#  kan användas för att t.ex rita ut linjer på skärmen.

# t=Tk()
# canvas=Canvas(t)
# canvas.create_line(10, 40, 100, 100)
# canvas.pack()
# t.mainloop()

# CheckButton(master, text=, variabel=, onvalue=, offvalue= ):
# master är en instans av klass Tk, text är textsträng, var är variabeln, onvalue är det som körs när ibockad,
# offvalue när icke ibockad. variabeln kan vara StringVar, Var, osv. var.set kan användas efter att var definierats,
# och bestämma om ibockad eller icke ibockad ska köras först.

# master=Tk()
# def check():
#   print(var.get())
# var = StringVar()
# c = Checkbutton(master, text="Color image", variable=var,onvalue="RGB", offvalue="L",command=check )
# c.pack()
# master.mainloop()

# master=Tk()
# def check():
#     print (v.get())
# v = IntVar()
# v2 = IntVar()
# r=Radiobutton(master, text="Long", variable=v, value=1, command=check)
# r2=Radiobutton(master, text="Small", variable=v, value=2, command=check)
# r3=Radiobutton(master, text="Fat", variable=v2, value=1, command=check)
# r4=Radiobutton(master, text="Skinny", variable=v2, value=2, command=check)
# r.pack(anchor=W)
# r3.pack(anchor=E)
# r2.pack(anchor=W)
# r4.pack(anchor=E)
# master.mainloop()

# master=Tk()
# def funk(e):
#     print(var.get(), e.x)
# var = StringVar()
# var.set("JAHA")
# e=Entry(master,textvariable=var)
# e.bind("<Return>", funk)
# e.insert(2,"hej")
# e.pack()
# print (e.get())
# master.mainloop()

# master=Tk()
# t=Text(master)
# t.insert(END,"HELLO")
# t.pack()
# mainloop()


# p = Tk()
# def funk(e):
#     print(e.x, e.y)
#     print(lb.curselection())
# lb=Listbox(p)
# lb.insert(0,"hej")
# lb.insert(END,"hej2")
# lb.insert(0,"hej3")
# lb.pack()
# lb.bind("<Button-1>", funk)
# lb.bind("<Down>", funk)
# lb.bind("<Up>", funk)
# mainloop()

# i=3
# def funk():
#     global i
#     if i%2==0:
#         f.destroy()
#     else:
#         f.unpack()
#     i+=1

# root=Tk()
# root.geometry("100x200")
# root.title("Mitt fina fonster")
# f=Frame(root)
# f.pack(side=LEFT)
# f2 = Frame(root)
# f2.pack(side=RIGHT)
# e= Entry(f)
# e.pack()
# b = Button(f,text="knapp")
# mainloop()

win = Tk()
scroll = Scrollbar(win, orient=VERTICAL)
select = Listbox(win, yscrollcommand=scroll.set, height=6)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)
for i in range(10):
    select.insert(i,"rad "+str(i))
win.mainloop()