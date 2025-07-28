print('--------------------------------------------')

def myFunc(str1):
    print('a')
    print('b')
    print('c')
    if str1 =='a':
        return
    print('d')
    print('e')


myFunc('a')

print('--------------------------------------------')


def myabs(arg):
    if(arg <=0):
        result = arg * -1
    else:
        result = arg
    return result

myabs(-10)
myabs(10)
myabs(-8)
myabs(-0)
myabs(0)

print('----------------------------------------------------------------------------------------')

def funca():
    print('funca 호출')
def funcb():
    funca()
    print('funcb 호출')
def funcc():
    funcb
    print('funcc 호출')


funcc()


sta = 'python'

def string_length(stb):
    cnt = 0
    for i in stb:
        cnt+=1
    return cnt


print(string_length(sta))



def a(num):
    sum = 0
    for i in range(0,101):
        if i % num ==0:
            sum+=i 
    return sum

a(8)        
    


def gugudan(num):

    
    total = 0
    for i in range(1,10):
        total = i * num
        print (f'{num} x {i} = {total}')


gugudan(2)