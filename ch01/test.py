import tkinter as tk
from tkinter import messagebox

# 피자 종류별 조각당 가격
PRICES = {
    "치즈 피자": 2000,
    "페퍼로니 피자": 2500,
    "고구마 피자": 2200,
    "불고기 피자": 2700,
}

def calculate_price():
    try:
        slices = int(entry_slices.get())
        if slices <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("입력 오류", "조각 수는 1 이상의 정수여야 합니다.")
        return

    pizza_type = pizza_var.get()
    price_per_slice = PRICES.get(pizza_type, 0)
    total_price = slices * price_per_slice

    label_result.config(text=f"주문: {pizza_type} {slices}조각\n총 금액: {total_price}원")

# 메인 윈도우 생성
root = tk.Tk()
root.title("조각 피자 주문 프로그램")
root.geometry("300x250")

# 피자 종류 선택 라디오 버튼
pizza_var = tk.StringVar(value="치즈 피자")

tk.Label(root, text="피자 종류 선택:").pack(pady=5)

for pizza in PRICES.keys():
    tk.Radiobutton(root, text=pizza, variable=pizza_var, value=pizza).pack(anchor="w")

# 조각 수 입력
tk.Label(root, text="조각 수 입력:").pack(pady=5)
entry_slices = tk.Entry(root)
entry_slices.pack()

# 계산 버튼
btn_order = tk.Button(root, text="주문하기", command=calculate_price)
btn_order.pack(pady=10)

# 결과 표시 레이블
label_result = tk.Label(root, text="", fg="blue")
label_result.pack()

root.mainloop()
