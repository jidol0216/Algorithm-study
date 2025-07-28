while True:
    user_input = input("숫자를 입력하세요: ")
    try:
        num = float(user_input)
        print(f"{num}의 제곱은 {num ** 2}입니다.")
        break
    except ValueError:
        print("올바른 숫자를 입력하세요!")
