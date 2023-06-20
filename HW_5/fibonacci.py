
def fibonacci_generator(limit):
    a = 0
    b = 1
    while a <= limit:
        yield a
        a, b = b, a + b

for num in fibonacci_generator(100):

    print(num)