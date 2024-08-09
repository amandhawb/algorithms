# The Fibonacci numbers, commonly denotated F(n) form a sequence, called the fibonacci sequence, such that each number is the sum of the two precending ones, starting form 0 and 1.

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(4))