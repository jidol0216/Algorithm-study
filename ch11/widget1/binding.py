import tkinter

def msg():
    print("start tkinter")

root = tkinter.Tk()

mlabel = tkinter.Label(root,text=" 시작레이블")
mlabel.pack(side="top")

mbutton = tkinter.Button(root,text="시작",command = msg)

mbutton.pack(side="bottom")
root.mainloop()