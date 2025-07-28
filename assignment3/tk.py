

from tkinter import *

def on_click():
    print("버튼이 클릭되었습니다!")


otk = Tk()
otk.title("간단한 Tkinter 앱")  
otk.geometry('200x400+300+300')     


btn = Button(otk, text="클릭하세요", command=on_click)
btn.pack(pady=50)  

otk.mainloop()
