print("------------------------------------------")

print("try_except")



while True:
    try:
        name =int(input())
        4* name +3
        result = 10 // (1/0)
    except NameError:
        print("이름 없다..")
    except ValueError:
        print("숫자 안맞다..")
    except ZeroDivisionError:
        print("0이다 이자식아")
print("프로그램 종료")


# try 와 except 블록은 지역(scope)은 같다.