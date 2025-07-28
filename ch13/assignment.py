div = lambda x,y: x//y

try:
    print(div(3,0))
except ZeroDivisionError as e:
    print ("ZeroDivisionError")


