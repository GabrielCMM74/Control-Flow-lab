# exercise-05 Fibonacci sequence for first 50 terms

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)


for num in range(1, 30):
    print("term: " + str(num) + " / number: " + str(fib(num)))