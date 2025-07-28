from tkinter import *


otk = Tk()
otk.geometry('300x400+300+300')
obtn1 = Button(otk,text='click me1')
obtn2 = Button(otk,text='click me2')
obtn3 = Button(otk,text='click me3')
obtn1.pack(side="left")
obtn2.pack(side="right")
obtn3.pack(side = "top")
otk.mainloop()

