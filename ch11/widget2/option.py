from tkinter import Tk
from tkinter import OptionMenu
from tkinter import StringVar


oroot = Tk()

oroot.geometry("600x400")
option_list=["불고기","새우","치즈"]

selected_option = StringVar()
selected_option.set(option_list[0])
option_menu = OptionMenu(oroot,selected_option,option_list)
option_menu.pack()



oroot.mainloop()