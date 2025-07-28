def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2


for square in generate_squares(5):
    print(square)