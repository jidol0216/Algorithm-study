a = [1,2,3]


iter_a =iter(a)

print(type(iter_a))

print(next(iter_a))
print(next(iter_a))
print(next(iter_a))



print('__iter__' in dir(list))
print('__iter__' in dir([1,2,3]))

print(dir(list))