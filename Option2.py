#option 2
def fibonacci(n):
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(1, n):
        third = first + second
        print(third)
        first, second = second, third

n = 8
fibonacci(n)
