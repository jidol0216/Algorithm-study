from tkinter import *


otk = Tk()
otk.geometry('300x400+300+300')
obtn1 = Button(otk,text='click me1')
obtn2 = Button(otk,text='click me2')
obtn3 = Button(otk,text='click me3')
obtn4 = Button(otk,text='click me4')
obtn1.place(x= 10 , y=60)
obtn2.place(x= 170 , y=60)
obtn3.place(x= 90 , y=100)
obtn4.place(x= 90 , y=10)
otk.mainloop()

