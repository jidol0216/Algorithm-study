from tkinter import Label
from tkinter import Tk

otk = Tk()
otk.geometry('300x400+300+300')
olabel1 = Label(otk,text='적',bg="red",width=20)
olabel2 = Label(otk,text='녹',bg="green",width=20)
olabel3 = Label(otk,text='파',bg="blue",width=20)
olabel1.pack()
olabel2.pack()
olabel3.pack()
otk.mainloop()

