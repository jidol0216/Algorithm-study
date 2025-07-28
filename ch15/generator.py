def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'


g = simple_generator()

print(type(g))
print(next(g))
print(next(g))
print(next(g))