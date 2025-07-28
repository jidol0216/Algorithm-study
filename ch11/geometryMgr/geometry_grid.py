from tkinter import *


otk = Tk()
otk.geometry('300x400+300+300')
obtn1 = Button(otk,text='click me1')
obtn2 = Button(otk,text='click me2')
obtn3 = Button(otk,text='click me3')
obtn1.grid(row=1,column=0)
obtn2.grid(row=1,column=1)
obtn3.grid(row=0,column=5)
otk.mainloop()

