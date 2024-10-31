def factorial(n):
    if type(n) != int:
        return "ERROR: Invalid input"
    if n < 0:
        return "ERROR: Number can not be negative"
    result = 1
    for i in range(1, n +1):
        result *= i
    return result

print("Factorial of", 5, "is...", factorial(5))
print("Factorial of", -1, "is...", factorial(-1))
print("Factorial of", "A", "is...", factorial("A"))