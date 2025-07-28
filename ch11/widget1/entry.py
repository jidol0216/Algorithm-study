from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar


otk = Tk()

otk.geometry("400x300+200+200")

ostring = StringVar()
oentry = Entry(otk ,textvariable= ostring)
oentry.pack()


olabel1 = Label(otk,textvariable=ostring)
olabel1.pack()

otk.mainloop()
