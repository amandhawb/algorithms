# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().

def sum_honey(hunny_jars):
    total_honey = 0
    for jar in hunny_jars:
        total_honey += jar
    return total_honey

# TESTS
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))