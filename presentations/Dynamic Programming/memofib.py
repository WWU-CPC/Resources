def fibonacci(x):
    global numCalls
    numCalls += 1

    if x <= 1:
        return 1
    elif x in fibNumbers:        # NEW
        return fibNumbers[x]     # NEW
    else:
        val = fibonacci(x-1) + fibonacci(x-2)
        fibNumbers[x] = val      # NEW
        return val

fibNumbers = {}                  # NEW
x = int(input())

numCalls = 0
print("Fibonacci number", x, "is", fibonacci(x))
print("This took", numCalls, "calls")