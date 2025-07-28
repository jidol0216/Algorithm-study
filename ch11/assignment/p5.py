from tkinter import *
otk = Tk()
otk.title("조각 피자 주문")
otk.geometry("400x300+300+300")

olabel = Label(otk,text ="피자",width=20)
prices = {
    "치즈 피자": 3200,
    "콤비네이션 피자": 3500,
    "불고기 피자": 3600
}
var1= IntVar()
var2= IntVar()
var3= IntVar()

cb1 = Checkbutton(otk,text="치즈 피자(3200원)",variable=var1)
cb2 = Checkbutton(otk,text="콤비네이션 피자(3500원)",variable=var2)
cb3 = Checkbutton(otk,text="불고기 피자(3600원)",variable=var3)




olabel.pack()
cb1.pack(anchor="w", padx=20)
cb2.pack(anchor="w", padx=20)
cb3.pack(anchor="w", padx=20)


result_label = Label(otk, text="")
result_label.pack()
def order():
    total = 0
    order_text = "주문내역:\n"

    if var1.get() == 1:
        total += prices["치즈 피자"]
        order_text += f"- 치즈 피자 ({prices['치즈 피자']}원)\n"
    if var2.get() == 1:
        total += prices["콤비네이션 피자"]
        order_text += f"- 콤비네이션 피자 ({prices['콤비네이션 피자']}원)\n"
    if var3.get() == 1:
        total += prices["불고기 피자"]
        order_text += f"- 불고기 피자 ({prices['불고기 피자']}원)\n"

    order_text += f"\n총 가격: {total}원"
    result_label.config(text=order_text)
   
odb = Button(otk,text="주문",command= order)
odb.pack(anchor="center")
otk.mainloop()
