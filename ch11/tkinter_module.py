from tkinter  import *

# otk = tkinter.Tk()
# obtn =tkinter.Button(otk,text='click me')
# obtn.pack()
# otk.mainloop()



def hello():
    print('hello there')

otk = Tk()
otk.geometry('200x400+300+300')
obtn = Button(otk,text='click me',command=hello)
obtn.pack()
otk.mainloop()

