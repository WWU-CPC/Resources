def fibonacci(n):
    if n <= 1:
        return 1

    fib_table = [1] * (n+1)  # Create an array of size n+1 and fill it with 1s

    for i in range(2, n+1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]


x = int(input())

print("Fibonacci number", x, "is", fibonacci(x))