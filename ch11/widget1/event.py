import tkinter

def order():
    print("주문해라")

root = tkinter.Tk()
btn =tkinter.Button(root,text="주문",command=order)
btn.pack()
root.mainloop()