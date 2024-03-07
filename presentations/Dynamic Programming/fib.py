def fibonacci(x):
    global numCalls
    numCalls += 1

    if x <= 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

x = int(input())

numCalls = 0
print("Fibonacci number", x, "is", fibonacci(x))
print("This took", numCalls, "calls")