def generate_squares(N):
    for i in range(1, N+1):
        yield i ** 2

N = 5
squares_generator = generate_squares(N)

for square in squares_generator:
    print(square)