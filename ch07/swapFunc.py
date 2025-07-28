

a = 0
print(f'외부 a{a}')
def scope_test():
    global a
    a=1
    a=3
    print(f'내부 a{a}')

scope_test()

print(a)


a =10
def my_func():
    b = 20
    print('locals: ',locals())
    print('globals: ',globals())




def scope_test():
    global a 
    a = 1 
    print('함수 안의 a값:',a)
a = 0
print('함수 밖의 a값:',a)
scope_test()
print('함수 호출 후 a값:',a)
print(locals())
print(globals())