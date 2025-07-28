from tkinter import Tk
from tkinter import PhotoImage
from tkinter import Button
from tkinter import Label




oroot = Tk()

oroot.geometry("300x200")
img1 = PhotoImage(file="C:/rokey/python/ch11/widget2/stone.png")
img_label=Label(oroot,image=img1)
img_label.place(x=0,y=0)

obtn1 = Button(oroot,text='click me1')
obtn2 = Button(oroot,text='click me2')
obtn3 = Button(oroot,text='click me3')
obtn1.place(x=10,y=60)
obtn2.place(x=140,y=60)
obtn3.place(x=80,y=10)


oroot.mainloop()